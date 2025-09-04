from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)

    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chat. Goodbye!")
        break

    res = model.invoke(chat_history)
    chat_history.append(res.content)
    print("AI:", res.content)

print(chat_history)
