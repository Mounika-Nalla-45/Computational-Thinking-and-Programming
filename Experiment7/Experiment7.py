import threading
import multiprocessing
import queue
import time

q = queue.Queue(maxsize=5)

lock = threading.Lock()
semaphore = threading.Semaphore(5)


# Producer
def producer():
    for i in range(1, 6):
        semaphore.acquire()

        with lock:
            q.put(i)
            print("Produced:", i)

        time.sleep(1)


# Consumer
def consumer():
    for i in range(1, 6):
        with lock:
            item = q.get()
            print("Consumed:", item)

        semaphore.release()
        time.sleep(1)


# Multiprocessing function
def process_task(name):
    print(name, "process started")
    time.sleep(1)
    print(name, "process completed")


# Main program
if __name__ == "__main__":

    # Threading
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print("Threading completed")

    # Multiprocessing
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