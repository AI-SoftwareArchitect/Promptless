from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from scheduled_api import ScheduledAPI
from strawberry_types import schema
from ai_agent import AIThinker
from ollama_strategy import OllamaStrategy
from strategy import IAIServiceStrategy
import threading
import uvicorn

file_paths = ["commands.txt", "memory.txt", "errors.txt"]

# 1. Scheduler
scheduled_api = ScheduledAPI(file_paths)
scheduled_api.start()

# 2. FastAPI + CORS + GraphQL
app = FastAPI()
# React’in koştuğu portu ekliyoruz
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# 3. AIThinker ayrı thread’de
def start_ai_thinker():
    try:
        ollama_strategy: IAIServiceStrategy = OllamaStrategy(model_name="qwen2.5-coder:3b")
        thinker = AIThinker(strategy=ollama_strategy)
        thinker.start()
    except KeyboardInterrupt:
        print("AI Thinker stopped by user")
    except Exception as e:
        print(f"Error starting AI Thinker: {e}")

if __name__ == "__main__":
    # AIThinker'ı başlat
    threading.Thread(target=start_ai_thinker, daemon=True).start()
    # FastAPI server’ını 4000 portunda ayağa kaldır
    uvicorn.run(app, host="0.0.0.0", port=4000)
