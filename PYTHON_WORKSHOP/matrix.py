# Matrix input by user and printing the matrix

def get_matrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            val = int(input(f"Element [{i+1}][{j+1}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    print("\nThe entered matrix is:")
    for row in matrix:
        print(' '.join(map(str, row)))    

       
def main():
    try:
        # Get matrix dimensions
        n = int(input("Enter the number of rows: "))
        m = int(input("Enter the number of columns: "))
        # Get matrix input
        matrix = get_matrix(n, m)
        # Print the matrix
        print_matrix(matrix)    
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()