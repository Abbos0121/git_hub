import time


def uxlating():
    start_time = time.time()
    for i in range(10):
        time.sleep(1)
        print("Uxlating...")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Boshlanish va tugash vaqtlari orasidagi farq:", elapsed_time, "soniya")


uxlating()
