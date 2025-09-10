import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model = "gpt-4")
result = llm.invoke("Translate the following sentence to Hindi : \nwelcome to INDIA" )
print(result.content) 
