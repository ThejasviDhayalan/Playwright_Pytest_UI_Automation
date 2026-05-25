'''
Configuration File: Pytest Conftest
Description: This configuration file contains pytest fixtures and hooks for setting up and tearing down test environments.
Author: Thejasvi Dhayalan
Date: May 2026
'''

import pytest

@pytest.fixture(scope="session")
def user_credentials(request):
    """
    Session-scoped fixture to provide user credentials.

    Args:
        request: Pytest request object

    Returns:
        User credentials parameter
    """
    return request.param

def pytest_addoption(parser):
    """
    Add custom command-line options to pytest.

    Args:
        parser: Pytest argument parser
    """
    parser.addoption("--browser_name", action = "store", default = "chromium", help = "launching_browser")
    parser.addoption("--url_name", action = "store", default = "https://automationexercise.com/",  help = "launching_url")
    parser.addoption("--enable_trace", action = "store_true", help = "enable_tracing" )

@pytest.fixture
def browser_instance(playwright, request):
    """
    Fixture to set up and tear down browser instance for each test.

    This fixture launches the specified browser, creates a new context,
    navigates to the specified URL, and handles cleanup after the test.

    Args:
        playwright: Playwright instance
        request: Pytest request object

    Yields:
        Page instance for test execution
    """
    # Get command-line options
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    enable_trace = request.config.getoption("enable_trace")

    # Launch the specified browser (default to chromium if unknown)
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        browser = playwright.chromium.launch(headless=False)

    # Create browser context and clear cookies for clean state
    context = browser.new_context()
    context.clear_cookies()

    # Enable tracing if requested (for debugging)
    if enable_trace:
        context.tracing.start(name = 'trace', screenshots = True, snapshots = True)

    # Create new page and navigate to the specified URL
    page = context.new_page()
    page.goto(url_name)
    yield page

    # Cleanup: Stop tracing, close context and browser
    test_name = request.node.name
    trace_path = f"traces/{test_name}.zip"
    if enable_trace:
        context.tracing.stop(path=trace_path)
    context.close()
    browser.close()

