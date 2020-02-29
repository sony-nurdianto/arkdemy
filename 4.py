import random

class Random :
    def array (self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        third = random.randint(1,6)
        four = random.randint(1,6)
        five = random.randint(1,6)
        print (first,second,third,four,five)
        list = [first,second,third,four,five]
        print (list)
        return first + second + third + four + five

data = Random()
print (data.array())




























