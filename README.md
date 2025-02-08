# Langchain Chatbot
 
## 📌 Overview
This is a custom AI chatbot built using **Langchain, Qdrant, and Flask**. It extracts technical course data from **Brainlox**, generates embeddings, and stores them in a vector database for efficient semantic search. The chatbot responds to user queries by retrieving the most relevant course information.

## 🚀 Features
- Extracts course data from **Brainlox** using Langchain URL loaders.
- Generates embeddings and stores them in **Qdrant** vector database.
- Implements a **Flask RESTful API** to handle chatbot queries.
- Retrieves the most relevant course information based on user queries.

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/langchain-chatbot.git
cd langchain-chatbot
```

### 2️⃣ Start Qdrant (if running locally)
```bash
docker run -p 6333:6333 qdrant/qdrant
```

### 3️⃣ Run Data Extraction (Only Once)
```bash
python extract_data.py
```

### 4️⃣ Start the Flask API
```bash
python app.py
```


## 📡 API Usage
Send a **POST** request to query the chatbot:

```bash
curl -X POST "http://127.0.0.1:5000/query" \
     -H "Content-Type: application/json" \
     -d '{"query": "What courses are available?"}'
```

### Sample JSON Response
```json
{
    "query": "What courses are available?",
    "results": [
        {"text": "Python for Beginners", "score": 0.92},
        {"text": "Machine Learning Basics", "score": 0.89},
        {"text": "Deep Learning with TensorFlow", "score": 0.85}
    ]
}
```

## 🏗️ Project Structure
```
📦 langchain-chatbot
│── ├── app.py                # Flask chatbot API
│── ├── extract_data.py        # Data extraction script
│── ├── store_embedding.py     # Embedding Storing script
│── ├── load_model.py         # Embedding Model loading script
│── ├── README.md              # Documentation
```

## 📝 Future Enhancements
- Add **memory** to track conversation history.
- Integrate with **LLMs** for better responses.
- Deploy API to **Cloud (AWS/GCP)**.

## 💡 Contributing
Feel free to fork this repo, make improvements, and submit a pull request! 😊

## 📄 License
This project is licensed under the **MIT License**.


