### E-commerce Automated UI Testing with Playwright & Python

#### Key Takeaways
- **End-to-End (E2E) Testing Proficiency**: End-to-End (E2E) Testing Proficiency: Ability to automate the full customer journey, from account creation to final checkout.
- **Modern Locators Strategy**: Effective use of **XPath** to ensure test stability.
- **Project Architecture Awareness**: Implementing a clean structure with a clear separation between **configuration (`settings.py`) and test logic**.
- **Data-Driven Approach**: Utilizing external variables for sensitive and configuration data (URLs, emails).

---

#### Project overview
This repository contains a comprehensive suite of automated UI tests for an e-commerce platforms: **Fakestore Testelka**, **Automation Exercise**. 
The goal of this project was to simulate a real-world Automation Tester's task: ensuring that critical business paths remain functional despite UI complexity. The project covers the entire "Happy Path" and demonstrates advanced techniques for bypassing common automation blockers like payment security frames.

---

#### Tools & technologies
- **Python** – core programming language.
- **Playwright** – modern automation framework for fast and reliable E2E testing.
- **Pytest** – testing framework used for test execution and organization.
- **Git & GitHub** – version control and documentation.

---

#### Repository structure 
```
universal_qa_toolkit/
│
├── config/
│   └── settings.py           # centralized configuration (URLs, test data, credentials)
│
├── tests/
│   ├── test_registration.py  # User account creation scenarios
│   ├── test_login.py         # Authentication & security checks
│   ├── test_product_search.py# Navigation and search functionality
│   ├── test_edit_cart.py     # Quantity updates and product removal
│   └── test_checkout.py      # Complex checkout flow with Stripe/BLIK integration
│
├── .venv/                    # virtual environment (local only)
├── README.md                 # main project documentation and report
└── .gitignore                # files to be excluded from version control
```

--- 

#### How to run the tests

Tests are designed to run in a Python 3.14+ environment.
- **Install dependencies:** pip install playwright pytest and playwright install.
- **Set up environment:** Ensure PYTHONPATH is set to the project root.
- **Run all tests:** ```powershell $env:PYTHONPATH="."; pytest tests/ --headed
- **Run specific test:** ```powershell $env:PYTHONPATH="."; pytest tests/test_checkout.py --headed

---

#### Test coverage  
The suite covers critical e-commerce functionalities, ensuring high-quality user experience:
- **T1: User Registration:** Verify successful account creation with unique data, PASS
- **T2: Secure Login:** Validate authentication with correct/incorrect credentials, PASS
- **T3: Dynamic Search:** Confirm product findability via the search bar, PASS
- **T4: Cart Management:** Verify quantity updates and "Remove Product" functionality, PASS
- **T5: Advanced Checkout:** - Finalize order using BLIK/Credit Card, including iframe handling and Stripe Link bypass, PASS

---

#### Related
- [Tests](https://github.com/natmaleclachowska/universal_qa_toolkit/tree/main/config)
- [Configuration](https://github.com/natmaleclachowska/universal_qa_toolkit/tree/main/tests)

