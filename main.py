from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv
from haiku_generator import generate_haiku
from database import save_haiku, get_all_haikus

load_dotenv()

app = FastAPI(title="Haiku Generator")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the main UI"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def create_haiku(
    theme: str = Form(...),
    season: str = Form(...),
    mood: str = Form(...),
    keywords: str = Form(...)
):
    """Generate a new haiku based on user input"""
    try:
        haiku_text = generate_haiku(theme, season, mood, keywords)

        # Save to database
        haiku_id = save_haiku(theme, season, mood, keywords, haiku_text)

        return {
            "success": True,
            "haiku": haiku_text,
            "id": haiku_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
async def get_history():
    """Get all previously generated haikus"""
    try:
        haikus = get_all_haikus()
        return {"haikus": haikus}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)