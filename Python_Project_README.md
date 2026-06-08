# Netflix Data Analysis — Python Project

**Author:** Devendar Reddy Gurram  
**Tools:** Python, Pandas, Matplotlib, Seaborn  
**Dataset:** Netflix Titles 2015–2025 (100 titles)

---

## About This Project

I analyzed a Netflix titles dataset using Python to understand content trends, genre popularity, country contributions, and how Netflix has grown its library over the years.

This is the kind of exploratory data analysis a Data Analyst does at the start of any project — understanding the data, cleaning it, and pulling out insights that actually mean something to the business.

---

## Business Questions Answered

| # | Question | Finding |
|---|---|---|
| 1 | What is the split between Movies and TV Shows? | Movies make up ~60% of content |
| 2 | Which genres are most popular? | Drama, Crime, and Action lead |
| 3 | How has content grown year by year? | Significant growth from 2019–2022 |
| 4 | Which countries produce the most content? | USA leads, followed by UK and South Korea |
| 5 | What ratings dominate the platform? | TV-MA dominates — Netflix targets adults |
| 6 | How does genre differ between Movies and TV Shows? | Crime is more common in TV, Action in Movies |
| 7 | Is Korean content really growing? | Yes — South Korea titles grew significantly after 2021 |

---

## Key Findings

- Netflix content is majority Movies (~60%) but TV Shows drive more engagement
- Drama, Crime, and Action are the top 3 genres across the platform
- The United States produces the most content but South Korea, UK, Germany, and Spain are growing fast
- TV-MA is the most common rating — Netflix is clearly targeting adult audiences
- Korean content exploded after Squid Game in 2021, showing how one hit can shift a platform's entire content strategy
- 2022 was the peak year for new content additions in this dataset

---

## Charts Generated

| Chart | Description |
|---|---|
| chart1_movies_vs_tvshows.png | Pie chart — Movies vs TV Shows |
| chart2_top_genres.png | Horizontal bar — Top 10 genres |
| chart3_content_per_year.png | Bar chart — Content added per year |
| chart4_top_countries.png | Horizontal bar — Top 10 producing countries |
| chart5_ratings.png | Bar chart — Ratings distribution |
| chart6_genre_by_type.png | Grouped bar — Genre split by content type |
| chart7_korean_content.png | Line chart — Rise of Korean content |

---

## How to Run This Project

**Step 1 — Install required libraries**
```
pip install pandas matplotlib seaborn
```

**Step 2 — Make sure both files are in the same folder**
```
netflix_analysis.py
netflix_data.csv
```

**Step 3 — Run the script**
```
python netflix_analysis.py
```

All 7 charts will be saved automatically as PNG files in the same folder.

---

## Files in This Repository

| File | Description |
|---|---|
| `netflix_data.csv` | Dataset — 100 Netflix titles from 2015 to 2025 |
| `netflix_analysis.py` | Full Python analysis script with 7 analyses |
| `README.md` | This file |

---

## Skills Demonstrated

- Data loading and exploration with Pandas
- Data cleaning — handling missing values and formatting
- Exploratory Data Analysis (EDA)
- Data visualization with Matplotlib and Seaborn
- Business insight generation from raw data
- Clear communication of findings through charts and summaries

---

## Connect With Me

LinkedIn: linkedin.com/in/devendarreddy-gurram-380179252  
Email: devendarreddygurram@gmail.com  
GitHub: github.com/devendarreddygurram-cell
