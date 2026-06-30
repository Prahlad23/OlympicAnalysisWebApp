import pandas as pd

def preprocess():
    df = pd.read_csv('athlete_events.csv')
    region_df = pd.read_csv('noc_regions.csv')

    # filtering for summer olympics
    df =df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(region_df, how='left', on='NOC')
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df,pd.get_dummies(df['Medal'])],axis=1)
    return df