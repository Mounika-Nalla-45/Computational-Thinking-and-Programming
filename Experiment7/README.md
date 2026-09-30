Practical 7: Producer-Consumer Application
Question

Develop a Producer-Consumer application using threading, multiprocessing, and synchronization primitives.

Aim

To develop a simple Producer-Consumer application using Python threading, multiprocessing, Lock, and Semaphore.

Algorithm
Create a shared queue.
Producer adds items to the queue.
Consumer removes items from the queue.
Use Lock to protect the shared queue.
Use Semaphore to control queue access.
Use threading for concurrent execution.
Use multiprocessing for separate processes.
Display the produced and consumed items.
Program
import threading
import multiprocessing
import queue
import time

q = queue.Queue(maxsize=5)

lock = threading.Lock()
semaphore = threading.Semaphore(5)

def producer():
    for i in range(1, 6):
        semaphore.acquire()

        with lock:
            q.put(i)
            print("Produced:", i)

        time.sleep(1)

def consumer():
    for i in range(1, 6):
        with lock:
            item = q.get()
            print("Consumed:", item)

        semaphore.release()
        time.sleep(1)

# Threading
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()

print("Threading completed")


# Multiprocessing
def process_task(name):
    print(name, "process started")
    time.sleep(1)
    print(name, "process completed")

p1 = multiprocessing.Process(
    target=process_task,
    args=("Producer",)
)

p2 = multiprocessing.Process(
    target=process_task,
    args=("Consumer",)
)

p1.start()
p2.start()

p1.join()
p2.join()

print("Multiprocessing completed")
Input
Number of items = 5
Queue size = 5
Output
Produced: 1
Consumed: 1
Produced: 2
Consumed: 2
Produced: 3
Consumed: 3
Produced: 4
Consumed: 4
Produced: 5
Consumed: 5
Threading completed

Producer process started
Consumer process started
Producer process completed
Consumer process completed
Multiprocessing completed
Inference
Producer adds data to the queue.
Consumer removes data from the queue.
Lock protects shared data.
Semaphore controls access to the queue.
Analysis
Threading runs tasks concurrently.
Multiprocessing runs tasks in separate processes.
Queue stores the data.
Synchronization prevents conflicts.
Result

The Producer-Consumer application was successfully implemented using threading, multiprocessing, Lock, and Semaphore.
