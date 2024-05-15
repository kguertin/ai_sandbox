from dotenv import load_dotenv

from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationSummaryMemory, FileChatMessageHistory

load_dotenv()

chat = ChatOpenAI(verbose=True)

memory = ConversationSummaryMemory(
    memory_key="messages", 
    return_messages=True, 
    llm=chat
    # chat_memory=FileChatMessageHistory("messages.json")
)

prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
    verbose=True
)

while True: 
    content = input(">> ")
    result = chain({
        "content": content
    }) 

    print(result["text"])

