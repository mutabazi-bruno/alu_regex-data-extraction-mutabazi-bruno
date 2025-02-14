import re

sample_text = '''
user@example.com
firstname.lastname@company.co.uk
https://www.example.com
https://subdomain.example.org/page
(123) 456-7890
123-456-7890
#example
#ThisIsAHashtag
$19.99
14:30
'''

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url_pattern = r'https?://[a-zA-Z0-9./-]+'
phone_pattern = r'(\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4})'
hashtag_pattern = r'#\w+'
currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

time_pattern = r'\b\d{1,2}:\d{2}(?:\s?[APMapm]{2})?\b'

emails = re.findall(email_pattern, sample_text)
urls = re.findall(url_pattern, sample_text)
phone_numbers = re.findall(phone_pattern, sample_text)
hashtags = re.findall(hashtag_pattern, sample_text)
currency_amounts = re.findall(currency_pattern, sample_text)
times = re.findall(time_pattern, sample_text)

print("Emails:", emails)
print("URLs:", urls)
print("Phone Numbers:", phone_numbers)
print("Hashtags:", hashtags)
print("Currency Amounts:", currency_amounts)
print("Times:", times)
