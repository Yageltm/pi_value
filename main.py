import random
import threading
import math
import keyboard


def find_pi(trials):
    c = 0
    for i in range(trials):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            c += 1
        if (i+1) % 1000000 == 0:
            calculated_pi = 4 * c / (i+1)
            print("Real value of Pi:", math.pi)
            print("Calculated value of Pi:", calculated_pi)
            print("Number of attempts:", i+1)
            print()



def run_pi_estimation(num_batches):
    trials = num_batches * 1000000
    t = threading.Thread(target=find_pi, args=(trials,))
    t.start()
    t.join()


def phase1():
    num_batches = int(input("Enter the number of batches: "))
    run_pi_estimation(num_batches)

phase1()