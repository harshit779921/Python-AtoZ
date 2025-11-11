from loguru import logger

# Print 1 to N using Recursion Using Head 
def fun(i,N):
    if i>N:
        return
    logger.info(i)
    fun(i+1,N)

fun(1,4)

# Using Tail Recursion

def fun1(i, N):
    if i>N:
        return 
    fun1(i+1,N)
    logger.info(i)
fun1(1,5)

# Second Part
def fun2(N):
    if N == 0:
        return 
    fun2(N-1)
    logger.info(N)
fun2(5)