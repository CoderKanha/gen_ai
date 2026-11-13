# Context
# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context1 = browser.new_context()
#     context2 = browser.new_context()
#     context3 = browser.new_context()
#     page1 = context1.new_page()
#     page1.goto("https://www.google.com")
#     page2 = context1.new_page()
#     page2.goto("http://www.youtube.com")
#     page3 = context2.new_page()
#     page3.goto("http://www.amazon.com")
#     page4 = context2.new_page()
#     page4.goto("http://www.flipkart.com")
#     browser.close()


# from playwright.sync_api import sync_playwright
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.youtube.com")
#     print("Page URL", page.url)
#     page.goto("https://www.wikipedia.com")
#     page.go_back()
#     print("After back Page URL", page.url)
#     page.go_forward()
#     print("After forward Page URL", page.url)
#     context.close()
#     browser.close()

# Assignment
# 1. Launch Chromium in visible mode.
# 2. Create two independent browser contexts.
# 3. Open Google and YouTube in Context 1.
# 4. Open GitHub and Playwright documentation in Context 2.
# 5. Print the title and URL of all four pages.
# 6. Take full-page screenshots of all four websites.
# 7. Reload the Google page.
# 8. Close both contexts and the browser.

# Importing required modulels
from playwright.sync_api import sync_playwright
with sync_playwright() as p:

    # launching the chromium browser
    browser = p.chromium.launch(headless=False)

    # Creating the context
    context1 = browser.new_context()
    context2 = browser.new_context()

    # Creating the pages and goto some particular urls
    page1 = context1.new_page()
    page1.goto("https://www.google.com")
    page2 = context1.new_page()
    page2.goto("http://www.youtube.com")
    page3 = context2.new_page()
    page3.goto("http://www.github.com")
    page4 = context2.new_page()
    page4.goto("http://www.playwright.dev")

    # Printing title and URL for all pages
    print("Page 1 Title", page1.title())
    print("Page 1 URL", page1.url)

    print("Page 2 Title", page2.title())
    print("Page 2 URL", page2.url)

    print("Page 3 Title", page3.title())
    print("Page 3 URL", page3.url)

    print("Page 4 Title", page4.title())
    print("Page 4 URL", page4.url)

    # Taking screenshot and saving the full page image
    page1.screenshot(path="page1.png", full_page=True)
    page2.screenshot(path="page2.png", full_page=True)
    page3.screenshot(path="page3.png", full_page=True)
    page4.screenshot(path="page4.png", full_page=True)

    # Reloading the first page (Google)
    page1.reload()

    # Closing the context and browser
    context1.close()
    context2.close()
    browser.close()