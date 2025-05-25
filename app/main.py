import streamlit as st
from chain import Chain
from portfolio import Portfolio
from utils import clean_text
from langchain_community.document_loaders import WebBaseLoader

PORTFOLIO_FILE_PATH = "app/resources/my_portfolio.csv"

def generate_email(portfolio_file_path):
    st.title("Cold Email Generator")

    url_input = st.text_input("Enter URL:", value="For Example: https://example.com/job-14693/")

    submit_button = st.button("Submit")

    if submit_button:
        # loader = WebBaseLoader('https://www.google.com/about/careers/applications/jobs/results/126881918376387270-cloud-engineer-ai?q=%22Data%20Scientist%22&location=Bengaluru%2C%20India&target_level=EARLY')
        loader = WebBaseLoader(url_input)
        page_data = loader.load().pop().page_content
        cleaned_text = clean_text(page_data)
        new_chain = Chain()
        requirements = new_chain.extract_requirements(cleaned_text)
        portfolio = Portfolio(portfolio_file_path)
        portfolio.load_portfolio()
        print(requirements)
        links = portfolio.query_links(requirements['skills'])
        response = new_chain.write_email(requirements, links)
        email = response.content

        st.code(email, language="Markdown")

if __name__ == "__main__":
    generate_email(PORTFOLIO_FILE_PATH)