"""
多进程与单进程之间的差别
仅模拟,非真实
"""
from multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep

def download_task(filename):
    print('开始下载%s...'%filename)
    time_to_download=randint(5,10)
    sleep(time_to_download)
    print('%s下载完成!耗费了%d秒'%(filename,time_to_download))

def download_simple():
    start = time()
    download_task('python从入门到入土.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗时%.2f秒' % (end - start))

def download_multi():
    start=time()
    p1=Process(target=download_task,args=('python从入门到入土.pdf',))
    p1.start()
    p2=Process(target=download_task,args=('Peking Hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end=time()
    print('总共耗费了%.2f秒'%(end-start))



def main():
    download_multi()


if __name__ == '__main__':
    main()
