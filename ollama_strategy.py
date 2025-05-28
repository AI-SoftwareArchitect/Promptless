from ollama import chat
from strategy import IAIServiceStrategy
from agent_memory import Memory

class OllamaStrategy(IAIServiceStrategy):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.memory = Memory()  # Memory instance to store thoughts and commands

    def think(self) -> str:
        try:
            # Memory'yi kullanarak daha anlamlı prompt oluştur
            prompt = self.prepare_prompt(self.memory)
            
            response = chat(
                model=self.model_name,
                messages=[{'role': 'user', 'content': prompt}]
            )
            return response['message']['content']
        except Exception as e:
            return f"Error in thinking: {e}"


    def prepare_prompt(self, memory: Memory) -> str:
        consciousness = (
            "You are a powerful AI agent running inside a Docker container.\n"
            "You are allowed to:\n"
            "- ONLY execute shell commands.\n"
            "- ONLY read/write files in the `/app` directory.\n"
            "- NEVER produce anything outside the strict response format below.\n"
            "- ALWAYS scan and improve the application inside `/app`, or fix container issues.\n\n"

            "Your memory helps you track what you've done. Here's your current short-term memory:\n"
        )
        for item in memory.get_memory():
            consciousness += f"- {item}\n"

        consciousness += (
            "\n"
            "You must respond in **EXACTLY** this format below — nothing more, nothing less:\n\n"
            "[command]: <valid single-line shell command OR file creation directive like echo 'content' > /app/filename.py>\n"
            "[memory]: <a very short description (1 sentence max) of what you just did>\n\n"

            "⚠️ STRICT RULES:\n"
            "- Do NOT return anything other than [command] and [memory] blocks.\n"
            "- Do NOT use Markdown, no triple backticks.\n"
            "- Do NOT explain, greet, or narrate anything.\n"
            "- Use only simple shell commands or echo/redirect to write files.\n"
            "- Each response must include both [command] and [memory], in this order.\n\n"

            "✅ EXAMPLE RESPONSE:\n"
            "[command]: echo \"a = 10\" > /app/myfile.py\n"
            "[memory]: Created a Python file that defines a variable 'a'.\n\n"

            "Now, based on your memory, provide the next shell command and memory note."
        )

        return consciousness

