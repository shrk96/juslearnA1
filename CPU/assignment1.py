# Assignments (Use any programming language)
# 1. Write a program which make use of ~100% CPU (single core).
# 2. Write a program which make use of ~50% CPU (single core).
# 3. Write a program which make use of ~100% CPU (all cores).
# 3. Write a program which make use of ~50% CPU (all cores).

import multiprocessing
import time
import os

def loader():
    while True:
        pass

def restfulLoader(): #phasing this out. I feel sleep isn't directly a good method of ensuring cpu util
    while True:
        time.sleep(0.001)
        pass

def adaptiveLoader(target_load=0.5, interval=1.0):
    work_time = target_load * interval
    idle_time = (1 - target_load) * interval
    
    while True:
        start = time.time()
        while time.time() - start < work_time:
            pass
        time.sleep(idle_time)

def mc100(a):
    processes = []
    for _ in range(a):
        p = multiprocessing.Process(target=loader)
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

def mc50(a):
    processes = []
    for _ in range(a):
        p = multiprocessing.Process(target=restfulLoader)
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

def ac100():
    coreCount = os.cpu_count()
    mc100(coreCount)

def ac50():
    coreCount = os.cpu_count()
    mc50(coreCount)

if __name__ == "__main__":
    choice = input("Choose mode: 1. 100% single core, 2. 50% single core, 3. 100% selected core count, 4. 50% selected core count, 5. 100% all cores, 6. 50% all cores: ")
    
    if choice == "1":
        loader()
    elif choice == "2":
        adaptiveLoader()
    elif choice in ["3", "4"]:
        coreCount = os.cpu_count()
        coreSelected = int(input(f"Enter number of cores (1 to {coreCount}): "))
        if coreSelected < 1 or coreSelected > coreCount:
            print("Invalid core count.")
        elif choice == "3":
            mc100(coreSelected)
        elif choice == "4":
            mc50(coreSelected)
    elif choice == "5":
        ac100()
    elif choice == "6":
        ac50()
    else:
        print("Invalid choice.")

# Wanted to make Prime 95 lol
# Also wanted to use cpu_affinity. Maybe sometime later. 