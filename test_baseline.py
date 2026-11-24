import time
from validator import is_payload_safe

def test_configuration(payload, validator_enabled):
    start_time = time.perf_counter()

    if validator_enabled:
        allowed = is_payload_safe(payload)
    else:
        allowed = True

    latency = time.perf_counter() - start_time

    return allowed, latency

from agent import load_attack_payloads

cases = load_attack_payloads()

for enabled in [False, True]:
    print("\nValidator enabled:", enabled)

    allowed_count = 0
    blocked_count = 0
    total_latency = 0

    for case in cases:
        allowed, latency = test_configuration(
            case["payload"], enabled
        )

        total_latency += latency

        if allowed:
            allowed_count += 1
        else:
            blocked_count += 1

        time.sleep(3)

    print("Total payloads:", len(cases))
    print("Allowed:", allowed_count)
    print("Blocked:", blocked_count)
    print("Blocking rate:", blocked_count / len(cases) * 100, "%")
    print("Average latency:", total_latency / len(cases), "seconds")