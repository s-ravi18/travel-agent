# VoyageCompass Travel Planner

A Streamlit travel planning app built with LangChain and OpenAI.

It is inspired by AI travel-agent demos, but it uses a different app structure and planning flow:

- OpenAI `ChatOpenAI` through the `langchain-openai` package
- Streamlit trip brief plus follow-up chat
- OpenAI API key required
- No required search or weather API keys beyond `OPENAI_API_KEY`
- Tools for geocoding, near-term weather, web research, currency conversion, budget estimates, and packing prep

## Setup

```bash
cd simple_ai_agents/nebius_travel_planner

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

cp env.example .env