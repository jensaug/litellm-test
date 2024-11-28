import os 
from litellm import completion

#os.environ["OPENAI_API_KEY"] = "your-api-key"

# openai call
response = completion(
    model = "gpt-4o", 
    messages=[{ "content": "Hello, how are you?","role": "user"}]
)
print("OpenAI:\n", response.choices[0].message.content)

# Ollama call
response = completion(
    api_base="http://192.168.50.105:11434",
    model = "ollama/mistral:7b", 
    messages=[{ "content": "Hello, how are you?","role": "user"}]
)
print("Ollama:\n", response.choices[0].message.content)