# Manual Test Cases – Login Flow

Test Case: Login with valid credentials  
Steps: Open login page, enter username and password, click submit  
Input: username="munky", password="password123"  
Expected Result: User is logged in successfully  

Test Case: Login with wrong username  
Steps: Open login page, enter wrong username and correct password, click submit  
Input: username="wronguser", password="password123"  
Expected Result: Login fails, error message displayed  

Test Case: Login with wrong password  
Steps: Open login page, enter correct username and wrong password, click submit  
Input: username="munky", password="wrongpass"  
Expected Result: Login fails, error message displayed  

Test Case: Login with empty fields  
Steps: Open login page, leave username and password blank, click submit  
Input: username="", password=""  
Expected Result: Login fails, error message displayed  

Test Case: Login with special characters  
Steps: Open login page, enter special characters in username and/or password, click submit  
Input: username="!@#", password="%$#"  
Expected Result: Login fails, error message displayed
