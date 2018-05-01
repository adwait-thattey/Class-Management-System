import os
import time
check = "1\n"
while check[-2] != "0":
    # print("hello")
    check = os.popen('python3 genetic_observer.py', 'r').read()

print_string = check.split("\n")
# print(print_string)
i=0
while i < len(print_string) :
    if print_string[i]=="...." :
        break
    print(print_string[i])
    
    if i%3==1 :
        input()

    i+=1    

i+=1
for j in range(4):
    print(print_string[i])
    i+=1

time.sleep(1.5)

for j in range(2):
    print(print_string[i])
    i += 1

time.sleep(1)    
while i < len(print_string) :
    print(print_string[i])
    i+=1
    # check = int(check.strip('\n'))
