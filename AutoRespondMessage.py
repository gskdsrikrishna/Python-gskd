def autorespond(message):
    if 'hello' in message.lower():
        return "Hello! How can I assist you?"
    elif 'thank you' in message.lower():
        return "You're welcome!"
    else:
        return "Thank you for your message. We will get back to you soon."


if __name__ == '__main__':
    # Simulating an incoming message
    incoming_message = "Hello, can you help me with my order?"

    # Autorespond based on the incoming message
    response = autorespond(incoming_message)

    print("Incoming Message:", incoming_message)
    print("Autoresponse:", response)