**1. Overview**

This project automates a user journey flow for an e-commerce website using Selenium and Python. The automation includes testing key functionalities like product search, adding products to the cart, and checkout.

**2. Setup Instructions**


	Prerequisites
    * Python 3.9+
    * Docker (for containerized setup)
    * Selenium WebDriver
    * Allure (for reporting)


  Steps
- Clone the repository:
     -     git clone <repository-url

- Create a virtual environment and activate it:
     -     python3 -m venv 
           .venv source .venv/bin/activate

- Install required dependencies: 
     -     pip install -r requirements.txt

**3. Running Tests**

- Using Docker:
  - To build and run the Docker image:
    -     docker build -t test-assessment .
          docker run test-assessment

- Locally (without Docker):
  - Run tests with pytest:
    -     pytest tests/all_tests.py alluredir=allure-results


**4. Reporting :**
- Generate an Allure report:
  -     allure serve allure-results
- The Allure test report is available in the `allure-report.zip` file. To view the report:
  - Download the `allure-report.zip` file.
  - Extract the zip file.
  - Open the `index.html` file inside the extracted folder using a web browser.

**5. Test Structure**
- Page Object Model: Organized structure for handling UI elements and actions.
- Tests: Located in the test's directory. Each test follows the user journey scenarios.

- Key Files:
    * test_browse_products.py: Tests for browsing the products
    * test_shopping.py: Tests for purchasing the products.

**6. Dockerized Setup**
- The project includes a Dockerfile that sets up the testing environment with     Selenium and Chrome for headless testing. Use Docker for isolated and consistent test execution.
