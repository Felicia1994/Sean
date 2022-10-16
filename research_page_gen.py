try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
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

research_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-4">
                <div class="row">
                  <mypadding>
                    <div class="about-img">
                      <img src="img/Sean.jpg" class="img-fluid rounded b-shadow-a" alt="">
                    </div>
                  </mypadding>
                </div>
              </div>
              <div class="col-md-8">
                <div class="row">
                  <mypadding>
                    <div class="service-content">
                      <h2 class="s-title text-center">
                        <p id = "list-physical-network" onclick="myClickList(this)" class = "text-left">
                          <myclick>PHYSICAL NETWORK</myclick>
                        </p>
                      </h2>
                    </div>
                  </mypadding>
                </div>
              </div>
              <div class="col-md-12">
                <div class="row">
                  <mypadding>
                    <div class="service-content">
                      <ul id="ullist-physical-network" style="display: none;">
                        <li><a href = "publications.html#1">Quantum spatial-periodic harmonic model for daily price-limited stock markets.</a></li>
                        <li><a href = "/exampleFolder/file2.txt">List Item 2</a></li>
                        <li><a href = "/exampleFolder/file3.txt">List Item 3</a></li>
                        <li><a href = "/exampleFolder/file4.txt">List Item 4</a></li>
                        <li><a href = "/exampleFolder/file5.txt">List Item 5</a></li>
                      </ul>
                    </div>
                  </mypadding>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-4">
                <div class="row">
                  <mypadding>
                    <div class="about-img">
                      <img src="img/Sean.jpg" class="img-fluid rounded b-shadow-a" alt="">
                    </div>
                  </mypadding>
                </div>
              </div>
              <div class="col-md-8">
                <div class="row">
                  <mypadding>
                    <div class="service-content">
                      <h2 class="s-title">
                        <p id = "list-quantum-network" onclick = "myClickList(this)" class = "text-left">
                          <myclick>QUANTUM NETWORK</myclick>
                        </p>
                      </h2>
                    </div>
                  </mypadding>
                </div>
              </div>
              <div class="col-md-12">
                <div class="row">
                  <mypadding>
                    <div class="service-content">
                      <br>
                      <ul id="ullist-quantum-network" style="display: none;">
                        <li><a href = "/exampleFolder/file1.txt">List Item 1</a></li>
                        <li><a href = "/exampleFolder/file2.txt">List Item 2</a></li>
                        <li><a href = "/exampleFolder/file3.txt">List Item 3</a></li>
                        <li><a href = "/exampleFolder/file4.txt">List Item 4</a></li>
                        <li><a href = "/exampleFolder/file5.txt">List Item 5</a></li>
                      </ul>
                    </div>
                  </mypadding>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-4">
                <div class="row">
                  <mypadding>
                    <div class="about-img">
                      <img src="img/Sean.jpg" class="img-fluid rounded b-shadow-a" alt="">
                    </div>
                  </mypadding>
                </div>
              </div>
              <div class="col-md-8">
                <div class="row">
                  <mypadding>
                    <div class="service-content">
                      <h2 class="s-title">
                        <p id = "list-citation-network" onclick = "myClickList(this)" class = "text-left">
                          <myclick>CITATION NETWORK</myclick>
                        </p>
                      </h2>
                      <p>
                        This is a network of not just explicit citations,
                        but hidden citations—representing clear textual credits to a discovery
                        without references to the publication embodying it.
                        Case in point are Einstein's relativity,
                        which is so embedded into scientific literacy
                        that only rarely do manuscripts focusing on the topic
                        explicitly cite Einstein's papers.
                      </p>
                    </div>
                  </mypadding>
                </div>
              </div>
              <div class="col-md-12">
                <div class="row">
                  <mypadding>
                    <div class="service-content">
                      <br>
                      <ul id="ullist-citation-network" style="display: none;">
                        <li><a href = "/exampleFolder/file1.txt">List Item 1</a></li>
                        <li><a href = "/exampleFolder/file2.txt">List Item 2</a></li>
                        <li><a href = "/exampleFolder/file3.txt">List Item 3</a></li>
                        <li><a href = "/exampleFolder/file4.txt">List Item 4</a></li>
                        <li><a href = "/exampleFolder/file5.txt">List Item 5</a></li>
                      </ul>
                    </div>
                  </mypadding>
                </div>
              </div>
            </div>
          </div>
        </div>
"""

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(research_html)

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
