# ============================================================
# PROJECT 2: NETFLIX DATA ANALYSIS
# Author: Devendar Reddy Gurram
# Tool: Python (Pandas, Matplotlib, Seaborn)
# Dataset: Netflix Titles 2015-2025 (100 titles)
# ============================================================

# ── STEP 1: IMPORT LIBRARIES ────────────────────────────────
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set a clean visual style for all charts
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.dpi'] = 120
plt.rcParams['font.family'] = 'DejaVu Sans'

print("Libraries loaded successfully!")
print("=" * 55)


# ── STEP 2: LOAD AND EXPLORE THE DATASET ────────────────────
df = pd.read_csv('netflix_data.csv')

print("\n📋 DATASET OVERVIEW")
print(f"Total titles in dataset : {len(df)}")
print(f"Columns                 : {list(df.columns)}")
print(f"Shape                   : {df.shape}")
print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values per column:")
print(df.isnull().sum())


# ── STEP 3: DATA CLEANING ───────────────────────────────────
# Convert release_year to integer
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

# Clean up date_added column
df['date_added'] = df['date_added'].str.strip()

# Fill missing directors with Unknown
df['director'] = df['director'].fillna('Unknown')

# Fill missing country with Unknown
df['country'] = df['country'].fillna('Unknown')

print("\n✅ Data cleaning complete!")
print(f"Dataset ready: {len(df)} rows, {len(df.columns)} columns")
print("=" * 55)


# ── ANALYSIS 1: MOVIES VS TV SHOWS ──────────────────────────
print("\n📊 ANALYSIS 1: Content Type Breakdown")

type_counts = df['type'].value_counts()
type_pct = df['type'].value_counts(normalize=True) * 100

for t, count in type_counts.items():
    print(f"  {t}: {count} titles ({type_pct[t]:.1f}%)")

# Chart
fig, ax = plt.subplots(figsize=(7, 5))
colors = ['#E50914', '#221F1F']
wedges, texts, autotexts = ax.pie(
    type_counts,
    labels=type_counts.index,
    autopct='%1.1f%%',
    colors=colors,
    startangle=90,
    textprops={'fontsize': 13}
)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

ax.set_title('Netflix Content: Movies vs TV Shows', fontsize=15, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('chart1_movies_vs_tvshows.png', bbox_inches='tight')
plt.show()
print("✅ Chart 1 saved!")


# ── ANALYSIS 2: TOP 10 GENRES ────────────────────────────────
print("\n📊 ANALYSIS 2: Top 10 Most Popular Genres")

genre_counts = df['genre'].value_counts().head(10)
print(genre_counts.to_string())

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(
    genre_counts.index[::-1],
    genre_counts.values[::-1],
    color=sns.color_palette("Reds_r", len(genre_counts))
)
for bar, val in zip(bars, genre_counts.values[::-1]):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            str(val), va='center', fontsize=11, fontweight='bold')

ax.set_xlabel('Number of Titles', fontsize=12)
ax.set_title('Top 10 Most Popular Genres on Netflix', fontsize=15, fontweight='bold')
ax.set_xlim(0, genre_counts.max() + 4)
plt.tight_layout()
plt.savefig('chart2_top_genres.png', bbox_inches='tight')
plt.show()
print("✅ Chart 2 saved!")


# ── ANALYSIS 3: CONTENT ADDED PER YEAR ──────────────────────
print("\n📊 ANALYSIS 3: How Many Titles Were Added Each Year?")

yearly = df['release_year'].value_counts().sort_index()
yearly = yearly[yearly.index >= 2015]
print(yearly.to_string())

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(yearly.index, yearly.values, color='#E50914', edgecolor='white', width=0.6)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Titles Added', fontsize=12)
ax.set_title('Netflix Content Added Per Year (2015–2025)', fontsize=15, fontweight='bold')
ax.xaxis.set_major_locator(mticker.MultipleLocator(1))
for i, (year, val) in enumerate(zip(yearly.index, yearly.values)):
    ax.text(year, val + 0.1, str(val), ha='center', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('chart3_content_per_year.png', bbox_inches='tight')
plt.show()
print("✅ Chart 3 saved!")


# ── ANALYSIS 4: TOP 10 COUNTRIES PRODUCING CONTENT ──────────
print("\n📊 ANALYSIS 4: Which Countries Produce the Most Netflix Content?")

country_counts = df['country'].value_counts().head(10)
print(country_counts.to_string())

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(
    country_counts.index[::-1],
    country_counts.values[::-1],
    color=sns.color_palette("Blues_r", len(country_counts))
)
for bar, val in zip(bars, country_counts.values[::-1]):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
            str(val), va='center', fontsize=11, fontweight='bold')

ax.set_xlabel('Number of Titles', fontsize=12)
ax.set_title('Top 10 Countries Producing Netflix Content', fontsize=15, fontweight='bold')
ax.set_xlim(0, country_counts.max() + 5)
plt.tight_layout()
plt.savefig('chart4_top_countries.png', bbox_inches='tight')
plt.show()
print("✅ Chart 4 saved!")


# ── ANALYSIS 5: CONTENT RATINGS BREAKDOWN ───────────────────
print("\n📊 ANALYSIS 5: Content Ratings Breakdown")

rating_counts = df['rating'].value_counts()
print(rating_counts.to_string())

fig, ax = plt.subplots(figsize=(10, 5))
colors_list = sns.color_palette("Set2", len(rating_counts))
ax.bar(rating_counts.index, rating_counts.values, color=colors_list, edgecolor='white')
ax.set_xlabel('Rating', fontsize=12)
ax.set_ylabel('Number of Titles', fontsize=12)
ax.set_title('Netflix Content Ratings Distribution', fontsize=15, fontweight='bold')
for i, val in enumerate(rating_counts.values):
    ax.text(i, val + 0.1, str(val), ha='center', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('chart5_ratings.png', bbox_inches='tight')
plt.show()
print("✅ Chart 5 saved!")


# ── ANALYSIS 6: MOVIES VS TV SHOWS BY GENRE ─────────────────
print("\n📊 ANALYSIS 6: Genre Split Between Movies and TV Shows")

genre_type = df.groupby(['genre', 'type']).size().unstack(fill_value=0)
genre_type = genre_type.sort_values(
    by=genre_type.columns.tolist(), ascending=False
).head(10)
print(genre_type.to_string())

fig, ax = plt.subplots(figsize=(12, 6))
genre_type.plot(
    kind='bar',
    ax=ax,
    color=['#E50914', '#221F1F'],
    edgecolor='white',
    width=0.7
)
ax.set_xlabel('Genre', fontsize=12)
ax.set_ylabel('Number of Titles', fontsize=12)
ax.set_title('Movies vs TV Shows by Genre', fontsize=15, fontweight='bold')
ax.legend(title='Content Type', fontsize=11)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('chart6_genre_by_type.png', bbox_inches='tight')
plt.show()
print("✅ Chart 6 saved!")


# ── ANALYSIS 7: KOREAN CONTENT GROWTH ───────────────────────
print("\n📊 ANALYSIS 7: Rise of Korean Content on Netflix")

korean = df[df['country'] == 'South Korea']
korean_by_year = korean['release_year'].value_counts().sort_index()
print(f"Total Korean titles: {len(korean)}")
print(korean_by_year.to_string())

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    korean_by_year.index,
    korean_by_year.values,
    marker='o', color='#E50914',
    linewidth=2.5, markersize=8
)
ax.fill_between(korean_by_year.index, korean_by_year.values, alpha=0.15, color='#E50914')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Korean Titles', fontsize=12)
ax.set_title('Rise of Korean Content on Netflix', fontsize=15, fontweight='bold')
for x, y in zip(korean_by_year.index, korean_by_year.values):
    ax.annotate(str(y), (x, y), textcoords="offset points",
                xytext=(0, 10), ha='center', fontsize=10, fontweight='bold')
plt.tight_layout()
plt.savefig('chart7_korean_content.png', bbox_inches='tight')
plt.show()
print("✅ Chart 7 saved!")


# ── FINAL SUMMARY ────────────────────────────────────────────
print("\n" + "=" * 55)
print("📋 EXECUTIVE SUMMARY — KEY FINDINGS")
print("=" * 55)

movies = df[df['type'] == 'Movie']
shows = df[df['type'] == 'TV Show']
top_genre = df['genre'].value_counts().index[0]
top_country = df['country'].value_counts().index[0]
top_rating = df['rating'].value_counts().index[0]
peak_year = df['release_year'].value_counts().idxmax()

print(f"""
1. CONTENT MIX
   Netflix has {len(movies)} Movies and {len(shows)} TV Shows in this dataset.
   Movies make up {len(movies)/len(df)*100:.1f}% of total content.

2. TOP GENRE
   The most common genre is {top_genre}, 
   appearing in {df['genre'].value_counts().iloc[0]} titles.

3. TOP PRODUCING COUNTRY
   {top_country} produces the most Netflix content 
   with {df['country'].value_counts().iloc[0]} titles.

4. MOST COMMON RATING
   {top_rating} is the most frequent content rating,
   showing Netflix heavily targets mature audiences.

5. PEAK CONTENT YEAR
   {peak_year} had the highest number of titles released,
   with {df['release_year'].value_counts().max()} new additions.

6. KOREAN CONTENT
   South Korea has {len(korean)} titles, proving 
   K-dramas and Korean films are a major Netflix growth area.

7. BUSINESS INSIGHT
   Netflix is investing more in international content 
   (Korea, UK, Germany, Spain) alongside US productions,
   showing a clear global expansion strategy.
""")

print("=" * 55)
print("✅ Project 2 Complete! All 7 charts saved.")
print("Upload the .py file and all chart images to GitHub!")
print("=" * 55)
