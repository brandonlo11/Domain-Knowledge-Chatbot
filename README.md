# Domain-Knowledge-Chatbot

A knowledge-graph-powered chatbot for answering questions about the UCLA Course Catalog & Prerequisites. It uses Neo4j as a knowledge graph database and FastAPI for the chat API.

## What We've Accomplished
- Set up a local Neo4j database using Docker
- Created Python scripts to connect to Neo4j and ingest sample course/prerequisite data
- Built a FastAPI app with a `/chat` endpoint that answers questions about course prerequisites
- Implemented a simple rule-based retriever for course queries
- Verified end-to-end functionality with curl and Python test scripts

## Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop/)
- Python 3.8+
- pip (Python package manager)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Domain-Knowledge-Chatbot
```

### 2. Start Neo4j with Docker
Replace `your_password` with a password of your choice:
```bash
docker run \
  --name neo4j-local \
  -p7474:7474 -p7687:7687 \
  -d \
  -e NEO4J_AUTH=neo4j/your_password \
  -v $HOME/neo4j/data:/data \
  neo4j:5
```
- Access the Neo4j Browser at [http://localhost:7474](http://localhost:7474) (login: `neo4j` / `your_password`)

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```
If you don't have a `requirements.txt`, install manually:
```bash
pip install fastapi uvicorn neo4j
```

### 4. Ingest Sample Data
Update `ingest.py` with your Neo4j password, then run:
```bash
python ingest.py
```
This will add sample UCLA CS courses and their prerequisites to the database.

### 5. Run the FastAPI Server
Update `retriever.py` with your Neo4j password, then start the server:
```bash
uvicorn app:app --reload
```
The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 6. Test the Chatbot Endpoint
Use curl or Postman:
```bash
curl -X POST "http://127.0.0.1:8000/chat" -H "Content-Type: application/json" -d '{"question": "What are the prerequisites for CS 180?"}'
```

## Troubleshooting
- **Connection refused:** Make sure the Neo4j Docker container is running and you are using the correct password.
- **No data returned:** Ensure you have ingested data and are querying the correct database.
- **Course not found:** Check for typos or punctuation in your question; the chatbot expects course codes like `CS 180`.

## Next Steps
- Expand the retriever to handle more question types
- Add more data (departments, instructors, etc.)
- Improve natural language understanding
- Add a frontend UI

---
Feel free to open issues or contribute improvements!