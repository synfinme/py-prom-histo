FROM python:alpine3.14

RUN python -m pip install --upgrade pip && \
    pip install prometheus-client && \
    mkdir /opt/scripts

COPY dataset.py /opt/scripts/dataset.py
COPY main.py /opt/scripts/py-prom-histo.py

RUN chmod +x /opt/scripts/py-prom-histo.py

CMD ["/opt/scripts/py-prom-histo.py"]
