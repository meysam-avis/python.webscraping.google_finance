from playwright.sync_api import sync_playwright

if __name__=="__main__":
    url = "https://store.steampowered.com/"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto(url,timeout=0)
        page.wait_for_load_state("networkidle")
        page.evaluate("()=>window.scrollTo(0, document.body.scrollHeight)")
        page.screenshot(path="steampowered.png",full_page=True)




