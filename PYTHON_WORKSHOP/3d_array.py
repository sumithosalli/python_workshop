# User-defined 3D array in Python

def create_3d_array(x, y, z):
    """Creates a 3D array of dimensions x * y * z filled with user input."""
    array = []
    for i in range(x):
        layer = []
        for j in range(y):
            row = []
            for k in range(z):
                value = input(f"Enter value for element [{i}][{j}][{k}]: ")
                row.append(value)
            layer.append(row)
        array.append(layer)
    return array

def print_3d_array(array):
    """Prints the 3D array in a formatted way."""
    for i, layer in enumerate(array):
        print(f"Layer {i}:")
        for row in layer:
            print(' '.join(map(str, row)))
        print()  # Newline for better readability
# Example usage:
if __name__ == "__main__":
    x = int(input("Enter number of layers (x): "))
    y = int(input("Enter number of rows (y): "))
    z = int(input("Enter number of columns (z): "))
    arr = create_3d_array(x, y, z)
    print("3D Array:")
    print(print_3d_array(arr))