import json, numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.metrics import accuracy_score, roc_auc_score

rng = np.random.default_rng(42)
n = 1000
amount = np.clip(rng.lognormal(mean=7.5, sigma=1.0, size=n), 50, 200000)
hour = rng.integers(0, 24, n).astype(float)
dist = np.clip(rng.exponential(20, n), 0, 3000)
txhr = rng.poisson(1.2, n).astype(float)
foreign = rng.binomial(1, 0.12, n).astype(float)
present = rng.binomial(1, 0.85, n).astype(float)
night = ((hour < 5) | (hour > 22)).astype(float)
logit = (-2.4 + 0.85*np.log(amount/1000.0) + 1.2*night + 1.2*np.log1p(dist)/3.0
         + 0.9*np.clip(txhr, 0, 5)/2.0 + 1.2*foreign - 1.4*present + rng.normal(0, 0.3, n))
p = 1/(1+np.exp(-logit))
y = (rng.random(n) < p).astype(int)
# Engineered features used by the model (and mirrored in the browser demo)
X = np.column_stack([np.log(amount), night, np.log1p(dist),
                     np.clip(txhr, 0, 5), foreign, present]).astype(float)
names = ["log_amount", "night", "log1p_distance", "tx_last_hour_clipped", "foreign", "card_present"]
mu, sd = X.mean(0), X.std(0)
Xs = (X - mu) / sd
model = LogisticRegression(C=1.0, max_iter=1000).fit(Xs, y)
skf = StratifiedKFold(5, shuffle=True, random_state=42)
pred_cv = cross_val_predict(LogisticRegression(C=1.0, max_iter=1000), Xs, y, cv=skf)
proba_cv = cross_val_predict(LogisticRegression(C=1.0, max_iter=1000), Xs, y, cv=skf, method="predict_proba")[:, 1]
acc = float(accuracy_score(y, pred_cv)); auc = float(roc_auc_score(y, proba_cv))
base = float(max(y.mean(), 1-y.mean()))
print(f"CV accuracy={acc:.3f} AUC={auc:.3f} baseline={base:.3f} fraud_rate={y.mean():.3f} n={n}")
print("coef", model.coef_, "intercept", model.intercept_)
mj = {"features": names, "means": mu.tolist(), "stds": sd.tolist(),
      "coef": model.coef_[0].tolist(), "intercept": float(model.intercept_[0]),
      "metrics": {"cv_accuracy": acc, "cv_auc": auc, "baseline_accuracy": base, "fraud_rate": float(y.mean()), "n": n}}
with open("model.json", "w") as f: json.dump(mj, f, indent=1)

def predict_raw(amount_v, hour_v, dist_v, tx_v, foreign_v, present_v):
    night_v = 1.0 if (hour_v < 5 or hour_v > 22) else 0.0
    v = np.array([np.log(amount_v), night_v, np.log1p(dist_v), min(tx_v, 5), foreign_v, present_v], dtype=float)
    z = (v - mu) / sd
    lg = float(model.intercept_[0] + z @ model.coef_[0])
    return 1/(1+np.exp(-lg))
samples = [[2500, 14, 5, 1, 0, 1], [85000, 3, 1200, 4, 1, 0],
           [500, 10, 2, 0, 0, 1], [45000, 2, 800, 3, 1, 0],
           [12000, 19, 30, 1, 0, 1]]
for s in samples: print(s, round(predict_raw(*s)*100, 2), "%")
