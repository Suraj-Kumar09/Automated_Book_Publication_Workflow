uvicorn.run(app, host="127.0.0.1", port=8000)
import uvicorn
import sys
import os

# 🔧 Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.agentic_api.api_router import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
