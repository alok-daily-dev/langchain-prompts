from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

messages = [
    SystemMessage(content="You are dsa expert. You should only answer dsa related questions. If anybody ask anything other than dsa, you should politely refuse to answer."),
]

while True:
    user_input = input("You: ")
    messages.append(HumanMessage(content=user_input))

    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chat. Goodbye!")
        break

    res = model.invoke(messages)
    messages.append(AIMessage(content=res.content))
    print("AI:", res.content)
