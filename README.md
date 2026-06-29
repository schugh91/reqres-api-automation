# 🚀 ReqRes API Automation Framework

A Python-based API Automation Framework developed using **Pytest** and **Requests** to validate CRUD operations on the ReqRes REST API.

This project demonstrates API testing concepts such as request validation, response verification, fixture usage, environment variable management, and automated test execution.

---

## 📌 Project Overview

The framework automates the following API operations:

* Get All Users
* Get Single User
* Create User
* Update User Details
* Delete User

The project uses dynamic test data, reusable fixtures, and environment variables to improve maintainability and scalability.

---

## 🛠️ Tech Stack

* Python
* Pytest
* Requests
* Python-dotenv
* ReqRes API

---

## 📂 Project Structure

```text
reqres_api_automation
│
├── tests
│   ├── test_get_users.py
│   ├── test_get_single_user_data.py
│   ├── test_create_new_user.py
│   ├── test_update_user_details.py
│   └── test_delete_user_data.py
│
├── utils
│   └── config.py
│
├── conftest.py
├── .env.example
├── requirements.txt
└── README.md
```

---

## ✅ Test Scenarios Covered

### Get All Users

* Verify status code is 200
* Validate pagination details
* Verify user list is not empty
* Store random user details for subsequent tests

### Get Single User

* Verify status code is 200
* Validate selected user ID
* Validate first name of selected user

### Create User

* Verify status code is 201
* Validate user details in response
* Verify successful user creation

### Update User Details

* Verify status code is 200
* Validate updated user information
* Verify presence of `updatedAt` field
* Validate API response time

### Delete User

* Verify status code is 204
* Verify response body is empty

---

## 🔧 Configuration

Environment variables are stored in a `.env` file.

Example:

```env
BASE_URL=https://reqres.in
API_KEY=your_api_key_here
```

---

## 🧩 Pytest Fixtures

The framework uses reusable fixtures defined in `conftest.py`:

* Headers Fixture
* Random User Fixture
* User Details Fixture
* Update User Fixture

These fixtures help eliminate duplicate code and improve maintainability.

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/schugh91/reqres-api-automation.git
```

Navigate to the project directory:

```bash
cd reqres-api-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_get_users.py
```

---

## 📊 Sample Test Results

```bash
============================= test session starts =============================
collected 5 items

tests/test_get_users.py .                                              [20%]
tests/test_get_single_user.py .                                        [40%]
tests/test_create_user.py .                                            [60%]
tests/test_update_user.py .                                            [80%]
tests/test_delete_user.py .                                            [100%]

============================== 5 passed ======================================
```

---

## 🎯 Key Learning Outcomes

* REST API Testing
* CRUD Operations Validation
* Pytest Framework
* Pytest Fixtures
* Environment Variables
* Response Validation
* Status Code Verification
* Response Time Validation
* Automated API Testing using Python

---

## 🔮 Future Enhancements

* API Client Utility Module
* Logging
* HTML Reports
* Allure Reporting
* Data-Driven Testing
* Schema Validation
* CI/CD Integration using GitHub Actions
* Docker Support

---

## 👩‍💻 Author

**Surabhi Chugh**

QA Engineer transitioning from Manual Testing to Automation Testing using Python, Postman, Pytest, and Playwright.
