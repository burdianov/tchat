from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.runnables import RunnableSequence

load_dotenv()

chat = ChatOpenAI(model="gpt-4o-mini")

prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages=[HumanMessagePromptTemplate.from_template("{content}")],
)

chain = RunnableSequence(prompt, chat)

while True:
    content = input(">> ")

    result = chain.invoke({"content": content})

    print(result.content)
