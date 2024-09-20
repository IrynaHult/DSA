
from BinarySearchTestDataFactory import *


test_data_factory = BinarySearchTestDataFactory()

test_dataset_1k = test_data_factory.generate_sorted_list_with_duplicates(1000, 50)
test_dataset_100k = test_data_factory.generate_sorted_list_with_duplicates(100000, 500)
test_dataset_1kk = test_data_factory.generate_sorted_list_with_duplicates(1000000, 5000)
test_dataset_10kk = test_data_factory.generate_sorted_list_with_duplicates(10000000, 50000)

def binarySearch(dataset, target_val):
    search_status = {}
    search_status["alghorithm"] = "binary search"
    search_status["size"] = len(dataset)
    search_status["status"] = "not found"
    search_status["operations"] = 0
    
    if len(dataset) == 0:
        return search_status
    
    iterations = 0
    left = 0
    right = len(dataset) - 1
    


    while left <= right:
        iterations = iterations + 1
        mid = (left + right) // 2
        search_status["operations"] = iterations
        if dataset[mid] == target_val:
            search_status["status"] = "found"
            search_status["index"] = mid
            
            return search_status
        
        if dataset[mid] < target_val:
            left = mid + 1
        else:
            right = mid - 1

    return search_status



def linear_search(dataset, target_vall):
    operations = 0
    search_status = {}
    search_status["alghorithm"] = "linear search"
    search_status["size"] = len(dataset)
    search_status["status"] = "not found"
    search_status["operations"] = operations
    
    for element in dataset:
        operations+=1
        if element == target_vall:
            search_status["status"] = "found" 
            search_status["operations"] = operations
            return search_status
    return search_status
            
            
def print_search_result(search_status):
    print("=" * 10)
    if search_status["status"] == "found":
        print(f"Alghoritm: {search_status['alghorithm']}\nDataset size: {search_status['size']} \nTarget found in {search_status['operations']} operation")
    else:
        print(f"Dataset size: {search_status['size']} \nSearch status: {search_status['status']} in {search_status['operations']} operations")
    print("=" * 10)
    print("\n")





myTarget = 823

result = linear_search(test_dataset_1k, myTarget)
print_search_result(result)

result = binarySearch(test_dataset_1k, myTarget)
print_search_result(result)




myTarget = 99499

result = linear_search(test_dataset_100k, myTarget)
print_search_result(result)

result = binarySearch(test_dataset_100k, myTarget)
print_search_result(result)

myTarget = 130580
result = linear_search(test_dataset_1kk, myTarget)
print_search_result(result)
result = binarySearch(test_dataset_1kk, myTarget)
print_search_result(result)

myTarget = 25695478
result = linear_search(test_dataset_10kk, myTarget)
print_search_result(result)
result = binarySearch(test_dataset_10kk, myTarget)
print_search_result(result)


myTarget = -1
result = binarySearch(test_dataset_10kk, myTarget)
print_search_result(result)


empty_list = []
myTarget = -1
result = binarySearch(empty_list, myTarget)
print_search_result(result)




