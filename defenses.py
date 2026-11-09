import time
from web3 import Web3

class SecurityBoundaryViolation(Exception):
    """Custom exception raised when a transaction fails deterministic security checks."""
    pass

# --- Security Configuration ---
MAX_TRANSFER_ETH = 1.0
RATE_LIMIT_TX_PER_MINUTE = 3

# This will be populated dynamically by agent.py once the mock accounts are generated
WHITELISTED_WALLETS = set()

# --- State Tracking ---
_transaction_timestamps = []

def validate_transaction(recipient: str, amount_eth: float) -> bool:
    """
    Validates a proposed transaction against deterministic security boundaries.
    Raises SecurityBoundaryViolation if any check fails, halting the AI before execution.
    """
    global _transaction_timestamps
    
    # 1. Address Normalization & Formatting
    if not Web3.is_address(recipient):
        raise SecurityBoundaryViolation(f"Invalid Ethereum address format: {recipient}")
    
    checksum_recipient = Web3.to_checksum_address(recipient)

    # 2. Access Control (Whitelist Check)
    if checksum_recipient not in WHITELISTED_WALLETS:
        raise SecurityBoundaryViolation(
            f"Access Denied: Destination wallet {checksum_recipient} is not whitelisted."
        )

    # 3. Transfer Cap Enforcement
    if amount_eth <= 0:
        raise SecurityBoundaryViolation("Transaction amount must be greater than 0 ETH.")
        
    if amount_eth > MAX_TRANSFER_ETH:
        raise SecurityBoundaryViolation(
            f"Limit Exceeded: {amount_eth} ETH exceeds the maximum allowed {MAX_TRANSFER_ETH} ETH."
        )

    # 4. Rate Limiting (Sliding Window)
    current_time = time.time()
    
    # Prune timestamps older than 60 seconds
    _transaction_timestamps = [t for t in _transaction_timestamps if current_time - t <= 60]

    if len(_transaction_timestamps) >= RATE_LIMIT_TX_PER_MINUTE:
        raise SecurityBoundaryViolation(
            "Rate Limit Exceeded: Maximum transactions per minute reached. Try again later."
        )

    # If all checks pass, record the transaction timestamp and approve
    _transaction_timestamps.append(current_time)
    return True