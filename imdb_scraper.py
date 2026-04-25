from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import re

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://www.imdb.com/chart/top/"
driver.get(url)

wait = WebDriverWait(driver, 20)

# Wait for page to load
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Scroll down to load all movies
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Now get all movie elements
movies = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")

print("Movies found:", len(movies))

movie_data = []
rank = 1

for movie in movies:
    try:
        full_title = movie.find_element(By.TAG_NAME, "h3").text
        title = re.sub(r"^\d+\.\s*", "", full_title)

        year = ""
        spans = movie.find_elements(By.TAG_NAME, "span")
        for span in spans:
            text = span.text.strip()
            if re.fullmatch(r"\d{4}", text):
                year = text
                break

        rating = movie.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--rating").text

        movie_data.append([rank, title, year, rating])
        rank += 1

    except:
        continue

driver.quit()

df = pd.DataFrame(movie_data, columns=["Rank", "Movie Name", "Year", "IMDb Rating"])
df.to_csv("imdb_top_250_movies.csv", index=False, encoding="utf-8")

print("✅ IMDb Top 250 Movies scraped successfully!")
print("📁 File saved as imdb_top_250_movies.csv")
