#!/usr/bin/env python3

#from prometheus_client import start_http_server, Histogram
from prometheus_client import start_http_server, Summary
import os
import random
import sys
import time

try:
    from dataset import data
except ImportError:
    from default_dataset import data


METRIC_NAME_BASE = 'py_prometheus_summary'
METRIC_NAME_SUFFIX = os.environ.get('METRIC_NAME_SUFFIX', '')
DELAY_SECONDS      = os.environ.get('DELAY_SECONDS', '15.0')

metric_name = METRIC_NAME_BASE
if len(METRIC_NAME_SUFFIX) > 0:
    metric_name += '_' + METRIC_NAME_SUFFIX


#h = Histogram(metric_name, 'Description of %s' % (metric_name))
s = Summary(metric_name, 'Description of %s' % (metric_name), ['endpoint'])


def update_stats():
    # Populates 'h' metric with a bunch of values from imported dataset
    for v in data:
        s.labels(endpoint='/v1/set_id').observe(v)
        s.labels(endpoint='/v1/get_id').observe((v / 3.0))
        time.sleep(float(DELAY_SECONDS))


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


if __name__ == '__main__':
    main()
