# EgoTrack | Digital Ledger for Informal Market Merchants

**EgoTrack** is a mobile-first digital ledger built for informal market merchants across Nigeria, starting with high-volume auto spare-parts dealers. It helps merchants track sales, debts, receipts, and business growth.

## 🎯 Features

- **Daily Ledger** - Record every purchase, expense, sale, and inventory cost in seconds
- **Debt Registry** - Track who owes what, payment status, and due dates from one clean list
- **Growth Analytics** - See weekly, monthly, and yearly business performance without spreadsheets
- **Proof of Trade** - Generate digital receipts and transaction logs that serve as verifiable proof

## 📋 Waitlist

This repository contains the **EgoTrack Waitlist Website** where potential pilot users can sign up to be the first to use the platform.

### Getting Started

#### Prerequisites
- Python 3.7+
- pip (Python package manager)

#### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/egotrack-website.git
cd egotrack-website
```

2. **Create a virtual environment (optional but recommended):**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
```bash
cp .env.example .env
# Edit .env with your configuration if needed
```

5. **Run the server:**
```bash
python3 app.py
```

6. **Open in browser:**
Navigate to `http://localhost:5000`

## 📁 Project Structure

```
egotrack-website/
├── app.py                    # Flask backend server
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── README.md                # This file
│
├── templates/
│   └── index.html           # Website HTML
│
├── static/
│   ├── script.js            # Form handling & interactivity
│   └── styles.css           # Website styling
│
└── docs/
    ├── START_HERE.md        # Quick start guide
    ├── SETUP_GUIDE.md       # Detailed setup instructions
    └── IMPLEMENTATION_SUMMARY.md  # Technical details
```

## 🚀 Features

### Form Submission
- Users fill out a waitlist form with their business details
- Form data is automatically saved to JSON file
- Instant confirmation message on successful submission
- Full form validation on both client and server

### Data Storage
- All submissions stored in `waitlist_submissions.json`
- Timestamped entries for tracking
- Easy to export or migrate to database later

## 📧 Email Configuration (Optional)

To enable email notifications:

1. Get a Gmail App Password (requires 2-FA):
   - Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
   - Select Mail and Windows Computer
   - Copy the 16-character password

2. Update `.env`:
```
GMAIL_ADDRESS=your-email@gmail.com
GMAIL_PASSWORD=your-app-password
```

3. Uncomment email functionality in `app.py`

## 🛠️ Development

### Local Testing
```bash
python3 app.py
# Server runs on http://127.0.0.1:5000
```

### View Submissions
- Submissions are automatically saved to `waitlist_submissions.json`
- Can be viewed/exported for further processing

## 📦 Deployment

This Flask app can be deployed to:
- **Heroku** - Free tier available
- **Render** - Free tier available
- **Railway** - Free tier available
- **PythonAnywhere** - Free tier available
- **AWS** - Scalable option
- **Google Cloud Run** - Serverless option

### Quick Heroku Deployment

1. **Install Heroku CLI** and login:
```bash
heroku login
```

2. **Create Procfile:**
```
web: gunicorn app:app
```

3. **Deploy:**
```bash
heroku create your-app-name
git push heroku main
```

## 📝 File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Flask backend server handling form submissions |
| `script.js` | Frontend form handling and validation |
| `styles.css` | Website styling and responsive design |
| `index.html` | Website HTML structure |
| `requirements.txt` | Python package dependencies |
| `.env` | Sensitive configuration (not committed) |
| `.gitignore` | Files to exclude from version control |

## 🔒 Security

- **Never commit `.env` file** - Contains sensitive credentials
- Use `.env.example` as a template
- All environment variables should be configured per deployment
- Form data validated on both client and server

## 📞 Support

For issues or questions:
1. Check `SETUP_GUIDE.md` for troubleshooting
2. Check `IMPLEMENTATION_SUMMARY.md` for technical details
3. Review Flask documentation: [flask.palletsprojects.com](https://flask.palletsprojects.com/)

## 📄 License

[Add your license here - MIT, Apache 2.0, etc.]

## 👤 Author

Nwokolo Victor Oluebubechukwu  
Contact: nwokoloebube21@gmail.com

---

**Built for informal market merchants in Nigeria.** 🇳🇬  
Track the money. Prove the trade. Grow the business. 💼
