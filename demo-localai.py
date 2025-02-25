#  curl https://localai.io/install.sh | sh
import requests
import openai

# Set the LocalAI server as the API base_url
client = openai.OpenAI(api_key="dummy",base_url="http://localhost:8080/v1")

# Function to send a chat using OpenAI API
def localai_with_openai(prompt):
    response = client.chat.completions.create(model="phi-4", messages = [
        {
            "role": "user",
            "content": prompt
        }
    ])
    return response.choices[0].message.content

# Function to send a chat using Requests and HTTP
def localai_with_requests(prompt):
    url = "http://localhost:8080/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    payload = {
        #"model": "phi-4",
        "model": "llama-3.2-3b-instruct:q8_0",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == "__main__":
    #user_prompt = input("Enter your prompt: ")
    user_prompt = "Who is the president of Sweden?"
    print("\nResponse from LocalAI with requests:", localai_with_requests(user_prompt))
    print("\nResponse from LocalAI with requests:", localai_with_openai(user_prompt))


