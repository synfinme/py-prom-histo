FROM python:alpine3.14

RUN python -m pip install --upgrade pip && \
    pip install prometheus-client && \
    mkdir /opt/scripts

COPY default_dataset.py /opt/scripts/default_dataset.py
COPY main.py /opt/scripts/py-prom-histo.py

RUN chmod +x /opt/scripts/py-prom-histo.py

CMD ["/opt/scripts/py-prom-histo.py"]
