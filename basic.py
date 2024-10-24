import time
start1 = time.time()
for i in range(1,100):
    print(i)
start2 = time.time()
j =1
while j < 100:
    print(j)
    j = j + 1

print(time.time() - start1)
print(time.time() - start2)