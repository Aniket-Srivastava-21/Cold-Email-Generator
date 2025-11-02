import streamlit as st
from chain import Chain
from portfolio import Portfolio
from utils import clean_text
from langchain_community.document_loaders import WebBaseLoader

PORTFOLIO_FILE_PATH = "app/resources/my_portfolio.csv"

def generate_email(new_chain, portfolio):
    st.set_page_config(page_title="Cold Email Generator", page_icon=":email:", layout="centered")
    st.title("Cold Email Generator")

    url_input = st.text_input("Enter URL:", value="", placeholder="For Example: https://example.com/job-14693/")

    submit_button = st.button("Submit")

    if submit_button:
        st.write("Processing URL:", url_input)

        loader = WebBaseLoader(url_input)
        page_data = loader.load().pop().page_content

        print("Page Data:", page_data[:100])

        st.write("Cleaning text from page data...")
        cleaned_text = clean_text(page_data)
        jobs = new_chain.extract_requirements(cleaned_text)

        if not jobs:
            st.error("No job postings found in the provided URL.")
            return
        
        if 'job_postings' not in jobs:
            jobs = {"job_postings": [jobs]}

        st.write("Extracted Job Postings:", jobs)

        for job in jobs["job_postings"]:
            st.write("Extracted Requirements:")
            st.json(job)
            links = portfolio.query_links(job['skills'])
            st.write("Relevant Links:")
            st.json(links)
            response = new_chain.write_email(job, links)
            email = response.content
            st.write("Generated Email:")
            st.text_area(" ", email, height=500, key="email_output")

if __name__ == "__main__":
    new_chain = Chain()
    portfolio = Portfolio(PORTFOLIO_FILE_PATH)
    portfolio.load_portfolio()
    generate_email(new_chain, portfolio)