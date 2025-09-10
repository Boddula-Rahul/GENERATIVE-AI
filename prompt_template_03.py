import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

prompt = PromptTemplate(

        input_variables= ["style", "data"] ,
        template= "Summarize the following output in a {style} : \n\n{data}"
)

text = "Generative AI Generative Artificial Intelligence is a type of artificial intelligence that can create new content such as text, images, music, code, or even videos, instead of just analyzing or processing existing data.It is based on machine learning models  especially deep learning that learn patterns from huge amounts of data and then generate outputs that look similar to human-created content."

input_prompt  = prompt.format(
    style = "bullet point",
    data = text
   )
llm = ChatOpenAI(model = "gpt-4")
res = llm.invoke(input_prompt)
print(res.content)