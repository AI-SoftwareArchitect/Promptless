import docker

class DockerizedAIExecutor:
    CONTAINER_ID = "2d7b07a048b8" 

    @staticmethod
    def execute(command: str):
        try:
            client = docker.from_env()
            container = client.containers.get(DockerizedAIExecutor.CONTAINER_ID)
            result = container.exec_run(f"sh -c '{command}'", stdout=True, stderr=True)
            decoded = result.output.decode("utf-8")
            if result.exit_code != 0:
                print(f"Command failed with exit code {result.exit_code}: {decoded}")
                return f"Error: {decoded}"
            else:
                print(f"Command output: {result.output.decode('utf-8')}")
                return decoded
        except Exception as e:
            print(f"Docker execution error: {e}")
            return f"Error: {e}"