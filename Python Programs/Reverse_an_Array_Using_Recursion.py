from loguru import logger

def reverse(nums, left, right):
    if left >= right:
        return 
    arr[left],arr[right] = arr[right], arr[left]
    reverse(arr, left+1, right-1)

def revArr(nums, left, right):
    reverse(nums,left, right)
    return nums 

arr = [1, 2, 3, 4, 5, 7, 9, 8]
result = revArr(arr, 0, len(arr) - 1)
logger.info(result)