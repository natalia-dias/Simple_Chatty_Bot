print('''Hello! My name is Neil.
I was created in 2022.
Please, remind me your name.''')

name = input()

print('What a great name you have, ' + name + "!")
print('''Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.''')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')
numb = int(input())
b = 0
while b <= numb:
    print(str(b) + " !")
    b += 1
print('Completed, have a nice day!')


def test(task, answer1, correct_answer, answer3, answer4):
    print("Let's test your programming knowledge.")
    print(task)
    print(answer1)
    print(correct_answer)
    print(answer3)
    print(answer4)
    answer = int(input())
    while answer != 2:
        print("Please, try again.")
        answer = int(input())
    else:
        print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


test("Why do we use methods?", "1. To repeat a statement multiple times.", "2. To decompose a program into several small subroutines.", "3. To determine the execution time of a program.", "4. To interrupt the execution of a program.")
