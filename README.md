# Product Scraper

Web scraper for extracting product information from e-commerce websites.

## Features

- Multi-site scraping support
- Product data extraction (name, price, description, images)
- Pagination handling
- Rate limiting and request throttling
- Data export to CSV/JSON
- Proxy support for distributed scraping
- Error handling and retry logic

## Structure

```
src/
├── scrapers/     - Site-specific scraper implementations
├── parsers/      - HTML parsing and data extraction
├── utils/        - Storage, export, and helper utilities
└── config/       - Configuration and site definitions
```

## Installation

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run a scraper for a specific site:
```bash
python main.py --site example-store --output products.json
```

Python API:
```python
from src.scrapers import ProductScraper

scraper = ProductScraper('https://example.com')
products = scraper.scrape_products()

for product in products:
    print(f"{product['name']}: ${product['price']}")
```

## Requirements

- Python 3.6 or higher
- BeautifulSoup4
- requests
- lxml

## License

MIT
