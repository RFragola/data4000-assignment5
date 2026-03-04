# data4000-assignment5

## Installation

Before running Exercise 2, install the required dependency:

```
pip install requests
```

---

## Exercise 1 — Point-of-Sale Checkout System

### How to Run

```
python pos_checkout.py
```

### Example Run

```
Student key: alice123
Item name: Coffee
Unit price: 4.50
Quantity: 3
Item name: Notebook
Unit price: 8.00
Quantity: 2
Item name: DONE

Seed: 532
Units: 5
Subtotal: $29.50
Discount: 0%
Perk applied: NO
Total: $29.50
```

---

## Exercise 2 — Inventory Reorder Analyzer with API Spot Check

### How to Run

```
python inventory_spotcheck.py
```

Requires `requests` (see Installation above).

### Example Run

```
Student key: alice123
SKU: Item 3
On hand: 20
SKU: Item 2
On hand: 5
SKU: PART-C
On hand: 11
SKU: DONE

Seed: 532
Threshold: 12
SKUs entered: 3
Reorder flagged: 2
Spotcheck term: weezer
Songs returned: 5
API status: OK
```
