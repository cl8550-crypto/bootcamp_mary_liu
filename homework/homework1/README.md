# Homework 1
# Daily Drawdown Risk Alerts for a Student-Managed Equity Portfolio
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Student portfolio managers currently lack a systematic early-warning signal for outsized single-day losses in individual holdings. Unexpected >2% drawdowns erode performance, trigger reactive selling, and increase turnover.  
We aim to provide a daily pre-close risk signal that flags positions with elevated next-day drawdown risk so the PM can right-size, hedge, or set tighter stops.  

Success will be measured by: (i) achieving higher precision/recall for “high-risk tomorrow” vs. a naive baseline, and (ii) reducing realized severity/frequency of next-day losses among flagged names in out-of-sample tests.

## Stakeholder & User
- **Decision owner:** Student Portfolio Manager (PM).  
- **End users:** PM and, where relevant, a Risk Officer.  
- **Workflow context:** Signals are generated ~30 minutes before market close each trading day and integrated into the PM’s rebalance/hedge workflow.

## Useful Answer & Decision
- **Type:** Predictive — binary classification (will tomorrow’s drawdown exceed 2%?).  
- **Primary metrics:** Precision-Recall AUC; Recall@Top-K; calibration quality.  
- **Artifact delivered:** Daily CSV of tickers with risk scores; optional short list in dashboard or Slack/email alert.  
- **Decision supported:** Trim, hedge, or adjust stops on flagged holdings before the close.

## Assumptions & Constraints
- **Data:** Daily OHLCV + simple factors/volatility measures; no MNPI.  
- **Latency:** <5 minutes end-to-end runtime on a laptop.  
- **Capacity:** <200 tickers scored daily; retrain weekly.  
- **Governance:** Reproducible pipeline with versioning and documented features.

## Known Unknowns / Risks
- Class imbalance (few big drops) → risk of false negatives; mitigate with time-series CV.  
- Market regime shifts → need weekly retraining and drift monitoring.  
- Label leakage (post-close info accidentally used) → ensure strict feature timing.  
- Overfitting → walk-forward validation; start with simple baselines.

## Lifecycle Mapping
Goal → Stage → Deliverable
- Frame the stakeholder problem → Stage 01 (Problem Framing & Scoping) → README + stakeholder memo  
- Audit available data, define label → Stage 02 (Data Audit & EDA) → EDA notebook + label spec  
- Train & evaluate baseline models → Stage 03 (Modeling) → Baseline classifier + evaluation report  
- Operationalize daily scoring → Stage 04 (Deployment) → Script producing CSV alerts + lightweight dashboard

## Repo Plan
- **Folder structure:** `/data/`, `/src/`, `/notebooks/`, `/docs/`.  
- **Cadence:** Weekly commits until baseline; stakeholder memo in `/docs/`; daily scorer in `/src/`.
