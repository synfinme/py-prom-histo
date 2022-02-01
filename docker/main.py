#!/usr/bin/env python3

from prometheus_client import start_http_server, Histogram
import os
import random
import sys
import time

try:
    from dataset import data
except ImportError:
    from default_dataset import data


METRIC_NAME_BASE = 'py_prometheus_histo'
METRIC_NAME_SUFFIX = os.environ.get('METRIC_NAME_SUFFIX', '')

metric_name = METRIC_NAME_BASE
if len(METRIC_NAME_SUFFIX) > 0:
    metric_name += '_' + METRIC_NAME_SUFFIX


h = Histogram(metric_name, 'Description of %s' % (metric_name))


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
