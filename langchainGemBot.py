from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

query = input('Prompt: ')


llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro-latest")
result = llm.invoke(query)
print(result.content)           