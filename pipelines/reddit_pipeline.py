import pandas as pd

from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH


def reddit_pipeline(filename: str, subreddit: str, time_filter='day', limit=None):
    # connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    # extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    # transformation
    transformed_df = transform_data(post_df)
    # loading to csv
    load_data_to_csv(transformed_df, f'{OUTPUT_PATH}/{filename}.csv')
    print(f'Loading {filename}.csv to {OUTPUT_PATH} directory successfully')

# reddit_pipeline("reddit", "dataengineering", "day", 100)
