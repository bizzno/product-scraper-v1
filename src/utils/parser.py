"""HTML parsing utilities"""
from bs4 import BeautifulSoup

def parse_html(html_content):
    """Parse HTML content"""
    return BeautifulSoup(html_content, 'html.parser')

def extract_text(element):
    """Extract text from element"""
    return element.get_text(strip=True)
Update 3 on 2014-03-05 21:14:52
Update 8 on 2014-03-05 18:54:34
Update 17 on 2014-03-10 09:43:27
Update 23 on 2014-03-10 03:16:28
Update 24 on 2014-03-14 07:13:48
Update 26 on 2014-03-14 21:32:39
