import pandas as pd
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Read CSV for phone numbers
def read_phone_numbers():
    csv_file = "phone_numbers.csv"
    df = pd.read_csv(csv_file, header=None)  # No headers in CSV
    return df.iloc[:, 0].astype(str).tolist()  # Convert to list of strings

# Load message from text file
def read_message():
    txt_file = "message_template.txt"
    with open(txt_file, "r", encoding="utf-8") as file:
        return file.read()  # Read and remove extra spaces/newlines

numbers = read_phone_numbers()
message = read_message()
# Encode message for URL
encoded_message = urllib.parse.quote(message)

def bot_send_message():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    input("Scan the QR code and press Enter")

    for number in numbers:
        driver.get(f"https://web.whatsapp.com/send?phone={number}&text={encoded_message}")
        time.sleep(15)

        try:
            send_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Send"]')
            send_button.click()
            print(f"Successfully send message to number {number}")
            time.sleep(15)
        except Exception as ex:
            print(f"Failed to send message to {number}. Reason : {ex}")

    driver.quit()

bot_send_message()
