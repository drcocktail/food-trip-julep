# AI Foodie Tour Planner

This project uses the Julep AI platform to create a sophisticated, multi-city "foodie tour" planner. Given a list of cities, it generates a personalized, one-day itinerary for each, taking into account real-time weather, iconic local dishes, and top-rated restaurants.

This project was built to fulfill the requirements of the Julep AI Engineering Intern selection process.

## Architecture

The application is architected around a **task-driven workflow** using Julep, which is more robust and scalable than a simple chatbot. The core logic is defined declaratively in `foodie_tour_task.yaml` rather than being hard-coded in a prompt.

The workflow proceeds in the following steps, running operations for multiple cities in parallel to ensure efficiency:
1.  **Fetch Weather:** Gets the current weather for each city using the OpenWeatherMap integration.
2.  **Suggest Iconic Dishes:** Prompts the LLM to suggest 3 weather-appropriate iconic dishes for each city.
3.  **Find Restaurants:** Uses the Google Custom Search API to find top-rated, authentic restaurants for each suggested dish.
4.  **Generate Narrative Tour:** In the final step, a specialized LLM prompt crafts a delightful "foodie tour" narrative for each city, weaving together the weather, dishes, and restaurant suggestions for breakfast, lunch, and dinner.

## Setup Instructions

To run this project, you need Python 3 and a few API keys. The setup script will guide you through creating the necessary `.env` file.

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Install Dependencies

It's recommended to use a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure API Keys

This project requires API keys to function.

1.  Find the `env_example.txt` file in the root directory.
2.  Rename or copy it to a new file named `.env`.
3.  Open the `.env` file and add your API keys.

The file requires the following keys:

*   **`JULEP_API_KEY`** (Required): Get from the [Julep Dashboard](https://dashboard.julep.ai).
*   **`OPENWEATHERMAP_API_KEY`** (Required): Get a free key from [OpenWeatherMap API](https://openweathermap.org/api).
*   **`BRAVE_API_KEY`**: This is included in the project and set up automatically.

### 4. Run the Application

Once your `.env` file is configured, you can run the main application:

```bash
python app.py
```

The script will create a new Julep agent, execute the foodie tour task for the cities defined in `app.py` (Paris, Tokyo, Mumbai), and print the final, formatted plan to the console.

## Files

*   `app.py`: The main entry point of the application. It handles agent creation and task execution.
*   `foodie_tour_task.yaml`: Defines the entire multi-step Julep workflow. This is the core logic of the application.
*   `requirements.txt`: A list of necessary Python packages.
*   `env_example.txt`: An example file showing the required environment variables.
*   `README.md`: This file.
*   `trip_planner_test/`: A separate directory containing a direct implementation of the official Julep Trip Planning tutorial.

## Sanity Check: Running the Official Trip Planner Tutorial

If you encounter issues with the main application, you can run a clean, separate test to validate your environment and API keys. This implementation exactly follows the official Julep documentation.

To run the test:

```bash
cd trip_planner_test
python run_trip_planner.py
```

## 🍛 Interactive AI Foodie Assistant

Interactive chatbot that discovers local food culture with real-time search! Tell it your city and get personalized food recommendations with current time, weather, iconic dishes, and top restaurants.

## ✨ Features

🗣️ **Interactive Chatbot** - Just tell it your city  
🕐 **Real-time Info** - Current time and weather via search  
🍛 **Iconic Local Dishes** - 3 must-try specialties per city  
🏪 **Live Restaurant Search** - Current top restaurants via Google/Bing  
🌤️ **Weather-Smart Recommendations** - Dine-in vs takeout based on weather  
📍 **Immediate Action** - Ready-to-eat suggestions right now  

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up API Keys
```bash
python setup_api_keys.py
```

### 3. Run the App
```bash
python app.py
```

## 🔧 API Keys

### Required
- **JULEP_API_KEY** - Get free at [dashboard.julep.ai](https://dashboard.julep.ai)

### Optional (for real-time search)
- **BRAVE_API_KEY** - Free (generous free tier) at [Brave Search API](https://brave.com/search/api/)

*Without search APIs, the assistant uses AI knowledge only.*

## 🛠️ Tools Configuration

Tools are defined in `tools.yaml`:

- **search_time_weather** - Gets current time and weather for any city
- **search_restaurants** - Finds top restaurants for specific dishes

## 🎯 How It Works

1. **Tell your city**: "I'm in Mumbai"
2. **AI searches**: Current time/weather + restaurant info
3. **Get recommendations**: 3 iconic dishes + best restaurants + weather-aware dining strategy
4. **Take action**: Immediate suggestions for right now

## 💬 Example Conversation

```
👤 You: I'm in Mumbai

🤖 Assistant: 
*searches for Mumbai time and weather*

Great! You're in Mumbai! It's currently 3:30 PM and 28°C with partly cloudy skies - perfect weather for exploring the city's amazing food scene!

🍛 **3 Iconic Mumbai Dishes:**
1. **Vada Pav** - Mumbai's beloved street burger
2. **Pav Bhaji** - Spicy mashed vegetables with bread
3. **Bombay Duck Fry** - Seasonal coastal delicacy

🏪 **Top Restaurants Right Now:**
*searches for current restaurant info*
- **Olympia Coffee House** (Colaba) - Legendary Irani cafe
- **Swati Snacks** (Tardeo) - Modern street food
- **Gajalee** (Multiple locations) - Best seafood

🌤️ **Weather-Smart Recommendation:**
Perfect weather for outdoor dining! Head to a street food market or terrace restaurant. Try Vada Pav from a street vendor, then sit at an outdoor cafe for Irani chai!

📍 **Right Now:** Visit Mohammed Ali Road for authentic street food - the weather is ideal for walking and outdoor eating!
```

## 📁 Project Structure

```
julep/
├── app.py                 # Main interactive app
├── tools.yaml             # Search tool definitions
├── setup_api_keys.py      # API key setup
├── requirements.txt       # Dependencies
└── README.md              # This file
```

## 🌍 Supported Cities

The assistant works best with major cities worldwide, especially:
- **Indian cities**: Mumbai, Delhi, Bangalore, Chennai, Kolkata, Pune, Hyderabad
- **Global cities**: Any major city with searchable restaurant info

## 🔄 Search APIs Info

### Google Custom Search (Recommended)
- **Free**: 100 queries/day
- **Setup**: Create project → Enable API → Create search engine
- **Best for**: Most comprehensive results

### Bing Search API (Alternative)
- **Free**: 1,000 queries/month  
- **Setup**: Azure account → Cognitive Services → Bing Search
- **Best for**: Higher volume usage

## 🤝 Contributing

Feel free to enhance the tool configurations, add more cities, or improve the conversation flow!

## 📄 License

Open source project for food lovers and travelers.

---

**Ready to discover amazing local food? Run `python app.py` and start chatting!** 🍛✨ 