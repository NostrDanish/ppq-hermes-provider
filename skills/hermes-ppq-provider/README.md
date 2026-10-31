# PPQ Hermes provider

Adds [PayPerQ](https://ppq.ai/invite/949880ca) to Hermes without changing your
default model.

Create an account: https://ppq.ai/invite/949880ca

```bash
python3 scripts/add_ppq.py --apply
```

That lists models at `https://api.ppq.ai/v1/models` (no key), copies the plugin,
and adds PPQ to the provider list.

Get a key after opening https://ppq.ai/invite/949880ca, then:

```bash
export HERMES_CUSTOM_PPQ_API_KEY="sk-..."
```

Do not paste the key into chat.

## License

MIT
