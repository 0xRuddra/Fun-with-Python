import re
pattern=r"@gmail.com$"
matches=[]
with open("spy.txt","rt") as file:
    for line in file:
        pattern = re.compile(pattern)
        x=pattern.finditer(line)
    for z in matches:
        print(z)
    file.close()