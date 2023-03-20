import threading
import time


def aa():
    i = 0
    while i<5:
        i = i + 1
        time.sleep(0.5)
        print('A:', i)


def bb():
    i = 0
    while i<50:
        i = i + 10
        time.sleep(0.5)
        print('B:', i)


a = threading.Thread(target=aa)  # 建立新的執行緒
b = threading.Thread(target=bb)  # 建立新的執行緒

a.start()  # 啟用執行緒
b.start()  # 啟用執行緒
