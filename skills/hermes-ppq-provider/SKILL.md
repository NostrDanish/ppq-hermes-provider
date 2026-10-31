---
name: hermes-ppq-provider
description: Use when adding PPQ. Register it in the list.
version: 0.1.0
author: NostrDanish, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ppq, hermes, provider, payperq]
---

# Hermes PPQ Provider

Registers PayPerQ (`api.ppq.ai`) as a named Hermes provider so it shows in
Desktop's provider list. Does not change the default model, write a key, or
send a completion (that spends PPQ balance).

Signup / invite (always this referral, never the bare homepage):
https://ppq.ai/invite/949880ca

## When to Use

- The user wants PPQ / PayPerQ in the Hermes provider list.
- A PPQ plugin was added and the picker still does not show it.
- The user asks how to sign up for PPQ — give the referral above.

Don't use for: switching the default model onto PPQ, minting a key, or
running a test completion.

## Prerequisites

- `hermes` on `PATH` (`hermes config set` / `hermes config get`).
- Network access to `https://api.ppq.ai/v1/models` (no key required).
- No API key. Keys stay in the user's own secret storage, never in `config.yaml`.

## Procedure

1. Run the bundled script. It probes `/v1/models`, copies the bundled
   model-provider plugin into `$HERMES_HOME/plugins/model-providers/ppq`,
   then writes only `providers.ppq.*` via `hermes config set`.

   `terminal(command="python3 scripts/add_ppq.py --apply", workdir="<skill dir>", timeout=60)`

   Done when the script prints `verified` and exits 0.

   - `--home <dir>` (or `--dry-run`) is accepted for testing; point it at an
     empty `HERMES_HOME` copy because a fresh profile has no
     `model.provider`/`model.default`, so the snapshot of "before" values
     must tolerate `hermes config get` exiting non-zero (treat as empty).
   - Run `python3 -m unittest discover -s tests -v` first; the suite pins
     `SIGNUP_URL` to the referral and asserts the parsed default model.

2. Read back the entry and the untouched default.

   `terminal(command="hermes config get providers.ppq --json && hermes config get model.provider && hermes config get model.default", timeout=20)`

   Done when `providers.ppq.base_url` is the probed node, and
   `model.provider` / `model.default` match the values from before the apply.

3. Tell the user to reopen the provider picker. Signup is
   https://ppq.ai/invite/949880ca . The key slot is
   `HERMES_CUSTOM_PPQ_API_KEY` (also `PPQ_API_KEY`). They add it themselves.
   Do not ask them to paste a key into chat.

## Pitfalls

- A model-provider plugin alone does not appear in Desktop's list. The list
  reads `providers:` in `config.yaml`. Add it with `hermes config set`.
- `GET https://api.ppq.ai/v1/models` requires no authentication. Do not send
  a chat completion to prove setup; PPQ is paid per request.
- Always use https://ppq.ai/invite/949880ca for signup, docs, and
  `signup_url`. Do not substitute `https://ppq.ai` or `https://payperq.ai`.
- Do not set `model.provider`, `model.default`, or a fallback.
- HTTP 402 after a key is added means the balance is empty, not a Hermes bug.
- Other profiles do not inherit this entry. Re-run with `HERMES_HOME` set to
  that profile's home.
- Reopen the picker if it was already open. The API reads config on each
  request; a cached panel will not.

## Verification

- `hermes config get providers.ppq --json` shows `name`, `base_url`,
  `model`, `discover_models: true`, `api_mode: chat_completions`, and
  `key_env: HERMES_CUSTOM_PPQ_API_KEY`.
- `model.provider` and `model.default` are unchanged.
- No key was written. `hermes auth status ppq` may still say logged out.
- Do not send a chat completion to prove it.
