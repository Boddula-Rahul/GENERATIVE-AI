import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv

# prompt = PromptTemplate.from_template("Translate the following sentence to Hindi : {sentence} ")
prompt = PromptTemplate(
                input_variables=["sentence"],
                template= "Translate the following sentence to Hindi : {sentence} "
)

input_promt = prompt.format(sentence = "Hello Friend how are you")

model = ChatOpenAI(model = "gpt-4")
result = model.invoke(input_promt)
print(result.content)