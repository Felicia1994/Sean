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
        <div class="col-md-6" style="text-align: center; margin-bottom:30px;">
            <div class="more-info">
              <ul class="list-ico">
                  <li><span class="ion-email"></span> xm@northwestern.edu </li>
                  <!-- <li><span class="ion-ios-telephone"></span> (617) 902-8536</li> -->
                  <!-- <li><span class="ion-ios-location"></span> 590 Commonwealth Avenue, Boston, MA 02135</li> -->
              </ul>
            </div>
        </div>
        <div class="col-md-3"></div>
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-12" style="text-align: center; margin-bottom:30px;">
                <h6>
                  You live through certain things before you understand them.
                </h6>
                <h6>
                  You can't always take the analytical position.
                </h6>
                <h6>
                  &mdash; Sally Rooney, Conversations with Friends.
                </h6>
              </div>
              <div class="col-md-12" style="text-align: center;">
                <h6>
                  (If I am not on campus, you can likely find me at one of the locations marked on this map.)
                </h6>
              </div>
            </div>
"""

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(contact_html)

# embeded google maps: too slow
maps_html = """
            <div class="row">
              <div class="col-md-12" style="text-align: center;">
                <div class="iframe-placeholder">Loading...</div>
                <div class="iframe-content">
                  <iframe class="iframe-content" src="
"""
maps_filename = "data/maps.html"
with open(maps_filename, "r") as maps_file:
    maps_html += BeautifulSoup(maps_file.read(), 'html.parser').find_all('iframe')[0]['src']
maps_html += """
                  " onload="showImage()"></iframe>
                </div>
              </div>
            </div>
"""

# google maps screenshot
# maps_html = """
#             <div class="row">
#               <div class="col-md-12" style="text-align: center;">
#                 <a href="
# """
# maps_filename = "data/maps.html"
# with open(maps_filename, "r") as maps_file:
#     maps_html += BeautifulSoup(maps_file.read(), 'html.parser').find_all('iframe')[0]['src']
# maps_html += """
#                 " target="_blank">
#                   <img title="click for the interactive view" src="img/google_maps.png" alt="Google Maps" style="width:840px;height:512px;">
#                 </a>
#               </div>
#             </div>
# """

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(maps_html)

#################### footer ####################
footer_html = """
          </div>
        </div>
      </div>
    </div>
  </section>
"""
footer_filename = "footer.html"
with open(footer_filename, "r") as footer_file:
  for line in footer_file.readlines():
    if "preloader" not in line:
      footer_html += line

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(footer_html)
