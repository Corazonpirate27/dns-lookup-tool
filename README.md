# DNS Lookup Tool

A Python command-line tool for DNS reconnaissance. Looks up A, MX, NS, and TXT records, performs reverse DNS lookups, and pulls WHOIS registration data for any domain.

## Features

- A record lookup (domain to IP)
- MX record lookup (mail servers)
- NS record lookup (nameservers)
- TXT record lookup
- Reverse DNS lookup (IP to domain)
- WHOIS lookup (registrar, creation date, expiration date)
- Error handling for invalid domains and missing input

## Installation

```bash
pip install dnspython python-whois
```

## Usage

```bash
python3 dns_lookup.py <domain>
```

Example:

```bash
python3 dns_lookup.py google.com
``
