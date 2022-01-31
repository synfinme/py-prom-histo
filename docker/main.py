#!/usr/bin/env python3

from prometheus_client import start_http_server, Histogram
import random
import sys
import time

try:
    from dataset import data
except ImportError:
    from default_dataset import data


h = Histogram('py_prometheus_histo', 'Description of py_prometheus_histo')


def update_stats():
    # Populates 'h' metric with a bunch of values from imported dataset
    for v in data:
        h.observe(v)


def main():
    start_http_server(9100)
    x = 0
    while True:
        update_stats()
        x += 1

        # Some cosmetic stuff
        sys.stdout.write('.')
        sys.stdout.flush()
        if (x % 60) == 59:
            sys.stdout.write('\n')
            sys.stdout.flush()

        time.sleep(60)


if __name__ == '__main__':
    main()
