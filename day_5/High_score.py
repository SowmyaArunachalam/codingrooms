'''
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91
e.g. When you hit run, this is what should happen:



Hint
Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?
Test Your Code
Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.

Solution
https://repl.it/@appbrewery/day-5-2-solution
'''
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

g=0
for i in student_scores:
  if i>g:
    g=i
print("The highest score in the class is:",g)