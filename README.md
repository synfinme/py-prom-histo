# Prometheus Histogram metric example

This simple Python app which exposes Histogram metric on `tcp/9100` port.

An example of metric exposition: [docs/metrics.txt](docs/metrics.txt).

## Histogram metrics visualization
described in \[2\].  Example in [docs/grafana.dash.01.png](docs/grafana.dash.01.png).

## Hints on Prometheus setup
```sh
% helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
% helm repo add grafana https://grafana.github.io/helm-charts
% helm repo update

% helm install k8s-prom prometheus-community/prometheus
% helm install k8s-gra grafana/grafana
```

---

1. `https://github.com/prometheus/client_python`
2. `https://grafana.com/blog/2020/06/23/how-to-visualize-prometheus-histograms-in-grafana/`
