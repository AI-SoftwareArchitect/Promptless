import re
import time
from agent_memory import Memory
from docker_operations import DockerizedAIExecutor
from strategy import IAIServiceStrategy

class AIThinker:
    def __init__(self, strategy: IAIServiceStrategy):
        self.strategy = strategy
        self.memory = Memory()

    def think_and_execute(self):
        try:
            # 1) Modelden raw çıktı al
            raw = self.strategy.think()
            print(f"AI Raw Output: {raw}")

            # 2) [command] ve [memory] bölümlerini ayıkla
            m = re.search(r"\[command\]:\s*(.+?)\s*\[memory\]:\s*(.+)", raw, re.DOTALL)
            if not m:
                print("⚠️ Format hatası: Beklenen `[command]: ... [memory]: ...` yapısı bulunamadı.")
                self.memory.add(f"Unparsable output: {raw[:100]}...")  # ilk 100 karakteri hafızaya al
                return  # Uygulama çökmeden devam et

            command = m.group(1).strip()
            mem_note = m.group(2).strip()

            # 3) Komutu çalıştır ve sonucu yazdır
            output = DockerizedAIExecutor.execute(command)
            print(f"Executed Command: {command}\nOutput: {output}")

            # 4) Memory'e sadece mem_note'u ekle
            self.memory.add(mem_note)

        except Exception as e:
            print(f"🔥 Hata oluştu: {e}")
            self.memory.add(f"Exception occurred: {str(e)}")


    def start(self):
        while True:
            self.think_and_execute()
            time.sleep(3)
