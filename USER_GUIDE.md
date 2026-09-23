# HarborFlow Dispatch Console — User Guide

## Purpose
This guide explains how to use the HarborFlow Dispatch Console and what input format each service expects. It supplements the required console prompts without changing them.

## Main Menu
At `Select service:`, enter one integer from **1 to 8**.

1. Close console
2. Validate booking reference
3. Calculate delivery quote
4. Consolidate parcel labels
5. Check van capacity
6. Classify service performance
7. Produce weekly dispatch report
8. Compare service scenarios

## 1. Close Console
Enter `1` to close the console.

## 2. Validate Booking Reference
Required format:

```text
HFL-CCC-NNNN
```

- `HFL` is the fixed HarborFlow prefix.
- `CCC` is exactly three letters.
- `NNNN` is exactly four digits.

Valid example:

```text
HFL-NOR-2048
```

Lowercase letters and surrounding spaces are normalized. Internal spaces are not part of the required format.

## 3. Calculate Delivery Quote
Enter:
- distance in kilometres, greater than 0
- total weight in kilograms, greater than 0
- service code: `S`, `X`, or `P`

```text
S = Standard
X = Express
P = Priority
```

Example:

```text
Distance (km): 12.5
Weight (kg): 8
Service code: X
```

## 4. Consolidate Parcel Labels
Enter **all parcel labels on one line**, separated by commas.

Example:

```text
gb-104, GB-220, gb-104, se-011, GB-220
```

The program removes surrounding spaces, converts labels to uppercase, removes duplicates, and preserves first-seen order.

Example result:

```text
Unique load list:
1. GB-104
2. GB-220
3. SE-011
Total unique parcels: 3
```

## 5. Check Van Capacity
This service checks **weight capacity in kilograms** for one van.

Enter a positive van capacity, then enter **all parcel weights on one line**, separated by commas.

Example:

```text
Van capacity (kg): 100
Parcel weights (kg): 40,65,20,35
```

The program checks parcels from left to right. A rejected parcel does not stop the process; a later lighter parcel may still fit.

## 6. Classify Service Performance
Enter:
- promised minutes
- actual minutes
- damaged parcels

These values must be non-negative, meaning zero is allowed but negative values are not.

Damage has priority over timing.

## 7. Produce Weekly Dispatch Report
Enter **exactly seven non-negative integers on one line**, separated by commas.

Order:

```text
Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
```

Example:

```text
42,55,55,38,61,61,20
```

Then enter the daily target, for example:

```text
50
```

If several days share the same highest or lowest value, the last tied day is reported.

## 8. Compare Service Scenarios
Enter a positive distance and positive weight.

Example:

```text
Distance (km): 18
Weight (kg): 12
```

The program compares Standard, Express, and Priority prices and reports the cheapest and most expensive service.

## Input Notes

### Comma-separated input
Several values are entered on **one line** with commas between them.

Example:

```text
40,65,20,35
```

### Positive
`value > 0`

### Non-negative
`value >= 0`

## Scope Notes
- Van capacity is weight in kilograms, not physical volume.
- Task 5 handles one van per service run, not a full fleet.
- This guide explains expected input without changing the required console interface.
