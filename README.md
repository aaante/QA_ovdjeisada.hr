# Disclaimer

All the test cases are inside the following files:

- /naslovna/test_naslovna.py
- /usluge/test_usluge.py
- /kontakt/test_kontakt.py

https://github.com/aaante/QA_ovdjeisada.hr/assets/134620137/49252680-a3a1-4fa3-a5f0-836f7ae59e46

# Summary

"Ovdje I Sada", an educational-advisory center launched its website in May 2023. The website was tested for full functionality, using functional testing methodology, both automated (smoke testing) and manual (exploratory testing). 106 test cases were executed using Python + Selenium combination.

# Software Testing Life Cycle (STLC)

### The project was structured around specific STLC steps:

1️⃣ Requirement analysis

2️⃣ Test planning

3️⃣ Test case design & development

4️⃣ Test environment setup

5️⃣ Test execution & reporting

6️⃣ Test closure

# 1️⃣ Requirement analysis

### Summary of stakeholder (client + lead designer and developer) interviews:

👋 The website is live and was never tested

🚫 There are no known defects

👤 No specific user flows were designed (the primary design guideline was a WordPress template)

📄 Specific pages are similar in content and functionality

⏰ Time constraint (testing should be done before migrating the website to a different server)

### Testing to be done:

⚫️ Dynamic -> Black box -> Functional -> Smoke Testing (Automated) & Exploratory Testing (Manual)

<img src="https://github.com/aaante/QA_ovdjeisada.hr/assets/134620137/4b75e939-e68c-4132-9c5d-6197e152d19c" alt="Flowchart of testing types" width="600"/>

_Flowchart of testing types_

# 2️⃣ Test planning

## Test approach:

### Smoke testing:

⚽️ Purpose: Testing of the most critical functionalities of the website

🔍 Scope: Part of the website, critical functionalities/flows

👉 Method: Automatic scripts (Selenium + Python), defects recorded in Excel

### Exploratory testing:

⚽️ Purpose: Undocumented testing on the fly

🔍 Scope: Entire site, all functionalities/flows

👉 Method: Manual, defects recorded in Excel

## Test Pass/Fail/Incomplete criteria:

🟩 A test case will be considered passed if all of its steps are executed successfully, and the actual results match the expected results

🟥 A test case will be considered failed if at any step the actual result does not match the expected result: a defect will be logged for each failed test case

🟨 A test case will be considered incomplete if it did not complete execution due to several reasons, for example, the automated script failed, or test data was missing

## Test environment & infrastructure:

### Required infrastructure:

💻 MacBook Air M1 (latest macOS update)

💻 Chrome browser (latest version)

💻 PyCharm IDE (latest version)

# 3️⃣ Test case design & development

### Test cases for smoke testing (automated):

#️⃣ 106 test cases in total

#️⃣ 95 test cases for "Naslovna" page

#️⃣ 11 test cases spread across other pages ("Usluge" and "Kontakt" pages) that test critical functionalities not present in "Naslovna" page

### A few specific test cases:

🎠 Testing carousel functionality

🗺️ Testing map widget functionality

✉️ Testing contact input form

<img src="https://github.com/aaante/QA_ovdjeisada.hr/assets/134620137/2da80f85-b8cc-4e30-8869-eeb94609d631" alt="Excel spreadsheet of 'Naslovna' test suite" width="600"/>

_Excel spreadsheet of “Naslovna” test suite_

<img src="https://github.com/aaante/QA_ovdjeisada.hr/assets/134620137/36938974-d065-45a9-88e0-d99f182018de" alt="Python scripts for 'Naslovna' test suite" width="600"/>

_Python scripts for “Naslovna” test suite_

[Link to Excel test cases spreadsheet](https://1drv.ms/x/s!Aic-y_rltApahFEkREDKIKeSjkP6?e=BJ5kao)

# 4️⃣ Test environment setup

### MacOS:

1. Install Xcode

2. Install Homebrew

3. Install Python3 with Brew

4. Create Virtual Environment

5. Install PyCharm IDE

6. Install Selenium

7. Install Chrome Webdriver Manager

8. Install PyTest

# 5️⃣ Test execution & reporting

https://github.com/aaante/QA_ovdjeisada.hr/assets/134620137/522509f8-57cd-4342-a1e8-2933f7b080c4

_Test case execution: Testing map widget functionality_

https://github.com/aaante/QA_ovdjeisada.hr/assets/134620137/b937e06c-35f1-42e7-9714-266a4acfa6e5

_Test case execution: Testing carousel functionality_

# 6️⃣ Test closure

<img src="https://github.com/aaante/QA_ovdjeisada.hr/assets/134620137/ea4de312-c09a-43a5-b20e-d50745f1aa0d" alt="Results of the execution of 106 test cases: smoke testing (automated)" width="600"/>

_Results of the execution of 106 test cases: smoke testing (automated)_

<img src="https://github.com/aaante/QA_ovdjeisada.hr/assets/134620137/482d97ca-b2af-4e31-a9d2-53b135206add" alt="3 bugs were found during exploratory testing (manual)" width="600"/>

_3 bugs were found during exploratory testing (manual)_

# Next steps

➡️ Troubleshoot incomplete test cases

➡️ Collaborate with the developer in fixing bugs

➡️ Conduct non-functional performance testing

➡️ Conduct all testing on other browsers (Firefox, Safari, Edge, Opera)

# Conclusion

To wrap it all up, the thing that made this project a really interesting experience was the challenge of keeping track of all the different test cases (I can imagine something like TestRail would be really helpful here 😁) as well as the challenges of creating and debugging the automated tests that I've found really enjoyable so I'm already planning to do some personal automation projects to further refine my skills.

📊 [Link to Excel test cases spreadsheet](https://1drv.ms/x/s!Aic-y_rltApahFEkREDKIKeSjkP6?e=BJ5kao)
