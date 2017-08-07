import threading
import queue
import urllib.request
from datetime import datetime
# from html import escape


def get_url(q:queue.Queue, url:str):

    t1 = datetime.now()
    item = str(urllib.request.urlopen(url).read(100000))
    # item = escape(item)
    t2 = datetime.now()

    q.put(f"{url} loaded in {str(t2-t1)}:" + item)


def main():
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
        t.start()

    for t in threads:
        t.join()

    while not q.empty():
        print(q.get())


if __name__ == '__main__':
    main()