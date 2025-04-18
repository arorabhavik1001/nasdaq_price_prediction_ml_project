# 📈 NASDAQ Stock Price Prediction using Ensemble Regression

A machine learning project that predicts NASDAQ stock closing prices using an ensemble regression model. Combines historical stock data and economic indicators with a Flask backend and a Next.js frontend.

![License](https://img.shields.io/badge/ML-Flask-blue)
![License](https://img.shields.io/badge/Frontend-Next.js-lightgrey)
![License](https://img.shields.io/badge/Model-Ensemble%20Regressor-brightgreen)

## 🔍 Project Overview

This project uses a **Voting Regressor** combining **Linear Regression**, **Lasso Regression**, and **Decision Tree Regression** to predict the **closing price** of NASDAQ stocks.

### ✅ Key Features
- **Ensemble Regression Model** with a cross-validation score of **0.83**
- Trained on **20 years (2005–2025)** of NASDAQ stock and economic data
- Predicts based on:
  - Open, High, Low prices
  - Trading Volume
  - Economic Indicators:
    - Gold Prices
    - Crude Oil Prices
    - USD/EUR Forex rates
- **Flask** backend for model deployment
- **Next.js** frontend for user interaction

## ⚙️ Tech Stack

- **Python**, **Scikit-learn**, **Pandas**, **NumPy**
- **Flask** – Backend API
- **Next.js** – Frontend
- **Vercel** – Deployment for frontend

## 📊 Model Training

The model was trained on:
- **NASDAQ price history (2005–2025)** 
- **Macroeconomic indicators** scraped or compiled from reliable sources.


## 🚀 Live Demo

👉 [Try the Web App](https://nasdaqpriceprediction.vercel.app/)

