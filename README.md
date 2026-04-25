# 🎬 IMDb Movie Rating Scraper

## 📌 Project Description
This project is a Python-based web scraping tool that extracts movie data from IMDb's Top 250 Movies list using Selenium.

It collects important details such as movie rank, title, release year, and IMDb rating, and stores the data in a CSV file for further analysis.

---

## 🚀 Features
- Dynamic web scraping using Selenium
- Extracts Top 250 movies from IMDb
- Captures movie name, year, and rating
- Saves data into CSV format
- Handles JavaScript-loaded content
- Fully automated process

---

## 🛠️ Technologies Used
- Python
- Selenium
- Pandas
- WebDriver Manager
- Google Chrome

---

## 📂 Project Structure
MDb_Movie_Scraper/
│── imdb_scraper.py
│── imdb_top_250_movies.csv
│── README.md
│── sivimdb.docx


---

## ▶️ How to Run

1. Install required libraries:

pip install selenium pandas webdriver-manager


2. Run the script:

python imdb_scraper.py


---

## 📊 Output
- The program scrapes IMDb Top 250 movies
- Stores data in:

imdb_top_250_movies.csv


Sample output:

| Rank | Movie Name | Year | IMDb Rating |
|------|------------|------|-------------|
| 1 | The Shawshank Redemption | 1994 | 9.3 |
| 2 | The Godfather | 1972 | 9.2 |

---

## ⚠️ Limitations
- Depends on IMDb website structure
- Requires internet connection
- Selenium may be slower than API-based methods

---

## 🎯 Conclusion
This project demonstrates dynamic web scraping using Selenium and data processing using Pandas. It can be extended for movie recommendation systems, dashboards, and analytics.

---

## 👤 Author
Sivanya S