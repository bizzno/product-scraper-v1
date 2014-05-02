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
Update 107 on 2014-04-16 21:54:40
Update 113 on 2014-04-16 22:40:29
Update 119 on 2014-04-20 07:30:26
Update 122 on 2014-04-21 05:24:06
Update 125 on 2014-04-21 11:57:54
Update 131 on 2014-04-21 02:35:52
Update 133 on 2014-04-22 05:01:43
Update 134 on 2014-04-22 18:51:36
Update 138 on 2014-04-22 04:11:24
Update 148 on 2014-04-23 18:34:55
Update 152 on 2014-05-02 07:41:58
Update 155 on 2014-05-02 08:03:54
