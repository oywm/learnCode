from threading import Thread
import time


def test():
    print('asdasd')
    time.sleep(1)


for i in range(5):
    t = Thread(target=test)
    t.start()
