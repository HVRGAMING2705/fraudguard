# FraudGuard — Card Fraud Detector

A 2nd-year B.Tech AI/ML project by Vikranth Reddy (Woxsen University).

Logistic regression (C=1.0) on engineered features — log amount, night-time flag, log distance from home, capped recent-transaction count, foreign flag, card-present flag — trained on 1,000 synthetic card transactions (seed 42).

- 5-fold CV accuracy: 75.7%, AUC: 0.77 (always-legit baseline: 71.2%)
- Fraud rate in training data: 28.8%
- Live demo: https://fraudguard-alpha.vercel.app (runs fully in the browser — no backend)
- `train.py` trains the model and writes `model.json`; `index.html` applies the same weights in JavaScript.
