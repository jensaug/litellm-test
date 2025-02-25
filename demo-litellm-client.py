import os 
from litellm import completion

#os.environ["OPENAI_API_KEY"] = "your-api-key"

# openai call
response = completion(
    model = "gpt-4o", 
    messages=[{ "content": "Hello, how are you?","role": "user"}]
)
print("OpenAI using LiteLLM client:\n", response.choices[0].message.content)

# Ollama call
response = completion(
    api_base="http://0.0.0.0:11434",
    model = "ollama/mistral:latest", 
    messages=[{ "content": "Hello, how are you?","role": "user"}]
)
print("Ollama using LiteLLM client:\n", response.choices[0].message.content)