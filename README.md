# Simple Email Scraper

If you have a long list with domains, you put this list on `domains.txt`, and this script save all emails on other archive called `emails.txt`.

## Requirements

Python 3

`pip install -r requirements.txt`

## How to use?

1. You copy your domain list on `domains.txt`, domain por line, example:

```
domain.com
domain.com/contact
domain-3.com
domain-3.com/contact
...
```

2. Run script with `python extract_emails.py`.

3. Select option 1 for run script.

4. When the script finished, you can view all result on `emails.txt`.

## Thanks

- Thanks to **Oleh Kopyl**, report problem with request in some websites and duplicate emails.