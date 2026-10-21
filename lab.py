# This program asks for your name and calculates your average and highest test scores
# It contains several errors (syntax, runtime, and logic) for you to find and fix

print("Welcome to the Debugging Lab!") # completed quotation marks -- syntax error

name = input("Enter your name:")
print(f"Hello {name} ! Let's calculate your test scores.") # changed format to f-string formatting

scores = [85, 90, 78, 88, 92] # removed quotation marks around 88

total = 0
for score in scores: # added colon -- syntax error
    total = total + score

average = total / len(scores)
print(f"Your average score is: {average}") # changed format to f-string formatting

highest = 0
for s in scores:
    if s > highest:
        highest = s

print(f"Your highest score was: {highest}") # changed format to f-string formatting