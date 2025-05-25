import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("GROQ_API_KEY")

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
                    temperature = 0,
                    api_key = "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",
                    model = "llama-3.3-70b-versatile"
                )
        
    def extract_requirements(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
                                """
                                    ### SCRAPED TEXT FROM WEBSITE:
                                    {data}
                                    ### INSTRUCTION:
                                    The scraped text is from the career's page of a website.
                                    Your task is to extract the job postings and return them in JSON format containing the 
                                    following keys: role, experience, skills and description.
                                    ### VALID JSON, NO PREAMBLE:
                                """
                        )
        chain_extract = prompt_extract | self.llm

        try:
        # Invoking the pipeline made in previous step
            response = chain_extract.invoke(input={'data': cleaned_text})
        except Exception as e:
            print("The input was too big. Limit the input text to 10000 chars\n" + e)

        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(response.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        
        return res if isinstance(res, dict) else res[0]
    
    def write_email(self, jd, links):
        prompt_email = PromptTemplate.from_template(
                    """
                        ### JOB DESCRIPTION:
                        {job_description}
                        
                        ### INSTRUCTION:
                        You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
                        the seamless integration of business processes through automated tools. 
                        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
                        process optimization, cost reduction, and heightened overall efficiency. 
                        Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
                        in fulfilling their needs.
                        Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
                        Remember you are Mohan, BDE at AtliQ. 
                        Do not provide a preamble.
                        ### EMAIL (NO PREAMBLE):
                    """
        )

        chain = prompt_email | self.llm
        res = chain.invoke(input={'job_description': jd, 'link_list': links})

        return res
    