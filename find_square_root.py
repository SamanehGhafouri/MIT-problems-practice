x = 12345
epsilon = 0.01
num_guesses = 0
ans = 0.0
while abs(ans ** 2 - x) >= epsilon and ans <= x:
    ans += 0.00001
    num_guesses += 1
print("number of guesses = ", num_guesses)
if abs(ans ** 2 - x) >= epsilon:
    print("Failed on square root of", x)
else:
    print(ans, "is close to square root of", x)