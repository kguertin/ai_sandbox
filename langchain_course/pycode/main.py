import os
from dotenv import load_dotenv
from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

llm = openai.OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))

code_prompt = PromptTemplate(template="Write a very short {language} function that will {task}", input_variables=["language", "task"])

code_chain = LLMChain(llm=llm, prompt=code_prompt)
\
result = code_chain({
    "language": "python",
    "task": "return a list of numbers"
})

print(result["text"])