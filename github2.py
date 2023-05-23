import time
import threading


def uxlating():
    start_time = time.time()
    for i in range(10):
        time.sleep(1)  # 1
        print("Uxlating...")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Boshlanish va tugash vaqtlari orasidagi farq:", elapsed_time, "soniya")


def boshqa_ish():
    for i in range(5):
        time.sleep(2)
        print("Boshqa ish")


thread1 = threading.Thread(target=uxlating)
thread2 = threading.Thread(target=boshqa_ish)


thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("Barcha threadlar tugadi")
