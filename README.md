# Automated Testing Tool

This project is designed to streamline the process of testing your code against expected outputs on competitive programming platforms such as Codeforces. It helps you manage bigger and multiple test cases efficiently and aids in debugging.

## Features

- Automates the testing process for multiple test cases.
- Simplifies debugging by comparing your output with the expected output.
- Provides a clear structure to manage inputs and outputs.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AbdulselamAbdurehman/Automated-Testing.git
   ```

2. Navigate to the cloned directory:
   ```bash
   cd Automated-Testing
   ```

## Usage

1. Copy and paste the sample inputs into the `input.txt` file.
2. Copy and paste the expected outputs into the `output.txt` file.
3. Ensure your solution code is in `main.py`.
4. Run the handler script:
   ```bash
   python handler.py
   ```

### Note
The handler script assumes that the first line of the input file contains the number of test cases. Comment out or remove the debugging prints before running the handler.


## Debugging
When your code fails on some tests, handler will tell you where your output differed from the expected output. To debug your code with print statements, run your test cases directly in `main.py`. Keep in mind that any debugging prints will confuse the handler and cause it to  take is as an error.

## Example

Here’s an example for testing a program that prints the square of a given number for the given number of tests:

### input.txt
```
3
2
5
7
```

### output.txt
```
4
25
49
```

### main.py
```python
t = int(input())
for _ in range(t):
    print(int(input())**2)
```

### Running the Example

1. Ensure your `input.txt`, `output.txt`, and `main.py` are set up as shown above.
2. Run the handler script:
   ```bash
   python handler.py
   ```
3. The handler will execute `main.py`, capture its output, and compare it to `output.txt`, providing feedback on which test cases passed or failed:
   ```
   All tests passed
   ```

---

Feel free to customize the project further to suit your needs or Request Addional programming languages support! 