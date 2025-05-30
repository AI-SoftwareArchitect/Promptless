**Promptless** is a self-thinking, autonomous AI agent that monitors and maintains applications running inside Docker containers — completely **prompt-free**.  
It detects anomalies, errors, vulnerabilities, and can even generate or improve applications on its own inside a containerized environment.

⚠️ Caution: This software may cause unintended effects or issues when running inside Docker containers. Please thoroughly test before using in production environments.

##

![Promptless](promptless_logo.png)

---

## Features

-  **Autonomous Thinking:** Thinks and acts without external prompts.  
-  **Docker Intelligence:** Monitors running containers, executes shell commands, detects issues.  
-  **Self-Healing:** Fixes common container-related problems automatically.  
-  **App Improvement:** Continuously improves code or generates new applications inside `/app` folder.  
-  **Short-Term Memory:** Stores past thoughts and actions to guide future decisions.  
-  **Secure & Isolated:** Operates within a container with limited permissions.
-  **Dashboard (Reactjs & GraphQL)** Sends data and see visually errors , memory of ai agent and commands performed.

---

## Project Structure

Promptless/
├── ai_agent.py # Core AI loop that thinks and executes
├── agent_memory.py # In-memory short-term memory manager
├── docker_operations.py # Docker exec command runner
├── strategy.py # Strategy pattern interface
├── ollama_strategy.py # Ollama-based LLM strategy
├── main.py # Entry point

##

![Image](promptless.png)

Promptless Dashboard UI

##
![Image 1](1.png)

##

![Image 2](2.png)
