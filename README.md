# Starting Price Lookup

OBJECTIVE: The Starting Price Lookup program is developed with an aim to automate the process of extracting information of the phone models that match given criteria on the CLI(Command-line interface).

DESCRITION: As a user starts the program a welcome message is displayed, followed by which the program navigates to Bell Smart Phone Homepage and waits for user inputs to the prompted questions.The program asks for the following OPTIONAL questions which can be skipped by entering '-1': Preferred Vendors (Multiple vendors can be provided, entering '-1' when done),Preferred lower and upper limit for 24 month monthly price at $0 down,Preferred lower and upper limit for Full Device price, Preferred Colors (Multiple colors can be provided, entering '-1' when done).

The program fetches the phone models which satisfy the search criteria, extracts and displays the details on the CLI(Command-line interface).

## Instructions to run the project (Windows)

1) Clone the project from GitHub.

2) Download chromedriver (Chrome): https://sites.google.com/a/chromium.org/chromedriver/downloads depending on the Chrome version you are using.

3) Extract the: chromedriver_win32.zip folder and it will give you the: chromedriver.exe

4) Place the executable file: chromedriver.exe in C:\Windows so that Python and Selenium can find it.

* If you already have PIP installed skip step 5-7:

5) Download get-pip.py to install pip: https://phoenixnap.com/kb/install-pip-windows

6) Open Command Prompt and navigate to the location of the get-pip.py file

7) To install PIP, type

```bash
python get-pip.py
```
8) Open Command Prompt

9) To install Selenium Webdriver, type

```bash
pip install selenium
```
10) Now go to the Project Directory via the command prompt

11) Now, to run the program, type 

```bash
python source_price_lookup.py
```
12) After execution, you will see a welcome message, after which the Bell Smartphone Homepage will load in the foreground.

13) The questions will be prompted for user inputs that form the basis for search criteria.


## Instructions to run the project (Linux)

1) Clone the project from GitHub

2) Install pip on Ubuntu

```bash
apt install python3-pip
```
3) Install Selenium by executing the following command in Terminal:

```bash
pip install selenium
```
4) Install Chromedriver for Chrome:

```bash
wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip
```
```bash
unzip chromedriver_linux64.zip
```
```bash
sudo mv chromedriver /usr/local/bin/
```
5) Open Terminal

6) Go to the Project Directory

7) Now, to run the program, type 

```
python source_price_lookup.py
```

8) After execution, you will see the a welcome message, after which the Bell Smartphone Homepage will load in the foreground.

9) The questions will be prompted for user inputs that form the basis for search criteria.