from io_manager import IOManager
import threading
import time
from global_state import file_contents, lock

class ScheduledAPI:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.io_managers = [IOManager(fp) for fp in file_paths]

    def scheduled_task(self):
        while True:
            for io_manager, fp in zip(self.io_managers, self.file_paths):
                try:
                    content = io_manager.read()
                except FileNotFoundError:
                    content = ""
                with lock:
                    file_contents[fp] = content
            time.sleep(3)

    def start(self):
        t = threading.Thread(target=self.scheduled_task, daemon=True)
        t.start()
