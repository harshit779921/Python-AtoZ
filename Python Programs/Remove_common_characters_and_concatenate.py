from loguru import logger

s1 = input("Enter s1:")
s2 = input("Enter s2:")
word = ''
        
for i in s1:
    if i not in s2:
        word += i
                
for j in s2:
    if j not in s1:
        word += j
                
if len(word)>=1:
     logger.info(word)
else:
    logger.info(-1)