from fastapi import FastAPI, Body
from scraping.playwright_scraper import scrape_chapter_with_screenshot  # ✅ this must match function name

app = FastAPI()

@app.post("/scrape")
def scrape_url(url: str = Body(...), chapter_id: str = Body(...)):
    content, screenshot_path = scrape_chapter_with_screenshot(url, chapter_id)
    return {"chapter_id": chapter_id, "content": content, "screenshot_path": screenshot_path}
