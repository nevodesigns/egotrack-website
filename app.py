from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

# File to store submissions
SUBMISSIONS_FILE = 'waitlist_submissions.json'
GMAIL_ADDRESS = os.getenv('GMAIL_ADDRESS', 'nwokoloebube21@gmail.com')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-waitlist', methods=['POST'])
def submit_waitlist():
    try:
        data = request.json
        
        # Validate required fields
        required_fields = ['Full name', 'Email', 'WhatsApp number', 'Business type', 'Market or location']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} is required'}), 400
        
        # Add timestamp
        data['Submitted at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Load existing submissions
        submissions = []
        if os.path.exists(SUBMISSIONS_FILE):
            with open(SUBMISSIONS_FILE, 'r') as f:
                submissions = json.load(f)
        
        # Add new submission
        submissions.append(data)
        
        # Save to file
        with open(SUBMISSIONS_FILE, 'w') as f:
            json.dump(submissions, f, indent=2)
        
        print(f"✅ New submission saved! Total: {len(submissions)}")
        print(f"   Name: {data.get('Full name')}")
        print(f"   Email: {data.get('Email')}")
        
        return jsonify({
            'success': True, 
            'message': 'Thank you for joining the EgoTrack waitlist! We will reach out soon with your pilot access.'
        }), 200
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Failed to submit. Please try again.'}), 500

@app.route('/submissions', methods=['GET'])
def get_submissions():
    """View all submissions (you can add password protection later)"""
    try:
        if os.path.exists(SUBMISSIONS_FILE):
            with open(SUBMISSIONS_FILE, 'r') as f:
                submissions = json.load(f)
            return jsonify({'submissions': submissions, 'total': len(submissions)}), 200
        return jsonify({'submissions': [], 'total': 0}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
