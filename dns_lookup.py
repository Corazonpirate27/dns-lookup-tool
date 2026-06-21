import dns.resolver
import sys
import whois

if len(sys.argv) !=2:
     print("Usage: python3 dns_lookup.py <domain>")
     sys.exit(1)

domain = sys.argv[1]

try:
    answer = dns.resolver.resolve(domain, "A")
    for answer in answer:
        print(domain, "->", answer.address)
except dns.resolver.NXDOMAIN:
    print(f"Error: {domain} does not exist.")

try:
    mx_answers = dns.resolver.resolve(domain, "MX")
    for mx in mx_answers:
        print(domain, "MX ->", mx.exchange)
except dns.resolver.NXDOMAIN:
     print(f"Error: {domain} does not exist.")
except dns.resolver.NoAnswer:
     print(f"{domain} has not MX record.")

try:
     ns_answers = dns.resolver.resolve(domain, "NS")
     for ns in ns_answers:
        print(domain, "NS->", ns.target)
except dns.resolver.NXDOMAIN:
     print(f"Error: {domain} does not exist.")
except dns.resolver.NoAnswer:
     print(f"Error: {domain} has not NS record.")

try:
     txt_answers = dns.resolver.resolve(domain, "TXT")
     for txt in txt_answers:
        print(domain, "TXT->", txt)
except dns.resolver.NXDOMAIN:
        print(f"Error: {domain} does not exist.")
except dns.resolver.NoAnswer:
        print(f"{domain} has not TXT record.")

try:
     rev_answers = dns.resolver.resolve_address(answer.address)
     for rev in rev_answers:
         print(domain, "Reverse DNS ->", rev.target)
except dns.exception.DNSException:
       print(f"No reverse DNS found for {domain}'s IP.")

try:
     w = whois.whois(domain)
     print(domain, "Registrar ->", w.registrar)
     print(domain, "Created ->", w.creation_date)
     print(domain, "Expires ->", w.expiration_date)
except Exception as e:
     print(f"WHOIS lookup failed for {domain}: {e}") 
