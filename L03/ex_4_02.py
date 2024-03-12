import time
def do_something():
    print('Hello, world!')
t1 = time.perf_counter()
do_something()
t2 = time.perf_counter()
print(f'do_something()用时: {t2 - t1:0.6f}s')