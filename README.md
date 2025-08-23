# 🏢 SureLife Insurance Agent

An intelligent AI-powered insurance assistant built with Google Gemini, designed to provide accurate information about SureLife Insurance Ltd. products, policies, and services using a knowledge base and vector search capabilities.

## 🚀 Features

- **AI-Powered Responses**: Uses Google Gemini 2.5 Flash for intelligent, context-aware answers
- **Knowledge Base Integration**: Comprehensive insurance knowledge base with vector search
- **Semantic Search**: FAISS-based vector similarity search for relevant information retrieval
- **Interactive Interface**: Command-line interface for direct interaction with the agent
- **Configurable**: Environment-based configuration for API keys and model settings

## 🏗️ Architecture

The project follows a modular architecture with the following components:

- **`agent.py`**: Main agent logic that orchestrates query processing and response generation
- **`retriever.py`**: Vector search implementation using FAISS for document retrieval
- **`ingest.py`**: Knowledge base ingestion and vector index building
- **`config.py`**: Configuration management and environment variables
- **`api.py`**: FastAPI web interface (placeholder for future development)
- **`intent.py`**: Intent classification (placeholder for future development)

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API key
- Virtual environment (recommended)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Blazious/customer-support-agent.bmm.git
   cd customer-support-agent.bmm
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   EMBED_MODEL=models/text-embedding-004
   GEN_MODEL=gemini-2.5-flash
   INDEX_DIR=./vectorstore
   KB_PATH=./data/kb.md
   TOP_K=6
   MAX_CONTEXT_CHARS=12000
   ```
   
   **⚠️ IMPORTANT: You MUST get your own Google Gemini API key:**
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Create a new API key
   - **Never share your API key or commit it to version control**

## 🔧 Setup

1. **Build the vector index**
   ```bash
   python src/ingest.py
   ```
   This will create a FAISS index from the knowledge base in `data/kb.md`.

2. **Verify the setup**
   ```bash
   python src/retriever.py
   ```
   This will test the retrieval system with a sample query.

## 🚀 Usage

### Interactive Mode
Run the agent in interactive mode:
```bash
python src/agent.py
```

Example interaction:
```
Interactive Agent (type 'exit' to quit)

Enter your question: What is the claims process?

Agent: [AI response based on knowledge base]

Enter your question: exit
```

### Programmatic Usage
```python
from src.agent import ask_agent

# Ask a question
response = ask_agent("What are the health insurance plans?")
print(response)
```

## 📚 Knowledge Base

The system includes a comprehensive knowledge base covering:
- Company profile and leadership
- Product specifications (Health, Life, Motor, Property insurance)
- Claims processes and procedures
- Customer service information
- Regulatory compliance details

The knowledge base is stored in `data/kb.md` and automatically indexed for vector search.

## 🔍 How It Works

1. **Query Processing**: User input is received and processed
2. **Vector Search**: Query is embedded and compared against indexed documents
3. **Context Retrieval**: Top-k most relevant documents are retrieved
4. **Prompt Construction**: Context and query are combined into a structured prompt
5. **AI Generation**: Google Gemini generates a response based on the context
6. **Response Delivery**: Generated answer is returned to the user

## ⚙️ Configuration

Key configuration options in `config.py`:

- `GEMINI_API_KEY`: Your Google Gemini API key
- `EMBED_MODEL`: Embedding model for vector generation
- `GEN_MODEL`: Generation model for responses
- `TOP_K`: Number of documents to retrieve for context
- `MAX_CONTEXT_CHARS`: Maximum characters for context inclusion

## 🧪 Testing

Test individual components:

```bash
# Test retrieval system
python src/retriever.py

# Test knowledge base ingestion
python src/ingest.py

# Test full agent
python src/agent.py
```

## 📁 Project Structure

```
customer-support-agent.bmm/
├── data/
│   └── kb.md                 # Knowledge base
├── src/
│   ├── agent.py             # Main agent logic
│   ├── retriever.py         # Vector search implementation
│   ├── ingest.py            # Knowledge base ingestion
│   ├── config.py            # Configuration management
│   ├── api.py               # FastAPI interface (placeholder)
│   ├── intent.py            # Intent classification (placeholder)
│   ├── prompts.py           # Prompt templates (placeholder)
│   └── tools.py             # Utility functions (placeholder)
├── vectorstore/             # Generated vector index
├── requirements.txt          # Python dependencies
├── README.md                # This file
└── .env                     # Environment variables (create this)
```

## 🔮 Future Enhancements

- **Web Interface**: FastAPI-based REST API
- **Intent Classification**: Better understanding of user intent
- **Multi-modal Support**: Image and document processing
- **Conversation Memory**: Context-aware conversations
- **Analytics Dashboard**: Usage statistics and insights

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is proprietary software for SureLife Insurance Ltd.

## 🆘 Support

For technical support or questions about the SureLife Agent:
- Contact: IT Department
- Email: it@surelife.co.ke
- Phone: +254 700 123 456

## 🔐 Security Notes

- **Never commit your `.env` file or API keys**
- **Keep your Gemini API key secure and private**
- **Each user must get their own API key from Google AI Studio**
- **Never share your API key with others**
- **Regularly rotate API keys for security**
- **Monitor API usage and costs in your Google Cloud Console**
- **Your API key gives access to your billing account - keep it safe!**

---

**Built with ❤️ for SureLife Insurance Ltd.**
