## Basic - Print all integers from 0 to 150.

count = 0
while count <= 150:
    print(count)
    count += 1

## Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for x in range(0, 1001, 5):
    print(x)

## Counting, the Dojo Way - Print integers 1 to 100. 
## If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for x in range (1, 101):
    print(x)
    if x % 5 == 0:
        print("Coding")
    if x % 10 == 0:
        print("Dojo")

## Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for x in range(1, 500001, 2):
    sum += x
print(sum)

## Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

y = 2018 
while y > 0:
    print(y)
    y = y - 4

## Flexible Counter - Set three variables: lowNum, highNum, mult. 
## Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
## For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6.

lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum, highNum):
    if x % mult == 0:
        print(x)