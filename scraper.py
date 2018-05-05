import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        tables = sp.find_all("table")[3]
        rows = tables.find_all("tr")
        with open("output.txt", "w") as f:
            for row in rows:
                for name in row.find_all("td", attrs={"class":"s14_24"}):
                    if name.get_text() is None:
                        continue
                    else:
                        print("\n" + name.get_text())
                        f.write(name.get_text() + "\n")

news = "http://www.shugiintv.go.jp/jp/index.php?ex=VL&u_day=20180502"
Scraper(news).scrape()
