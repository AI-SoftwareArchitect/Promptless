import re
import time
from docker_operations import DockerizedAIExecutor
from agent_memory import Memory
from io_manager import IOManager
from strategy import IAIServiceStrategy

class AIThinker:
    def __init__(self, strategy: IAIServiceStrategy):
        self.strategy = strategy
        self.memory = Memory()
        # Her dosya için ayrı manager
        self.io_manager_commands = IOManager(file_path="commands.txt")
        self.io_manager_memory   = IOManager(file_path="memory.txt")
        self.io_manager_errors   = IOManager(file_path="errors.txt")
        self.waiting_time = 5

    def think_and_execute(self):
        try:
            raw = self.strategy.think()
            print(f"AI Raw Output: {raw}")

            m = re.search(r"\[command\]:\s*(.+?)\s*\[memory\]:\s*(.+)", raw, re.DOTALL)
            if not m:
                note = f"Unparsable output: {raw[:100]}..."
                print("⚠️ Format hatası:", note)
                self.memory.add(note)
                self.io_manager_errors.append(note + "\n")
                return

            command = m.group(1).strip()
            mem_note = m.group(2).strip()

            # Komutu çalıştır
            output = DockerizedAIExecutor.execute(command)
            print(f"Executed Command: {command}\nOutput: {output}")
            # Komut çıktılarını commands.txt’e
            self.io_manager_commands.append(f"Command: {command}\nOutput: {output}\n")

            # Hafızaya ekle ve memory.txt’e yaz
            self.memory.add(mem_note)
            self.io_manager_memory.append(f"Memory Note: {mem_note}\n")

        except Exception as e:
            err = f"Exception occurred: {e}"
            print(f"🔥 Hata oluştu: {err}")
            self.memory.add(err)
            self.io_manager_errors.append(err + "\n")

    def start(self):
        while True:
            self.think_and_execute()
            time.sleep(self.waiting_time)
