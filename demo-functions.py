import os
import requests

def get_current_weather(location):
    """
    Get the current weather for a given location.
    """
    # Replace with your actual weather API endpoint and API key
    api_key = os.getenv("WEATHER_API_KEY")
    endpoint = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'

    response = requests.get(endpoint)
    if response.status_code == 200:
        data = response.json()
        return {
            "location": data['location']['name'],
            "temperature_c": data['current']['temp_c'],
            "condition": data['current']['condition']['text']
        }
    else:
        return {"error": "Unable to fetch weather data."}
    

function_description = {
    "name": "get_current_weather",
    "description": "Get the current weather for a specified location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and country, e.g., 'San Francisco, USA'."
            }
        },
        "required": ["location"]
    }
}

import openai
import json

# Initialize the OpenAI client
api_key=os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key) # Open-WebUI url

# User input
user_input = "What's the weather like in Paris today?"
messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
]

# request to OpenAI
response = client.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages = messages,
    functions=[function_description],
    function_call="auto"
)

# Check if the model wants to call a function
if response.choices[0].message.tool_calls:
    call = response.choices[0].message.tool_calls
    name = call["name"]
    arguments = json.loads(call["arguments"])

    # Call the function
    if name == "get_current_weather":
        result = get_current_weather(arguments.get("location"))

        # Add the function's response to the messages
        messages.append({
            "role": "function",
            "name": name,
            "content": json.dumps(result)
        })

        # Get a new response from the model that includes the function's result
        final_response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages = messages
        )        

        # Output the model's final response
        print(final_response.choices[0].message.content)
else:
    # If no function call is needed, output the model's response
    print(response.choices[0].message.content)
