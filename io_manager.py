import os
import tempfile

class IOManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def write(self, data):
        dir_name = os.path.dirname(self.file_path) or '.'
        with tempfile.NamedTemporaryFile('w', dir=dir_name, delete=False) as tmp_file:
            tmp_file.write(data)
            temp_name = tmp_file.name
        os.replace(temp_name, self.file_path)  

    def append(self, data):
        content = ''
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                content = file.read()
        content += data
        self.write(content)  
