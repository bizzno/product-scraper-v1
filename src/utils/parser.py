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
