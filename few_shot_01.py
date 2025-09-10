import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

sample_examples = """

Q : If i have 10 oranges and buy 5 more, How many do i have ? 
A:15

Q : Kumar had 10 balloons. He gave away 3, How many are left ?
A : 7

"""

query = "Shanti had 9 pens  and she lost 5. How many are left ?"

prompt = PromptTemplate(
          input_variables=["exampples", "question"],
          template = """ You are a math teacher. Solve the question based on the few examples.input_types = {examples}
          Q : {question}
          A :   """
)

input_prompt = prompt.format(examples = sample_examples, question = query)
 
llm = ChatOpenAI(model = "gpt-4") 
res = llm.invoke(input_prompt)
print(res.content)