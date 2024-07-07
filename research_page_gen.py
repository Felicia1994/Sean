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
researches = ["quantum-network", "physical-network", "network-of-physics", "network-of-networks"]
abstracts = {
  "quantum-network": "What will a future quantum network look like? How can we efficiently communicate and compute within such a network? Does the size of the network affect its connectivity and scalability? To answer these questions, it is essential to delve into the large-scale statistical behaviors of quantum networks—more deeply than ever before.",
  "physical-network": "What if a network has a shape? Using string theory, we explore the possibility of equipping a network with differential geometry, making the network a smooth manifold. We find that a minimization principle of not only the wiring length but also higher-dimensional manifold measures (such as surface area or volume) can explain some universal morphologies of biological systems that have long been observed, yet not theorized.",
  "network-of-physics": "This network displays 880 foundational physics papers (Blue: high energy. Red: condensed matter. Yellow: quantum. Green: astrophysics. Gray: other fields) as nodes and halos. Node size corresponds to explicit citations, while halos represent hidden citations—representing clear textual credits to a discovery (e.g., general relativity) without references to the publication (Einstein’s 1915 paper) embodying it. Accounting for hidden citations allows us to uncover deeper connections between topics and reshape how we allocate scientific credit based on citation counts.",
  "network-of-networks": "In many real-world systems, individual networks depend on other networks, forming interdependent networks. For example, a traffic network and a power grid may rely on each other: the power grid provides lighting for roads, while the traffic network enables maintenance of the power cables. We are interested in the structural and dynamical behaviors of such a network of networks, analyzing them using a rich set of tools, from percolation theories to dynamical equations.",
}
research_to_label = {
  "quantum-network": "quantum-network",
  "physical-network": "",
  "network-of-physics": "",
  "network-of-networks": "network-of-network", 
}
research_to_img = {
  "quantum-network": "research_1.png",
  "physical-network": "research_2.mp4",
  "network-of-physics": "research_3.png",
  "network-of-networks": "research_4.png",
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
      ans += "<li><a href='publications_page.html#{}'>{}</a></li>".format(_pub_parser.get_id(), _pub_parser.get_title())
  return ans

def get_img(research):
  img = research_to_img[research]
  if img.endswith("png"):
    return """
                      <img src="img/research/{}" class="img-fluid rounded b-shadow-a" alt="">
    """.format(img)
  if img.endswith("mp4"):
    return """
                      <video autoplay class="img-fluid rounded b-shadow-a">
                        <source src="img/research/{}" type="video/mp4" class="img-fluid rounded b-shadow-a">
                        Your browser does not support the video tag.                    
                      </video>
    """.format(img)
  return ""

researches_html = ""
for research in researches:
  research_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-4">
                <div class="row">
                  <wide-padding>
                    <div class="about-img">
                      {} 
                    </div>
                  </wide-padding>
                </div>
              </div>
              <div class="col-md-8">
                <div class="row">
                  <wide-padding>
                    <div id = "list-{}">
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
                  </wide-padding>
                </div>
              </div>
            </div>
          </div>
        </div>
  """.format(get_img(research), research, " ".join(research.split("-")).upper(), abstracts[research], research)
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
