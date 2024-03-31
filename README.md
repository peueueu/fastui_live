# Server Driven User Interface

This is a project that uses SDUI's, the FE will only handle with the renderization of the components,
All of the components will be sended by the BE, leaving for the FE only the responsability to render it.

Absolutely! Here's a README.md tailored for your existing FastAPI project that's already running:

## FastAPI Project with File Uploads

This project is a FastAPI application that leverages various functionalities:

* **FastAPI:** A high-performance framework for building APIs in Python.
* **Uvicorn:** An ASGI server for running FastAPI applications.
* **python-multipart:** Enables handling multipart form data submissions.

### Project Overview

This project utilizes FastAPI to create a web API. The functionalities and features are implemented within the `main.py` file. You can extend and modify this file to create your desired API endpoints.

### Installation (Optional)

**Prerequisites:**

* **Poetry (if used):** Ensure Poetry is installed and added to your PATH environment variable. Refer to [https://python-poetry.org/docs/](https://python-poetry.org/docs/) for installation instructions.

* **Python Version:** Verify you have the appropriate Python version installed (check with `python --version`). The project likely uses Python 3.12.1 based on your previous information.

**If you haven't already set up the environment and you want to recreate it:**

1. **Create a virtual environment (optional, but recommended):**

   Poetry automatically creates a virtual environment by default. You can skip this step if you prefer a global environment.

2. **Install dependencies (using Poetry, if applicable):**

   ```bash
   poetry install
   ```

**If you're using a different environment management tool or have a pre-existing environment:**

* Refer to your environment management tool's documentation for installation instructions.
* Ensure the necessary dependencies (FastAPI, Uvicorn, python-multipart) are installed.

### Running the Application

1. **Start the development server:**

   If you're using Poetry:

   ```bash
   poetry run uvicorn main:app --reload
   ```

   Otherwise, assuming `main.py` is your main application file:

   ```bash
   uvicorn main:app --reload
   ```

   * `main:app` specifies the module (`main.py`) containing the FastAPI application (`app`).
   * `--reload` enables automatic server restart whenever you make changes to the code.

**Consult `main.py` for specific API endpoint details and usage instructions.**

### Project Structure

```text
fastui_live/
├── main.py        # The core FastAPI application file
├── pyproject.toml  # Poetry configuration file (if using Poetry)
└── README.md      # This file (instructions)
```
