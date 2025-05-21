
def get_matrix(n,m):
    for i in range(n):
        row = []
        for j in range(m):
            val = int(input(f"Element [{i+1}][{j+1}]: "))
            row.append(val)
        a.append(row)
    return a
def print_matrix(a):
    print("\nThe entered matrix is:")
    for row in a:
        print(' '.join(map(str, row)))    

def sum_diagonal(a):
    if(n != m):
        print("Matrix is not square, cannot calculate diagonal sum.")
        return None
    else:
        diagonal_sum = 0
    for i in range(n):
        diagonal_sum += a[i][n-1-i]
        diagonal_sum += a[i][i]
        if n%2==1:
            diagonal_sum -= a[n//2][n//2]
    return diagonal_sum
       
def main():
    get_matrix(n,m)
    print_matrix(a)
    diagonal_sum = sum_diagonal(a)
    print(f"The sum of the diagonal elements is: {diagonal_sum}")

if __name__ == "__main__":
    n=int(input("Enter the number of rows: "))
    m=int(input("Enter the number of columns: "))
    a = []
    main()    