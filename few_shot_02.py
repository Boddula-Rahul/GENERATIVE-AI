import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

samples = [


    {
        "review" : "The product exceeded my expectations and arrived early",
        "sentiment" : "Positive"

    } ,
    
    {

        "review" : "Product is okay, its performing normally as per expectations, nothing exciting",
        "sentiment" : "Neutral"
    
    }, 

    {
        
        "review" : "Very disappointed, it stops working right after two days of purchase ",
        "sentiment" : "Negative"
        
        }

]

query = "Initially i was very excites about the product but it disappointed me right after days"
#query = input("enter the review :")

prompt = PromptTemplate(

    input_variables= ["examples", "question"] ,
    template = """
                you are an AI assistant that analyze customer reviews and classifies them as 
                'Positive' or 'Negative' or 'Neutral'

            {examples}

            review : {question}
            sentiment :  """  )

input_prompt = prompt.format(examples = samples , question = query)

llm = ChatOpenAI(model = "gpt-4")
res = llm.invoke(input_prompt)

print(res.content)