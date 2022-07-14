import threading, time
 
def sum():
    total = 0
    low = 1
    high = 2
    for i in range(low, high):
        total += i
    time.sleep(60)
    print("Subthread", total)
 
t = threading.Thread(target=sum)
t.start()
 
print("Main Thread")
time.sleep(3)

t = threading.Thread(target=sum)
t.start()

print("Main Thread")