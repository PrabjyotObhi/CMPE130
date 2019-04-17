
import random

f = open("lastnames.txt", "r")
StreetType = ["Road", "Drive", "Street", "Court", "Lane", "Way"]
StreetNames = []
Address = {" "}
j = 0
for x in f:
    StreetNames.append(x)


for j in range(0,1010):
    indexForType = random.randint(0, 5)
    index = random.randint(0, 45905)
    numeral = random.randint(10000, 99999)
    numeral = str(numeral)

    index = random.randint(1,101)
    tempAddy = numeral + ' ' + StreetNames[index].strip('\n') + ' '+ StreetType[indexForType]

    Address.add(tempAddy)


print(Address)
