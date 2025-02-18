# Weather Information Retrieval Script

This Python script retrieves and displays current weather information for a specified city using the OpenWeatherMap API.

## Features

*   Retrieves weather data from OpenWeatherMap API.
*   Displays city name, country, temperature (in Celsius), and weather condition.
*   Handles API errors gracefully and provides informative error messages.

## Requirements

*   Python 3.x
*   `requests` library. Install it using `pip install requests`

## How to Use

1.  **Obtain an API key:** You need to sign up for a free account at [OpenWeatherMap](https://openweathermap.org/) to obtain an API key.  Replace `"get api key"` in the script with your actual API key.
2.  **Save the code:** Save the Python code as a `.py` file (e.g., `weather_app.py`).
3.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute the script using `python weather_app.py`.
4.  **Modify the city (Optional):** The default city is set to "Lagos". You can change this by modifying the `city` variable in the script before running it.

## Code Explanation

*   **`get_weather(city, api_key)`:** This function makes the API call to OpenWeatherMap. It constructs the API URL with the city and API key as parameters and uses the `requests` library to retrieve the data. It handles potential errors by checking the response status code and raising an exception if the request fails.
*   **`display_weather(data)`:** This function takes the JSON data returned by the API and extracts the relevant information (city, country, temperature, and weather description). It then neatly prints this information to the console.
*   **Main execution block:** The script first defines the API key and city. It then calls the `get_weather` function to retrieve the data and the `display_weather` function to display it.  A `try...except` block is used to catch any exceptions that might occur during the API call or data processing, ensuring the script doesn't crash and provides a user-friendly error message.
