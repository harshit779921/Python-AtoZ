from loguru import logger

k = 16
arr = [9, 7, 16, 16, 4]

for i in range(len(arr)):
    if arr[i] == k:
        logger.info(i+1)
        break
logger.info(-1)