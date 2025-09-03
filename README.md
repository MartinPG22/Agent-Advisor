# Agent-Advisor

Agent-Advisor is a multi-agent AI system designed to classify user queries and provide insights across various domains, including budget, legal, and marketing. The system utilizes specialized agents to analyze queries and synthesize recommendations based on their responses.

## Project Structure

```
LaunchyAdvisor
├── srchuggingface
│   ├── agents
│   │   ├── middle_agents.py       
│   │   ├── decision_agent.py       # Synthesizes insights and makes final recommendations
│   │   └── classify_query.py       # Classifies user queries into relevant categories
│   ├── graph
│   │   └── graph_builder.py        # Sets up the StateGraph for processing
│   │ 
│   ├──.env                         # Access token
│   ├── huggingface.py              # General implementation of the model used by the agents
│   ├── config.py                   # Defines the model name
│   └── main.py                     # Entry point for the application
├── requirements.txt                # Lists project dependencies
└── README.md                       # Documentation for the project
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the application, execute the `main.py` file:

```bash
python srchuggingface/main.py
```

