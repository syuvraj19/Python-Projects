# Simple Python Calculator

"""
This is a simple calculator program written in Python that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

Features:
- Addition
- Subtraction
- Multiplication
- Division

How to Use:
1. Clone the Repository:
   Clone this repository to your local machine using:
   git clone <repository_url>

2. Navigate to the Project Directory:
   cd <repository_directory>

3. Run the Calculator:
   Execute the `calculator.py` file to start the calculator:
   python calculator.py

4. Select Operation:
   - You will be prompted to select an operation:
     Select operation:
     1. Add
     2. Subtract
     3. Multiply
     4. Divide
   - Enter the number corresponding to the operation you want to perform.

5. Enter Numbers:
   - You will be prompted to enter the first and second numbers.
   - Enter the numbers and the calculator will perform the selected operation.

6. View Result:
   - The result of the calculation will be displayed.

7. Perform Another Calculation:
   - You will be asked if you want to perform another calculation. Enter `yes` to continue or `no` to exit.

Code Explanation:
Functions:
- add(x, y): Returns the sum of `x` and `y`.
- subtract(x, y): Returns the difference between `x` and `y`.
- multiply(x, y): Returns the product of `x` and `y`.
- divide(x, y): Returns the quotient of `x` divided by `y`. Checks to prevent division by zero.

Main Calculator Function:
- calculator(): 
  - Displays a menu for selecting the operation.
  - Takes user input for the choice of operation and the numbers to operate on.
  - Performs the selected operation and displays the result.
  - Asks the user if they want to perform another calculation and continues or exits based on the response.

Example:
Here's an example of how the calculator works:

Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice(1/2/3/4): 1
Enter first number: 10
Enter second number: 5
10.0 + 5.0 = 15.0
Do you want to perform another calculation? (yes/no): yes
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice(1/2/3/4): 4
Enter first number: 10
Enter second number: 0
Error! Division by zero.
Do you want to perform another calculation? (yes/no): no

License:
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements:
- Inspired by various basic Python calculator examples.
- Created as a learning project to understand Python functions, loops, and conditionals.
"""
