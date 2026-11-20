# Creating Cohorts of Songs Using Spotify Data

**Machine Learning — Course-End Project 2**
**Dataset:** Rolling Stones tracks from Spotify

## Project objective

Use exploratory data analysis (EDA) and unsupervised machine learning to group recordings with similar audio characteristics. Examine song popularity and album recommendations, evaluate dimensionality reduction, and interpret the resulting cohorts.

The analysis is based on the supplied Rolling Stones Spotify dataset. It is an exploratory content-based segmentation project, **not** a personalized recommendation system trained on listener behavior.

## Repository layout

This project lives inside the existing `Python_Course_End_Projects` repository:

```text
Python_Course_End_Projects/
├── .venv/                            # Existing repo-level environment (not committed)
└── machine_learning/
    └── spotify_song_clustering/
        ├── data/
        │   ├── raw/
        │   │   └── rolling_stones_spotify.csv
        │   └── processed/
        │       └── spotify_clustered_songs.csv
        ├── notebooks/
        │   └── Spotify_Song_Clustering.ipynb
        ├── references/               # Supplied assignment and data dictionary
        ├── reports/
        │   └── figures/              # Save exported charts here
        ├── src/                       # Optional reusable code
        ├── README.md
        └── requirements.txt
```

## Data inspection and preparation

- **1,610 track records**, **18 original columns**.
- No missing values, exact duplicate rows, or repeated Spotify track IDs were found.
- Removed the redundant `Unnamed: 0` saved-index column.
- Converted `release_date` to datetime and derived `release_year` (listed album release years span **1964–2022**).
- Validated expected numerical ranges and examined outliers with boxplots and the IQR method.
- Retained plausible outliers, including extended live performances, for the initial clustering analysis.

A unique Spotify track ID does not guarantee a unique musical composition: live performances, remasters, and album editions can contain related versions of a song.

## Exploratory data analysis

The analysis examines popularity, albums, numerical distributions, audio-feature correlations, and differences across listed album release years.

**Popularity threshold:** the 90th percentile of the dataset, a Spotify popularity score of **36 or higher**, selects **176 recordings (10.93%)**. This is a dataset-relative threshold, not an official Spotify definition of popularity.

**Album recommendations by number of qualifying tracks:**

| Album | Qualifying tracks | Notes |
|---|---:|---|
| Exile On Main Street (2010 Re-Mastered) | 18 | Most qualifying tracks; 18 of 18 tracks qualify |
| Sticky Fingers (Remastered) | 10 | Tied for second by count; highest average popularity (53.30) among the albums tied at 10 |

The other albums tied at ten qualifying tracks include *Some Girls*, *Tattoo You (2009 Re-Mastered)*, and *Beggars Banquet (50th Anniversary Edition)*. Album size and repeat editions limit the interpretation of simple counts.

## Machine learning methodology

1. Selected ten audio features: `acousticness`, `danceability`, `energy`, `instrumentalness`, `liveness`, `loudness`, `speechiness`, `tempo`, `valence`, and `duration_ms`.
2. Excluded Spotify IDs, track titles, album names, release metadata, and popularity from the clustering feature matrix.
3. Standardized the ten numerical features with `StandardScaler`.
4. Applied Principal Component Analysis (PCA): **seven components retain 90.21%** of standardized feature variance.
5. Evaluated K-Means cluster counts from **2 through 10** using the elbow method and silhouette scores on the ten-feature and seven-component representations.
6. Chose **K = 2 with seven PCA components** as the candidate final configuration, then profiled clusters using original audio features and checked titles containing the word “Live.”

## Results from the local notebook

The numbers below are from `notebooks/Spotify_Song_Clustering.ipynb`, using `KMeans(n_clusters=2, random_state=42, n_init=10)` with the seven PCA components.

| Metric | Result |
|---|---:|
| Tracks assigned | 1,610 |
| Original-feature silhouette score at K = 2 | Approximately 0.202 |
| PCA-feature silhouette score at K = 2 | **0.2213** |
| Cluster 0 | **901 tracks (55.96%)** |
| Cluster 1 | **709 tracks (44.04%)** |

| Feature (cluster mean) | Cluster 0 | Cluster 1 |
|---|---:|---:|
| Energy | 0.694 | 0.917 |
| Danceability | 0.544 | 0.373 |
| Liveness | 0.261 | 0.785 |
| Valence | 0.662 | 0.481 |
| Tempo (BPM) | 118.980 | 135.107 |
| Loudness (dB) | -8.225 | -5.379 |
| Popularity (not used to train model) | 22.584 | 18.506 |
| Titles containing “Live” | 116 (12.87%) | 597 (84.20%) |

**Cluster 0 — More danceable, lower-liveness recordings:** Relatively greater danceability and valence, lower energy and liveness. Representative centroid-near songs include versions of *Who's Been Sleeping Here?* and *Crazy Mama*.

**Cluster 1 — High-energy live-style recordings:** Higher energy, liveness, loudness and tempo. Representative tracks include live versions of *Let It Bleed*, *Street Fighting Man*, *Start Me Up*, and *Dead Flowers*.

Clusters are descriptive groupings, not official genres or ratings. The relatively low silhouette score indicates **modest separation and some overlap**.

## Run the analysis locally

From a PowerShell terminal at the **`Python_Course_End_Projects` repository root**:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r machine_learning\spotify_song_clustering\requirements.txt
```

Open `machine_learning/spotify_song_clustering/notebooks/Spotify_Song_Clustering.ipynb` in VS Code, select the repository `.venv` kernel, then choose **Restart → Run All**. The notebook should read the CSV from `data/raw/` and regenerate its analysis outputs. The existing `.venv` is reused; there is no need to create another environment inside this project.

## Outputs

- **Notebook:** `notebooks/Spotify_Song_Clustering.ipynb`
- **Raw dataset:** `data/raw/rolling_stones_spotify.csv`
- **Clustered dataset:** `data/processed/spotify_clustered_songs.csv` (1,610 rows, 21 columns, based on the latest local export)
- **Figures:** `reports/figures/` is the intended folder for charts; images must be explicitly saved before they are claimed as exported artifacts.

## Limitations and future work

- The dataset represents only one artist; clusters may not generalize to other artists or genres.
- Separate Spotify IDs can refer to related versions of the same composition, which may overrepresent certain songs or editions.
- A title containing “Live” is an imperfect proxy for whether a recording is live.
- Album release dates include reissues and live releases, so they should not be interpreted as the date a song was first recorded.
- PCA preserves variance, not necessarily the information most useful for clustering.
- Scores in different feature spaces are not directly comparable as definitive model-quality measures; the cluster interpretation also matters.
- Future work could compare alternative clustering methods, evaluate stability, de-duplicate near-identical recordings where appropriate, and incorporate listener feedback for personalized recommendations.

## Conclusion

The analysis demonstrates that Spotify audio characteristics can be used to form interpretable cohorts of Rolling Stones recordings. The selected candidate model broadly distinguishes higher-energy, live-style tracks from more danceable, lower-liveness tracks. The results are exploratory and could inform future content-based recommendation experiments.
