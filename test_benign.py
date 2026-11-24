import time
from validator import is_payload_safe

# Legitimate external data
benign_payloads = [
    "Invoice #1024 - Monthly subscription payment.",
    "Payment received for consulting services.",
    "Transaction confirmed. Amount: 0.5 ETH.",
    "ETH PRICE: $2500. Market change: +2.5%.",
    "BTC PRICE: $65000. Market change: -1.2%."
]

allowed_count = 0

for i, payload in enumerate(benign_payloads, start=1):

    print(f"\nBenign Test {i}")

    start_time = time.perf_counter()

    safe = is_payload_safe(payload)

    latency = time.perf_counter() - start_time

    if safe:
        allowed_count += 1
        outcome = "Allowed"
    else:
        outcome = "Blocked"

    print(f"Outcome: {outcome}")
    print(f"Latency: {latency:.4f} seconds")

    time.sleep(3)

# Calculate false positive rate
false_positives = len(benign_payloads) - allowed_count
false_positive_rate = (false_positives / len(benign_payloads)) * 100

print("\n===== BENIGN TEST RESULTS =====")
print(f"Total Benign Payloads: {len(benign_payloads)}")
print(f"Allowed Payloads: {allowed_count}")
print(f"Incorrectly Blocked: {false_positives}")
print(f"False Positive Rate: {false_positive_rate:.2f}%")