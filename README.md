# 🎧 Spotify Track Popularity Analysis using AWS

An end-to-end **Data Engineering Project** that analyzes Spotify music trends using scalable AWS services — **S3, Glue, Athena, and QuickSight**. This project transforms raw Spotify track data into actionable insights using cloud-native tools and a visual ETL pipeline.

---

## Objective

To uncover patterns in Spotify track popularity using real-world datasets by building a **data lake + ETL + analytics pipeline** on AWS.

---

##  Architecture

<img width="1024" height="1536" alt="AWS PIPELINE IMAGE" src="https://github.com/user-attachments/assets/2eeac0dc-6b23-4978-860e-65c40d4b5615" />

---

##  Dataset

- **Source:** [Spotify Dataset (2023) on Kaggle](https://www.kaggle.com/datasets/tonygordonjr/spotify-dataset-2023)
- Contains metadata for tracks, albums, artists, including:
  - Track popularity
  - Genre
  - Followers
  - Duration, tempo, key, mode

---

## Project Structure
spotify-aws-project/
│
├── README.md
├── glue_jobs/
│   └── etl_script.py               
├── data/
│   └── artists.csv
│   └── albums.csv
│   └── tracks.csv
├── sql_queries/
│   └── top_tracks.sql
├── screenshots/
│   └── architecture.png
│   └── quicksight_dashboard.png
└── .gitignore.

---

## Technologies used
Amazon S3 – Stores raw and transformed data.

AWS Glue – ETL pipeline using PySpark.

Amazon Athena – SQL-based querying on transformed data.

Amazon QuickSight – Dashboards for business insights.

PySpark – Data processing scripts inside Glue jobs.

SQL – Analytical querying with Athena.

---

## Key Insights
Top artists: Billie Eilish, Imagine Dragons, Drake

Popular genres: Pop, Hip-hop

QuickSight dashboards reveal:
Track popularity distribution,
Genre heatmaps,
Artist followers,
Album trends over time.

---

## Future Scope
Real-time data streaming using Amazon Kinesis

Sentiment analysis on lyrics

ML-based popularity prediction with Amazon SageMaker

