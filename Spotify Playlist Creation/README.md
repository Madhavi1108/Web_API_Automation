# Billboard Top 100 to Spotify Playlist Creator

This Python application creates a Spotify playlist from the Billboard Hot 100 chart for a specified date.

## Overview

The `main.py` script automates the process of generating a Spotify playlist based on the Billboard Hot 100 chart. It performs the following actions:

1.  **Scrapes Billboard Chart:** It scrapes the Billboard Hot 100 chart for a given date to extract the list of songs.
2.  **Authenticates with Spotify:** It authenticates with the user's Spotify account using the Spotipy library.
3.  **Searches for Songs on Spotify:** It searches for each song from the Billboard chart on Spotify.
4.  **Creates a Playlist:** It creates a new private playlist on the user's Spotify account.
5.  **Adds Songs to Playlist:** It adds the found songs to the newly created playlist.
6.  **Provides Download Option:** It provides an option to download the list of songs as a CSV file.

## Getting Started

### Prerequisites

* **Python 3.x:** Ensure you have Python 3 installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).
* **Python Libraries:** You need to install the following Python libraries:
    * `streamlit`
    * `requests`
    * `beautifulsoup4` (or `bs4`)
    * `spotipy`
    * `pandas`

    You can install them using pip:

    ```bash
    pip install streamlit requests beautifulsoup4 spotipy pandas
    ```
* **Spotify API Credentials:** You'll need to obtain Spotify API credentials:
    * `YOUR_UNIQUE_CLIENT_ID`: Your Spotify application's client ID.
    * `YOUR_UNIQUE_CLIENT_SECRECT`: Your Spotify application's client secret.
    * You'll also need to set the `REDIRECT_URI`. In the provided code, it's set to the Billboard Hot 100 chart URL, but you might need to adjust this depending on your Spotify application's configuration.

    You can get these credentials by creating a developer application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

    *(Replace `<repository_url>` with the actual URL of your GitHub repository and `<repository_name>` with the name of your repository.)*

2.  **Set your Spotify API Credentials:**
    * Replace the placeholder values for `YOUR_UNIQUE_CLIENT_ID`, `YOUR_UNIQUE_CLIENT_SECRECT`, and `REDIRECT_URI` in the `main.py` file with your actual credentials.

### Running the Script

1.  **Open a terminal or command prompt** and navigate to the project directory.
2.  **Run the Streamlit application:**

    ```bash
    streamlit run main.py
    ```

    This will open the application in your web browser.

## Usage

1.  **Enter a Date:** In the application, enter the date for the Billboard Hot 100 chart you want to use (in YYYY-MM-DD format).
2.  **Create Playlist:** Click the "Create Playlist" button.
3.  **Spotify Authentication:** You'll be prompted to authenticate with your Spotify account.
4.  **Playlist Creation:** The application will create a new private playlist in your Spotify account with the songs from the specified Billboard chart.
5.  **Open in Spotify:** A link will be provided to open the created playlist in Spotify.
6.  **Download CSV:** You can download the list of songs as a CSV file using the provided button.

## Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the [MIT License].
