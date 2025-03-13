import pandas as pd
import urllib
import time
import pywhatkit as kit

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
    for number in numbers:
        try: 
            #Caption image
            kit.sendwhats_image(
                receiver=number.strip(),  # Phone number
                img_path="kmcc.jpeg",  # Path to the image file
                close_time=10,
                tab_close=True
            )
            time.sleep(5)
            kit.sendwhatmsg_instantly(
                phone_no=number, 
                message=message,
                close_time=10,
                tab_close=True
            )
            time.sleep(5)
            #Schedule mesage
            #kit.sendwhatmsg(contact, message, hour, minute)
            print(f"Message sent to {number}")
        except Exception as ex:
            print(f"Failed to send message to {number}. Reason : {ex}")



bot_send_message()
