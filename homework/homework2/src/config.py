from pathlib import Path
import os
from dotenv import load_dotenv

_ROOT = Path(__file__).resolve().parents[1]

def load_env() -> bool:
    """Load environment variables from homework/homework2/.env"""
    env_path = _ROOT / ".env"
    if env_path.exists():
        load_dotenv(env_path)
        return True
    return False

def get_key(name: str, default=None):
    """Fetch a single key from the environment."""
    return os.getenv(name, default)

def get_data_dir() -> Path:
    """Resolve DATA_DIR from .env, defaulting to ./data."""
    data_dir = os.getenv("DATA_DIR", str(_ROOT / "data"))
    return Path(data_dir).resolve()
