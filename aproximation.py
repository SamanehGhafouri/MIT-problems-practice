# x = 12345
# epsilon = 0.01
# num_guesses = 0
# ans = 0.0
# while abs(ans ** 2 - x) >= epsilon and ans <= x:
#     ans += 0.00001
#     num_guesses += 1
# print('numGuesses = ', num_guesses)
# if abs(ans ** 2 - x) >= epsilon:
#     print("Failed on square root at ", x)
# else:
#     print(ans, 'is close to square root of ', x)

# ---------------------------------------------------------- #
# Make this faster but not good return Failed

# x = 12345
# epsilon = 0.01
# num_guesses = 0
# ans = 0.0
# while abs(ans ** 2 - x) >= epsilon and ans <= x:
#     ans += 1
#     num_guesses += 1
# print('numGuesses = ', num_guesses)
# if abs(ans ** 2 - x) >= epsilon:
#     print("Failed on square root at ", x)
# else:
#     print(ans, 'is close to square root of ', x)

# ---------------------------------------------------------------- #
# Make it faster properly using Bisection Search which make the space in half and
# search for the answer in half of the space every time

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
print(ans, ' is close to square root of ', x)

