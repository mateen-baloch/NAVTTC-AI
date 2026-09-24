#Program for Range of Unknown Data Types
import sys

my_dict = {}
print(sys.getsizeof(my_dict))  # 64 bytes

my_dict = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
print(sys.getsizeof(my_dict))

