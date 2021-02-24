x = 12345
epsilon = 0.01
num_guesses = 0
low = 0.0
high = x
ans = (high + low) / 2.0
while abs(ans ** 2 - x) >= epsilon and ans <= x:
    num_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print(ans, "is close to square root of ", x)