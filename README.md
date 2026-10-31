# ppq-hermes-provider

Hermes plugin for [PayPerQ](https://ppq.ai/invite/949880ca).

Create an account: https://ppq.ai/invite/949880ca

PPQ charges per request. Do not send a test call unless you mean to spend.

## Add PPQ in Hermes Desktop

This does not change your default model.

```bash
hermes skills tap add NostrDanish/ppq-hermes-provider
hermes skills install NostrDanish/ppq-hermes-provider/skills/hermes-ppq-provider --yes
cd "$HOME/.hermes/skills/hermes-ppq-provider"
python3 scripts/add_ppq.py --apply
```

Or clone and run:

```bash
git clone https://github.com/NostrDanish/ppq-hermes-provider.git
cd ppq-hermes-provider/skills/hermes-ppq-provider
python3 scripts/add_ppq.py --apply
```

Then set a key locally (not in chat):

```bash
export HERMES_CUSTOM_PPQ_API_KEY="sk-..."
# also accepted: PPQ_API_KEY
```

## pip install

Same repo, if you want the Python plugin directly:

```bash
pip install -e .
export PPQ_API_KEY=your_key_here
hermes -z "hello" --provider ppq -m <model-name>
```

Upstream: https://github.com/PayPerQ/ppq-hermes-provider

## Test

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT
