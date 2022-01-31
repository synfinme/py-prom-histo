# To reproduce

```
% ./default_dataset.py > _data

% R
b <- c(0.0, 0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0)
x <- scan("_data", numeric())
h <- hist(x, breaks=b, plot=FALSE)
barplot(h$counts, names.arg=b[-1])
grid(nx=NA, ny=NULL)
```

![R.barplot.00.png](https://github.com/synfinme/py-prom-histo/blob/master/docs/R.barplot.00.png?raw=true)

## Other pictures

![grafana.dash.00.png](https://github.com/synfinme/py-prom-histo/blob/master/docs/grafana.dash.00.png?raw=true)

![grafana.dash.01.png](https://github.com/synfinme/py-prom-histo/blob/master/docs/grafana.dash.01.png?raw=true)
