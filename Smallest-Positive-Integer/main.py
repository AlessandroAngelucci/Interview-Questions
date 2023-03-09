import numpy as np


def main(array_a):
    print(f"Input array: {array_a}")  # Print input array
    array_a = np.append(array_a, 0)  # Add 0 to array to indicate start of positive numbers
    array_a.sort()  # Sort array in ascending order
    array_a = np.unique(array_a)  # Remove duplicate values from array
    index_zero = np.array(array_a).tolist().index(0)  # Store index of 0 in array
    array_a = array_a[index_zero + 1:]  # Slice array from first element after 0 until end of array
    if len(array_a) == 0:  # If modified array is empty
        return 1  # Return 1
    else:  # If modified array is not empty
        smallest_positive_int = 1  # Set smallest positive integer to 1
        for i in array_a:  # For each element in modified array
            if smallest_positive_int >= i:  # If smallest positive integer is larger than or equal to element
                smallest_positive_int += 1  # Increment smallest positive integer
            else:  # If smallest positive integer is less than element
                return smallest_positive_int  # Return smallest positive integer


if __name__ == '__main__':
    print(f"Smallest positive integer not contained in array: {main(np.array([1, 4, 3, 7]))}")
