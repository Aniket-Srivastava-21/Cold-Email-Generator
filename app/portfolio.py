import pandas as pd
import uuid
import chromadb

class Portfolio:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.client = chromadb.PersistentClient("Vector_Store")
        self.portfolio = self.client.get_or_create_collection("portfolios")

    def load_portfolio(self):
        if not self.portfolio.count():
            for idx, row in self.df.iterrows():
                self.portfolio.add(
                    documents=row["Techstack"],
                    metadatas={"url": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )
        
    def query_links(self, requirements):
        query_output = self.portfolio.query(query_texts=requirements, n_results=2)
        links = query_output['metadatas']
        return links