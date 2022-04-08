import multiprocessing
from random import randint
def wait(seconds):
    from datetime import datetime
    from time import sleep
    print(f'wait {seconds} seconds')
    sleep(seconds)
    print('current time: ', datetime.now().time())
    
if __name__ == "__main__":
    for i in range(3):
        from random import randint
        seconds=randint(1,5)
        p=multiprocessing.Process(target=wait, args=(seconds,))
        p.start()