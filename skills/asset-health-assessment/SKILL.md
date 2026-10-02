---
name: asset-health-assessment
description: Assess industrial asset health using validated sensor readings and operating information.
---

# Asset Health Assessment

## Purpose

Assess the current health state of an industrial asset from supplied operational measurements.

## Inputs

Accept an asset identifier, numerical sensor readings, and optional operating-hour information.

## Processing

Validate the input values and evaluate the configured health indicators using deterministic calculations implemented by the asset-health tool.

## Outputs

Return a structured health assessment containing the asset identifier, health indicators, and resulting health state.

## Limitations

The assessment is based only on the supplied measurements and configured rules. It does not perform physical inspection or guarantee future equipment behavior.
