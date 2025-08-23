# src/config.py
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
EMBED_MODEL = os.getenv("EMBED_MODEL", "models/text-embedding-004")
GEN_MODEL = os.getenv("GEN_MODEL", "gemini-2.5-flash")
INDEX_DIR = os.getenv("INDEX_DIR", "./vectorstore")
KB_PATH = os.getenv("KB_PATH", "./data/kb.md")
TOP_K = int(os.getenv("TOP_K", 6))
MAX_CONTEXT_CHARS = int(os.getenv("MAX_CONTEXT_CHARS", 12000))
