# Password generator and checker
#### Video Demo:  [https://www.youtube.com/watch?v=Sc0Unbr7qKc](https://www.youtube.com/watch?v=Sc0Unbr7qKc)
## Description:
```Password generator and checker``` is my final project for CS50's Introduction to Programming with Python. I created this program because I am passionate about cybersecurity and believe in the importance of strong passwords for your accounts.

## Folder Contents
- **project.py**: This file contains my ```main``` function and the other functions necessary to implement the program.
- **test_project.py**: This file contains my test functions for project.py.
- **requirements.txt**: All ```pip```-installable libraries that I used for this project are listed here.

## Libraries Used
- ```sys```: for system-specific functions like signaling an intention to exit the interpreter
- ```secrets```: for generating cryptographically strong random numbers suitable for managing passwords
- ```string```: for manipulation of strings and creating new passwords
- ```pytest``` : for testing functions

## How it works
- Run the program via

    ```
    python project.py
    ```

- Answear the first question if you want or not to generate a new password
    - If the answear is ```yes``` you will be asked a length for your password
    - Then the program will generate the password for you

- Answear the second question if you want or not to check if a password is strong enough
    - If the answear is ```yes``` you will be prompted to write the password you want to check
    - If the password is not strong enough you will get a list with the requirements that are not fulfilled
    - Then you will be asked if you want to generate a new password
        - If you type ```yes``` you will get your new secure password
        - If you type ```no``` the program will exit

- If the answear is ```no``` for both questions the program will exit

## Documentation
### project.py Functions (excluding main)
```python
def generate(length):
```
**Description:**
- Generates a new password.

**Args:**
- ```length``` (```str```): password length

**Returns:**
- ```str```: returns the password

```python
def check(password):
```
**Description:**
- Checks if a password is strong enough

**Args:**
- ```password``` (```str```): the password

**Returns:**
- ```str```: returns the result of password verification

```python
def check_length(password):
```
**Description:**
- Checks the length of a password

**Args:**
- ```password``` (```str```): the password

**Returns:**
- ```str```: returns a message if the password is too short or ```None``` if the password length is ok

```python
def check_special(password):
```
**Description:**
- Checks if the password contains special characters

**Args:**
- ```password``` (```str```): the password

**Returns:**
- ```str```: returns a message if the password doesn't contain special characters or ```None``` otherwise

```python
def check_a_z(password):
```
**Description:**
- Checks if the password contains A-Z letters

**Args:**
- ```password``` (```str```): the password

**Returns:**
- ```str```: returns a message if the password doesn't contain A-Z letters or ```None``` otherwise

```python
def check_a_z(password):
```
**Description:**
- Checks if the password contains A-Z letters

**Args:**
- ```password``` (```str```): the password

**Returns:**
- ```str```: returns a message if the password doesn't contain A-Z letters or ```None``` otherwise

```python
def check_num(password):
```
**Description:**
- Checks if the password contains numbers

**Args:**
- ```password``` (```str```): the password

**Returns:**
- ```str```: returns a message if the password doesn't contain numbers or ```None``` otherwise