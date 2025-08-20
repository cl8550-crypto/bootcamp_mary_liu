# Stakeholder Memo — Daily Drawdown Risk Alerts

**Owner / Decision Maker**  
Student Portfolio Manager (PM)

**Users**  
PM; optionally a Risk Officer who reviews alerts and actions.

**Decision & When It Happens**  
About 30 minutes before market close each trading day, decide whether to trim, hedge, or tighten stops for holdings flagged as high risk for a >2% next‑day drawdown.

---

## Pain Point
Unexpected single‑day losses in individual positions cause reactive selling and drag on performance. There is no lightweight, systematic early‑warning list the PM can review before the close.

## Useful Answer (What “good” looks like)
- A **ranked list** of tickers with next‑day **drawdown risk probabilities**.  
- **Metrics:** PR‑AUC and Recall@Top‑K on rolling out‑of‑sample windows; probability **calibration** checked monthly.  
- **Artifacts:** A daily **CSV** and a short “Top‑K” list that can be read in <60 seconds; optional Slack/email alert.

## Inputs / Assumptions / Constraints
- **Data:** Daily OHLCV + simple market factors/volatility; strictly timestamp‑safe (no post‑close leakage).  
- **Latency:** End‑to‑end scoring < 5 minutes on a laptop/Colab.  
- **Scope:** ≤ 200 tickers; weekly retraining.  
- **Governance:** Reproducible pipeline, versioned code, documented features.

## Risks & Mitigations
- **Class imbalance (rare big drops):** time‑series CV; threshold tuning; Recall@Top‑K reporting.  
- **Regime shifts:** weekly retrains; drift monitoring.  
- **Overfitting:** start with simple baselines; walk‑forward validation.  
- **Alert fatigue:** cap list to Top‑K by score; show brief context (e.g., recent vol spike).

## Near‑Term Milestones (Stage 01 → Stage 02)
- This week (Stage 01): finalize scope (this memo) and README; set repo structure.  
- Next (Stage 02): assemble data dictionary, define label (>2% next‑day drop), and run EDA to confirm class balance and leakage checks.

*This memo satisfies the “stakeholder context artifact” requirement from the Homework 1 sheet (stakeholder memo / slide / or top‑of‑notebook comments).* 
