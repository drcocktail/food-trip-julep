#!/usr/bin/env python3
"""
AI Foodie Tour Planner
Generates a one-day foodie tour for a list of cities based on weather,
iconic dishes, and top-rated restaurants.
"""

from julep import Julep, Client
from dotenv import load_dotenv
import os 
import yaml
import time
from pathlib import Path

# Load environment variables from .env file
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

def run_foodie_tour_workflow(client: Client, agent_id: str, locations: list[str]):
    """
    Loads, creates, and executes the foodie tour task.

    Args:
        client: The Julep API client.
        agent_id: The ID of the agent to use for the task.
        locations: A list of city names.
    """
    print("   -> Loading workflow from foodie_tour_task.yaml...")
    try:
        with open('foodie_tour_task.yaml', 'r') as file:
            task_definition = yaml.safe_load(file)
    except FileNotFoundError:
        print("❌ Error: foodie_tour_task.yaml not found.")
        print("   Please ensure the workflow definition file is in the same directory.")
        return

    print("   -> Creating task on Julep platform...")
    task = client.tasks.create(
        agent_id=agent_id,
        **task_definition
    )
    print(f"   ✅ Task created successfully! Task ID: {task.id}")

    print("\n🚀 Kicking off the foodie tour generation...")
    print(f"   Cities: {', '.join(locations)}")
    
    # Create the execution
    execution = client.executions.create(
        task_id=task.id,
        input={"locations": locations}
    )
    print(f"   Workflow started! Execution ID: {execution.id}")
    print("   Please wait, this may take a few minutes as the AI plans your tours...")

    # Poll for the result
    while True:
        retrieved_execution = client.executions.get(execution.id)
        current_status = retrieved_execution.status
        print(f"   Current status: {current_status}...")
        
        if current_status not in ["starting", "queued", "running"]:
            break
        
        time.sleep(10)

    print("-" * 50)
    if retrieved_execution.status == "succeeded":
        print("Workflow completed successfully!\n")
        final_plan = retrieved_execution.output.get('final_plan', 'No plan generated.')
        print("YOUR PERSONALIZED FOODIE TOUR PLAN")
        print("==============================")
        print(final_plan)
    else:
        state = retrieved_execution.status
        error = retrieved_execution.error
        print(f"Workflow failed with state: {state}")
        print(f"Error details: {error}")

def main():
    """Main application entry point."""
    
    print("AI Foodie Tour Planner")
    print("==============================")
    
    # --- API Key Checks ---
    api_keys = ["JULEP_API_KEY", "OPENWEATHERMAP_API_KEY", "BRAVE_API_KEY"]
    missing_keys = [key for key in api_keys if not os.getenv(key)]
    
    if missing_keys:
        print(f"Error: Missing required API keys in your .env file: {', '.join(missing_keys)}")
        print("Please create a .env file from env_example.txt and add your keys.")
        return
        
    client = Julep(api_key=os.getenv("JULEP_API_KEY"))

    try:
        print("Creating a new agent...")
        agent = client.agents.create(
            name="Foodie Tour Guide",
            about="An AI agent that designs personalized, weather-aware food tours based on a structured workflow.",
            model="claude-3.5-sonnet",
        )
        print(f"Agent created successfully. Agent ID: {agent.id}")

        # Define the list of cities to plan for
        cities_to_plan = ["Paris", "Tokyo", "Mumbai"]
        
        run_foodie_tour_workflow(client, agent.id, cities_to_plan)
        
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        print("\nHelp:")
        print("   • Ensure all API keys are correctly set in your .env file.")
        print("   • Check your internet connection and firewall settings.")
        print("   • If the problem persists, visit https://docs.julep.ai for help.")

if __name__ == "__main__":
    main() 