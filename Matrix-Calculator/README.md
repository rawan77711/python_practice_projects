# 🧮 Matrix Calculator
A command-line matrix calculator built with Python and NumPy.
Supports the core matrix operations through a simple interactive menu.

## ✨ Features
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division (`matrix1 × inverse(matrix2)`)
- 🔄 Transpose
- 🔁 Inverse
- 📐 Determinant

## 📦 Requirements
- Python 3
- NumPy


## 🚀 Usage
Run the script:
```bash
python main.py
```
You'll be prompted to choose an operation, then enter one or two matrices depending on the operation.

### 📋 Menu options
| Key | Operation      |
|-----|----------------|
| A   | ➕ Addition       |
| S   | ➖ Subtraction    |
| M   | ✖️ Multiplication |
| V   | ➗ Division       |
| T   | 🔄 Transpose      |
| I   | 🔁 Inverse        |
| D   | 📐 Determinant    |

### ⌨️ Entering a matrix
When prompted, first enter the number of rows and columns, then enter each row as space-separated numbers.
```
Number of rows: 2
Number of columns: 2
Enter row: 1 2
Enter row: 3 4
```

## 💡 Example
```
Please, Enter Your Option: a
Enter the first matrix:
Number of rows: 2
Number of columns: 2
Enter row: 1 2
Enter row: 3 4
Enter the second matrix:
Number of rows: 2
Number of columns: 2
Enter row: 5 6
Enter row: 7 8

The Result is:
[[ 6.  8.]
 [10. 12.]]
```

## 🛡️ Error Handling
The calculator validates input and matrix dimensions before performing operations:
- Addition/Subtraction require matrices of the same shape.
- Multiplication requires the number of columns in the first matrix to equal the number of rows in the second.
- Division requires the second matrix to be square and invertible, plus dimension compatibility for the resulting multiplication.
- Inverse requires a square, non-singular matrix.
- Row input is validated against the declared number of columns.
