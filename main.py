#Read from file where each line is [Element] [Name]
file = open("elements.txt")
file_content = file.readlines()
abbriv = dict()
for line in file_content:
    a = line.split()[0]
    e = line.split()[1]
    abbriv[a] = e

#Input Setup
text = input("Enter text: ").strip(" ")
N = len(text)
output = []
possible = True

#Check if possible and save output
i=0
while i<N:
    if i<N-1 and text[i:i+2].capitalize() in abbriv.keys():
        output.append(text[i:i+2].capitalize())
        i+=2
    elif text[i].capitalize() in abbriv.keys():
        output.append(text[i].capitalize())
        i+=1
    else:
        possible = False
        break
    
#Build output
if possible:
    print("Are you made of ", end="")
    for e in output:
        print(abbriv[e], end=" ")
    print("? Because you are ")
    for e in output:
        print(e,end="")
else:
    print("Sorry, no can do")