#!/usr/bin/env python3
"""Offline tests for add_ppq.py. No network, no hermes CLI."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "hermes-ppq-provider"
    / "scripts"
    / "add_ppq.py"
)


def load_mod():
    spec = importlib.util.spec_from_file_location("add_ppq", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


class TestAddPpq(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = load_mod()

    def test_signup_url(self):
        self.assertEqual(self.m.SIGNUP_URL, "https://ppq.ai/invite/949880ca")

    def test_key_env(self):
        self.assertEqual(self.m.key_env_for("ppq"), "HERMES_CUSTOM_PPQ_API_KEY")

    def test_models_url(self):
        self.assertEqual(self.m.models_url("https://api.ppq.ai/v1"), "https://api.ppq.ai/v1/models")
        self.assertEqual(self.m.models_url("https://api.ppq.ai"), "https://api.ppq.ai/v1/models")

    def test_parse_openai_shape(self):
        ids = self.m.parse_model_ids({"data": [{"id": "openai/gpt-4o-mini", "type": "chat"}]})
        self.assertEqual(ids, ["openai/gpt-4o-mini"])

    def test_parse_list(self):
        self.assertEqual(self.m.parse_model_ids(["a", "b"]), ["a", "b"])

    def test_pick_preferred(self):
        ids = ["claude-opus-5.5", "openai/gpt-4o-mini", "gpt-5.4-nano"]
        self.assertEqual(self.m.pick_model(ids), "openai/gpt-4o-mini")

    def test_pick_override(self):
        self.assertEqual(self.m.pick_model(["a"], "b"), "b")

    def test_pick_first_when_no_preferred(self):
        self.assertEqual(self.m.pick_model(["only-this"]), "only-this")

    def test_plugin_signup_constant_matches(self):
        plugin = (
            Path(__file__).resolve().parents[1]
            / "skills"
            / "hermes-ppq-provider"
            / "plugins"
            / "model-providers"
            / "ppq"
            / "__init__.py"
        )
        text = plugin.read_text(encoding="utf-8")
        self.assertIn('SIGNUP_URL = "https://ppq.ai/invite/949880ca"', text)
        self.assertNotIn("https://payperq.ai", text)


if __name__ == "__main__":
    unittest.main()
