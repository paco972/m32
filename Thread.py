#!/usr/bin/env python3
import threading
from time import sleep

def fonction(n):
    for i in range(5):
        print(f"Thread {n}: on est dans la boucle {i}")
        sleep(0.5)

# création de thread
t1 = threading.Thread(target=fonction, args=(1,))
t2 = threading.Thread(target=fonction, args=(2,))

# démarrer le thread t1
t1.start()
# démarrer le thread t2
t2.start()

# attendre que t1 soit exécuté
t1.join()
# attendre que t2 soit exécuté
t2.join()

# les deux thread sont exécutés
print("C'est fini!")