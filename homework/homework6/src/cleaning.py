
from __future__ import annotations
import pandas as pd
import numpy as np

def fill_missing_median(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    out = df.copy()
    for c in cols:
        if c in out.columns:
            med = out[c].median(skipna=True)
            out[c] = out[c].fillna(med)
    return out

def drop_missing(df: pd.DataFrame, thresh: float = 0.0, subset: list[str] | None = None) -> pd.DataFrame:
    out = df.copy()
    if subset is None:
        subset = out.columns.tolist()
    if thresh <= 0:
        return out.dropna(subset=subset)
    if 0 < thresh <= 1:
        mask = out[subset].isna().mean(axis=1) <= thresh
        return out[mask]
    raise ValueError("thresh must be between 0 and 1 (inclusive) or 0 to behave like dropna.")

def normalize_data(df: pd.DataFrame, cols: list[str], method: str = "zscore") -> pd.DataFrame:
    out = df.copy()
    for c in cols:
        if c not in out.columns:
            continue
        s = pd.to_numeric(out[c], errors="coerce")
        if method == "zscore":
            mu, sd = s.mean(skipna=True), s.std(skipna=True)
            out[c] = (s - mu) / sd if (sd and sd != 0) else 0.0
        elif method == "minmax":
            lo, hi = s.min(skipna=True), s.max(skipna=True)
            rng = hi - lo
            out[c] = (s - lo) / rng if (rng and rng != 0) else 0.0
        else:
            raise ValueError("method must be 'zscore' or 'minmax'")
    return out
