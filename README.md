# Counsellor Bot Demo
## How to Run:
1. Instal Ollama server from the official website: [Ollama](https://ollama.com/)
2. `git clone` this repo
3. `cd` into the cloned repo, run `pip install -r requirements.txt`
4. Run `streamlit run streamlit_app.py` for deploying on your local machine (for on-server deployment, Ollama needs to be deployed on a cloud VM and the IP must be taken, and the base URL must be updated in `llm_interface.py`)