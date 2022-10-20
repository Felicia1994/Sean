try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
from pub_parser import PubParser

tgt_filename = "contact_page.html"
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
              Contact
            </h3>
            <div class="line-mf"></div>
          </div>
        </div>
      </div>
      <div id="contact" class="row">
"""
with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(header_html)



#################### content ####################

contact_html = """
        <div class="col-md-3"></div>
        <div class="col-md-6" style="text-align: center;">
            <div class="more-info">
              <ul class="list-ico">
                  <li><span class="ion-email"></span> x.meng@neu.edu </li>
                  <!-- <li><span class="ion-ios-telephone"></span> (617) 902-8536</li> -->
                  <!-- <li><span class="ion-ios-location"></span> 590 Commonwealth Avenue, Boston, MA 02135</li> -->
              </ul>
            </div>
            <div class="socials">
              <ul>
                <li><a href="https://scholar.google.com/citations?user=WpxQwZUAAAAJ&hl=en" target="_blank"><span class="ico-circle"><i class="ion-social-google"></i></span></a></li>
                <li><a href="https://www.zotero.org/xiangyi_meng" target="_blank"><span class="ico-circle"><i class="ion-ios-paper-outline"></i></span></a></li>
                <li><a href="https://www.researchgate.net/profile/Xiangyi-Meng-2" target="_blank"><span class="ico-circle"><i class="ion-ios-paper"></i></span></a></li>
              </ul>
            </div>
        </div>
        <div class="col-md-3"></div>
"""

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(contact_html)

#################### footer ####################

footer_filename = "footer.html"
with open(footer_filename, "r") as footer_file:
    footer_html = footer_file.read()

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(footer_html)
