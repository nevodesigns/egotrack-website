# 🚀 GitHub Hosting Guide for EgoTrack Website

Your project is **ready to push to GitHub**! Follow these steps:

## Step 1: Create GitHub Repository

1. Go to **https://github.com/new**
2. **Repository name:** `egotrack-website` (or your preferred name)
3. **Description:** "EgoTrack waitlist website - Flask backend for signing up pilot users"
4. **Public or Private:** Choose based on your preference
5. **DO NOT initialize with README** (we already have one)
6. **DO NOT add .gitignore** (we have one)
7. Click **"Create repository"**

## Step 2: Add Remote and Push

Copy the commands from the GitHub page (it will show you exactly what to run).

Generally, it will be:

```bash
cd "/home/nwokolo/egotrack website"

# Add the remote repository
git remote add origin https://github.com/YOUR_USERNAME/egotrack-website.git

# Rename branch to main (optional but recommended)
git branch -m master main

# Push to GitHub
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 3: Verify on GitHub

1. Go to your repository: `https://github.com/YOUR_USERNAME/egotrack-website`
2. You should see all your files listed
3. README.md will display automatically

## 📋 What's Included

✅ Flask backend (app.py)  
✅ HTML, CSS, JavaScript (templates & static)  
✅ Complete documentation  
✅ .gitignore (excludes .env and private files)  
✅ requirements.txt (for dependencies)  

## 🔐 Security Notes

⚠️ **The `.env` file is NOT included** (protected by .gitignore)  
- Your Gmail credentials stay private
- Each deployment has its own .env

✅ **To use after cloning:**
```bash
cp .env.example .env
# Edit .env with your actual credentials
```

## 🌐 Deployment Options

### Option 1: Deploy to Render (Free)
```bash
# 1. Create account at render.com
# 2. Connect GitHub repo
# 3. Create Web Service
# 4. Set build command: pip install -r requirements.txt
# 5. Set start command: gunicorn app:app
# 6. Add environment variables (same as .env)
```

### Option 2: Deploy to Heroku
```bash
# 1. Create account at heroku.com
# 2. Install Heroku CLI
# 3. Create Procfile (included in repo)
# 4. Push: git push heroku main
```

### Option 3: Deploy to Railway
```bash
# 1. Create account at railway.app
# 2. Connect GitHub
# 3. Select repo and deploy
# 4. Add environment variables
```

## 📝 Common Git Commands

```bash
# Check status
git status

# Add new changes
git add .

# Commit changes
git commit -m "Your message here"

# Push to GitHub
git push

# Pull latest changes
git pull

# View commit history
git log --oneline
```

## ✨ Next Steps

1. ✅ Create GitHub repository
2. ✅ Push code to GitHub
3. ✅ (Optional) Deploy to Render/Heroku/Railway
4. ✅ Share live link with people

## 🎯 Live URL After Deployment

Once deployed, share your live website link:
```
https://your-deployed-app.onrender.com
```

Users can fill the form from anywhere!

---

**Good luck! Your EgoTrack website is ready for the world! 🚀**
