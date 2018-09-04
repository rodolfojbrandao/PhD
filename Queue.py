import multiprocessing as mp


def foo(q):
    for i in range(0, 1000000):
        q.put('hello')


if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()


