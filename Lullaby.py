import whois
import dns.resolver

def domain_info(target):
    print(f"\[+] Gathering WHOIS info for: {target}")
    try:
        w = whois.whois(target)
        print("Domain Name:", w.domain_name)
        print("Registrar:", w.regristrar)
        print("Creation Date:", w.creation_date)
        print("Expiration Date:", w.expiration_date)
        print("Name Servers:", w.name_servers)
    except Exception as e:
        print("WHOIS lookup failed:",e)

    print(f"\n[+] Gathering DNS records for: {target}")
    try:
        for record in ["A", "AAA", "MX", "NS", "TXT"]:
            try:
                answers = dns.resolver.resolve(target, record)
                print(f"{record} Records:")
                for rdata in answers:
                    print("   ", rdata.to_tex())
            except Exception:
                pass
    except Exception as e:
        print("DNS lookup failed:", e)

if __name__ == "__main__":
    target + input("Enter a domain (e.g., example.com)")
    domain_info(target)
