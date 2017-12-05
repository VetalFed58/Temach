import requests
from lxml.html.html5parser import fromstring
from lxml.html import html5parser

published_links = set()
with open('teams.csv') as f:
    for line in f:
        fields = line.split(',')
        published_links.add(fields[5].strip())
print(published_links)

with open('teams.csv','a') as f:
    fixtures = ''
    for year in [2017]:
        for month in range(1,13):
            print(year, month)
            url='http://www.bbc.com/sport/football/premier-league/scores-fixtures/%d-%02d' %(year, month)
            res = requests.get(url)
            
            html = fromstring(res.text)
            
            for e in html.cssselect('.sp-c-fixture__block-link'):
                link = 'http://www.bbc.com' + e.attrib['href']
                if link in published_links:
                    continue
                team1, team2 = e.cssselect('.qa-full-team-name')
                score = e.cssselect('.sp-c-fixture__number')
                live = e.cssselect('.sp-c-fixture__status--live')
                if live:
                    break
                if len(score)==2:
                    score1 = e.cssselect('.sp-c-fixture__number')[0]
                    score2 = e.cssselect('.sp-c-fixture__number')[1]
                    line = '%s, %s, %s, %s, %s, %s\n' %(team1.text, score1.text + ' - ' + score2.text, team2.text, year, month, link)
                    f.write(line)
                    print(line)
                    fixtures += line
                    requests.post('http://dmytrolutchyn.pythonanywhere.com/new_post/')
                    client =requests.session()
                    res = client.get('http://dmytrolutchyn.pythonanywhere.com/new_post/')
                    html = html5parser.fromstring(res.text)
                    csrffield = html.cssselect('[name="csrfmiddlewaretoken"]')[0]
                    res = client.post('http://dmytrolutchyn.pythonanywhere.com/new_post/', {
                        "csrfmiddlewaretoken": csrffield.attrib['value'],
                        "fixtures": fixtures
                    })
                    