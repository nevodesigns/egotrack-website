# EgoTrack Waitlist Setup Guide

## Overview
Your form submission system is now set up to:
- Collect form submissions locally from your website
- Automatically send email notifications to your Gmail inbox
- Work completely offline on your laptop

## Prerequisites
You need to have Python installed on your laptop. Check by running:
```bash
python --version
```

## Setup Instructions

### Step 1: Get a Gmail App Password
Since Gmail has 2-Factor Authentication enabled, you need to create an "App Password":

1. Go to https://myaccount.google.com/
2. Click **Security** in the left sidebar
3. Scroll down and find **App passwords** (if you don't see it, make sure 2-FA is enabled)
4. Select "Mail" and "Windows Computer"
5. Google will generate a 16-character password like `abcd efgh ijkl mnop`
6. Copy this password (without spaces)

### Step 2: Update .env File
1. Open the `.env` file in the project folder
2. Replace `your_app_password_here` with the 16-character password you just copied
3. Make sure the file looks like this:
```
GMAIL_ADDRESS=nwokoloebube21@gmail.com
GMAIL_PASSWORD=abcdefghijklmnop
```

### Step 3: Install Dependencies
Open terminal/command prompt and navigate to the project folder:
```bash
cd /home/nwokolo/egotrack
```

Then install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask Server
In the same terminal, run:
```bash
python app.py
```

You should see output like:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Step 5: Test the Form
1. Open your browser and go to: `http://localhost:5000`
2. Fill out the form with test data
3. Click "Submit Details"
4. Check your Gmail inbox for an email with subject "EgoTrack Waitlist"

## How It Works
- The form submits data to your local Flask server (no internet needed)
- Flask receives the data and sends an email to your Gmail account
- The email contains all the user's information in a formatted table
- Users get an instant confirmation message on the page

## Troubleshooting

### "Cannot GET /" error
Make sure you're running the Flask server. The terminal should show `Running on http://127.0.0.1:5000`

### "Server is not running" message on form submission
1. Check that the Flask server is still running in the terminal
2. If it crashed, run `python app.py` again

### Email not sending
1. Double-check the App Password in `.env` (no spaces, exactly 16 characters)
2. Check that Gmail 2-FA is enabled in your account settings
3. Make sure you're using a Gmail address (not Outlook, Yahoo, etc.)
4. Check the terminal for error messages

### Permission Error
If you get a permission error, try:
```bash
pip install --user -r requirements.txt
```

## File Structure
```
egotrack/
├── app.py                 # Flask backend server
├── .env                   # Gmail credentials (DO NOT SHARE)
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Website (served by Flask)
├── static/
│   ├── script.js         # Form handling JavaScript
│   └── styles.css        # Website styling
└── [other files]
```

## Keeping the Server Running
If you want the form to always be ready:
- Keep the terminal window open while testing
- The server runs on `http://localhost:5000` until you close it
- Press `CTRL+C` to stop the server

## Next Steps
Once everything is working:
- Share the local URL only on your machine (`http://localhost:5000`)
- To make it accessible online, you can deploy to services like:
  - Heroku, Render, Railway, or PythonAnywhere
  - Each has free tiers for testing
