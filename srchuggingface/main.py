from graph.graph_builder import ClassifierState, graph
import json

def main():
    user_query = input("Please enter your query: ")

    initial_state = ClassifierState(query=user_query)

    # Process the graph with the initial state
    result = graph.invoke(initial_state)
    
    #print("Full State:", json.dumps(result, indent=2))  # Muestra todo el estado

if __name__ == "__main__":
    main()