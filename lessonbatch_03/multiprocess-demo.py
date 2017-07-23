from multiprocessing.dummy import Pool
import urllib.request
import queue
import itertools
from datetime import datetime


def get_url(q:queue.Queue, url:str):

    t1 = datetime.now()
    item = str(urllib.request.urlopen(url).read(100000))
    # item = escape(item)
    t2 = datetime.now()

    q.put(f"{url} loaded in {str(t2-t1)}:" + item)


def main():
    pool = Pool(4)
    q = queue.Queue()

    sites = [
        "http://www.godaddy.com",
        "http://www.repeatableread.com",
        "http://www.google.com",
        "http://www.yahoo.com",
        "http://www.msn.com",
        "http://www.cnn.com",
        "http://www.msnbc.com"
    ]

    results = pool.starmap(get_url, zip(itertools.repeat(q), sites))
    print(results)

    while not q.empty():
        print(q.get())


if __name__ == '__main__':
    main()
