# Asset Health Assessment

## Purpose
Estimate a normalized asset health score from temperature, vibration, and operating-age indicators.

## Inputs
Temperature in Celsius, vibration in mm/s, and non-negative operating hours.

## Processing
Normalize each indicator to a bounded component and combine them using fixed transparent weights.

## Outputs
A 0-100 health score, a health band, and component contributions.

## Limitations
Thresholds are generic screening assumptions and should be replaced by validated equipment-specific limits before production use.

## Expected behavior
Reject negative durations and invalid numeric values.
