from flask import Flask, request, jsonify
from qdrant_client import QdrantClient  
import pickle

app = Flask(__name__)

# Loading Qdrant client
client = QdrantClient("http://localhost:6333") 
COLLECTION_NAME = "brainlox_courses"

# Loading embedding model
with open("embedding_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/query", methods=["POST"])
def query_chatbot():
    data = request.json
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Query parameter is required"}), 400

    # Converting query to embedding
    query_embedding = model.encode([user_query]).tolist()[0]

    # Searching in Qdrant
    search_result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=3  # Get top 3 results
    )

    # Extracting matched results
    results = [{"text": hit.payload["text"], "score": hit.score} for hit in search_result]

    return jsonify({"query": user_query, "results": results})

if __name__ == "__main__":
    app.run(debug=True)