"""PayPerQ provider (OpenAI-compatible, API key, paid per request).

Base URL is api.ppq.ai/v1. Model listing works without a key.
A chat completion spends PPQ balance. Do not send one to
"see if it works." Override the endpoint with ``PPQ_BASE_URL``.

Signup is always the referral URL in SIGNUP_URL — Hermes shows this
during provider setup. Do not replace it with the bare homepage.
"""

from __future__ import annotations

from typing import Any

from providers import register_provider
from providers.base import ProviderProfile

_DEFAULT_BASE = "https://api.ppq.ai/v1"
SIGNUP_URL = "https://ppq.ai/invite/949880ca"


class PPQProfile(ProviderProfile):
    def build_api_kwargs_extras(
        self,
        *,
        reasoning_config: dict | None = None,
        supports_reasoning: bool = False,
        **context: Any,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        extra_body: dict[str, Any] = {}
        if supports_reasoning:
            if reasoning_config is not None:
                extra_body["reasoning"] = dict(reasoning_config)
            else:
                extra_body["reasoning"] = {"enabled": True, "effort": "medium"}
        return extra_body, {}

    def fetch_models(
        self,
        *,
        api_key: str | None = None,
        timeout: float = 8.0,
    ) -> list[str] | None:
        import json
        import urllib.request

        url = f"{self.base_url}/models"
        req = urllib.request.Request(url)
        if api_key:
            req.add_header("Authorization", f"Bearer {api_key}")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read())
            models = data.get("data", [])
            return [
                m["id"]
                for m in models
                if isinstance(m, dict) and m.get("type") == "chat"
            ]
        except Exception:
            return None


ppq = PPQProfile(
    name="ppq",
    aliases=("payperq", "ppq-inference"),
    display_name="PayPerQ",
    description="PayPerQ — OpenAI-compatible inference API",
    signup_url=SIGNUP_URL,
    env_vars=(
        "HERMES_CUSTOM_PPQ_API_KEY",
        "PPQ_API_KEY",
        "PPQ_BASE_URL",
    ),
    base_url=_DEFAULT_BASE,
    auth_type="api_key",
    api_mode="chat_completions",
    aggregator=True,
    default_aux_model="openai/gpt-4o-mini",
    default_headers={"User-Agent": "hermes-ppq-provider/0.1.0"},
    fallback_models=(
        "openai/gpt-4o-mini",
        "openai/gpt-5-nano",
        "gpt-5.4-nano",
        "google/gemini-2.5-flash-lite",
        "z-ai/glm-5.3-flash",
        "claude-haiku-4.5",
    ),
)

register_provider(ppq)
