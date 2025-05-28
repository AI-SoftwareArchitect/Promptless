from ai_agent import AIThinker
from ollama_strategy import OllamaStrategy
from strategy import IAIServiceStrategy

if __name__ == "__main__":
    try:
        ollama_strategy: IAIServiceStrategy = OllamaStrategy(model_name="qwen2.5-coder:3b")
        thinker = AIThinker(strategy=ollama_strategy)
        thinker.start()
    except KeyboardInterrupt:
        print("AI Thinker stopped by user")
    except Exception as e:
        print(f"Error starting AI Thinker: {e}")