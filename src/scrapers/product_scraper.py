"""Product scraper for e-commerce sites"""
import requests
from bs4 import BeautifulSoup

class ProductScraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def scrape_products(self):
        """Scrape product listings"""
        products = []
        # TODO: Implement scraping logic
        return products

    def extract_price(self, element):
        """Extract price from element"""
        return 0.0
Update 5 on 2014-03-05 06:10:34
Update 13 on 2014-03-07 08:59:30
Update 21 on 2014-03-10 13:02:33
Update 25 on 2014-03-14 13:50:11
Update 34 on 2014-03-17 17:39:29
Update 36 on 2014-03-17 18:28:51
Update 46 on 2014-03-24 14:55:25
Update 48 on 2014-03-24 18:41:53
Update 49 on 2014-03-24 20:36:34
Update 50 on 2014-03-24 17:49:38
Update 53 on 2014-03-24 03:46:13
Update 67 on 2014-03-31 01:47:27
Update 78 on 2014-04-06 20:58:32
Update 81 on 2014-04-07 20:56:38
Update 82 on 2014-04-07 10:06:47
Update 101 on 2014-04-14 21:45:20
Update 105 on 2014-04-16 11:17:43
Update 109 on 2014-04-16 12:00:11
Update 110 on 2014-04-16 05:11:01
Update 115 on 2014-04-16 16:20:35
Update 121 on 2014-04-20 19:25:30
Update 123 on 2014-04-21 08:40:02
Update 127 on 2014-04-21 05:47:33
Update 132 on 2014-04-21 09:18:58
Update 145 on 2014-04-23 15:18:53
Update 146 on 2014-04-23 07:50:05
Update 153 on 2014-05-02 07:16:41
Update 158 on 2014-05-02 20:11:36
Update 159 on 2014-05-02 17:33:25
Update 164 on 2014-05-02 03:19:20
Update 166 on 2014-05-06 08:33:43
Update 174 on 2014-05-06 06:07:00
Update 175 on 2014-05-08 13:59:02
Update 179 on 2014-05-08 16:43:22
Update 185 on 2014-05-08 02:45:03
Update 200 on 2014-05-15 10:59:40
Update 205 on 2014-05-15 02:41:01
Update 206 on 2014-05-16 03:18:47
Update 207 on 2014-05-16 21:11:13
Update 212 on 2014-05-16 10:28:47
Update 221 on 2014-05-21 08:47:28
Update 224 on 2014-05-21 10:28:31
Update 226 on 2014-05-21 02:30:37
Update 232 on 2014-05-22 00:12:56
Update 237 on 2014-05-22 12:53:37
Update 238 on 2014-05-22 17:56:26
Update 240 on 2014-05-22 23:04:37
Update 243 on 2014-05-22 02:49:14
Update 244 on 2014-05-26 10:55:58
Update 248 on 2014-05-27 22:28:27
Update 250 on 2014-05-27 05:19:05
Update 253 on 2014-05-27 21:33:38
Update 259 on 2014-05-29 02:30:17
Update 270 on 2014-05-30 13:02:10
Update 271 on 2014-06-03 23:46:04
Update 272 on 2014-06-03 03:38:34
Update 277 on 2014-06-03 23:54:18
Update 283 on 2014-06-04 16:12:21
Update 294 on 2014-06-10 20:27:18
Update 295 on 2014-06-10 22:03:21
Update 297 on 2014-06-11 10:31:18
Update 313 on 2014-06-20 10:00:51
Update 316 on 2014-07-08 11:42:33
Update 321 on 2014-07-08 13:55:57
Update 332 on 2014-07-14 08:58:16
Update 334 on 2014-07-14 17:22:29
Update 339 on 2014-07-14 09:27:50
Update 340 on 2014-07-14 00:01:52
Update 344 on 2014-07-15 04:17:37
Update 346 on 2014-07-21 11:06:54
Update 349 on 2014-07-21 13:01:18
Update 351 on 2014-07-21 01:35:06
Update 356 on 2014-07-22 23:24:15
Update 357 on 2014-07-22 01:20:25
Update 358 on 2014-07-22 23:44:28
Update 359 on 2014-08-04 00:42:29
Update 362 on 2014-08-04 07:35:05
Update 371 on 2014-08-04 01:55:56
Update 374 on 2014-08-08 23:37:30
Update 380 on 2014-08-15 03:31:21
Update 382 on 2014-08-17 12:04:05
Update 393 on 2014-08-20 09:22:29
Update 397 on 2014-08-20 11:42:20
Update 402 on 2014-08-22 20:57:47
Update 404 on 2014-08-22 16:50:07
Update 407 on 2014-08-22 16:45:03
Update 412 on 2014-08-22 22:59:10
Update 413 on 2014-08-26 13:52:48
Update 414 on 2014-08-26 12:02:38
Update 424 on 2014-08-27 09:37:21
Update 430 on 2014-08-28 20:38:48
Update 436 on 2014-08-28 00:49:30
Update 447 on 2014-09-01 20:43:30
Update 449 on 2014-09-03 22:03:07
Update 454 on 2014-09-05 19:06:33
Update 463 on 2014-09-10 13:43:32
Update 466 on 2014-09-11 09:02:48
Update 470 on 2014-09-18 19:19:20
Update 471 on 2014-09-19 20:22:06
Update 473 on 2014-09-19 10:23:31
Update 479 on 2014-09-21 03:09:25
Update 485 on 2014-09-26 06:35:07
Update 494 on 2014-09-29 20:45:48
Update 500 on 2014-10-01 07:10:48
Update 501 on 2014-10-01 02:35:00
Update 503 on 2014-10-01 23:57:46
Update 512 on 2014-10-03 08:09:24
Update 522 on 2014-10-06 18:09:12
Update 527 on 2014-10-19 21:32:14
Update 531 on 2014-10-21 02:07:11
