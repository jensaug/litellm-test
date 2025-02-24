import openai # openai v1.0.0+
client = openai.OpenAI(api_key="sk-69eb7ea994234505ab2b776eb94ce523",base_url="http://0.0.0.0:8080/api") # Open-WebUI url

# request to Ollama model (mistral)
response = client.chat.completions.create(model="mistral:latest", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
])
print("Open-WebUI Mistral via OpenAI API:\n", response.choices[0].message.content)

# request to Ollama model (deepseek)
response = client.chat.completions.create(model="deepseek-r1:14b", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
])
print("Open-WebUI Deepseek via OpenAI API:\n", response.choices[0].message.content)
