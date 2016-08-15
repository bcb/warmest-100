from glob import glob
import pandas

def get():
    dfs = [pandas.read_json(i) for i in glob('clean/*')]
    df = pandas.concat(dfs, ignore_index=True)
    # Convert artists column to tuple
    df['artists'] = df['artists'].apply(tuple)
    # Group duplicates
    g = df.groupby(['name']).size().reset_index(
        name='plays').sort_values('plays', ascending=False)
    # Add rank column
    g['rank'] = g['plays'].rank(ascending=False)
    return g
