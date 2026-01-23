#All questions must use a loop for full points.
import random
def oddNumbers(n:int) ->str:
    answ = ""
    for i in range(0, n, 2):
        if i == 0:
            answ = "1"
        else:
            answ = answ + " " + str(i+1)
    return answ

def backwards(n)-> int:
    count = n
    ret = ""
    for i in range (n):
        if count == 1:
            ret = ret + "1"
        else:
            ret = ret + str(count) + " "
        count -= 1
    return(ret)

def randomRepeating():
    ran = 0
    count = 0
    while ran != 10:
        count += 1
        ran = random.randint(1, 10)
    #print(f"it took {count} tries to get a 10")
    return(count)

def randomRange(n):
    hold = []
    for i in range(0, n):
        hold.append(random.randint(0, 100))
    maxi = max(hold)
    mini = min(hold)
    return(maxi, mini)

def reverse(word:str)->str:
    hold = ""
    count = len(word)
    while count != 0:
        hold = hold + word[count-1]
        count -= 1
    return(hold)

def fizzBuzzContinuous(n):
    an = ""
    hold = ""
    for i in range (1, n+1):
        if i == 1:
            an = "1"
        else:
            if i%3 == 0 and i%5 == 0:
                hold = "fizzbuzz"
            elif i%3 == 0:
                hold = "fizz"
            elif i%5 == 0:
                hold = "buzz"
            elif i%5 != 0 and i%3 != 0:
                hold = str(i)
            an = an + " " + hold
    return(an)

def collatz(n):
    an = str(n)
    hold = n
    while n != 1:
        if n%2 == 0:
            an = an + " " + str(int((n/2)))
            n = int(n/2)
        else:
            an = an + " " + str(((n * 3) + 1))
            n = (n*3)+1
    return(an)

def fibonacci(n):
    one = 1
    two = 1
    three = 1
    hold = 0
    an = ""
    for i in range(n):
        three = one + two
        hold = two
        two = three
        one = hold
        an = an + " " + str(three)
    print(an)
    return(an)

fibonacci(5)

"""
    Print out all odd numbers from 1 to n(inclusive) in a single string seperated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
--
   modify the below function such that it prints out all the numbers from n to 1
   inclusive starting at n and counting down to 1
   example backwards(5) -> "5 4 3 2 1"
   example backwards(8) -> "8 7 6 5 4 3 2 1"
   example backwards(-2) -> ""
-- 
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
--
    Generate a random number from 1 to 100 n number of times. Then after that is
    done print out what the highest number and the lowers number was from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
--
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
--
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
--
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
--
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string sperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
   """