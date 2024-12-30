'''import threading
import time
def print_numbers():
    for i in range(1,6):
        print(i)
        time.sleep(1)
#print_numbers()
#print_numbers()

thread1=threading.Thread(target=print_numbers)

thread2=threading.Thread(target=print_numbers)
thread2.start()
thread1.start()
thread1.join()
thread2.join()'''

import threading 
import time

def num():
    for i in range(1,8):
        print(i)
        time.sleep(2)
def let():
    for char in['kanimozhi','mano','anu','vashu',"sneha","devi",'megam']:
        print(char)
        time.sleep(2)

def let1():
    for char in['a','b','c','d','e','f']:
        print(char)
        time.sleep(2)

thread1=threading.Thread(target=num)
thread3=threading.Thread(target=let1)
thread2=threading.Thread(target=let)
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
print("both threads have finished")

