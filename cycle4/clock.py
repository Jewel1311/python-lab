class Time:
    def __init__(self):
        self.__hour = int(input("Enter hour : "))
        self.__minute = int(input("Enter minute : "))
        self.__second = int(input("Enter second :"))

    def __add__(self, other):
        seconds = (self.__second + other.__second)%60
        minutes =  (self.__minute + other.__minute)%60 +(self.__second + other.__second)//60
        hours =  (self.__hour + other.__hour)%60 +(self.__minute + other.__minute)//60

        print("\nAfter addition\n***************")
        print(hours,":",minutes,":",seconds)

t1 = Time()
t2 = Time()

t1 + t2