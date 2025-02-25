# local-llm-demo

This code demonstrates Python client access to locally installed:
* Ollama
* Open WebUI
* LiteLLM Proxy Server
* LiteLLM Python SDK
* LocalAI
* OpenAI Functions API

The code complements [Google Slides "Demo Local LLM"](https://docs.google.com/presentation/d/1JeQcU1jfNWLBcyfsrk7gG2JNs6JyTrCgNNvQwJgXPVA/edit?usp=sharing)

## Configuration

* 'OPENAI_API_KEY' environment variable must be set
* Docker should work
* Ollama should be running on 'http://0.0.0.0:11434' (or adapt IP in 'config.yaml')
* Open WebUI or LocalAI should be running at http://0.0.0.0:8080
* LiteLLM Proxy Server should be running at http://0.0.0.0:4000
* PDM is installed - or manually pip install pyproject.toml, run its '[tool.pdm.scripts]' and execute python scripts

## Start servers

Start LiteLLM in Docker with 'config.yaml':
```
pdm run docker
```
Or just locally with:
```
litellm --config config.yaml
```

## Execute demo clients

Choose which demo to run using PDM, e.g:
```
pdm run demo-ollama.py
```

