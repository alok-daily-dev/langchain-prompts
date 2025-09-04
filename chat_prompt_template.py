from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate([
    ('system', "You are a {domain} expert. You should only answer {domain} related questions. If anybody ask anything other than {domain}, you should politely refuse to answer."),
    ('human', "What do you know about {topic}?")
])

prompt = chat_template.invoke(
    {
        'domain': 'cricket',
        'topic': 'Dusra'
    }
)

print(prompt)