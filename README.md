# Wikipedia_Scraper

A project to retrieve and scrape data about countries and their historical leaders. This project combines API data retrieval and web scraping techniques, saving the collected data for future processing. It’s organized in a Jupyter Notebook (`.ipynb` file) with individual cells for each task, allowing you to follow the workflow step-by-step.

## Overview

This project guides you through:
1. **Creating a Self-Contained Development Environment**: Setting up an isolated environment for package management and project organization.
2. **Retrieving Data from an API**: Accessing data about countries and leaders from an API.
3. **Web Scraping for Additional Data**: Extracting information from Wikipedia, a website without a public API.
4. **Saving Output for Future Use**: Persisting the scraped data for later analysis or further processing.


## Getting Started.

### Practical Usage

In addition to the `.ipynb` file, the project includes a `.py` script that allows you to run the scraping and data retrieval functions without opening a Jupyter Notebook. This script (`wikipedia_scraper.py`) is ideal for quick, practical usage and can be executed directly from the command line.

**Note**: The `.ipynb` file provides an easier way to test and troubleshoot each stage of the project, as it allows you to run code in isolated cells, making debugging and iterative testing more manageable.

## Getting Started


Clone the repository and open the `.ipynb` file in Jupyter Notebook or JupyterLab, or use `wikipedia_scraper.py` for command-line execution. The notebook is designed to be modular, with each cell labeled and self-contained. This makes it easy to run each task independently, follow the workflow, and gain a deeper understanding of the process.

### Prerequisites

- **Python 3.x**: Ensure you have Python installed.

- **Jupyter Notebook**: You can install Jupyter Notebook with `pip install notebook`.
- **Additional Packages**: Install  necessary libraries (e.g., `requests`, `BeautifulSoup`, etc.) by following instructions in the setup section of the notebook.

- **Jupyter Notebook** (optional): Install Jupyter Notebook with `pip install notebook`.
- **Additional Packages**: Install necessary libraries (e.g., `requests`, `BeautifulSoup`, etc.) by following instructions in the setup section of the notebook or by running the setup commands below.


### Setup

1. **Create a Virtual Environment**: Set up a virtual environment to keep dependencies isolated:
   ```bash
   python -m venv wikipedia_scraper_env
   source wikipedia_scraper_env/bin/activate  # On Windows, use `wikipedia_scraper_env\Scripts\activate`
