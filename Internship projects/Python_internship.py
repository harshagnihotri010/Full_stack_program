import smtplib
from googlesearch import search
from geopy.geocoders import Nominatim
from gtts import gTTS
import pyttsx3
import pyautogui
import time
import os

# Function to send an email
def send_email():
    sender_email = "email@example.com"
    sender_password = "password"
    receiver_email = input("Enter the receiver's email: ")
    subject = input("Enter the subject: ")
    body = input("Enter the body of the email: ")

    email_message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, email_message)
    print("Email sent successfully.")

# Function to send an SMS message
def send_sms():
    # This example uses the Twilio API
    from twilio.rest import Client

    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)

    to_phone_number = input("Enter the receiver's phone number: ")
    from_phone_number = "your_twilio_phone_number"
    message_body = input("Enter the message: ")

    message = client.messages.create(
        body=message_body,
        from_=from_phone_number,
        to=to_phone_number
    )
    print("SMS sent successfully.")

# Function to scrape top 5 search results from Google
def google_scrape():
    query = input("Enter the search query: ")
    results = []

    try:
        for result in search(query, num_results=5):
            results.append(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    for i, result in enumerate(results, start=1):
        print(f"{i}. {result}")

# Function to find current geo coordinates and location
def find_geo_coordinates():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("Your Address Here")
    print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")

# Function to convert text to audio
def text_to_audio():
    text = input("Enter the text: ")
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    print("Text converted to audio successfully.")

# Function to control volume of your laptop
def control_volume():
    volume = int(input("Enter the volume level (0-100): "))
    pyautogui.press('volumedown', presses=50)  # mute volume
    time.sleep(1)
    pyautogui.press('volumeup', presses=volume // 2)  # set to desired level

# Function to connect to your mobile and send SMS from your mobile messaging app
def send_sms_from_mobile():
    # Assuming you are using Android and have ADB installed
    phone_number = input("Enter the receiver's phone number: ")
    message = input("Enter the message: ")
    os.system(f'adb shell am start -a android.intent.action.SENDTO -d sms:{phone_number} --es sms_body "{message}" --ez exit_on_sent true')
    os.system('adb shell input keyevent 22')
    os.system('adb shell input keyevent 66')
    print("SMS sent from mobile successfully.")

# Function to send bulk email
def send_bulk_email():
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    subject = input("Enter the subject: ")
    body = input("Enter the body of the email: ")
    email_message = f"Subject: {subject}\n\n{body}"
    
    recipients = input("Enter the recipients' emails, separated by commas: ").split(',')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        for receiver_email in recipients:
            server.sendmail(sender_email, receiver_email, email_message)
    print("Bulk email sent successfully.")

# Main menu
def main_menu():
    while True:
        print("\nMenu:")
        print("1. Send Email")
        print("2. Send SMS")
        print("3. Scrape top 5 search results from Google")
        print("4. Find current geo coordinates and location")
        print("5. Convert text to audio")
        print("6. Control volume of your laptop")
        print("7. Send SMS from your mobile messaging app")
        print("8. Send bulk email")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            send_email()
        elif choice == "2":
            send_sms()
        elif choice == "3":
            google_scrape()
        elif choice == "4":
            find_geo_coordinates()
        elif choice == "5":
            text_to_audio()
        elif choice == "6":
            control_volume()
        elif choice == "7":
            send_sms_from_mobile()
        elif choice == "8":
            send_bulk_email()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
