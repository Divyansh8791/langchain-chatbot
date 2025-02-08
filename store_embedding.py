from qdrant_client import QdrantClient  
from qdrant_client.models import VectorParams, PointStruct  
import pickle
# Initialize Qdrant client
client = QdrantClient("http://localhost:6333")  

# Defining collection name
COLLECTION_NAME = "brainlox_courses"

# Loading the extracted data
with open("scraped_data.txt", "r", encoding="utf-8") as f:
    text_data = f.read()


text_chunks = text_data.split("\n")  

# Loading sentence transformer model
with open("embedding_model.pkl", "rb") as f:
    model = pickle.load(f)

# Converting text chunks into embeddings
embeddings = model.encode(text_chunks).tolist()

# Creating a collection in Qdrant
client.delete_collection(collection_name = COLLECTION_NAME)
client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=len(embeddings[0]), distance="Cosine")
)

print("Storing the embeddings.")
# Inserting embeddings into Qdrant
client.upsert(
    collection_name=COLLECTION_NAME,
    points=[
        PointStruct(id=i, vector=embedding, payload={"text": text_chunks[i]})  
        for i, embedding in enumerate(embeddings)
    ]
)

print(f"Stored {len(embeddings)} embeddings in Qdrant!")