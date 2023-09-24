import openai
# Set up your OpenAI API credentials
openai.api_key = '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'
# Define a function to generate a response from the model
def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
        n=2,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()
# Main loop
while True:
    # Get user input
    user_input = input("User: ")
    # Exit the loop if the user enters 'exit'
    if user_input.lower() == 'exit':
        break
    # Generate a response from the model
    prompt = f"User: {user_input}\nChatGPT: "
    response = generate_response(prompt)
    # Print the model's response
    print("ChatGPT:", response)