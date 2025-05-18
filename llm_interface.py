from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM

import os
import sys
from dotenv import load_dotenv

class Model:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Set LangChain environment variables
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        # os.environ["LANGSMITH_ENDPOINT"]=os.getenv("LANGSMITH_ENDPOINT")
        os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

        # Create the prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", open('config_prompt.txt').read()),
            ("user", "Question: {question}")
        ])

        # Ollama LLM model setup
        self.llm = OllamaLLM(model="smollm", base_url="https://127.0.0.1:11434")  # Change to "llama2" for the larger model
        self.output_parser = StrOutputParser()
        self.chain = self.prompt | self.llm | self.output_parser

    def invoke(self, input_text):

        # Display the result in the Streamlit UI
        if input_text:
            return self.chain.invoke({"question": input_text})