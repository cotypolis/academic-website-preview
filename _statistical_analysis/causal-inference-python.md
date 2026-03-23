---
title: 'Causal Inference in Python'
collection: statistical_analysis
permalink: /statistical-analysis/causal-inference-python/
tags:
  - Python
  - Causal Inference
---

Python provides an array of tools for sophisticated causal analysis, often utilized alongside machine learning paradigms.

### 1. Causalinference
Causalinference is a Python package that provides various statistical methods for causal analysis. It is a simple package that was used for basic causal analysis learning. The main features include Propensity score estimation and subclassification, Improvement of covariate balance through trimming, Estimation of treatment effects, and Assessment of overlap in covariate distributions.

```python
from causalinference import CausalModel
from causalinference.utils import random_data

#Y is the outcome, D is treatment status, and X is the independent variable
Y, D, X = random_data()
causal = CausalModel(Y, D, X)
print(causal.summary_stats)
causal.est_via_ols()
print(causal.estimates)
```

### 2. Causalimpact
Causalimpact is a Python package for Causal Analysis to estimate the causal effect of time series interventions. It analyzes the response time series and a control time series with the Bayesian structural time-series model.

```python
import numpy as np
import pandas as pd
from statsmodels.tsa.arima_process import arma_generate_sample
from causalimpact import CausalImpact

np.random.seed(1)
x1 = arma_generate_sample(ar=[0.999], ma=[0.9], nsample=100) + 100
y = 1.2 * x1 + np.random.randn(100)
y[71:100] = y[71:100] + 10
data = pd.DataFrame(np.array([y, x1]).T, columns=["y","x1"])
pre_period = [0,69]
post_period = [71,99]

impact = CausalImpact(data, pre_period, post_period)
impact.run()
impact.plot()
```

### 3. DoWhy
DoWhy is a Python package that provides state-of-art causal analysis with a simple API and complete documentation, guided by four steps: model a causal inference problem, identify an expression for the causal effect, estimate the expression, and verify the validity of the estimate.

```python
from dowhy import CausalModel
import dowhy.datasets

data = dowhy.datasets.linear_dataset(
    beta=10, num_common_causes=5, num_instruments=2,
    num_samples=10000, treatment_is_binary=True)

model = CausalModel(
    data=data["df"], treatment=data["treatment_name"],
    outcome=data["outcome_name"], graph=data["gml_graph"])

estimands = model.identify_effect()
estimate = model.estimate_effect(estimands, method_name="backdoor.propensity_score_matching")
refute_results = model.refute_estimate(estimands, estimate, method_name="random_common_cause")
```
