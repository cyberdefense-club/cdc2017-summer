from multiprocessing.dummy import Pool
import queue
import urllib.request
from datetime import datetime, timedelta
import itertools


def get_url(q:queue.Queue, url:str):

    t1 = datetime.now()
    item = str(urllib.request.urlopen(url).read(100000))
    t2 = datetime.now()

    q.put([f"{url} loaded in {str(t2-t1)} : " + item, t2-t1])


def main():

    sites = [
        "http://www.godaddy.com",
        "http://www.repeatableread.com",
        "http://www.google.com",
        "http://www.yahoo.com",
        "http://www.msn.com",
        "http://www.cnn.com",
        "http://www.msnbc.com",
        "http://www.snopes.com"
    ]

    q = queue.Queue()
    pool = Pool(len(sites))
    results = pool.starmap(get_url, zip(itertools.repeat(q), sites))

    items = []
    while not q.empty():
        items.append(q.get())

    sum_of_process_times = timedelta(seconds=0)
    for i in items:
        print(i[0][:200])
        sum_of_process_times += i[1]

    print(f"\nThe processes took a total of {sum_of_process_times} to execute.")


if __name__ == '__main__':
    t1 = datetime.now()
    main()
    t2 = datetime.now()

    print(f"The main() function took {str(t2-t1)} to execute.")