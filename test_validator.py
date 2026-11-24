import time
from agent import load_attack_payloads, save_result
from validator import is_payload_safe

# Load all attack test cases
cases = load_attack_payloads()

blocked_count = 0

# Test each payload against the validator
for case in cases:

    print(f"\nTesting Case {case['id']}")
    print(f"Attack Type: {case['attack_type']}")

    # Start measuring latency
    start_time = time.perf_counter()

    safe = is_payload_safe(case["payload"])

    # Calculate latency
    latency = time.perf_counter() - start_time

    if safe:
        outcome = "Allowed"
    else:
        outcome = "Blocked"
        blocked_count += 1

    # Save the experimental result
    save_result(
        case["id"],
        case["attack_type"],
        outcome,
        round(latency, 4)
    )

    print(f"Outcome: {outcome}")
    print(f"Latency: {latency:.4f} seconds")

    time.sleep(3)

# Calculate blocking rate
blocking_rate = (blocked_count / len(cases)) * 100

print("\n===== VALIDATOR RESULTS =====")
print(f"Total Payloads: {len(cases)}")
print(f"Blocked Payloads: {blocked_count}")
print(f"Allowed Payloads: {len(cases) - blocked_count}")
print(f"Blocking Rate: {blocking_rate:.2f}%")