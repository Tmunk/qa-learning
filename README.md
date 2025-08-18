# QA Learning Project
This repository contains sample tests for practicing Python + pytest automation.

## Run Tests
1. **Activate the virtual environment**  
   `source venv/bin/activate`  
2. **Install required packages**  
   `pip install -r requirements.txt`  
3. **Run all tests**  
   `pytest tests/`  
4. **Run a single test file**  
   `pytest tests/test_sample.py`  
5. **Run a specific test function**  
   `pytest tests/test_sample.py::test_login_with_params`  
6. **Generate an HTML report**  
   `pytest tests/ --html=report.html --self-contained-html`  

## Notes
- The tests demonstrate parameterized testing for positive and negative login scenarios.  
- HTML reports provide a clear summary of test results.
