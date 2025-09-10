
import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    input_variables= ["profession", "user","query"] ,
    template= "You are a {profession} helping a {user}. The {user} has following question : {query}"
        )
input_prompt = prompt.format(
     profession = "Data Scientist",
     user = "Fresher",
     query = "what is generative AI in artificial intelligence " 
     )

llm = ChatOpenAI(model = "gpt-4")
result = llm.invoke(input_prompt)
print(result.content)