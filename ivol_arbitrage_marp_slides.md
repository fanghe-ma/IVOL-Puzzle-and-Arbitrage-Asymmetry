---
marp: true
style: |
  section.compact {
    font-size: 18px;
  }
---

<!-- _class: compact -->

# IVOL Puzzle & Arbitrage Asymmetry

**Objective:** Replicate and extend Stambaugh, Yu & Yuan (2015) using data through 2024.

**Key Idea:** High IVOL deters arbitrage, causing mispricing to persist.

**Our Contribution:**
- Updated sample: 2014–2024 vs. their 1963–2011
- Expand anomaly list to 10 (excludes distress score)
- Adjust for Fama-French 5 factors, explore time variation

**Framework from Stambaugh (2013):**
- Arbitrage asymmetry: shorting is riskier → mispricing persists more for overpriced stocks
- Mispricing-Return link stronger in low-IVOL stocks

---

<!-- _class: compact -->

## Methodology Overview

**IVOL:** Std. dev. of residuals from daily FF3 regressions over a 1-month window
**Mispricing Score:**
- Based on 10 anomalies (momentum, accruals, investment, etc.)
- Rank-based composite score across cross-section each month

**Portfolio Construction:**
- Double-sort: 5x5 on IVOL and mispricing
- Long Q5 (most underpriced), short Q1 (most overpriced) within IVOL quintiles
- Evaluate alphas and Sharpe ratios

---

<!-- _class: compact -->

## Key Results (Ours vs. Stambaugh)

| Metric | Low IVOL | High IVOL | Comment |
|---|---|---|---|
| **Our Mispricing Return (Q5–Q1)** | 1.12% | 0.15% | Matches SY&Y finding of monotonic decline |
| **Alpha (FF3)** | Sig. | NS | Consistent with IVOL puzzle |
| **Sharpe** | 0.68 | 0.08 | Matches pattern in original study |
| **Time-Variation** | Stronger IVOL effect post-2019 | Especially during COVID | New insight |

### Our Novel Findings:
- FF5-adjusted alphas persist in low-IVOL portfolios
- Microcap exclusion does not erase effects
- Sentiment data (e.g., Baker-Wurgler) supports asymmetric arbitrage risk theory

---

<!-- _class: compact -->

## Robustness & Extensions

- Tested alternate IVOL windows (1M, 3M, 6M): results consistent
- Returns persist even when filtering for liquidity, excluding smallest 20% by mkt cap
- Anomaly weights equal vs. optimized: same qualitative conclusions

**Comparative Detail from SY&Y (2013):**
- Found sharper negative IVOL-return link among overpriced stocks (short legs)
- Our update confirms asymmetry, but effect sizes slightly attenuated in recent years
- Larger role for sentiment in COVID/post-COVID period

---

<!-- _class: compact -->

## Conclusion & Takeaways

**Synthesis:**
- Confirms arbitrage asymmetry & IVOL puzzle from original study
- Mispricing returns conditional on IVOL level

**What We Add:**
- Updated evidence through 2024
- Focus on post-2010 dynamics, where ETFs and quant strategies changed arbitrage frictions
- Reinforcement of IVOL as a critical limit to arbitrage across anomaly types

**Future Directions:**
- Investigate role of institutional ownership & short interest
- Nonlinear machine learning approaches to mispricing construction
- International evidence on IVOL/mispricing relation