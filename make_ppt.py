from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation(); prs.slide_width = Inches(13.33); prs.slide_height = Inches(7.5)
def add(i, title, lines):
    s = prs.slides.add_slide(prs.slide_layouts[1])
    s.shapes.title.text = title
    tf = s.placeholders[1].text_frame; tf.word_wrap = True
    for j, ln in enumerate(lines):
        p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
        p.text = ln; p.font.size = Pt(20); p.space_after = Pt(10)
add(0, "FraudGuard — Card Fraud Detector", ["An AI/ML project by Vikranth Reddy", "B.Tech CSE (AI & ML), 2nd Year — Woxsen University", "Logistic regression that scores card fraud risk right in your browser"])
add(1, "The Problem", ["Card fraud costs banks and customers crores every year", "A single rule (like a spending limit) misses clever fraud and blocks genuine users", "Risk depends on amount, time, location, frequency and card presence together", "A fast risk score lets banks flag suspicious transactions before money is lost"])
add(2, "The Solution — FraudGuard", ["Enter amount, hour, distance from home, recent transactions, foreign flag and card presence", "A trained logistic regression model returns a fraud-risk percentage", "Risk bands: below 25% low, 25–50% medium, above 50% high", "Runs fully in the browser — no backend, no waiting"])
add(3, "Tech Stack", ["Python + scikit-learn: data generation and model training", "Logistic regression (C = 1.0) on standardised engineered features", "HTML, CSS and vanilla JavaScript for the interactive demo", "GitHub for source control, Vercel for free hosting"])
add(4, "Architecture", ["Synthetic dataset: 1,000 card transactions, 6 features, seed 42", "Feature engineering: log amount, night flag, log distance, capped recent-transaction count", "Standardisation (mean / std) -> logistic regression -> model.json", "model.json ships with the site; JavaScript applies the same formula and a sigmoid"])
add(5, "Live Demo", ["Try it: enter a transaction and press Check Fraud Risk", "Example: Rs 2,500 at 2 PM, 5 km from home, card present -> about 15.42% fraud risk", "Risky example: Rs 85,000 at 3 AM, 1,200 km away, foreign, card not present -> about 99.94%", "Demo: https://fraudguard-alpha.vercel.app"])
add(6, "Results", ["5-fold cross-validation accuracy: 75.7%", "AUC: 0.77 — the model ranks fraudulent transactions well above genuine ones", "Baseline (always guessing legit): 71.2% accuracy", "Fraud rate in training data: 28.8%", "Browser demo matches Python predictions exactly on all test samples"])
add(7, "Future Scope", ["Train on real, anonymised transaction data with bank approval", "Add a merchant-category feature and device fingerprint", "Compare random forest and gradient boosting models", "Add an alert panel: block, OTP-verify, or allow based on the risk band"])
add(8, "Thank You", ["FraudGuard — Card Fraud Detector", "Vikranth Reddy, B.Tech CSE (AI & ML), Woxsen University", "Source: github.com/HVRGAMING2705/fraudguard", "Questions welcome!"])
prs.save("/home/hatch/workspace/goals/daily-ai-ml-project-factory/files/AIML_FraudGuard_2026-11-03.pptx")
print("slides:", len(prs.slides._sldIdLst))
