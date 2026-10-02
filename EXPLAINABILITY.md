# Explainability

## Inputs and Data Sources
Inputs are structured equipment observations supplied directly in a tool request, including temperature, vibration, operating hours, failure history, maintenance delay, or an ordered sensor-reading window. The data source is therefore the caller-provided telemetry or maintenance record; this implementation does not fetch external data and does not invent missing values.

### Input Requirements
Each tool defines required fields and validates their types and value ranges before execution. Numeric values must be finite, and lists used for anomaly detection must contain at least three numeric readings.

### Failure Handling
Missing fields, invalid types, negative durations, and malformed reading arrays return structured errors. A failed validation never proceeds to a domain calculation.

## Decision and Reasoning
The decision is a transparent analytical classification derived from normalized indicators and fixed weights, rather than an opaque model inference. Health uses temperature, vibration, and operating-age components; failure risk uses temperature, vibration, recent failures, and maintenance delay, while anomaly detection uses population z-scores.

### Rules Applied
Health is calculated as `100 × (1 − weighted component burden)` with weights 0.45 temperature, 0.40 vibration, and 0.15 age. Failure risk is `100 × (0.30 temperature + 0.35 vibration + 0.20 history + 0.15 overdue)`, with low/medium/high bands at 40 and 70; anomaly detection flags absolute z-scores above the supplied threshold, defaulting to 3.0.

### Expected Outputs
Every successful tool returns structured data containing the derived score or anomaly set and supporting component information. Every failure returns an error code and message through the common tool contract.

### Worked Example
For an asset with 70°C temperature, 6 mm/s vibration, and 4,000 operating hours, the health tool produces a lower health score because temperature and vibration contribute material burden. For a sensor window with one reading far from the population mean, the anomaly tool reports its index, value, and z-score when it exceeds the threshold.

## Limits and Constraints
The implementation provides generic screening analytics and is not a calibrated probability-of-failure model or a remaining-useful-life guarantee. Equipment-specific manufacturer limits, sensor calibration, operating context, and validated historical failure datasets are outside the current implementation and must be considered by a qualified maintenance professional.

### Constraints
The agent does not control machinery, issue shutdown commands, modify maintenance records, or fetch private plant data. It also does not claim compatibility with an external framework merely because an adapter interface exists.

### Unsupported Behavior
Automatic work-order creation, closed-loop machine control, hidden data acquisition, and model training are unsupported. The current tools are deterministic and framework-independent.
