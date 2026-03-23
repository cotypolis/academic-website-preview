---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

## Estimating population average treatment effects for food labelling policy: A causal inference modelling approach for generalising trial findings to target populations in non-nested designs.

### Synthesis of empirical evidence

The collective evidence generated through this thesis demands a fundamental shift in how researchers and policymakers conceptualise the pathway from policy implementation to public health impact. Traditionally, front-of-package (FOP) labelling has been treated as a straightforward tool for informational disclosure, resting on the neoclassical assumption that providing consumers with comprehensive data will naturally lead to optimised dietary consumption.

However, by synthesising the findings from the empirical investigations conducted in this dissertation, a more complex and nuanced reality emerges. This thesis demonstrates that the limited effectiveness of current labelling policies is not a failure of consumer willpower, but rather a systemic oversight regarding the perceptual and cognitive constraints of human information processing.

Situated within this interdisciplinary landscape, this thesis investigates FOP labelling effectiveness by addressing both the empirical constraints of individual cognition and the methodological challenges of integrating data to estimate population-level impacts. The remainder of this thesis is structured across four subsequent chapters: 
* Chapter 2: Theoretical and methodological background. This chapter outlines the theoretical and methodological background of the thesis. It details the potential outcomes framework, the structural assumptions required for causal transportability, and the use of doubly robust machine learning estimators to integrate data sources while minimizing model misspecification. 
* Chapter 3: Food label readability and consumption frequency: isolating content-specific effects via a non-equivalent dependent variable design. Directly linking to the aim of investigating mechanisms of label salience, this chapter explores the salience-to-understanding pathway using observational data. Acknowledging the challenges of unmeasured confounding in nutritional epidemiology, it applies a quasi-experimental non-equivalent dependent variable design to repeated cross-sectional UK survey data. It investigates whether subjective perceptions of label print size readability block the effectiveness of nutritional warnings on ultra-processed ready-to-eat meals, isolating content-specific effects from general label presence. By highlighting that perceptual clarity is a critical bottleneck for less-engaged consumers, this chapter connects the physical limitations of label design to the behavioral realities of consumption. 
* Chapter 4: Food label granularity and working memory: effects on food choice in a randomized controlled trial. Building on the need to understand cognitive barriers to comprehension, this chapter utilizes an experimental trial to generate internally valid causal estimates regarding label design. Grounded in cognitive-load theory, it tests how label granularity interacts with individual cognitive constraints. The analysis examines whether the effectiveness of detailed versus coarse nutritional labels on calorie selection is actively modified by a consumer's working memory capacity. While consumption decisions are ultimately driven by a multitude of cultural, environmental, and economic factors, this chapter specifically isolates the role of cognitive constraints and informational granularity to test the hypothesis that label effectiveness increases with available cognitive bandwidth. 
* Chapter 5: On the selection of covariates for transportability: a doubly robust BART approach for generalizing a food labeling trial and modeling long-term public health impact. Finally, addressing the aim of bridging the gap between experimental evidence and real-world impact, this chapter synthesizes the preceding analyses by applying transportability methods to a non-nested design. It integrates the experimental trial data from Chapter 4 with observational data from the UK National Diet and Nutrition Survey. Using doubly robust Bayesian additive regression trees (BART), this chapter transports the local trial behavioral effects to estimate the national population average treatment effect on consumption. Furthermore, it incorporates these estimates into a microsimulation to model longterm policy cost-effectiveness and utilizes sensitivity analyses to explicitly quantify the robustness of the estimates against potential omitted covariates. 

Each of the empirical chapters (Chapters 3, 4, and 5) is structured as a self-contained research paper, complete with specific introductions, methodologies, and conclusions. While the chapters can be read independently, the prescribed sequence reflects the methodological progression of the thesis: diagnosing behavioral constraints via observational data, identifying causal mechanisms experimentally, and utilizing generalizability frameworks to forecast national public health impact.

### Experimental Visuals & Policy Models

<figure>
  <img src="{{ site.url }}{{ site.baseurl }}/images/combined_model.png" alt="combined_model">
  <figcaption>Effects of FOLP on participants’ ability to choose cereal brands according to calorie counts, in relation to their performance on the n-back test. See in Avalos, C. (2025). Food label granularity and working memory: Effects on food choice in a randomised controlled trial. Journal of Health, Population and Nutrition, 44, 375. https://link.springer.com/article/10.1186/s41043-025-01076-x</figcaption>
</figure>

<figure>
  <img src="{{ site.url }}{{ site.baseurl }}/images/combined_nback_effects.png" alt="combined_nback_effects">
  <figcaption>Interaction effects between FOLP treatments and n-back test levels on participants’ ability to choose cereal brands according to calorie counts. The plots show the associations between d’ as n-back performance (1-back, 2-back, and 3-back) and participants’ calorie count estimates under different labelling conditions (black = no label, red = detailed label, blue = coarse label). The bands represent 95% confidence intervals. See in Avalos, C. (2025). Food label granularity and working memory: Effects on food choice in a randomised controlled trial. Journal of Health, Population and Nutrition, 44, 375. https://link.springer.com/article/10.1186/s41043-025-01076-x</figcaption>
</figure>

<figure>
  <img src="{{ site.url }}{{ site.baseurl }}/images/readability_5x3_grid.png" alt="readability_5x3_grid">
  <figcaption>Mean perceived MTL print size readability from 2012 to 2018, stratified by sociodemographic characteristics, behavioural characteristics, and food products. Higher scores denote enhanced readability. See in Avalos, C., Wang, Y., & Shryane, N. (2026). Food label readability and consumption frequency: Isolating content-specific effects via a non-equivalent dependent variable design. Nutrients, 18(2), 197. https://www.mdpi.com/2072-6643/18/2/197</figcaption>
</figure>

<figure>
  <img src="{{ site.url }}{{ site.baseurl }}/images/Trend_Plot_Absolute_BMI.png" alt="Trend_Plot_Absolute_BMI">
  <figcaption>Projected population mean BMI change over a 10-year horizon (2025–2035) under alternative FOP labelling policy scenarios. The Status Quo (Black line) represents the counterfactual baseline of natural weight gain (secular trend) in the absence of policy intervention. Coloured lines represent the mean projected trajectories for the Coarse Label (yellow), Coarse Label + Industry Reformulation (red), Detailed Label (light blue), and Detailed Label + Industry Reformulation (Blue) scenarios, based on Population Average Treatment Effect (PATE) estimates from Model A to F. Estimates under 0.3%, 0.5% and 0.7% dietary compensation assumptions. The projection incorporates a stochastic noise parameter to simulate natural year-to-year population variability and an implementation lag function assuming partial policy effect in years 1–2 before reaching steady state. Shaded ribbons indicate the 95% confidence intervals derived from the uncertainty in the transported treatment effect estimates. See in Avalos, C., Wang, Y., & Shryane, N. (in preparation). On the selection of covariates for transportability: A doubly robust machine learning approach for generalising a food labelling trial with mixed-type data.</figcaption>
</figure>
