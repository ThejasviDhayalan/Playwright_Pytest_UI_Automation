'''
Utility Module: Screenshot Capture
# Description: This utility module provides a function to capture screenshots during test execution for debugging and reporting purposes.
Author: Thejasvi Dhayalan
Date: May 2026
'''

import os
from datetime import datetime
from playwright.sync_api import Page

def capture_screenshot(page: Page, filename: str = "screenshot", full_page: bool = True) -> str:
    """
    Capture a screenshot of the current page and save it to the screenshots directory.

    This function creates a screenshots directory if it doesn't exist,
    generates a timestamped filename, and captures the screenshot.

    Args:
        page: Playwright Page instance
        filename: Base name for the screenshot file (default: "screenshot")
        full_page: Whether to capture the full page or just the viewport (default: True)

    Returns:
        str: File path of the captured screenshot, or empty string if failed
    """
    try:
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename_with_timestamp = f"{filename}_{timestamp}.png"
        filepath = os.path.join(screenshots_dir, filename_with_timestamp)

        page.screenshot(path=filepath, full_page=full_page)
        return filepath

    except Exception as e:
        print(f"Failed to capture screenshot: {str(e)}")
        return ""

