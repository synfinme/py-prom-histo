#!/usr/bin/env python3

from prometheus_client import start_http_server, Histogram
import random
import sys
import time

import dataset

h = Histogram('py_prometheus_histo', 'Description of py_prometheus_histo')

def update_stats(x):
    # Populates 'h' metric with a bunch of values
    #for i in range(500):
    #    r = 2.0 * random.random() - 1.0
    #    y = 4.0 * (r * r * r + 1.0)
    #    h.observe(y)
    for v in dataset.data:
        h.observe(v)

    # Other cosmetic stuff
    sys.stdout.write('.')
    sys.stdout.flush()
    if (x % 60) == 59:
        sys.stdout.write('\n')
        sys.stdout.flush()
    time.sleep(30)


def main():
    start_http_server(9100)
    x = 0
    while True:
        update_stats(x)
        x = x + 1
        #print('x=', x)


if __name__ == '__main__':
    main()
