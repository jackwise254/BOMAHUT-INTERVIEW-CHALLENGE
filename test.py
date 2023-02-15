import time
from .algorithm import MinMaxAlgorithm

# Test with a large matrix
rows = 1000
columns = 1000
matrix = [[j for j in range(columns)] for i in range(rows)]
start_time = time.time()
result = MinMaxAlgorithm(matrix)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken to execute function: {elapsed_time} seconds")