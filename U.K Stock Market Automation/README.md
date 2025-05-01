# Stock News Alert Application

This Python application retrieves stock market data and related news articles, and can be extended to send alerts based on significant stock price changes.

## Overview

The `main.py` script performs the following actions:

1.  **Fetches Stock Data:** It uses the Alpha Vantage API to get daily time series data for a specified stock (default: Tesla Inc. - TSLA).
2.  **Calculates Price Difference:** It calculates the percentage difference between yesterday's and the day before yesterday's closing stock prices.
3.  **Fetches News Articles:** If the percentage difference exceeds a threshold (currently 5%), it fetches news articles related to the company using the News API.
4.  **Formats Articles:** It formats the headlines and brief descriptions of the top 3 news articles.
5.  **\[Potential Extension]:** The script is set up to potentially send this information via SMS using the Twilio API (this part requires further implementation with your Twilio credentials).

## Getting Started

### Prerequisites

* **Python 3.x:** Ensure Python 3 is installed on your system.
* **API Keys:** You'll need API keys for the following services:
    * **Alpha Vantage API Key:** Obtain a free API key from [Alpha Vantage](https://www.alphavantage.co/).
    * **News API Key:** Get an API key from [News API](https://newsapi.org/).
    * **Twilio Account SID and Auth Token:** (If you intend to use the SMS functionality) Sign up for a Twilio account at [Twilio](https://www.twilio.com/) to get these credentials.
* **Install `requests` and `twilio`:** You'll need to install these Python libraries if you plan to use the SMS functionality:

    ```bash
    pip install requests
    pip install twilio
    ```

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

    *(Replace `<repository_url>` with the actual URL of your GitHub repository and `<repository_name>` with the name of your repository.)*

2.  **Set up Environment Variables:**

    You'll need to set the following environment variables or directly replace the placeholder strings in the `main.py` file with your actual API keys and Twilio credentials:

    ```python
    my_api = "<YOUR_ALPHA_VANTAGE_API_KEY>"
    my_news_api = "<YOUR_NEWS_API_KEY>"
    TWILIO_SID = "<YOUR_TWILIO_ACCOUNT_SID>"
    TWILIO_AUTH_TOKEN = "<YOUR_TWILIO_AUTH_TOKEN>"
    ```

    **Important:** It's highly recommended to use environment variables to keep your API keys secure.

### Running the Script

1.  **Navigate to the directory** containing `main.py`.
2.  **Run the script:**

    ```bash
    python main.py
    ```

    The script will fetch the stock data and news, and print the relevant information to the console.

## Usage

The script, as provided, will:

* Fetch stock data for "TSLA" (Tesla Inc.). You can change `STOCK_NAME` and `COMPANY_NAME` to analyze a different stock.
* Print yesterday's and the day before yesterday's closing prices.
* Calculate and print the percentage difference.
* If the difference is greater than 5%, it will print the headlines and descriptions of the top 3 news articles.

To enable SMS alerts, you'll need to add the Twilio code to send messages using the `TWILIO_SID`, `TWILIO_AUTH_TOKEN`, and your phone numbers.

## Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features (like adding more robust alert mechanisms or supporting different stock exchanges), please feel free to submit a pull request or open an issue.

## License

This project is licensed under the [MIT License].