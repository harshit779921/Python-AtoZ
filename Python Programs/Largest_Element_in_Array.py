from loguru import logger

arr = [1, 8, 7, 56, 90]
ans = float('-inf')
for i in range(len(arr)):
    if arr[i] > ans:
        ans = arr[i]
                
    else : 
        continue
        
logger.info(ans)