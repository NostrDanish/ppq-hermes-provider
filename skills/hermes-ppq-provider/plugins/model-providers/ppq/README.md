# PayPerQ Hermes plugin

OpenAI-compatible provider for [PayPerQ](https://ppq.ai/invite/949880ca).

- Base URL: `https://api.ppq.ai/v1`
- Signup (referral): https://ppq.ai/invite/949880ca
- Key env: `HERMES_CUSTOM_PPQ_API_KEY` or `PPQ_API_KEY`
- Listing `GET /v1/models` needs no key. Completions are paid — do not send one as a setup test.
