import re

sample_text = """
Emails: user@example.com, firstname.lastname@company.co.uk
URLs: https://www.example.com, https://subdomain.example.org/page
Phone Numbers: (123) 456-7890, 123-456-7890, 123.456.7890
Credit Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
Times: 14:30, 2:30 PM, 02:30 am
"""

patterns = {
    "Emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "URLs": r"https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[\w./]*)?",
    "Phone Numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "Credit Cards": r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
    "Times": r"\b(?:[01]?\d|2[0-3]):[0-5]\d\b|\b(?:1[0-2]|0?[1-9]):[0-5]\d\s?(?:AM|PM|am|pm)\b"
}

def extract_data(text, patterns):
    extracted_data = {}
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        extracted_data[key] = matches
    return extracted_data

results = extract_data(sample_text, patterns)
for category, matches in results.items():
    print(f"{category}: {matches}")
