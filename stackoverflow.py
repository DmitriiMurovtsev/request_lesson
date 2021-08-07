import requests
from datetime import datetime, timedelta

date = datetime.today() - timedelta(2)
url = (f'https://api.stackexchange.com/2.3/questions?fromdate={date.date()}'
       f'&order=desc&sort=activity&tagged=Python&site=stackoverflow')
r = requests.get(url)
for questions in r.json()['items']:
    print(f'{questions["title"]}: {questions["link"]}')
