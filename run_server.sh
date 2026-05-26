#!/bin/bash

# EgoTrack Waitlist Server - Quick Start

echo "======================================"
echo "EgoTrack Waitlist Server Starting..."
echo "======================================"
echo ""

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "ERROR: .env file not found!"
    echo "Please create a .env file with your Gmail credentials."
    echo "Refer to SETUP_GUIDE.md for instructions."
    exit 1
fi

# Check if Flask is installed
python -c "import flask" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

echo "Starting Flask server..."
echo ""
echo "📧 Email notifications will be sent to: nwokoloebube21@gmail.com"
echo "🌐 Website will be available at: http://localhost:5000"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

python app.py
