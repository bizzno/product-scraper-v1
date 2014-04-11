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
Update 33 on 2014-03-14 22:34:03
Update 35 on 2014-03-17 00:41:57
Update 38 on 2014-03-17 09:12:26
Update 39 on 2014-03-17 23:47:28
Update 51 on 2014-03-24 23:10:21
Update 52 on 2014-03-24 17:19:39
Update 56 on 2014-03-27 08:56:07
Update 62 on 2014-03-27 03:51:45
Update 63 on 2014-03-28 06:06:12
Update 64 on 2014-03-28 19:23:44
Update 68 on 2014-03-31 10:47:23
Update 75 on 2014-03-31 16:22:34
Update 77 on 2014-04-06 09:01:16
Update 89 on 2014-04-07 19:37:20
Update 92 on 2014-04-11 23:40:51
