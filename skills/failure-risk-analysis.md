# Failure Risk Analysis

## Purpose
Estimate near-term failure risk from condition, failure history, and maintenance delay indicators.

## Inputs
Temperature, vibration, recent failure count, and overdue-maintenance days.

## Processing
Normalize four indicators, combine them with documented weights, and map the result to low, medium, or high risk.

## Outputs
A 0-100 risk score, risk band, component values, and a proportionate maintenance suggestion.

## Limitations
This is not a trained failure-probability model and does not establish a calibrated probability of failure.

## Expected behavior
Never represent a risk band as a confirmed machine failure.
