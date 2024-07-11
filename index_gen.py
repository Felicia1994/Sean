try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
from pub_parser import PubParser
from news_parser import news_parser

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
                      <!-- Slideshow container -->
                      <div class="slideshow-container">
                        <!-- Full-width images with number and caption text -->
"""

images = ["research_1.png", "research_2.mp4", "research_3.png", "research_4.png"]
for image in images:
  if image.endswith("png"):
    index_html += """
                        <div class="mySlides">
                          <img src="img/research/{}" style="width: 100%;">
                        </div>
    """.format(image)
  if image.endswith("mp4"):
    index_html += """
                        <div class="mySlides">
                          <video autoplay muted loop style="width: 100%;">
                            <source src="img/research/{}" type="video/mp4">
                            Your browser does not support the video tag.                    
                          </video>
                        </div>
    """.format(image)

index_html += """
                        <!-- Next and previous buttons -->
                        <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
                        <a class="next" onclick="plusSlides(1)">&#10095;</a>
                      </div>
                      <br>
                      <!-- The dots/circles -->
                      <div style="text-align:center">
"""
for idx in range(4):
  index_html += """
                        <span class="dot" onclick="currentSlide({})"></span>
  """.format(idx+1)
index_html += """
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-md-7">
                <div class="about-me pt-4 pt-md-0">
                  <div class="title-box-2">
                    <h5 class="title-left">
                      Physics &thinsp;<span class=special-x>X</span> &thinsp;Network
                    </h5>
                  </div>
                  <p>
                    The physics of networks, or the network of physics?
                  </p>
                  <p>
                    This rhetorical question captures the interdisciplinary essence of our research group's mission
                    &mdash; to explore the rich interplay between network science and both statistical and quantum physics.
                  </p>
                  <p>
                    Led by Professor Xiangyi "X" Meng, the group's research spans several areas:
                  </p>
                  <p>
                    <ul>
                      <li>Quantum networks, communications, and computing; quantum complex systems.</li>
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
        <div class="col-sm-12">
          <div class="box-shadow-full">
            <div class="row">
              <div class="col-sm-10 col-md-10">
                <h6 style="text-transform: uppercase;">
                  <a href="news_page.html">News</a>
                </h6>
              </div>
            </div>
"""

news = news_parser()
for idx, news_piece in enumerate(news[:5]):
  index_html += """
            <div class="row">
              <div class="col-md-1">
                <div align="right">{}</div>
              </div>
              <div class="col-md-10">
                <div class="row">
                    <p>
                      [{}] {}
                    </p>
                </div>
              </div>
              <div class="col-md-1"></div>
            </div>
""".format("&#9670;", news_piece["date"], news_piece["content"])
index_html += """
            <div class="row">
              <div class="col-md-1">
                <div align="right">{}</div>
              </div>
              <div class="col-md-10">
                <div class="row">
                    <p>
                      ...
                    </p>
                </div>
              </div>
              <div class="col-md-1"></div>
            </div>
          </div>
        </div>
        <div class="col-sm-12">
          <div class="box-shadow-full">
            <div class="row">
              <div class="col-md-5">
                <div class="row">
                  <div class="col-sm-10 col-md-10">
                    <div class="about-img">
                      <img src="img/X.jpg" class="img-fluid rounded b-shadow-a" alt="">
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-md-7">
                <div class="row">
                    <horizontal-padding>
                      <p>
                        Prof. Xiangyi "X" Meng is an Assistant Professor in the Department of
                        Physics, Applied Physics, and Astronomy at Rensselaer Polytechnic Institute (RPI).
                        He earned his B.S. in microelectronics from Peking University
                        and completed his Ph.D. in physics at Boston University
                        (advised by Prof. Eugene Stanley).
                        Prior to his role at RPI, he worked with Prof. Albert-László Barabási
                        as a Postdoc at Northeastern University's Center for Complex Network Research,
                        and with Prof. István Kovács as a Research Associate at Northwestern University.
                      </p>
                      <p>
                        Prof. Meng's research spans several areas of physics and network science,
                        including quantum networks and quantum information,
                        open quantum field theories, science of science,
                        computational social science, physical and biological networks,
                        scale-free network theories, information diffusion,
                        tensor networks, and recurrent neural networks.
                        He also applies interdisciplinary network science approaches to explore brains and econophysics.
                      </p>
                      <p>
                        Prof. Meng has published 20+ publications in prestigious journals
                        such as <i>Physical Review Letters, PNAS, PNAS Nexus, Nature Human Behaviors,
                        Nature Communications, Communications Physics, Chaos Solitons & Fractals,
                        Physical Review D, Physical Review Research,</i> among others.
                        He has reviewed 40+ papers from the above journals and <i>Europhysics Letters,
                        New Journal of Physics, Magnetic Resonance in Medicine,</i> etc.
                        His work has been highlighted in <i>Physics World, Phys.org,</i> among other media outlets.
                      </p>
                    </horizontal-padding>
                </div>
              </div>
            </div>
          </div>
        </div>
""".format("&#9670;", "?")

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
