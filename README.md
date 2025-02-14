 Regex Data Extraction Project

## Project Overview
This project demonstrates the use of Python's `re` module to extract various types of data from a given text input using regular expressions. The script processes a sample text to find and display occurrences of the following data types:

1. **Email Addresses** (including plus signs and various domain formats)
2. **URLs**
3. **Phone Numbers** (with or without country codes)
4. **Hashtags**
5. **Currency Amounts** (with commas and decimals)
6. **Times** (both 12-hour and 24-hour formats)

## How It Works
The Python script applies specific regular expression patterns to identify and extract these data types from a multi-line string.

## Regular Expressions Used
- **Email Addresses:** `r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'`
- **URLs:** `r'https?://[a-zA-Z0-9./-]+'`
- **Phone Numbers:** `r'(\+?\d{1,2}[ -])?(\(\d{3}\) \d{3}-\d{4}|\d{3}[.-]\d{3}[.-]\d{4})'`
- **Hashtags:** `r'#\w+'`
- **Currency Amounts:** `r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'`
- **Times:** `r'\b\d{1,2}:\d{2}(?:\s?[APMapm]{2})?\b'`

## Running the Script
1. Make sure you have Python installed.
2. You can download it from the website or using microsoft store in windows
3. I used python 3.11 
4. Save the Python script as `regex_data_extraction.py`.
5. Open a terminal in the script's directory.
6. Run the script using:
    ```bash
    python regex_data_extraction.py
    ```

## This should be the Output
```
Emails: ['user@example.com', 'firstname.lastname@company.co.uk']
URLs: ['https://www.example.com', 'https://subdomain.example.org/page']
Phone Numbers: ['(123) 456-7890', '123-456-7890', '123.456.7890']
Credit Cards: ['1234 5678 9012 3456', '1234-5678-9012-3456']
Times: ['14:30', '2:30', '02:30']
```

## License
This project is open-source and free to use for educational and professional purposes.

thank you !!!!
