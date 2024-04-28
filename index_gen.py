try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
from pub_parser import PubParser

tgt_filename = "index.html"
with open(tgt_filename, "w") as tgt_file:
    pass

#################### header ####################

header_filename = "header.html"
with open(header_filename, "r") as header_file:
    header_html = header_file.read()

# header_html += """
#   <!--/ Intro Skew Start /-->
#   <div id="home" class="intro route bg-image" style="background-image: url(img/hidden-citations.png)">
#     <div class="overlay-itro"></div>
#     <div class="intro-content display-table">
#       <div class="table-cell">
#         <div class="container">
#           <!--<p class="display-6 color-d">Hello, world!</p>-->
#           <h1 class="intro-title mb-4">孟祥一<br>Xiangyi Meng</h1>
#           <!-- <p class="intro-subtitle"><span class="text-slider-items">CEO DevFolio,Web Developer,Web Designer,Frontend Developer,Graphic Designer</span><strong class="text-slider"></strong></p> -->
#           <!-- <p class="pt-3"><a class="btn btn-primary btn js-scroll px-4" href="#about" role="button">Learn More</a></p> -->
#         </div>
#       </div>
#     </div>
#   </div>
#   <!--/ Intro Skew End /-->
# """

header_html += """
  <br><br><br>
"""

header_html += """
  <section id="about" class="about-mf sect-pt4 route" style="background-image: url(img/bg1.jpg)">
    <div class="container">
      <div class="row">
"""

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(header_html)

#################### content ####################

index_html = """
        <div class="col-sm-12">
          <div class="box-shadow-full">
            <div class="row">
              <div class="col-md-5">
                <div class="row">
                  <div class="col-sm-10 col-md-10">
                    <div class="about-img">
                      <img src="img/Sean.jpg" class="img-fluid rounded b-shadow-a" alt="">
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="col-sm-10 col-md-10">
                    News
                    <ul>
                      <li>news 1</li>
                      <li>news 2</li>
                      <li>news 3</li>
                      <li>news 4</li>
                    </ul>
                    (more)
                  </div>
                </div>
              </div>
              <div class="col-md-7">
                <div class="about-me pt-4 pt-md-0">
                  <div class="title-box-2">
                    <h5 class="title-left">
                      <span class=special-x>X</span>-Meng Lab:
                      Physics <span class=special-x>X</span> Network
                    </h5>
                  </div>
                  <p>
                    The physics of network, or the network of physics?
                  </p>
                  <p>
                    This rhetorical question captures the interdisciplinary essence of the X-Meng lab’s mission
                    &mdash; to explore the rich interplay between network science and both statistical and quantum physics.
                  </p>
                  <p>
                    Led by Professor X Meng, the lab’s research spans several areas:
                  </p>
                  <p>
                    <ul>
                      <li>Quantum networks, communications, and computing.</li>
                      <li>Physical/biological networks (and their connections to string theory).</li>
                      <li>Statistical physics of complex networks, network metrics.</li>
                      <li>Open quantum systems, open quantum field theories.</li>
                    </ul>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
"""

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(index_html)

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
