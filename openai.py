import openai

openai.api_key = "YOUR_API_KEY"

def get_openai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
    )

    return response['choices'][0]['message']['content']

# Example usage
user_message = "Hello, how are you?"
chat_messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': user_message}]

response = get_openai_response(chat_messages)
print(response)