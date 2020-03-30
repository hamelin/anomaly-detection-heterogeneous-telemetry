# Anomaly detection on heterogeneous telemetry, using embeddings of graph topology dynamics

These notebooks implement and experiment with an anomaly detection method
applicable to heterogeneous time series of key-value records (denoted here
as *telemetry*). This detection method follows the template of a 2018 paper by
[Palladino and Thissen](https://arxiv.org/abs/1812.02848), who apply it to
streams of low-value cybersecurity alerts from multiple appliances. It also
takes into account many of improvements applied to the detector by [Element
AI](https://github.com/ElementAI/eai-graph-based-anomaly-detection).

To demonstrate, study and improve the performance of this methodology, we
apply it here to the [Los Alamos Cybersecurity
dataset](https://csr.lanl.gov/data/cyber1/). This dataset is composed of four
independant streams with distinct event data schemas, correlated in time. The
events reported in these streams are composed of *artifacts* that also appear
as part of other streams, making them intersectable.

## Setup

1. Have a Python 3.6+ install
1. Create and activate a Python virtual environment, using
   `virtualenv`, `pipenv`, `poetry` or `conda`.
1. `pip install -r requirements.txt`
1. Launch the notebook server.

## Notebook summary

**Basics**

Approximative replication of the methodology described by Palladino and
Thissen: graphs composed of all possible categorical/textual artifacts,
embeddings derived by ReFEx and RolX, role change analysis to detect
anomalies.
