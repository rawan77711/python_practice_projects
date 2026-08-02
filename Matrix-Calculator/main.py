"""
Matrix Calculator using NumPy
Supports addition, subtraction, multiplication, division,
transpose, inverse, and determinant.
"""

import numpy as np

def get_matrix():
    """Get a matrix from user input"""
    rows=int(input("Number of rows: "))
    columns=int(input("Number of columns: "))
    matrix=[]
    for _ in range(rows):
        row=input("Enter row: ").split()
        row=[float(x) for x in row]
        if len(row) != columns:
            print("Wrong number of values. Try again!")
            return get_matrix()
        matrix.append(row)
    return np.array(matrix)

#--------------Operations-------------------#

def addition(matrix1,matrix2):
    """Add two matrices"""
    if matrix1.shape != matrix2.shape:
        print("Both matrices must have the same shape!!")
        return None
    return matrix1+matrix2

def subtraction(matrix1,matrix2):
    """Subtract two matrices"""
    if matrix1.shape != matrix2.shape:
        print("Both matrices must have the same shape!!")
        return None
    return matrix1-matrix2

def multiplication(matrix1,matrix2):
    """Multiply two matrices"""
    if matrix1.shape[1]==matrix2.shape[0]:
        matrix3=np.matmul(matrix1,matrix2)
        return matrix3
    else:
        print("The Columns of The First Matrix must Equal The Rows of The Second Matrix!")
        return None

def division(matrix1,matrix2):
    """Divide matrix1 by matrix2 (matrix1 * inverse(matrix2))"""
    if matrix2.shape[0]!=matrix2.shape[1]:
        print("The Second matrix Must be Square!")
        return None
    try:
        inv=inverse(matrix2)
    except np.linalg.LinAlgError:
        print("The second matrix is not invertible!")
        return None
    if matrix1.shape[1]==inv.shape[0]:
        return multiplication(matrix1, inv)
    else:
        print("Matrix dimensions not compatible for division!")
        return None

def transpose(matrix):
    """Return transpose of a matrix"""
    return matrix.T

def inverse(matrix):
    """Return inverse of a matrix"""
    return np.linalg.inv(matrix)

def determinant(matrix):
    """Return determinant of a matrix"""
    return np.linalg.det(matrix)


#-------------------Menu----------------------#

def main():
    """Main menu for matrix calculator"""
    print('''\t\"A\" for Addition
        \"S\" for Subtraction 
        \"M\" for Multiplication
        \"V\" for Devision
        \"T\" for Transpose
        \"I\" for Inverse
        \"D\" for Determinant''')

    option=input("Please, Enter Your Option: ").strip().lower()
    result=None

    if option in ["a", "s", "m", "v"]:
        print("Enter the first matrix: ")
        matrix1=get_matrix()
        print("Enter the second matrix: ")
        matrix2=get_matrix()
        if option=="a":
            result=addition(matrix1, matrix2)
        elif option=="s":
            result=subtraction(matrix1, matrix2)
        elif option=="m":
            result=multiplication(matrix1, matrix2)
        else:
            result=division(matrix1, matrix2)

    elif option in ["t", "i", "d"]:
        print("Enter the matrix: ")
        matrix=get_matrix()
        if option=="t":
            result=transpose(matrix)
        elif option=="i":
            try:
                result=inverse(matrix)
            except np.linalg.LinAlgError:
                print("Matrix is not invertible!")
        else:
            result=determinant(matrix)

    else:
        print("Invalid Input! Try Again!")

    if result is not None:
        print(f"The Result is: \n{result}")

if __name__ == "__main__":
    main()
