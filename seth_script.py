import requests
from bs4 import BeautifulSoup

page_url = 'https://www.liverpool.ac.uk/careers/employment-fairs-and-events/'
aspx_url = 'https://careerhub.liv.ac.uk/rss/event.aspx?format=Javascript_2c3394&sso=true&hasPlaces=true&token=s0tZf4oIZ6kQDmlnwNeoqA2'

##page_html = urllib2.urlopen(page_url)
##
##soup = BeautifulSoup(page_html, 'html.parser')

url_get = requests.get(aspx_url)

soup = BeautifulSoup(url_get.content,'lxml')

soupstr = str(soup).replace('&gt;&lt;strong&gt','')

soupstr = soupstr.split('&lt;div class=')

soupstrNew = []
for l in soupstr:
    if l[:12] == "'ch-summary'":
        soupstrNew += [l]

output = []

for l in soupstrNew:
    string = l.replace("'ch-summary'&gt;",'')

    summary = string[:string.find("&lt")]
    string1 = string[string.find("<pubdate>")+9:]
    

    startTime = string1[:string1.find("</pubdate>")-1]
    string2 = string1[string1.find('.com.au/">')+10:]

    endTime = string2[:string2.find("</closingdate>")-4]
    string3 = string2[string2.find('com.au/">')+9:]

    string3 = string3[string3.find('com.au/">')+9:]
    string3 = string3[string3.find('com.au/">')+9:]

    venue = string3[:string3.find("</venue>")]
    try:
        print(string3)
        print()
        string4 = string3[string3.find("<title>")+7:]
        print(string4)
        title = string4[:string4.find("</title>")]
    except:
        title = "None"

    output += [[title,summary.replace('&amp;#8203;',''),startTime,endTime,venue]]

print(output)


##col = soup.find('div', class_="column_main")
##col_all = col.find_all('a')
##for link in col_all:
##   print(link.get('href'))