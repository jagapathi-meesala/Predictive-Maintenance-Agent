---
name: failure-risk-analysis
description: Estimate equipment failure risk from validated operational features and maintenance indicators.
---

# Failure Risk Analysis

## Purpose

Estimate the relative failure risk of an industrial asset from supplied operational features.

## Inputs

Accept an asset identifier and numerical features representing relevant equipment operating conditions.

## Processing

Validate the supplied features and calculate the risk estimate using the deterministic failure-risk implementation.

## Outputs

Return a structured risk result containing the asset identifier, calculated risk information, and supporting indicators.

## Limitations

The result is an analytical estimate based on the provided features and implemented model logic. It should not be interpreted as a guaranteed prediction of an actual equipment failure.
