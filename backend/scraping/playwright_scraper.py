from playwright.sync_api import sync_playwright
import os

def scrape_chapter_with_screenshot(url: str, chapter_id: str):
    os.makedirs("data/screenshots", exist_ok=True)
    screenshot_path = f"data/screenshots/{chapter_id}.png"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.inner_text("body")
        page.screenshot(path=screenshot_path, full_page=True)
        browser.close()

    return content, screenshot_path
