---
tags:
  - data-and-ai:data-science
  - data-and-ai:statistics
  - data-and-ai:machine-learning
  - languages:python
level: intermediate
category: data-science
duration_hours: 16
audience:
  - audiences:developers
  - audiences:data-scientists
  - audiences:data-analysts
---
<!-- course: time_series_analysis -->
# Time Series Analysis

## Description
This course provides a comprehensive introduction to time series analysis using `Python`.
Participants will learn to decompose time series into their fundamental components (trend,
seasonality, and noise), test for stationarity, and apply classical forecasting models
such as ARIMA and SARIMA. The course also covers modern approaches including exponential
smoothing, Prophet, and `machine learning` techniques for `temporal` data. Topics on anomaly
detection, cross-validation strategies specific to time series, and feature engineering
for `temporal` data round out the curriculum.

## Duration
16 hours / 2 days

## Intended Audience
* Data scientists building forecasting and anomaly detection systems
* Data analysts working with `temporal` and sequential data

## Prerequisites
* Basic understanding of statistics (mean, variance, distributions, `hypothesis` testing)

## Required Knowledge
* `Python` Programming (or equivalent experience)

## Objectives
* **Understand time series components** including trend, seasonality, cyclical patterns, and noise
* **Test and achieve stationarity** using statistical tests and transformation techniques
* **Build forecasting models** using ARIMA, SARIMA, and exponential smoothing methods
* **Apply Prophet** for scalable and interpretable time series forecasting
* **Detect anomalies** in `temporal` data using statistical and model-based approaches
* **Engineer `temporal` features** and apply proper cross-validation for time series models

## Outline
<!-- chapter: time-series-fundamentals, duration: 1h -->
* Time Series Fundamentals
    * What is a time series
    * Time series components (trend, seasonality, cyclical, noise)
    * Additive vs multiplicative decomposition
    * Time series data structures in `pandas`
    * Resampling, shifting, and rolling `windows`
    * Visualization of `temporal` patterns
<!-- chapter: stationarity, duration: 1h -->
* Stationarity
    * Definition and importance of stationarity
    * Augmented Dickey-Fuller test
    * KPSS test
    * Differencing for stationarity
    * Log and power transformations
    * Detrending techniques
<!-- chapter: seasonal-decomposition, duration: 1h -->
* Seasonal Decomposition
    * Classical decomposition (additive and multiplicative)
    * `STL` decomposition (Seasonal and Trend decomposition using Loess)
    * Interpreting decomposition results
    * Residual analysis
    * Identifying seasonal periods
<!-- chapter: autocorrelation-analysis, duration: 1h -->
* Autocorrelation Analysis
    * Autocorrelation function (ACF)
    * Partial autocorrelation function (PACF)
    * Interpreting ACF and PACF plots
    * Identifying model orders from correlograms
    * Ljung-Box test for white noise
<!-- chapter: exponential-smoothing, duration: 1h -->
* Exponential Smoothing
    * Simple exponential smoothing
    * Holt's linear trend method
    * Holt-Winters seasonal method
    * Damped trend models
    * Parameter optimization
    * State space models (ETS framework)
<!-- chapter: arima-and-sarima-models, duration: 2h -->
* ARIMA and SARIMA Models
    * Autoregressive (AR) models
    * Moving average (MA) models
    * ARIMA model formulation and parameters
    * Model identification (order selection)
    * AIC and BIC for model comparison
    * Seasonal ARIMA (SARIMA)
    * Diagnostic checking and residual analysis
<!-- chapter: forecasting-with-prophet, duration: 2h -->
* Forecasting with Prophet
    * Prophet model architecture and assumptions
    * Trend modeling (linear and logistic growth)
    * Seasonality handling (yearly, weekly, daily)
    * Holiday and special event effects
    * Changepoint detection
    * Uncertainty intervals
    * Hyperparameter tuning
<!-- chapter: anomaly-detection-in-time-series, duration: 1h -->
* Anomaly Detection in Time Series
    * Statistical methods (z-score, IQR)
    * Moving average-based detection
    * Isolation Forest for `temporal` data
    * Seasonal hybrid ESD (S-H-ESD)
    * Residual-based anomaly detection
    * Contextual and collective anomalies
<!-- chapter: feature-engineering-for-temporal-data, duration: 2h -->
* Feature Engineering for Temporal Data
    * Lag features and rolling statistics
    * Date-time feature extraction
    * Fourier features for seasonality
    * Holiday and event indicators
    * Interaction features
    * Target encoding for `temporal` data
<!-- chapter: cross-validation-for-time-series, duration: 2h -->
* Cross-Validation for Time Series
    * Why standard cross-validation fails for time series
    * Expanding window validation
    * Sliding window validation
    * Time series split strategies
    * Forecast horizon considerations
    * Backtesting frameworks
<!-- chapter: model-evaluation, duration: 2h -->
* Model Evaluation
    * Mean Absolute Error (MAE)
    * Mean Squared Error (MSE) and RMSE
    * Mean Absolute Percentage Error (MAPE)
    * Symmetric MAPE (sMAPE)
    * Forecast bias detection
    * Comparing model performance across horizons

## Copyright
Mark Veltzer [mark.veltzer@gmail.com](mailto:mark.veltzer@gmail.com), © 2026
