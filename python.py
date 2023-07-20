import openai

response = openai.ChatCompletion.create(
    model='gpt-4-0613',
    messages=[
        {'role': 'system', 'content': "You are a customer support agent for Gepeto (pronounced Geppetto), a company that makes AI chatbots. You're speaking to a potential customer. Your job is to empathize, ask questions, and understand what they want to use our chatbot for."},
        {'role': 'assistant', 'content': "Hi there, thanks for reaching out to Gepeto, can I please have your name?"},
        {'role': 'user', 'content': "Hi my name is Chris."}
    ],
    temperature=0,
    stream=True  # this time, we set stream=True
)

for chunk in response:
    print(chunk)
