# Agentic Theft: Exploiting and Hardening Autonomous Financial Agents Against Indirect Prompt Injections

## Project Overview

This project investigates indirect prompt injection vulnerabilities in autonomous financial agents operating within decentralized finance (DeFi) environments.

The system implements an AI-powered financial agent capable of executing cryptocurrency transactions within a simulated Ethereum blockchain. Two attack categories are evaluated:

- Transaction Memo Poisoning
- Oracle Data Poisoning

A layered security architecture is implemented to prevent unauthorized financial operations while maintaining legitimate agent functionality.

## Security Mechanisms

- **Wallet Whitelisting:** Restricts cryptocurrency transfers to approved wallet addresses.
- **Transaction Limits:** Restricts individual transactions to a maximum of 1 ETH.
- **Secondary AI Validator:** Classifies external data as safe or malicious.
- **Fail-Closed Mechanism:** Blocks external data when validation fails or an unexpected response occurs.

## Technologies Used

- Python 3.12
- Gemini 3.5 Flash-Lite
- Google Generative AI
- Web3.py
- EthereumTester
- Py-EVM
- Python-dotenv
- JSON
- CSV

## Project Structure

| File | Description |
|---|---|
| `agent.py` | Autonomous financial agent and simulated blockchain environment. |
| `defenses.py` | Wallet whitelisting and transaction limit enforcement. |
| `validator.py` | Secondary AI validator for external data. |
| `attack_payloads.json` | Dataset containing 15 malicious payloads. |
| `test_validator.py` | Malicious payload detection testing. |
| `test_benign.py` | Benign payload and false positive testing. |
| `test_asr.py` | End-to-end attack testing and blockchain verification. |
| `test_baseline.py` | Comparison of enabled and disabled validator configurations. |
| `experimental_results.csv` | Recorded malicious payload evaluation results. |
| `requirements.txt` | Required Python dependencies. |
| `.gitignore` | Excludes sensitive credentials and unnecessary files. |

## Installation and Setup

### 1. Prerequisites

- Python 3.12
- Gemini API key
- Git or a downloaded copy of the repository

### 2. Clone the Repository

```bash
git clone -b Version2 https://github.com/Fasepulveda/CompSecurityDeFi-AgenticAI.git
cd CompSecurityDeFi-AgenticAI
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

For Linux or macOS:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the API Key

Create a file named `.env` in the project directory.

Add the following line and replace the placeholder with your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

The `.env` file must not be uploaded to GitHub or shared publicly.

## Running the Project

Run the autonomous financial agent and preliminary security tests:

```bash
python agent.py
```

## Running the Experiments

### Malicious Payload Evaluation

Evaluates eight transaction memo poisoning payloads and seven oracle data poisoning payloads.

```bash
python test_validator.py
```

### Benign Payload Evaluation

Evaluates five legitimate payloads to measure the false positive rate.

```bash
python test_benign.py
```

### End-to-End Attack Evaluation

Evaluates a transaction memo poisoning scenario and compares blockchain state before and after the attack attempt.

```bash
python test_asr.py
```

### Baseline Comparison

Compares payload blocking rates and processing latency with the secondary validator enabled and disabled.

```bash
python test_baseline.py
```

## Experimental Results

| Metric | Result |
|---|---:|
| Malicious payloads evaluated | 15 |
| Benign payloads evaluated | 5 |
| Detection rate | 100% |
| False positive rate | 0% |
| False negative rate | 0% |
| Classification accuracy | 100% |
| Average malicious payload validation latency | 0.6339 s |
| Average benign payload validation latency | 0.6140 s |
| Observed end-to-end Attack Success Rate | 0% (0/1) |
| End-to-end execution latency | 1.7188 s |

### Baseline Comparison

| Metric | Validator Disabled | Validator Enabled |
|---|---:|---:|
| Malicious payloads tested | 15 | 15 |
| Payloads allowed | 15 | 0 |
| Payloads blocked | 0 | 15 |
| Blocking rate | 0% | 100% |
| Average latency | 0.000000947 s | 4.4497 s |

The enabled baseline experiment included two API timeouts and one unexpected classification response. All three payloads were successfully blocked through the fail-closed mechanism.

## Experimental Limitations

- The evaluation was limited to 15 malicious and five benign payloads.
- Oracle data poisoning was evaluated independently through the secondary validator.
- End-to-end blockchain verification was limited to one defended transaction memo poisoning scenario.
- The baseline comparison evaluated payload filtering rather than end-to-end attack success.
- External AI services may introduce variable latency and API errors.
- All blockchain experiments were conducted in a simulated environment.

## Ethical Considerations

This project was developed for academic and cybersecurity research purposes. All experiments were conducted within an isolated Ethereum testing environment. No real cryptocurrency, production blockchain networks, or unauthorized external systems were used.

## Team Members

- Fernando Sepulveda
- Nallely Martinez

## Academic Information

- **University:** University of Texas at El Paso
- **Course:** CS 5352
- **Semester:** Fall 2026