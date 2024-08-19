try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
from pub_parser import PubParser

tgt_filename = "publications_compact_page.html"
with open(tgt_filename, "w") as tgt_file:
    pass

#################### header ####################

header_filename = "header.html"
with open(header_filename, "r") as header_file:
    header_html = header_file.read()

header_html += """
  <div id="content"><br><br><br><br><br></div>

  <section class="services-mf route">
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <div class="title-box text-center">
            <h3 class="title-a">
              Publications
            </h3>
            <div class="line-mf"></div>
            <br>
            <h5 class="socials">
              <ul>
                Google Scholar:&ensp;<li><a href="https://scholar.google.com/citations?user=WpxQwZUAAAAJ&hl=en" target="_blank"><span class="ico-circle"><i class="ion-social-google"></i></span></a></li>
                |&emsp;Zotero:&ensp;<li><a href="https://www.zotero.org/xiangyi_meng" target="_blank"><span class="ico-circle"><i class="ion-ios-paper-outline"></i></span></a></li>
                |&emsp;ResearchGate:&ensp;<li><a href="https://www.researchgate.net/profile/Xiangyi-Meng-2" target="_blank"><span class="ico-circle"><i class="ion-ios-paper"></i></span></a></li>
              </ul>
            </h5>
            <h6 align="right">
              view: <a href="publications_page.html"><u>with preview</u></a> | <b>full list</b>
            </h6>
          </div>
        </div>
      </div>
      <div id="publications" class="row" style="font-family: var(--serif-font);">
        <div id="{}" class="col-sm-12">
          <div class="service-box">
            <ol reversed>
"""
with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(header_html)

#################### content ####################

src_filename = "data/publications.html"
with open(src_filename, "r") as src_file:
    src_html = src_file.read()
parsed_src_html = BeautifulSoup(src_html, "lxml")
publications = parsed_src_html.body.find_all('ul', recursive=False)[0].find_all('li', recursive=False)
def get_date(pub):
  _pub_parser = PubParser(pub)
  return _pub_parser.get_date()
publications = sorted(publications, key=get_date, reverse=True)
publications_html = ""
for idx, pub in enumerate(publications):
    _pub_parser = PubParser(pub)
    pub_html = """
              <li>
                {}
              </li>
    """.format(_pub_parser.get_citation_formatted())
    publications_html += pub_html

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(publications_html)

#################### footer ####################

footer_html = """
            </ol>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
footer_filename = "footer.html"
with open(footer_filename, "r") as footer_file:
    footer_html += footer_file.read()

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(footer_html)
