# odexpert-de-solver
ODEXpert is a Python-based GUI application designed to solve first-order differential equations. It supports checking whether an equation is homogeneous or exact, and it computes the corresponding solutions using SymPy. The GUI is built using CustomTkinter for a modern interface.

#Project Structure
- main.py: Splash screen
- logic.py: Differential equation logic (homogeneous & exact).
- calc.py: Main GUI and UI logic.

#Installation
Make sure you have Python 3.7+ installed on your system.
Then install the following libraries:
- customtkinter
- mpmath
- sympy

#How to Run
1. Run the project by opening main.py.
2. Click either dx or dy depending on which derivative you want to compute. This will enable the correct input field for your expression.
3. Click Solve to compute and display the answer.
