from bs4 import BeautifulSoup
import re
import pandas

def get():
    results = []
    with open('results.html') as f:
        for t in BeautifulSoup(f, 'html.parser').find_all('div', class_='hottest-countdown-track'):
            # Extract position, artist, title
            pos = t.find(class_='hottest-countdown-position').string
            title = t.find(class_='title').string
            artists = [t.find(class_='artist').string]
            # Sanitize (pull featured artists from title)
            matches = re.search(r' {Ft. ([^}]+)}', title)
            if (matches):
                artists += matches.group(1).split('/')
            title = re.sub(r' {Ft. ([^}]+)}', '', title)
            # Append to list of dicts
            results.append(
                {'rank': pos, 'name': title, 'artists': tuple(sorted(artists))})
    # Return as a DataFrame
    return pandas.DataFrame(results)
