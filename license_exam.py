"""
Author: Cristian Pintor
This program stores the correct answers in a list and then asks
the user to enter the answers for the 20 questions. The program
then outputs a fail or pass result based on the entries.
"""

ans = ["B", "D", "A", "A", "C", "A", "B", "A", "C", "D", "B", "C", "D", "A", "D", "C", "C", "B", "D", "A"]

# user input stored in this list
#store = []

# input will be placed in response as string and then set to items where it'll be split
response = input("Enter the 20 answers to the following questions: ")
items = response.split()

#store = [eval("x") for x in items]

store = list(items)
"""
print("Answers you entered: ")
for i in range(0, len(store)):
    print(store[i])

print("Your results: ")
#print(set(ans) & set(store))

ans.sort()
store.sort()

if ans == store:
    print("The lists are identical")
else:
    print("They fail")
"""
compare_lists = [1 if i == j else 0 for i, j in zip(ans, store)]

total = sum(compare_lists)
incorrect = 20 - total

if total >= 15:
    print("Exam passed!")
else:
    print("Exam failed.")

print("You got %d correct" % (total))
print("You got %d incorrect" % incorrect)
print()
print("Below is a list of the questions you got credit for: ")
print(compare_lists)
