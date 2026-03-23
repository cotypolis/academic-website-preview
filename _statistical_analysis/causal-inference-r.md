---
layout: single
author_profile: true
title: 'Causal Inference in R'
collection: statistical_analysis
permalink: /statistical-analysis/causal-inference-r/
tags:
  - R
  - Causal Inference
---

Causal inference can be seen as a subfield of statistical analysis. It is used in various fields such as econometrics, epidemiology, educational sciences, etc. With causal inference one addresses questions about effects of a treatment, intervention, or policy on some target over a given sample or population. Under certain identifiability and model assumptions, causal inference can be carried out by fitting simple regression models or combining several regression models in a specific way as will be sketched out later. For observational data, additional untestable assumptions have to be made to (non-parametrically) identify causal effects.

There are no basic R functions that are direct implementations of standard causal inference designs, but many methods - more or less complex - are implemented in different packages on CRAN, which we structure into main topics:

## Methods for experimental data
* Average treatment effect estimation and other univariate treatment effect estimates
* Heterogeneous treatment effect estimation
* Policy learning and dynamic treatment regimes
* Structural equation models (SEM), do-calculus causal discovery

Specific types of data
Specific application fields
Certain causal inference methods originated in specific fields such as econometrics or clinical trials and remain most popular therein.

### Methods for randomized controlled trial (RCT) and other experimental data
Construction of experimental designs is implemented in blocksdesign (blocks for general factorial treatment designs), BCHM (Bayesian cluster hierarchical model design for multiple subgroup basket trials), Boptbd (Bayesian optimal block designs under linear mixed effects model), seqDesign (sequential design of randomized two-stage treatment efficacy trials with time-to-event endpoints).

### Average treatment effect estimation
Regression models where the causal estimand is a regression parameter are implemented in lm() and glm() from stats, as well as in a number of more specialized packages such as fixest, estimatr, CausalGAM (using generalized additive models), sampleSelection, BCEE, borrowr, causaldrf, hdm.

Estimation in fixed effects designs is possible through fixest (linear and generalized linear fixed effects models and combined with instrumental variables), plm (for panel data), and alpaca (for high-dimensional k-way fixed effects).

G-computation and other conditional outcome regression based methods are supported in the packages gfoRmula, EffectLiteR, switchSelection, and riskRegression. Matches methods are implemented in MatchIt, MatchThem, Matching, optmatch, cem, stratamatch, FLAME, PanelMatch, and others. Multiple treatment matching approaches also exist.

More advanced methods such as Inverse Propensity Weighting (IPW/IPTW) are implemented in WeightIt, PSweight, inferference, CBPS, twang, sbw, optweight, and ebal. For doubly robust methods, one can look at AIPW, DoubleML, grf, and causalweight.
