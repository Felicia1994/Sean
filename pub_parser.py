import re

class PubParser(object):
    def __init__(self, pub):
        self._title = pub.find('h2', recursive=False).text
        self._info = pub.find('table').find('tbody')
        self._authors = []
        self._abstract = ""
        self._year = ""
        self._url = ""
        self._volume = ""
        self._pages = ""
        self._journal = ""
        self._has_doi = False
        self._doi = ""
        self._issue = ""
        self._journal_abbr = ""
        for item in self._info.find_all('tr', recursive=False):
            if item.find("th").text=="Author":
                self._authors.append(item.find("td").text)
            elif item.find("th").text=="Abstract":
                self._abstract = item.find("td").text
            elif item.find("th").text=="Date":
                date = item.find("td").text
                date = re.split(' |/|-', date)
                for x in date:
                    if len(x)==4 and x.isdigit():
                        self._year = x
            elif item.find("th").text=="URL":
                self._url = item.find("td").text        
            elif item.find("th").text=="Volume":
                self._volume = item.find("td").text        
            elif item.find("th").text=="Pages":
                self._pages = item.find("td").text        
            elif item.find("th").text=="Publication":
                self._journal = item.find("td").text
            elif item.find("th").text=="DOI":
                self._doi = item.find("td").text
                if self._doi.startswith("http://arxiv.org/"):
                    self._has_doi = False
                else:
                    self._has_doi = True
            elif item.find("th").text=="Issue":
                self._issue = item.find("td").text
            elif item.find("th").text=="Journal Abbr":
                self._journal_abbr = item.find("td").text
        try:
            self._img = pub.find_all('ul', class_="notes")[0].find('img')["src"]
        except:
            self._img = ""

    def get_img_src(self):
        return self._img

    def get_citation_formatted(self):
        ans = ""
        ans += ", ".join(self._authors)+". "
        ans += self._title+". "
        if self._has_doi:
            ans += "<i>"+self._journal_abbr+"</i> "
            ans += "<b>"+self._volume+"</b>, "
            ans += self._pages+" "
        else:
            ans += "<i>"+self._journal+"</i> "
        ans += "("+self._year+"). "
        if self._has_doi:
            ans += "doi: <a href='http://doi.org/"+self._doi+"' target='_blank'><u>"+self._doi+"</u></a>"
        else:
            ans += "at: <a href='"+self._url+"' target='_blank'>&lt<u>"+self._url+"</u>&gt</a>"
        return ans