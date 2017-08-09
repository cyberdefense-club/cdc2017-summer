import threading
import queue
import urllib.request
from datetime import datetime, timedelta


def get_url(q:queue.Queue, url:str):

    t1 = datetime.now()
    item = str(urllib.request.urlopen(url).read(100000))
    t2 = datetime.now()

    q.put([f"{url} loaded in {str(t2-t1)}:" + item, t2-t1])


def main():
    tstart = datetime.now()
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

    threads = []

    for u in sites:
        t = threading.Thread(target=get_url, args=(q, u), daemon=True)
        threads.append(t)

    # start and join in separate loops in order to get as close to possible
    # to starting all threads concurrently:
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    items = []
    while not q.empty():
        items.append(q.get())

    sum_of_thread_times = timedelta(seconds=0)
    for i in items:
        print(i[0][:200])
        sum_of_thread_times += i[1]

    print(f"\nThe processes took a total of {sum_of_thread_times} to execute.")

    tstop = datetime.now()
    print(f"The main() function took {str(tstop-tstart)} to execute.")


if __name__ == '__main__':
    main()
