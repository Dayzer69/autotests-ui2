from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
              wait_until='networkidle'
    )

    page.evaluate("""
    const title = document.getElementById('authentication-ui-course-title-text');
    title.textContent = 'New Text';
    """)