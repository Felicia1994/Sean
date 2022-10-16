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

header_html += """
  <!--/ Intro Skew Start /-->
  <div id="home" class="intro route bg-image" style="background-image: url(img/Sean.jpg)">
    <div class="overlay-itro"></div>
    <div class="intro-content display-table">
      <div class="table-cell">
        <div class="container">
          <!--<p class="display-6 color-d">Hello, world!</p>-->
          <h1 class="intro-title mb-4">孟祥一<br>Xiangyi Meng</h1>
          <!-- <p class="intro-subtitle"><span class="text-slider-items">CEO DevFolio,Web Developer,Web Designer,Frontend Developer,Graphic Designer</span><strong class="text-slider"></strong></p> -->
          <!-- <p class="pt-3"><a class="btn btn-primary btn js-scroll px-4" href="#about" role="button">Learn More</a></p> -->
        </div>
      </div>
    </div>
  </div>
  <!--/ Intro Skew End /-->

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
              <div class="col-md-6">
                <div class="row">
                  <div class="col-sm-10 col-md-10">
                    <div class="about-img">
                      <img src="img/Sean.jpg" class="img-fluid rounded b-shadow-a" alt="">
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-md-6">
                <div class="about-me pt-4 pt-md-0">
                  <div class="title-box-2">
                    <h5 class="title-left">
                      PHYSICS X NETWORK
                    </h5>
                  </div>
                  <p class="lead">
                    The physics of network, or the network of physics?
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
