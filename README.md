# ppq-hermes-provider

Hermes model provider plugin for [PayPerQ](https://ppq.ai/invite/949880ca).

Sign up with this referral: https://ppq.ai/invite/949880ca

This fork sets the plugin `signup_url` to that invite so Hermes setup
links use it. The registration skill (writes the Desktop `providers.ppq`
row without switching your default model) lives at
https://github.com/NostrDanish/hermes-ppq-provider

## Setup

```bash
export PPQ_API_KEY=your_key_here
hermes -z "hello" --provider ppq -m <model-name>
```

Do not send a test completion unless you intend to spend PPQ balance.

## Install from source

```bash
pip install -e .
```

## Desktop provider list

A plugin file alone does not appear in Hermes Desktop's provider picker.
Install and run the skill:

```bash
hermes skills install NostrDanish/hermes-ppq-provider/skills/hermes-ppq-provider --yes
python3 "$HOME/.hermes/skills/hermes-ppq-provider/scripts/add_ppq.py" --apply
```
