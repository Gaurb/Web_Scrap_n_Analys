# Web Scraper and Text Analyzer

## What the project does
This project is a web scraping and natural language processing tool designed to extract article texts from a given list of URLs and perform comprehensive text analysis. It computes various linguistic metrics, including sentiment scores (positive, negative, polarity, subjectivity), readability indices (Fog index), and structural word statistics (complex words, syllables, personal pronouns).

## Tech Stack
- **Python**: Core programming language.
- **Jupyter Notebook**: For interactive development and execution.
- **pandas**: Data manipulation, and reading/writing Excel files.
- **requests**: Fetching HTML content from URLs.
- **BeautifulSoup (bs4)**: Parsing HTML and extracting article titles and text.
- **NLTK (Natural Language Toolkit)**: Tokenization, stopword removal, and linguistic analysis.

## How to run it locally
1. **Prerequisites**: Ensure you have Python installed. Install the required libraries by running:
   ```bash
   pip install pandas requests beautifulsoup4 nltk openpyxl
   ```
2. **Download NLTK Data**: The analysis script requires the `punkt` tokenizer. It will automatically download on the first run, or you can manually download it via Python:
   ```python
   import nltk
   nltk.download('punkt')
   ```
3. **Data Extraction**: 
   - Open and execute `Data extraction.ipynb`.
   - This notebook reads the input URLs from `inp.xlsx`, scrapes the article title and content, and saves each extracted article as a text file inside an `Extracted Data/` directory. (Ensure this folder exists or is created by the script).
4. **Text Analysis**:
   - Open and execute `Analysis.ipynb`.
   - This notebook reads the extracted text files, processes them using custom `StopWords` and `MasterDictionary` files, and calculates all necessary metrics.
   - The final results are exported to `Output Data Structure.xlsx`.

## Key Design Decisions
- **Separation of Concerns**: The project is split into two distinct notebooks—one strictly for data extraction and another for analysis. This decoupled architecture allows for rerunning complex text analysis without needing to re-scrape the web pages, saving time and preventing rate-limiting.
- **Intermediate Data Storage**: Scraped articles are saved locally as individual text files (named by their `URL_ID`). This acts as a reliable cache and data backup, ensuring data integrity before the analysis phase begins.
- **Rule-based NLP Approach**: The text analysis relies on a deterministic, dictionary-based approach using predefined positive/negative word lists and custom stopword sets. This provides transparent, reproducible sentiment metrics without the computational overhead of large machine learning models.
