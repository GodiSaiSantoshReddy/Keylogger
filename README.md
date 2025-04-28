# An Advance Keylogger Project

## Aim of the Experiment
To develop an advance keylogging software that records keystrokes and captures screenshots and audio at regular intervals to monitor user activity. This tool aims to enhance security, assist in monitoring children’s or students' activities, and detect potential misuse of devices in an educational or parental monitoring context.

## Requirements

### 2.1 Software Requirements
- **Operating System**: Windows 10/Linux/macOS
- **Programming Languages**: Python
- **Libraries**: 
  - `pyHook`
  - `pynput`
  - `pyautogui`
  - `smtplib`
  - `email.mime.text`
  - `email.mime.multipart`
  - `cv2` (for screenshot capture)
  - `pyaudio` (for audio capture)
- **Database**: SQLite or other local storage for storing logs (optional)
- **Email Service**: SMTP configuration (Gmail or Mailtrap for sending email reports)

### 2.2 Hardware Requirements
- **Processor**: Intel Core i3 or higher
- **RAM**: Minimum 4 GB
- **Hard Disk**: 100 MB free for the installation and storage of logs
- **Internet Connection**: Required for email notifications

## Suggested Reading (Theoretical Background)
- Ethical use of surveillance and monitoring tools
- Keylogging techniques and their applications in educational and parental monitoring
- Email protocols (SMTP, MIME)
- Audio and screenshot capture using Python
- Data privacy and legal aspects of keylogging
- Machine learning for detecting anomalies in keystrokes

## Procedure/Step-by-Step Instructions

### 4.1 Problem Statement
The purpose of the keylogger is to monitor user activity, capture keystrokes, and periodically send screenshots and audio recordings to an administrator’s email. This tool can be used in educational contexts to prevent cheating during online exams or in parental monitoring scenarios.

### 4.2 Preparation of Software Requirement Specification Document
#### 4.2.1 Users and Characteristics
- **Administrators**: Receive keystroke logs, screenshots, and audio recordings to monitor the user’s activity.
- **Users**: Individuals whose keystrokes, screenshots, and audio are being monitored (with explicit consent in educational or parental settings).

#### 4.2.2 Non-Functional Requirements:
- **Performance**: The system should send logs at 1-minute intervals.
- **Availability**: Logs and notifications should be available in real-time.
- **Usability**: Simple and discreet background operation with minimal user interference.
- **Security**: Keystrokes and captured data must be encrypted to protect user privacy.
- **Scalability**: The system should be capable of handling multiple monitoring points for administrative purposes.

### 4.3 Preparation of Software Configuration Management Software Requirements
- **Operating System**: Windows 10/Linux/macOS
- **Programming Environment**: Python 3.x
- **Libraries/Packages**: `pyHook`, `pyautogui`, `pynput`, `pyaudio`, `smtplib`, `opencv-python`
- **IDE**: Visual Studio Code or PyCharm

### 4.4 Study and Usage of Any Design Phase CASE Tool
This project does not require specific CASE tools but recommends basic tools for version control like **Git** for managing source code changes and collaboration.

## Implementation

### 6.1 Working of the System
1. **Keystroke Logging**: The system records all keypresses in the background, storing each keystroke in a log file.
2. **Screenshot Capture**: Every minute, the system captures a screenshot of the active screen to monitor the user's actions visually.
3. **Audio Recording**: The system records audio every minute using the system’s microphone to capture surrounding sounds.
4. **Email Notification**: After every interval, the system sends an email to the administrator with the latest keystroke log, screenshot, and audio file as attachments.
5. **Anomaly Detection**: (Optional) Implemented using an anomaly detection algorithm like Isolation Forest to detect unusual keystroke patterns that may suggest unusual behavior.

### 6.2 Email Setup
1. Use Gmail or Mailtrap for sending periodic email reports.
2. Configure SMTP settings to securely send logs and media files.

### 6.3 Anomaly Detection (Optional)
Implementing an anomaly detection algorithm such as **Isolation Forest** to detect unusual keystroke patterns.

## Security and Data Protection
- **Data Encryption**: All sensitive data (keystrokes, screenshots, audio files) are encrypted before sending via email using strong encryption methods such as AES.
- **Authentication**: Use OAuth2 for secure email authentication to avoid security vulnerabilities.
- **Privacy**: The tool must be used with full consent, ensuring that all parties involved are aware of the monitoring.
- **Log Storage**: Optionally, logs and media files can be stored locally in an encrypted database (e.g., SQLite) for future reference.

## Benefits of the System
- **Enhanced Monitoring**: Helps monitor user activity discreetly.
- **Real-Time Reporting**: Provides administrators with real-time insights into user activity.
- **Anomaly Detection**: Detects unusual behavior based on keystroke patterns.
- **Parental or Educational Use**: Assists parents or educators in ensuring appropriate device usage.

## Challenges and Future Enhancements

### 9.1 Challenges
- **Privacy Concerns**: Must be used in a legal and ethical manner with explicit consent.
- **System Resource Usage**: Continuous logging and capturing may use considerable CPU and memory resources.
- **Accuracy**: False positives in anomaly detection algorithms.

### 9.2 Future Enhancements
- **Cloud Integration**: Store logs and media securely in cloud storage for better management and accessibility.
- **Real-Time Alerts**: Integrate push notifications or mobile alerts for administrators.
- **Advanced Analytics**: Implement more advanced machine learning models for deeper analysis of user behavior patterns.

## Sample Output/Result
1. **Keystroke Logs**: Capture of each key pressed by the user.
2. **Screenshots**: Periodic screenshots of the active screen.
3. **Audio Recordings**: Captured audio files.
4. **Email Report**: Regular email updates with attached logs and media.

## Inference
This project demonstrates the technical feasibility of a keylogging tool for educational or monitoring purposes. Ethical usage and proper consent are crucial for this tool to be implemented responsibly.
