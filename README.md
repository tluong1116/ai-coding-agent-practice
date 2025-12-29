# Gemini AI Coding Agent

This project is a Python-based AI agent that utilizes the **Google Gemini API** to interact with a local file system through autonomous function calling. The agent can reason through tasks, read or write code, and execute Python scripts within a secured working directory.

## 🚀 Features

* **Autonomous Iteration**: Uses a loop to handle multi-step reasoning and function execution until the task is complete.
* **File Management Tools**:
    * **List Files**: Inspect directory contents and file metadata.
    * **Read Content**: Extract text from files with safety limits on character count.
    * **Write Files**: Create or update files and automatically generate necessary parent directories.
* **Code Execution**: Runs Python scripts locally and returns the output (STDOUT/STDERR) directly to the AI for debugging or verification.
* **Security Scoping**: Restricts all file operations to a specific working directory (e.g., `./calculator`) to prevent unauthorized file system access.


## 🛠️ Technical Stack

* **LLM**: Google Gemini (`gemini-2.5-flash-lite`).
* **SDK**: `google-genai`.
* **Package Manager**: `uv`
* **Logic**: Python 3.13 with `subprocess` for script execution and `argparse` for CLI interactions.

## 📂 Project Structure

* `main.py`: The core engine managing the conversation loop and API interactions.
* `call_functions.py`: The dispatcher that maps Gemini's function calls to local Python logic.
* `config.py`: Contains global settings such as character limits for file reading.
* `functions/`: A directory containing the individual tool implementations.

## ⚙️ Setup

1.  **Environment Variables**: Create a `.env` file and add your Gemini API key:
    ```env
    GEMINI_API_KEY=your_api_key_here
    ```
2.  **Installation**: 
    If you have `uv` installed, you do not need to manually install dependencies. `uv` will automatically create a virtual environment and sync your packages based on the included `uv.lock` file the first time you run the project.

## 📖 Usage

Use `uv run` to execute the agent. This command automatically manages the virtual environment for you:

```bash
uv run main.py "Your prompt here" --verbose
The --verbose flag provides detailed logs of token counts and function calls.
