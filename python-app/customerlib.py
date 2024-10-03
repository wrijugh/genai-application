import os
from dotenv import load_dotenv

def load_keys():
    load_dotenv()
        

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def build_prompt(orgName):   
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", 
            ''' You bring the information about the organization.
            In following format:
            - Industry:
            - History of the Organization:
            - Official Website:
            '''
            ),
            ("user","{orgName}")
        ])

    return prompt

def get_org_details(orgName):
    load_keys()

    llm = AzureChatOpenAI(
        azure_deployment = os.getenv("AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME")
    )

    prompt = build_prompt(orgName)

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    response = chain.invoke({"orgName": orgName})

    return response