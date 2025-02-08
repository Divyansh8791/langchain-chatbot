import os
import pickle
from sentence_transformers import SentenceTransformer

# Define model file path
model_path = "embedding_model.pkl"

# Check if model exists
if not os.path.exists(model_path):
    print("Downloading and saving model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Save model using pickle
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print("Model saved successfully!")
else:
    print("Model already exists.")
