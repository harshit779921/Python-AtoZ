from loguru import logger

# Sum of 1 to N -> Parametrized

def fun(sum,i,N):

    if i > N:
        logger.info(sum)
        return

    fun(sum+i, i+1, N)

fun(0,1,10)

# Sum of 1 to N -> Functional 

def fun1(n):
    if n==1:
        return 1
    return n + fun1(n-1)

logger.info(fun1(5))
