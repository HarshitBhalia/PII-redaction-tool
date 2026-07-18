"""Comprehensive diagnostic to find all gaps in PII detection."""
from pii_engine import detect_pii, get_fake_value, clear_mapping

clear_mapping()

TEST_CASES = [
    # ADDRESSES - multiple formats
    ("ADDRESS", "123 MG Road, Bengaluru, Karnataka 560001"),
    ("ADDRESS", "Plot No. 45, Sector 12, Noida, Uttar Pradesh - 201301"),
    ("ADDRESS", "Flat 3B, Sunshine Apartments, Andheri West, Mumbai 400058"),
    ("ADDRESS", "House No. 12, Gandhi Nagar, New Delhi - 110031"),
    ("ADDRESS", "Door No. 5/2, 3rd Cross, Jayanagar, Bangalore 560041"),
    ("ADDRESS", "C-14, Defence Colony, New Delhi - 110024"),
    ("ADDRESS", "B-204, Silver Oak Society, Thane, Maharashtra 400601"),
    ("ADDRESS", "Near City Hospital, Main Bazaar, Jaipur 302001"),
    ("ADDRESS", "P.O. Box 1234, Connaught Place, New Delhi"),
    # PERSONS
    ("PERSON", "Rashi Patil"),
    ("PERSON", "Rohan Dey"),
    ("PERSON", "Dr. Sanjay Mehta"),
    ("PERSON", "Mr. Amit Kumar Singh"),
    ("PERSON", "Mrs. Priya Sharma"),
    # EMAILS
    ("EMAIL", "rashhi.patil@gmail.com"),
    ("EMAIL", "rohan.dey@company.co.in"),
    ("EMAIL", "admin@techfirm.org"),
    # PHONES
    ("PHONE", "+91 9876543210"),
    ("PHONE", "9123456789"),
    ("PHONE", "022-28001234"),
    ("PHONE", "+91-80-45053237"),
    # ORGS
    ("ORG", "TechSolutions India Pvt Ltd"),
    ("ORG", "Reliance Industries Limited"),
    ("ORG", "HDFC Bank Ltd"),
    # PAN
    ("PAN", "ABCDE1234F"),
    ("PAN", "ZZZZZ9999Z"),
    # AADHAAR
    ("AADHAAR", "1234 5678 9012"),
    ("AADHAAR", "123456789012"),
    # CREDIT CARD
    ("CREDIT_CARD", "4111-1111-1111-1111"),
    ("CREDIT_CARD", "5500 0000 0000 0004"),
    # IP
    ("IP", "192.168.1.100"),
    ("IP", "10.0.0.1"),
    # DATES OF BIRTH
    ("DOB", "15/08/1990"),
    ("DOB", "March 22, 1985"),
    ("DOB", "01-01-1975"),
    # SSN
    ("SSN", "123-45-6789"),
    ("SSN", "987-65-4321"),
]

print("=" * 70)
print("COMPREHENSIVE PII DETECTION DIAGNOSTIC")
print("=" * 70)

hits = 0
misses = []

for pii_type, sample in TEST_CASES:
    findings = detect_pii(sample)
    if findings:
        hits += 1
        rep = get_fake_value(findings[0]['entity_type'], findings[0]['text'])
        detected_type = findings[0]['entity_type']
        print(f"  [OK]  [{pii_type:12s}] '{sample[:50]}' -> '{rep}' (as {detected_type})")
    else:
        misses.append((pii_type, sample))
        print(f"  [MISS] [{pii_type:12s}] '{sample[:50]}'")

print()
print(f"Results: {hits}/{len(TEST_CASES)} detected")
print(f"MISSED ({len(misses)}):")
for t, s in misses:
    print(f"  - [{t}] '{s}'")
