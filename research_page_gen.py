try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import re
from pub_parser import PubParser

tgt_filename = "research_page.html"
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
              Research
            </h3>
            <div class="line-mf"></div>
          </div>
        </div>
      </div>
      <div id="research" class="row">
"""
with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(header_html)

#################### content ####################

# researches = ["physical-network", "quantum-network", "hidden-citations", "network-of-networks"]
researches = ["quantum-network", "physical-network", "network-of-networks"]
abstracts = {
  "physical-network": "What if a network has a shape? Using string theory, we explore the possibility of equipping a network with differential geometry, making the network a smooth <b>manifold</b>. We find that a minimization principle of not only the wiring length but also higher-dimensional manifold measures (such as surface area or volume) can explain some universal morphologies of biological systems that have long been observed, yet not theorized.",
  "quantum-network": "How to efficiently distribute <b>quantum entanglement</b> between two or more distant nodes that are not directly linked (hence not directed entangled)? To answer this question, we need to understand the large-scale statistical behaviors of quantum networks—at a level deeper than ever before.",
  "hidden-citations": "This is a network of not just explicit citations, but <b>hidden citations</b>, representing clear textual credits to a discovery without references to the publication embodying it. Case in point are Einstein's relativity, which is so embedded into scientific literacy that only rarely do manuscripts focusing on the topic explicitly cite Einstein's papers. Not only does counting hidden citations reveal the deeper connections between topics—it also reshapes our use of citations for scientific credit allocation.",
  "network-of-networks": "A network of networks contains multiple layers, each layer representing a network that is interdependent to other layers through bridge nodes and links. We are interested in the structual and dynamical behaviors of such a network of networks, analyzing them using a rich set of tools—from percolation theories to dynamical equations."
}
research_to_label = {
  "quantum-network": "quantum-network",
  "physical-network": "",
  "network-of-networks": "network-of-network", 
  "hidden-citations": ""
}

src_filename = "data/publications.html"
with open(src_filename, "r") as src_file:
    src_html = src_file.read()
parsed_src_html = BeautifulSoup(src_html, "lxml")
publications = parsed_src_html.body.find_all('ul', recursive=False)[0].find_all('li', recursive=False)
def get_date(pub):
  _pub_parser = PubParser(pub)
  return _pub_parser.get_date()
publications = sorted(publications, key=get_date, reverse=True)

def get_pubs(research):
  ans = ""
  for pub in publications:
    _pub_parser = PubParser(pub)
    label = research_to_label[research]
    if label in _pub_parser.get_labels():
      ans += "<li><a href='publications_page.html#{}' target='_blank' style='cursor: zoom-in;'>{}</a></li>".format(_pub_parser.get_id(), _pub_parser.get_title())
  return ans

researches_html = ""
for research in researches:
  research_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-4">
                <div class="row">
                  <mypadding>
                    <div class="about-img">
                      <img src="img/{}.png" class="img-fluid rounded b-shadow-a" alt="">
                    </div>
                  </mypadding>
                </div>
              </div>
              <div class="col-md-8">
                <div class="row">
                  <mypadding>
                    <div id = "list-{}" style='cursor: zoom-in;' onclick="myClickList(this)">
                      <div class="service-content">
                        <h2 class="s-title text-center">
                          <p class = "text-left">
                            {}
                          </p>
                        </h2>
                        <p>
                          {}
                        </p>
                      </div>
                    </div>
                  </mypadding>
                </div>
              </div>
              <div class="col-md-12">
                <div class="row">
                  <mypadding>
                    <div class="service-content">
                      <ul id="ullist-{}" style="display: none;">
                        {}
                      </ul>
                    </div>
                  </mypadding>
                </div>
              </div>
            </div>
          </div>
        </div>
  """.format(research, research, " ".join(research.split("-")).upper(), abstracts[research], research, get_pubs(research))
  researches_html += research_html

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(researches_html)

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
