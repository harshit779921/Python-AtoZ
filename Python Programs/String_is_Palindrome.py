from loguru import logger

def palin(s, left, right):
    if left >= right:
        return True
    elif s[left] != s[right]:
        return False
    return palin(s, left+1, right-1)

s = input("Enter the character:")

s = s.lower()

logger.info(palin(s, 0, len(s)-1))