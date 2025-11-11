from loguru import logger

# Head Recursion
count = 0   # ✅ global variable

def head():
    global count   # ✅ tell Python we want to modify the global variable

    if count == 4:
        return

    logger.info("Harshit")
    count += 1
    head()

head()

# Tail Recursion

var = 0

def tail():
    global var

    if var == 4:
        return
        
    var += 1 
    tail()
    logger.info("Pandey")

tail()