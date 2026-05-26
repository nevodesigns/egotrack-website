# 🚀 EgoTrack Waitlist - Quick Start Checklist

## What Was Fixed
✅ **Removed** formsubmit.co dependency (the external service that was failing)
✅ **Created** a local Flask backend server  
✅ **Added** automatic Gmail integration to receive form submissions
✅ **Updated** form to submit to localhost instead of external service
✅ **Set up** proper project structure with Flask conventions

---

## ⚡ 3-Step Quick Start

### Step 1: Get Your Gmail App Password (2 minutes)
1. Go to **https://myaccount.google.com/**
2. Click **Security** on the left
3. Scroll down → Find **App passwords**
4. Select **Mail** and **Windows Computer** (or your OS)
5. Copy the 16-character password Google generates

### Step 2: Update .env File (1 minute)
Open `.env` in the project folder and paste your app password:
```
GMAIL_ADDRESS=nwokoloebube21@gmail.com
GMAIL_PASSWORD=abcdefghijklmnopqr
```

### Step 3: Run the Server (1 minute)

**On Linux/Mac:**
```bash
cd /home/nwokolo/egotrack
./run_server.sh
```

**On Windows:**
```
cd C:\path\to\egotrack
run_server.bat
```

**Or manually:**
```bash
python app.py
```

---

## 📋 What Each File Does

| File | Purpose |
|------|---------|
| `app.py` | Flask backend server - handles form submissions & sends emails |
| `.env` | Stores your Gmail credentials (KEEP PRIVATE!) |
| `requirements.txt` | Lists Python packages needed (Flask, CORS, dotenv) |
| `templates/index.html` | Your website (served by Flask) |
| `static/script.js` | Handles form submission & validation |
| `static/styles.css` | Website styling |
| `run_server.sh` | Easy start script for Linux/Mac |
| `run_server.bat` | Easy start script for Windows |

---

## ✅ Testing Checklist

Once the server is running at `http://localhost:5000`:

- [ ] Website loads properly in browser
- [ ] Form fields are visible and functional
- [ ] Fill out the test form completely
- [ ] Click "Submit Details"
- [ ] See success message in green
- [ ] Check your Gmail inbox for the email
- [ ] Email contains all form data submitted

---

## 🆘 If Something Goes Wrong

| Problem | Solution |
|---------|----------|
| "Cannot GET /" | Server isn't running. Run `python app.py` |
| Form says "Server is down" | Make sure Flask server is running in terminal |
| Email doesn't arrive | Check `.env` - make sure app password is correct (16 chars, no spaces) |
| Permission denied | Make sure you're in the right folder: `cd /home/nwokolo/egotrack` |
| Module not found (Flask, etc.) | Run: `pip install -r requirements.txt` |

---

## 📝 How It Works Now

```
User fills form → Submits to localhost:5000 → Flask processes → Sends email to Gmail
```

**No internet required for local testing!**

---

## 🎯 Next Steps (When Ready)

To make the form accessible online:
1. Deploy to free services like **Render**, **Railway**, or **Heroku**
2. Update script.js to point to your deployed server URL instead of localhost
3. Share the public URL with potential pilot users

---

## 📞 Support Resources

- **Gmail Help**: https://support.google.com/accounts/answer/185833
- **Flask Docs**: https://flask.palletsprojects.com/
- **Full Setup Guide**: See `SETUP_GUIDE.md` in this folder

---

**Ready? Start with Step 1 above! 🚀**
