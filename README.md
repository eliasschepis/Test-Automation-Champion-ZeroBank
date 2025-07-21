# ✅ QA Automation Framework - Zero Bank

This is a professional QA automation framework built with **Python**, **Selenium WebDriver**, and **Pytest**, following the **Page Object Model (POM)** design pattern. It is designed to automate UI testing of the [Zero Bank](http://zero.webappsecurity.com/) demo banking application.

---

## 🚀 Project Goals

- Automate core banking functionalities (login, transfers, payments, navigation)
- Ensure maintainability and scalability via Page Object Model
- Enable easy execution locally and in CI/CD pipelines using Docker and GitHub Actions
- Provide clear reporting and support visual regression testing

---

## 📁 Project Structure

```
zerobank-automation/
│
├── pages/                  # Page Object classes (LoginPage, HomePage, etc.)
├── tests/                  # Test files organized by feature
├── utils/                  # Utility functions and helpers
├── reports/                # Test reports (HTML, screenshots)
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration
└── conftest.py             # Fixtures and global setup
```

---

## 🧪 Tech Stack

- **Python 3.11+**
- **Selenium WebDriver**
- **Pytest**
- **Page Object Model (POM)**
- **Docker** (upcoming)
- **GitHub Actions** (upcoming)
- **Playwright** for visual testing (upcoming)

---

## 🔧 Installation & Setup

```
# 1. Clone the repo
git clone https://github.com/yourusername/zerobank-automation.git
cd zerobank-automation

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run Tests

```
# Run all tests
pytest

# Run tests with detailed output
pytest -v

# Run with HTML report
pytest --html=reports/report.html
```

---

## 📌 Notes

- This project is for educational and professional practice purposes.
- The target application is a public demo and not a production environment.
- The repository will evolve as features such as Docker, CI/CD, API and visual testing are added.

---

## 👤 Author

**Elias Schepis**  
QA Automation Engineer | Python | Selenium | Pytest | Docker | CI/CD  
[LinkedIn](https://www.linkedin.com/in/your-profile) • [GitHub](https://github.com/yourusername)
