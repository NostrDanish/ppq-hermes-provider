# ppq-hermes-provider

Hermes plugin for [PayPerQ](https://ppq.ai/invite/949880ca).

Create an account: https://ppq.ai/invite/949880ca

To add PPQ in Hermes Desktop without changing your default model, use
https://github.com/NostrDanish/hermes-ppq-provider

## Setup

```bash
export PPQ_API_KEY=your_key_here
hermes -z "hello" --provider ppq -m <model-name>
```

Completions spend PPQ balance.

## Install from source

```bash
pip install -e .
```
