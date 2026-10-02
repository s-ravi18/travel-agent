# VoyageCompass Travel Planner

An AI-powered travel planning application built with **Python, Streamlit, LangChain, and OpenAI**.

VoyageCompass uses an LLM-based agent that understands a user's travel requirements, decides which tools are needed, calls those tools, and combines their results into a personalized travel itinerary.

The project is designed as a practical example of an **agentic AI system using tool calling**.

---

## Features

- AI-generated personalized travel itineraries
- Interactive Streamlit interface
- Follow-up conversation for refining travel plans
- OpenAI-powered LangChain agent
- Function/tool calling
- Destination geocoding
- Near-term weather information
- Web-based destination research
- Currency conversion
- Daily and total budget estimation
- Packing and preparation recommendations
- Support for travel preferences and constraints
- CLI support for testing the agent without Streamlit

---

## Architecture

The application follows a simple agentic architecture:

```text
                         User
                          |
                          v
                   Streamlit UI
                          |
                          v
                  LangChain Agent
                          |
                          v
                     OpenAI LLM
                          |
              +-----------+-----------+
              |           |           |
              v           v           v
           Weather    Web Search   Currency
              |           |           |
              +-----------+-----------+
                          |
              +-----------+-----------+
              |           |           |
              v           v           v
          Geocoding    Budgeting   Packing
                          |
                          v
                     Tool Results
                          |
                          v
                     OpenAI LLM
                          |
                          v
                  Final Travel Plan
```

The LLM acts as the decision-making layer. It determines which tools are required, calls them, receives their results, and uses the information to generate the final travel plan.

---

## Agent Workflow

A typical request follows this flow:

```text
User Request
     |
     v
Understand travel requirements
     |
     v
Decide which tools are required
     |
     +----> Geocoding
     |
     +----> Weather
     |
     +----> Web Research
     |
     +----> Currency Conversion
     |
     +----> Budget Estimation
     |
     +----> Packing Recommendations
     |
     v
Combine tool results
     |
     v
Generate final travel itinerary
```

For example:

> "Plan a 5-day trip to Kyoto for two people from Bangalore with a budget of ₹1,00,000. We enjoy food, history and nature."

The agent can determine that it needs destination information, weather, web research, currency conversion, and budget estimation before generating the itinerary.

---

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Agent Framework | LangChain |
| LLM Provider | OpenAI |
| LLM Integration | `langchain-openai` |
| Language | Python |
| Weather | Open-Meteo |
| Geocoding | Open-Meteo |
| Web Research | DuckDuckGo |
| Currency | Frankfurter |

---

## Project Structure

```text
travel-agent/
│
├── app.py
├── agent.py
├── tools.py
├── main.py
├── requirements.txt
├── env.example
├── .gitignore
└── README.md
```

### `app.py`

Streamlit application and user interface.

Responsible for:

- Collecting trip requirements
- Displaying the generated itinerary
- Handling follow-up questions
- Maintaining conversation state

### `agent.py`

Core agent configuration.

Responsible for:

- Initializing the OpenAI model
- Creating the LangChain agent
- Defining the system prompt
- Connecting the agent to available tools

### `tools.py`

Contains the tools available to the agent:

- `geocode_destination`
- `get_weather_summary`
- `destination_research`
- `convert_currency`
- `estimate_daily_budget`
- `packing_and_prep_list`

### `main.py`

Optional command-line interface for testing the agent without Streamlit.

### `env.example`

Template for environment variables required by the application.

---

## Setup

Clone the repository:

```bash
git clone https://github.com/<YOUR_USERNAME>/travel-agent.git
cd travel-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the environment file:

```bash
cp env.example .env
```

---

## Environment Variables

Add your OpenAI API key to `.env`:

```env
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL=gpt-5.6-luna
```

The `.env` file is included in `.gitignore` and should **never be committed to the repository**.

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

You can provide information such as:

```text
Destination: Kyoto
Origin: Bangalore
Dates: 10 Oct - 15 Oct
Travelers: 2
Budget: ₹1,00,000
Travel Style: Standard
Interests: Food, History, Nature
Constraints: Avoid excessive walking
```

The agent will use the available tools to generate a personalized itinerary.

---

## Running from the Command Line

The agent can also be tested without Streamlit:

```bash
python main.py "Plan a 3-day trip to Rome for two people with a budget of $1500"
```

If no prompt is provided, `main.py` uses a default travel request.

---

## Available Tools

### 1. Geocoding

Converts a destination name into geographical information such as:

- Latitude
- Longitude
- Country
- State
- Timezone

Used when geographical information is required by other tools.

### 2. Weather

Retrieves near-term weather information using Open-Meteo.

The tool can provide:

- Minimum temperature
- Maximum temperature
- Precipitation probability
- Weather conditions

Weather forecasts are limited to the available forecast window.

### 3. Destination Research

Uses web search to obtain current information about destinations.

It can be used for:

- Attractions
- Neighborhoods
- Restaurants
- Activities
- Travel recommendations
- Destination-specific information

### 4. Currency Conversion

Uses the Frankfurter API to obtain exchange rates and convert between currencies.

### 5. Budget Estimation

Provides an estimated travel budget based on:

- Number of travelers
- Number of days
- Travel style
- Accommodation
- Food
- Transportation
- Activities

A contingency component is also included in the estimate.

### 6. Packing & Preparation

Generates packing recommendations based on planned activities and trip duration.

For example, hiking may result in recommendations for:

- Walking shoes
- Daypack
- Water bottle
- Rain protection

---

## Why This Is an Agent

A traditional LLM application might look like:

```text
User → Prompt → LLM → Answer
```

VoyageCompass uses an agentic architecture:

```text
User
 ↓
LLM Agent
 ↓
Decide which tool is needed
 ↓
Call tool
 ↓
Receive result
 ↓
LLM
 ↓
Decide next action
 ↓
...
 ↓
Final answer
```

The LLM is not responsible for performing every operation itself.

Instead:

```text
LLM
→ decides what needs to be done

Tools
→ perform deterministic or external operations

LLM
→ interprets the results and generates the response
```

This makes the system useful for tasks that require external information or calculations.

---

## Example

Input:

```text
Plan a 4-day trip to Tokyo for two people.
Budget: $2,000
Interests: Food, culture and technology.
```

The agent may perform:

```text
1. Research Tokyo
2. Check available weather information
3. Estimate the trip budget
4. Convert currencies if required
5. Generate packing recommendations
6. Combine the results
7. Generate the final itinerary
```

The exact tools used depend on the user's request.

---

## Agent Execution

The CLI version can expose the agent's observable execution steps, including model and tool updates.

Conceptually:

```text
User Request
     |
     v
OpenAI Model
     |
     v
Tool Selection
     |
     +----> destination_research()
     |
     +----> get_weather_summary()
     |
     +----> estimate_daily_budget()
     |
     v
Tool Results
     |
     v
OpenAI Model
     |
     v
Final Answer
```

These execution steps represent tool calls and tool results rather than the model's private chain-of-thought.

---

## Key Learning Concepts

This project demonstrates several important concepts in agentic AI:

- LLM-based agents
- Tool/function calling
- Agent loops
- External API integration
- Prompt engineering
- State and conversation history
- Deterministic tools vs. LLM reasoning
- Agent orchestration with LangChain
- Building AI applications with Streamlit

The central concept is:

```text
LLM + Tools + Agent Loop = Agentic Application
```

---

## Limitations

- Weather information is limited to the available forecast window.
- Budget estimates are approximate and should not be treated as actual booking prices.
- Web search results may vary depending on search availability and destination.
- The application does not directly book flights, hotels, restaurants, or activities.
- Exchange rates can change over time.
- Generated itineraries should be verified before making actual travel arrangements.
- External APIs may have their own availability, rate limits, or data limitations.

---

## Security

Never commit API keys to Git.

The project uses:

```text
.env
```

for local credentials, and `.env` should be listed in `.gitignore`.

If an API key is accidentally committed or exposed, revoke or rotate it immediately.

---

## Future Improvements

Potential extensions include:

- Flight and hotel search
- Hotel and restaurant booking integrations
- Persistent user preferences
- Long-term conversation memory
- Vector database / RAG for travel guides
- Route and travel-time optimization
- Multi-agent architecture
- LangGraph-based workflow orchestration
- Cost-aware tool selection
- Structured itinerary output
- Exporting itineraries to PDF or calendar formats

---

## License

This project is intended for educational and experimentation purposes.
