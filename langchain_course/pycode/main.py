import os
from dotenv import load_dotenv
from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import argparse

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
args = parser.parse_args()


llm = openai.OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))

code_prompt = PromptTemplate(template="Write a very short {language} function that will {task}", input_variables=["language", "task"])

code_chain = LLMChain(llm=llm, prompt=code_prompt)

result = code_chain({
    "language": args.language,
    "task": args.task
})

print(result["text"])