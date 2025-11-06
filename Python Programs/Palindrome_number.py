temp = 501020105
ans = 0
n = temp
while n > 0:
    last_digit = n % 10
    ans = ans * 10 + last_digit
    n //= 10
print(temp, ans)
print(temp == ans)
