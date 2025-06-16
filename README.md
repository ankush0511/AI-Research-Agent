![image](https://github.com/user-attachments/assets/e28a72e0-ef74-4353-9ced-256266b6db3a)


## 🧠 AI Research Agent

AI Research Agent is an automated research assistant built to streamline the discovery, ingestion, embedding, and intelligent querying of research data—particularly in the patent or scientific literature domain. It integrates LLMs with OpenSearch and RAG (Retrieval-Augmented Generation) to provide an end-to-end solution for patent analysis, semantic search, and report generation.

---

### 🔍 Features

* **Automated Data Ingestion:** Fetch and store research or patent documents.
* **Vector Embeddings:** Embed text using transformer models for semantic retrieval.
* **OpenSearch Integration:** Index and search documents via OpenSearch.
* **Agentic RAG System:** Uses Retrieval-Augmented Generation to answer complex queries over ingested documents.
* **Tool-Oriented Pipeline:** Includes specialized tools like `information_collector`, `patent_search_tools`, and more.
* **Docker Support:** Containerized setup for reproducibility and deployment.

---

### 📁 Project Structure

```
ai research agent/
│
├── agentic_rag.py               # Main RAG logic using agents
├── embedding.py                 # Code to generate vector embeddings
├── ingestion.py                 # Handles data ingestion into vector DB
├── information_collector.py    # Gathers external research information
├── opensearch_client.py        # Interface with OpenSearch
├── patent_search_tools.py      # Tools for structured patent search
├── patent_crew.py              # Possibly multi-agent crew architecture
├── requirements.txt            # Python dependencies
├── docker-compose.yaml         # Docker configuration
├── dev.ipynb                   # Development notebook for quick testing
└── .env                        # Environment variable configs
```

---

### ⚙️ Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Research-Agent.git
cd AI-Research-Agent/ai\ research\ agent
```

#### 2. Set Up Environment

Install Python packages:

```bash
pip install -r requirements.txt
```



---

### 🛠️ Core Technologies

* **Python**
* **LangChain / LLMs**
* **OpenSearch**
* **Docker**
* **RAG Pipeline**

---

## ⚙️ Configuration

### 🔐 Environment Variables (Optional)

Create a `.env` file in the root directory to include your API keys or configuration settings:

```dotenv
# Optional API keys
SERPAPI_API_KEY=your_key_here
```

### 🛠️ OpenSearch Setup

The system will automatically create the necessary indices in OpenSearch if they do not already exist.

---

## 🚀 Usage

### ▶️ Run the Main Application

To start the system:

```bash
python agentic_rag.py
```

This will launch a CLI menu with multiple options for interaction.

---

### 📋 Application Menu Options

#### 1. Run Complete Patent Trend Analysis and Forecasting

* Executes the **multi-agent workflow**
* Outputs **comprehensive analysis and predictions**
* Saves results to a **text file**

#### 2. Search for Specific Patents

* **Keyword-based search**
* **Semantic similarity-based search**
* **Hybrid search** (combining both techniques)

#### 3. Iterative Patent Exploration

* Refines search queries step-by-step
* Helps discover **related patents** and **emerging technologies**

#### 4. View System Status

* Check OpenSearch connection
* Verify Ollama model availability
* Test embedding system

---

## 🧪 Example Workflow

1. **Start the Application**

   ```bash
   python agentic_rag.py
   ```

2. **Check System Health**

   * Choose **Option 4: View System Status**

3. **Run Patent Analysis**

   * Choose **Option 1**
   * Enter your research topic (e.g., `"Lithium Battery"`)
   * Select a language model (e.g., `"llama2"`)


![image](https://github.com/user-attachments/assets/cbed4a73-94c8-4297-a4bf-cbed023797f1)

![image](https://github.com/user-attachments/assets/1229fffb-836c-499f-bee3-c28dc177568a)
