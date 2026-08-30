import importlib.util
import os
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


def load_module(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class LocalDeploymentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.configure = load_module(
            "configure_local_cliproxyapi_test",
            ROOT / "scripts" / "configure_local_cliproxyapi.py",
        )
        cls.launchagents = load_module(
            "manage_local_launchagents_test",
            ROOT / "scripts" / "manage_local_launchagents.py",
        )
        cls.deploy = load_module(
            "deploy_local_runtime_test",
            ROOT / "scripts" / "deploy_local_runtime.py",
        )
        cls.server = load_module(
            "local_debug_server_deployment_test",
            ROOT / "src" / "local_debug_server.py",
        )

    def test_reads_first_client_key_without_exposing_management_secret(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "cliproxyapi.conf"
            path.write_text(
                "remote-management:\n"
                "  secret-key: management-hash\n"
                "api-keys:\n"
                "  - client-key-one\n"
                "  - client-key-two\n",
                encoding="utf-8",
            )
            self.assertEqual(self.configure.read_first_client_api_key(path), "client-key-one")

    def test_configure_env_writes_generic_and_legacy_compatibility_keys(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            example = root / ".env.example"
            env = root / ".env"
            example.write_text("# example\nLLM_API_KEY=\n", encoding="utf-8")
            self.configure.configure_env(
                env,
                example,
                api_key="local-client-key",
                base_url="http://127.0.0.1:8317",
                model="gpt-5.4-mini",
                chat_models=["gpt-5.4"],
            )
            text = env.read_text(encoding="utf-8")
            self.assertIn("LLM_PROVIDER=cliproxyapi", text)
            self.assertIn("LLM_API_KEY=local-client-key", text)
            self.assertIn("SUMMARY_API_KEY=local-client-key", text)
            self.assertIn("DEEPSEEK_API_KEY=local-client-key", text)
            self.assertIn("DPR_LOCAL_CHAT_MODELS=gpt-5.4-mini,gpt-5.4", text)
            self.assertEqual(env.stat().st_mode & 0o777, 0o600)

    def test_launchagent_plists_are_loopback_and_secret_free(self):
        root = pathlib.Path("/tmp/daily-paper-reader")
        web = self.launchagents.build_web_plist(root, host="127.0.0.1", port=8567)
        daily = self.launchagents.build_daily_plist(root, hour=2, minute=30)
        self.assertEqual(web["ProgramArguments"][-3:], ["127.0.0.1", "--port", "8567"])
        self.assertTrue(web["KeepAlive"])
        self.assertEqual(daily["StartCalendarInterval"], {"Hour": 2, "Minute": 30})
        serialized = repr({"web": web, "daily": daily})
        self.assertNotIn("API_KEY", serialized)
        self.assertNotIn("secret", serialized.lower())

    def test_runtime_deployment_rejects_macos_protected_user_paths(self):
        home = pathlib.Path("/Users/example")
        self.assertTrue(
            self.deploy.is_macos_protected_user_path(
                home / "Desktop" / "daily-paper-reader",
                home=home,
            )
        )
        self.assertFalse(
            self.deploy.is_macos_protected_user_path(
                home / "Services" / "daily-paper-reader",
                home=home,
            )
        )

    def test_runtime_config_exposes_models_but_not_api_key(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = pathlib.Path(tmp) / ".env"
            env.write_text(
                "LLM_PROVIDER=cliproxyapi\n"
                "LLM_API_KEY=private-key\n"
                "LLM_BASE_URL=http://127.0.0.1:8317\n"
                "LLM_MODEL=gpt-5.4-mini\n"
                "DPR_LOCAL_CHAT_MODELS=gpt-5.4-mini,gpt-5.4\n",
                encoding="utf-8",
            )
            cleared = {
                key: ""
                for key in [
                    "LLM_API_KEY", "SUMMARY_API_KEY", "DEEPSEEK_API_KEY",
                    "LLM_BASE_URL", "SUMMARY_BASE_URL", "DEEPSEEK_BASE_URL",
                    "LLM_MODEL", "SUMMARY_MODEL", "DEEPSEEK_MODEL",
                ]
            }
            with patch.object(self.server, "ENV_PATH", env), patch.dict(os.environ, cleared, clear=False):
                private = self.server.get_local_llm_runtime()
                public = self.server.public_local_llm_runtime()
            self.assertTrue(private["configured"])
            self.assertEqual(private["api_key"], "private-key")
            self.assertEqual(public["models"], ["gpt-5.4-mini", "gpt-5.4"])
            self.assertNotIn("api_key", public)
            self.assertNotIn("private-key", repr(public))

    def test_local_api_rejects_nonlocal_origin_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = pathlib.Path(tmp) / ".env"
            env.write_text("DPR_LOCAL_ALLOW_REMOTE_API=0\n", encoding="utf-8")
            with patch.object(self.server, "ENV_PATH", env):
                self.assertTrue(
                    self.server.is_allowed_local_request("127.0.0.1", "http://127.0.0.1:8567")
                )
                self.assertFalse(
                    self.server.is_allowed_local_request("127.0.0.1", "https://evil.example")
                )

    def test_frontend_loads_local_proxy_before_secret_and_exposes_provider_controls(self):
        secret = (ROOT / "app" / "secret.session.js").read_text(encoding="utf-8")
        chat = (ROOT / "app" / "chat.discussion.js").read_text(encoding="utf-8")
        self.assertIn("DPR_LOCAL_LLM_READY", secret)
        self.assertIn("app/local-llm.js", secret)
        self.assertIn('value="cliproxyapi"', secret)
        self.assertIn("secret-setup-custom-discover", secret)
        self.assertIn("buildModelsEndpoint", secret)
        self.assertIn("window.DPRLocalLLM.getChatModels", chat)
        self.assertIn("modelEntry.endpoint", chat)

    def test_hosted_daily_can_be_disabled_without_breaking_manual_dispatch(self):
        workflow = (ROOT / ".github" / "workflows" / "daily-paper-reader.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("vars.DPR_DISABLE_HOSTED_DAILY != 'true'", workflow)
        self.assertIn("github.event_name != 'schedule'", workflow)

    def test_zsh_publish_script_does_not_shadow_path(self):
        script = (ROOT / "scripts" / "publish_local_results.sh").read_text(encoding="utf-8")
        self.assertNotIn('\n  path="${line:3}"', script)
        self.assertNotIn("while IFS= read -r path", script)
        self.assertIn('changed_path="${line:3}"', script)


if __name__ == "__main__":
    unittest.main()
