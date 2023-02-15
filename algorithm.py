import time
import sys

def testFunction():
    rows = 1000
    columns = 1000
    matrix = [[j for j in range(columns)] for i in range(rows)]
    start_time = time.time()
    result = MinMaxAlgorithm(matrix)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to execute function: {elapsed_time} seconds")
    return result

def measure(func):
    """A function to meassure time and space complexity"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.3f}s")

        space = sys.getsizeof(result)
        print(f"Space complexity: {space} bytes")

        return result
    return wrapper


def InputFunction():
    # get the size of the matrix from user
    rows = int(input("Input number of rows: "))
    columns = int(input("Input number of columns: "))
    # Initialize an empty matrix
    matrix = []
    # get input values for each element
    for i in range(rows):
        try:
            row = []
            for column in range(columns):
                value = int(input(f"Enter the value at: ({i}, {column}): "))
                row.append(value)
            matrix.append(row)
        except Exception as e:
            print(e)
    
    solution = MinMaxAlgorithm(matrix)

    return solution


@measure
def MinMaxAlgorithm(matrix):
    """A function to implement an algorithm that given an M X N  matrix return 
    all numbers that are the maximum value inits row but the minimum in its column"""
    # Find the maximum value in each row that is also the minimum in its column
    result = []
    print(f'''\nInput matrix: {matrix}''')
    for i in range(len(matrix)):
        # print(f'''matrix:{matrix}''')
        for j in range(len(matrix[0])):
            is_max_in_row = True
            is_min_in_col = True
            for k in range(len(matrix)):
                if matrix[i][j] > matrix[k][j]:
                    is_max_in_row = False
                    break
            for k in range(len(matrix[0])):
                if matrix[i][j] < matrix[i][k]:
                    is_min_in_col = False
                    break
            if is_max_in_row and is_min_in_col:
                result.append(matrix[i][j])

    # Return the result
    return result


output = InputFunction()
# test = testFunction()
