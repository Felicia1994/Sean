try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import re
from pub_parser import PubParser
from news_parser import news_parser

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
            <br>
            <h5 class="socials">
              <ul>
                X (Twitter):&ensp;<li><a href="https://twitter.com/drxiangyimeng" target="_blank"><span class="ico-circle"><i class="ion-social-twitter"></i></span></a></li>
                |&emsp;Threads:&ensp;<li><a href="https://www.threads.net/@xmeng.io" target="_blank"><span class="ico-circle"><i class="ion-social-instagram"></i></span></a></li>
              </ul>
            </h5>
          </div>
        </div>
      </div>
      <div id="news" class="row">
        <div class="col-sm-12">
          <div class="service-box">
            <ul>
"""
with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(header_html)

#################### content ####################

news_html = ""

news = news_parser()

for idx, news_piece in enumerate(news):
  new_html = """
              <li>
                <p>
                  [{}] {}
                </p>
              </li>
  """.format(news_piece["date"], news_piece["content"])
  news_html += new_html

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(news_html)

#################### footer ####################

footer_html = """
            </ul>
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
