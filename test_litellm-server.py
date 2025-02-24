import openai # openai v1.0.0+
client = openai.OpenAI(api_key="sk-1234",base_url="http://0.0.0.0:4000") # set proxy to base_url

# request to OpenAI model
response = client.chat.completions.create(model="gpt-3.5-turbo-instruct", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
])
print("LiteLLM using OpenAI model:\n", response.choices[0].message.content)

# request to Ollama model
response = client.chat.completions.create(model="mistral:latest", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
])
print("LiteLLM using Ollama model:\n", response.choices[0].message.content)


