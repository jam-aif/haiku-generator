# Haiku Generator

A simple web app that generates beautiful haikus using AI and stores them in a cloud database.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your API keys:
   - Get OpenAI API key from: https://platform.openai.com/api-keys
   - Get Supabase credentials from your project dashboard

3. **Create database table in Supabase:**
   Go to your Supabase SQL Editor and run:
   ```sql
   CREATE TABLE haikus (
       id SERIAL PRIMARY KEY,
       theme VARCHAR(255) NOT NULL,
       season VARCHAR(50) NOT NULL,
       mood VARCHAR(50) NOT NULL,
       keywords TEXT,
       haiku_text TEXT NOT NULL,
       created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
   );
   ```

4. **Run the app:**
   ```bash
   python main.py
   ```

5. **Open browser to:** http://localhost:8000

## Features

- ✨ Generate haikus based on theme, season, mood, and keywords
- 💾 Store haikus in Supabase database
- 📖 View history of generated haikus
- 🎨 Beautiful, responsive UI

## Demo Script

Perfect for live coding demonstrations:

1. "Let's build a haiku generator in under an hour"
2. Show the simple file structure (6 files total)
3. Demonstrate the form inputs and generation
4. Show the database storage and history feature
5. Deploy-ready with environment variables

## Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** HTML + CSS + Vanilla JavaScript
- **AI:** OpenAI GPT-3.5
- **Database:** Supabase (PostgreSQL)
- **Deployment:** Ready for Railway, Heroku, or Vercel