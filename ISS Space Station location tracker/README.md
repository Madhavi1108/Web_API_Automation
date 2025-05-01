# ISS Overhead Notifier

This Python application checks the real-time location of the International Space Station (ISS) and sends an email notification if the ISS is overhead and it's nighttime.

## Overview

The `main.py` script performs the following actions:

1.  **Fetches ISS Location:** It retrieves the current latitude and longitude of the ISS from the Open Notify API.
2.  **Checks if ISS is Overhead:** It determines if the ISS is within a 5-degree range of the user's specified latitude and longitude.
3.  **Fetches Sunrise and Sunset Times:** It uses the Sunrise Sunset API to get the sunrise and sunset times for the user's location.
4.  **Checks if it's Night:** It checks if the current time is after sunset or before sunrise.
5.  **Sends Email Notification:** If the ISS is overhead and it's nighttime, it sends an email notification to the user.

## Getting Started

### Prerequisites

* **Python 3.x:** Ensure you have Python 3 installed on your system.
* **`requests` library:** This script uses the `requests` library to make HTTP requests. You can install it using pip:

    ```bash
    pip install requests
    ```
* **`smtplib` library:** This script uses the `smtplib` library, which is part of the Python standard library, for sending emails.
* **Email Account:** You need an email account to send notifications. You'll need to provide your email address and password in the script.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

    *(Replace `<repository_url>` with the actual URL of your GitHub repository and `<repository_name>` with the name of your repository.)*

2.  **Set your location and email credentials:**

    * Open the `main.py` file and modify the following variables:
        * `MY_LAT`: Replace with your latitude.
        * `MY_LONG`: Replace with your longitude.
        * `MY_EMAIL`: Replace with your email address.
        * `MY_PASSWORD`: Replace with your email password.

    **Important:** Be cautious about storing your email password directly in the script. Consider using environment variables or a more secure method to handle sensitive information.

### Running the Script

1.  **Open a terminal or command prompt** and navigate to the project directory.
2.  **Run the script:**

    ```bash
    python main.py
    ```

    The script will run continuously, checking the ISS location and sending email notifications as needed.

## Usage

The script runs in a loop, periodically checking the ISS location. You don't need to interact with it directly after starting it. Just make sure you have set your location and email credentials correctly.

## Contributing

Contributions to improve the script are welcome. You can suggest improvements or submit pull requests.

## License

This project is licensed under the [MIT License].