import twitter
import pandas as pd
import api_credentials

api = twitter.Api(**api_credentials.credentials)

def get_user_uri_df(screen_name = None):
    """Returns a Pandas dataframe of users connected to user_id as
       followers. Data includes all relevant columns for
       calculating URI (underrated index)."""

    user_records = []

    users = api.GetFollowers(screen_name=screen_name)

    for user in users:
        row = {}
        row['created_at'] = user.created_at
        row['followers_count'] = user.followers_count
        row['friends_count'] = user.friends_count
        row['id'] = user.id
        row['statuses_count'] = user.statuses_count
        row['verified'] = user.verified
        row['screen_name'] = user.screen_name
        row['name'] = user.name
        user_records.append(row)

    return_df = pd.DataFrame(user_records).drop_duplicates('id')
    return_df['screen_name'] = screen_name

    return return_df

def calculate_TURI_G_IF(user_obj):
    """Adds Twitter Underrated Index (TURI) for Twitter user
    as well as growth (G), influence of followers (IF)"""
    print(user_obj.screen_name)
    try:
        user_uri_df = get_user_uri_df(screen_name=user_obj.screen_name)
    except Exception as e:
        print(e)
        user_obj.TURI = None
        user_obj.G = None
        user_obj.IF = None
        return user_obj
    if user_obj.statuses_count == 0:
        user_obj.G = user_obj.followers_count
        user_obj.IF = user_uri_df['followers_count'].mean()
        user_obj.TURI = user_uri_df['followers_count'].mean()
        return user_obj
    user_obj.G = user_obj.followers_count / user_obj.statuses_count
    user_obj.IF = user_uri_df['followers_count'].mean()
    user_obj.TURI = user_uri_df['followers_count'].mean() / user_obj.statuses_count
    return user_obj

