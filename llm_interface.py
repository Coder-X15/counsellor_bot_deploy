from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.system import SystemMessage
from langchain_core.messages.human import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from langchain_core.runnables import RunnablePassthrough

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
        # In llm_interface.py
        self.prompt = ChatPromptTemplate([
            SystemMessage(content = open('config_prompt.txt').read()),
            # HumanMessage(content="{question}")
            ]
        )

        # Ollama LLM model setup
        self.llm = OllamaLLM(model="smollm", base_url="http://localhost:11434")  # Change to "llama2" for the larger model
        self.output_parser = StrOutputParser()
        self.chain = (
            RunnablePassthrough.assign(question=lambda x: x["question"])
            | self.prompt
            | self.llm
            | self.output_parser
        )

    def invoke(self, input_text):

        # Display the result in the Streamlit UI
        if input_text:
            return self.chain.invoke({"question": input_text})