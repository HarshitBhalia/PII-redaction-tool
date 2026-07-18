from pii_engine import detect_pii, get_fake_value

test = 'Contact Rashi Patil at rashhi.patil@gmail.com or +91 9876543210. Her PAN is ABCDE1234F. IP: 192.168.1.100'
findings = detect_pii(test)
print(f'Found {len(findings)} PII entities:')
for f in findings:
    rep = get_fake_value(f['entity_type'], f['text'])
    print(f'  [{f["entity_type"]}] "{f["text"]}" -> "{rep}"')
