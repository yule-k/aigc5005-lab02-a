# Lab 02: Aggregation Records - TV shows
This program downloads TV show records from the TVMaze public API and summarizes the data. It counts shows by genre, calculates the average rating by language, and counts how many shows premiered in each decade.
## Data source
The program uses the TVMaze public API:
https://api.tvmaze.com/shows?page=0
The API returns roughly 240 TV show records.
## Setup
Create and activate a Conda environment:

```bash
conda create -n aigc5005_lab02 python=3.13.15
conda activate aigc5005_lab02
pip install -r requirements.txt

## Run
lab02_tvshows.py
## Example output
A short excerpt of summary.json, and what it tells you.
This output shows how many records were processed and provides three summaries of the dataset: show counts by genre, average ratings by language, and show counts by premiere decade.
## Data quirks
- Some TV shows belong to more than one genre, so the program uses a nested loop to count every genre listed for each show.
- Some shows do not have an average rating. The program skips those records when calculating the average rating by language.
- Some shows may have missing premiere dates. The program provides skip those records using continue.
## Design choices
The program uses a list, dictionary, and tuple.
- List: The API returns the TV show records as a list, which is useful for looping through each show one at a time.
- Dictionary: Dictionaries are used to group and count data. The genre, language, or decade works as the key, while the aggregated result is stored as the value.
- Tuple: A tuple is used in the language rating calculation to store the rating sum and show count together as (rating_sum, show_count).
- Dictionary comprehension: A dictionary comprehension is used to convert the collected rating totals and counts into average ratings by language.
## Known limitations
Although this program analyzed only the records from the first page for the assignment, it could be developed into an analysis tool that utilizes the full dataset and data visualization to boost TVmaze's conversion rates.