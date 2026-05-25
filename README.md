# Playwright-Pytest UI Automation Framework

A scalable, maintainable, and enterprise-ready UI automation framework built using Playwright and Pytest for end-to-end web application testing.

---

# 🚀 Project Overview

This framework automates key business workflows of the Automation Exercise web application using modern automation practices and industry-standard framework design principles.

The framework is designed with:

- Page Object Model (POM)
- Data-Driven Testing
- BDD support using Gherkin
- Cross-browser execution
- Parallel execution capability
- Allure reporting integration
- Trace and screenshot debugging support
- CI/CD ready architecture

GitHub Repository:
https://github.com/ThejasviDhayalan/Playwright_UI_Automation

---

# 🏗️ Framework Architecture

## High-Level Design

```bash
Playwright-Pytest-Framework/
│
├── tests/                                # UI test cases using Playwright + Pytest
│   ├── test_01_user_registration.py
│   ├── test_02_order_placement.py
│   ├── test_03_contact_form_submission.py
│   ├── test_04_newsletter_subscription.py
│   └── test_05_invalid_user_login.py
│
├── features/                             # BDD feature files (Gherkin syntax)
│   ├── order_placement.feature
│   └── newsletter_subscription.feature
│
├── step_definitions/                     # Step definitions for BDD scenarios
│   ├── order_placement_steps.py
│   └── newsletter_subscription_steps.py
│
├── pages/                                # Page Object Model classes
│   ├── signup_page.py
│   ├── login_page.py
│   ├── home_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── payment_page.py
│   ├── contact_page.py
│   └── common_page.py
│
├── data/                                 # External test data
│   ├── user_login.json
│   ├── invalid_user_login.json
│   ├── payment.json
│   ├── test_data.xlsx
│   └── contact_form.txt
│
├── utils/                                # Reusable utility/helper modules
│   └── screenshot.py
│
├── screenshots/                          # Failure screenshots
│
├── traces/                               # Playwright trace files
│
├── reports/                              # Allure/HTML reports
│
├── pytest.ini                            # Pytest configurations
├── README.md                             # Project documentation
└── conftest.py                           # Shared fixtures and hooks
```

---

# 🎯 Features Implemented

## ✅ Functional Test Coverage

### 1. User Registration

- New user signup workflow
- Excel-driven registration test data
- Validation of successful account creation

### 2. End-to-End Order Placement

- Product selection and cart validation
- Checkout workflow automation
- Payment flow validation
- Order confirmation verification

### 3. Contact Form Submission

- Contact form validation
- File upload handling
- Successful submission verification

### 4. Newsletter Subscription

- Newsletter subscription workflow
- Success message validation

### 5. Invalid User Login Validation

- Negative login testing
- Invalid credential handling
- Error message verification

---

# 🧩 Framework Design Principles

## 1. Page Object Model (POM)

Encapsulates:

- Page locators
- Page actions
- Reusable UI operations

Benefits:

- Better code readability
- Improved maintainability
- High reusability
- Reduced code duplication

---

## 2. Data-Driven Testing

Externalized test data stored in:

- JSON files
- Excel files
- Text files

Benefits:

- Easy test maintenance
- Clear separation of test logic and test data
- Scalable test coverage

---

## 3. BDD Support

Implemented using:

- Gherkin feature files
- pytest-bdd step definitions

Advantages:

- Business-readable test scenarios
- Improved collaboration between QA and stakeholders
- Better requirement traceability

---

## 4. Reusable Utility Modules

Shared helper modules for:

- Screenshot capture
- File handling
- Reusable validations
- Common helper methods

---

# 🛠️ Technology Stack

| Technology        | Purpose                  |
|-------------------|--------------------------|
| Python 3.8+       | Programming Language     |
| Playwright        | Browser Automation       |
| Pytest            | Test Framework           |
| pytest-bdd        | BDD Support              |
| Allure Reports    | Advanced Reporting       |
| OpenPyXL          | Excel Data Handling      |
| Page Object Model | Framework Design Pattern |

---

# ⚙️ Setup Instructions

## Prerequisites

- Python 3.8+
- pip
- Git

---

## Installation

```bash
# Clone repository
git clone https://github.com/ThejasviDhayalan/Playwright_UI_Automation.git

# Navigate to project
cd Playwright_UI_Automation

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

---

# ▶️ Running Tests

## Run All Tests

```bash
pytest
```

---

## Run Specific Test File

```bash
pytest tests/test_01_user_registration.py
```

---

## Run Tests on Specific Browser

```bash
pytest tests/test_02_order_placement.py --browser_name=chromium
```

---

## Run BDD Scenarios

```bash
pytest step_definitions/order_placement_steps.py
```

---

## Run Tests in Parallel

```bash
pytest -n 2
```

---

# 📊 Reporting

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## Generate Allure Report

```bash
pytest --alluredir=reports/allure-results
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

---

# 🔍 Debugging Support

## Automatic Screenshot Capture

- Screenshots captured automatically on failures

## Playwright Trace Viewer

- Step-by-step execution tracing for debugging failed tests

```bash
playwright show-trace trace.zip
```

---

# 🔧 Configuration Files

## conftest.py

Contains:

- Browser setup
- Shared fixtures
- Setup and teardown methods
- Shared reusable configurations

---

## pytest.ini

Contains:

- Pytest markers
- Plugin configurations
- Test discovery settings
- Execution settings

---

# ✅ Best Practices Followed

- Modular framework architecture
- Separation of concerns
- Reusable page objects
- Externalized test data
- Explicit waits implementation
- Cross-browser support
- Parallel execution support
- CI/CD ready setup
- Clean and maintainable codebase

---

# 🚀 CI/CD Ready

The framework is designed for integration with:

- Jenkins
- GitHub Actions
- Azure DevOps
- Other CI/CD pipelines

Supports:

- Scheduled execution
- Automated reporting
- Parallel execution
- Headless execution

---

# 📌 Future Enhancements

- Docker integration
- API automation support
- Database validation
- Cloud execution support
- Slack/Email reporting integration
- Environment configuration management

---

# 👨‍💻 Author

Thejasvi Dhayalan

GitHub:
https://github.com/ThejasviDhayalan

---

# 🎉 Conclusion

This project demonstrates a scalable automation framework using modern QA automation practices with:

- Functional UI automation
- BDD implementation
- Data-driven testing
- Reporting and debugging capabilities
- Scalable framework architecture
- CI/CD integration readiness

The framework is designed to be maintainable, reusable, and extensible for enterprise-level automation projects.
