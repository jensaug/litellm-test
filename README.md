# litellm-test

## Configuration

* 'OPENAI_API_KEY' environment variable must be set
* Docker must work
* Ollama should be running on 'http://192.168.50.105:11434' (or adapt IP in 'config.yaml')
* PDM is installed - or manually pip install pyproject.toml, run its '[tool.pdm.scripts]' and execute python scripts

## Usage

Start LiteLLM in Docker with 'config.yaml':
```
pdm run docker
```

Call OpenAPI and Ollama through LiteLLM:
```
pdm run test_litellm.py
```
Or call OpenAI and Ollama without LiteLLM:
```
pdm run test_local.py
```

