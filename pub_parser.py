import re

class PubParser(object):
    def __init__(self, pub):
        self._id = pub.get("id")
        self._title = pub.find('h2', recursive=False).text
        self._info = pub.find('table').find('tbody')
        self._authors = []
        self._abstract = ""
        self._year = ""
        self._month = ""
        self._day = ""
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
                date = re.split('-', date)
                self._year = date[0]
                self._month = date[1]
                self._day = date[2] if len(date) >= 3 else "1"
                # date = re.split(' |/|-', date)
                # for x in date:
                #     if len(x)==4 and x.isdigit():
                #         self._year = x
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
        self._labels = []
        try:
            for item in pub.find_all('ul', class_="tags")[0].find_all('li'):
                label = item.text.lower()
                self._labels.append('-'.join(label.split()))
        except:
            pass
        try:
            self._img = pub.find_all('ul', class_="notes")[0].find('img')["src"]
        except:
            self._img = ""

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_date(self):
        return self._year + self._month + self._day

    def get_labels(self):
        return self._labels

    def get_img_src(self):
        return self._img

    def _get_authors_formatted(self):
        authors_formatted = []
        for name in self._authors:
            name = name.split(" ")
            lastname = name[-1]
            firstname = name[0]
            name_formatted = lastname+", "+firstname[0]+"."
            if len(name)==3:
                name_formatted += name[1][0]+"."
            authors_formatted.append(name_formatted)
        if len(authors_formatted) == 1:
            return authors_formatted[0]
        else:
            return ", ".join(authors_formatted[:-1])+" & "+authors_formatted[-1]

    def get_citation_formatted(self):
        ans = ""
        ans += self._get_authors_formatted()+" "
        ans += self._title+". "
        if self._has_doi:
            ans += "<i>"+self._journal+"</i> "
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