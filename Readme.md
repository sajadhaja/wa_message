# Bulk Messaging Automation

This script automates sending messages to multiple numbers.

**Author Name**: Mohammed Sajadh N.A

## Prerequisites

Ensure you have the following installed:

- **Python 3.x** ([Download Python](https://www.python.org/downloads/))
- **Google Chrome**

## Installation

1. **Install Required Libraries**
   ```sh
   pip install selenium
   ```

2. **Download ChromeDriver**
   - Check your Chrome version: Open `chrome://settings/help` in Chrome.
   - Download the corresponding version from [ChromeDriver](https://chromedriver.chromium.org/downloads).
   - Extract the downloaded file and place it in the same folder as this script or add it to the system PATH.

## Execution Steps

1. **Open a terminal or command prompt in the script directory.**
2. **Run the script:**
   ```sh
   python send_message.py
   ```
3. **Scan the QR Code** when prompted to log into WhatsApp Web.
4. Back to terminal and **press `Enter`**
4. **Messages will be sent automatically** to the numbers in the script.

## Customization
- Modify `phone_numbers`.csv to include your recipients.
- Edit `message_template.txt` to customize the message.
- Ensure CSV contains only valid phone numbers to avoid errors.
- The script automatically formats new lines, emojis, and bullet points using URL encoding.

## Note
Each message sent takes a minimum of 30 seconds to avoid heavy traffic on the WhatsApp server and to prevent being banned by WhatsApp.