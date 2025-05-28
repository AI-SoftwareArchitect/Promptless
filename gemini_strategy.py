import requests
from agent_memory import Memory

from strategy import IAIServiceStrategy

class GeminiStrategy(IAIServiceStrategy):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def think(self) -> str:
        response = requests.post(
            "https://gemini.googleapis.com/v1/think",
            json={"apiKey": self.api_key}
        )
        return response.text

    def execute_command(self, command: str):
        requests.post(
            "https://gemini.googleapis.com/v1/execute",
            json={"command": command}
        )

    def prepare_prompt(self,memory: Memory) -> str:
        raise NotImplementedError("prepare_prompt method is not implemented for GeminiStrategy")
