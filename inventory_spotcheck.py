import requests

# Part A

# Step 1 — Student Key
student_key = input("Student key: ")
seed = sum(ord(c) for c in student_key)

# Step 4 — Threshold Logic (computed once from seed)
if seed % 3 == 0:
    threshold = 15
elif seed % 3 == 1:
    threshold = 12
else:
    threshold = 9

# Step 2 & 3 — SKU Entry Loop
total_skus = 0
reorder_count = 0

while True:
    sku = input("SKU: ").strip()

    if sku.upper() == "DONE":
        break

    if sku == "":
        print("SKU cannot be blank. Please try again.")
        continue

    # Step 3 — On-Hand Quantity with validation
    while True:
        try:
            on_hand = int(input("On hand: "))
            if on_hand < 0:
                print("Quantity must be >= 0. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Step 5 — Reorder Decision
    total_skus += 1
    if on_hand < threshold:
        reorder_count += 1

# Part B 

# Step 6 — Select API Term
spotcheck_term = "weezer" if seed % 2 == 0 else "drake"

# Step 7 & 8 & 9 — API Request with Exception Handling
songs_returned = "N/A"
api_status = "FAILED"

try:
    response = requests.get(
        "https://itunes.apple.com/search",
        params={"entity": "song", "limit": 5, "term": spotcheck_term},
        timeout=10
    )
    response.raise_for_status()

    data = response.json()
    results = data["results"]

    song_count = sum(1 for item in results if item.get("kind") == "song")
    songs_returned = song_count
    api_status = "OK"

except requests.exceptions.RequestException:
    api_status = "FAILED"
    songs_returned = "N/A"
except (KeyError, ValueError):
    api_status = "INVALID_RESPONSE"
    songs_returned = "N/A"

# Step 10 — Output
print(f"\nSeed: {seed}")
print(f"Threshold: {threshold}")
print(f"SKUs entered: {total_skus}")
print(f"Reorder flagged: {reorder_count}")
print(f"Spotcheck term: {spotcheck_term}")
print(f"Songs returned: {songs_returned}")
print(f"API status: {api_status}")