import openai # openai v1.0.0+
client = openai.OpenAI(api_key="kalle",base_url="http://0.0.0.0:11434/v1") # Ollama_url

# request to Ollama model (mistral)
response = client.chat.completions.create(model="mistral", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
])
print("Ollama Mistral via OpenAI API:\n", response.choices[0].message.content)

# request to Ollama model (deepseek)
response = client.chat.completions.create(model="deepseek-r1:14b", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
])
print("Ollama Deepseek via OpenAI API:\n", response.choices[0].message.content)