import os
from langchain_community.document_loaders import WebBaseLoader

# Seting User-Agent in the environment variable
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

# Define the website URL
url = "https://brainlox.com/courses/category/technical"

# Loading data from the website
loader = WebBaseLoader(url)
docs = loader.load()

# Saving extracted text to a file for review
with open("scraped_data.txt", "w", encoding="utf-8") as f:
    f.write(docs[0].page_content)

print("Data extracted and saved to scraped_data.txt")