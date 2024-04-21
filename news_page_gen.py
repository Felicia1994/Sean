try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import re
from pub_parser import PubParser

tgt_filename = "news_page.html"
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
              News
            </h3>
            <div class="line-mf"></div>
          </div>
        </div>
      </div>
      <div id="news" class="row">
"""
with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(header_html)

#################### content ####################

news_html = ""
for i in range(5):
  new_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
            </div>
          </div>
        </div>
  """
  news_html += new_html

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(news_html)

#################### footer ####################

footer_html = """
      </div>
    </div>
  </section>
"""
footer_filename = "footer.html"
with open(footer_filename, "r") as footer_file:
    footer_html += footer_file.read()

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(footer_html)
