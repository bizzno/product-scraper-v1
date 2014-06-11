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
Update 170 on 2014-05-06 21:24:28
Update 173 on 2014-05-06 11:35:16
Update 177 on 2014-05-08 06:12:18
Update 178 on 2014-05-08 17:03:24
Update 182 on 2014-05-08 12:21:08
Update 191 on 2014-05-09 13:39:21
Update 194 on 2014-05-09 10:15:38
Update 195 on 2014-05-09 09:52:24
Update 201 on 2014-05-15 15:06:19
Update 209 on 2014-05-16 21:28:36
Update 214 on 2014-05-17 03:09:35
Update 215 on 2014-05-17 02:37:47
Update 222 on 2014-05-21 13:38:15
Update 223 on 2014-05-21 21:36:37
Update 229 on 2014-05-21 14:03:50
Update 233 on 2014-05-22 01:25:10
Update 254 on 2014-05-27 11:57:15
Update 258 on 2014-05-29 10:39:34
Update 279 on 2014-06-03 17:02:22
Update 284 on 2014-06-06 04:40:36
Update 286 on 2014-06-09 10:49:19
Update 288 on 2014-06-10 17:56:23
Update 291 on 2014-06-10 08:32:53
Update 293 on 2014-06-10 11:34:51
Update 300 on 2014-06-11 16:12:34
