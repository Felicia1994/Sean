try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import re
from pub_parser import PubParser

tgt_filename = "people_page.html"
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
              People
            </h3>
            <div class="line-mf"></div>
          </div>
        </div>
      </div>
      <div id="people" class="row">
"""
with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(header_html)

#################### content ####################

people_html = ""
open_positions_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-12">
                <div class="row">
                  <mypadding>
                    <div id = "open-positions" style='cursor: zoom-in;' onclick="myClickExpand(this)">
                      <div class="service-content">
                        <h2 class="s-title text-center">
                          <p class = "text-left">
                            Open Positions (expand)
                          </p>
                        </h2>
                      </div>
                    </div>
                  </mypadding>
                </div>
              </div>
              <div class="col-md-12">
                <div class="row">
                  <mypadding>
                    <div class="service-content">
                      <div id="expand-open-positions" style="display: none;">
                        <p>Postdoctoral Researchers:</p>
                        <p>
                          The X-Meng Lab within the Department of Physics, Applied Physics, and Astronomy at RPI
                          are actively seeking postdoctoral researchers who are strongly motivated
                          and have a robust publication record.
                          Ideal candidates will bring fresh, synergistic ideas that align with our research focus
                          in quantum information, statistical physics, and network science.
                        </p>
                        <p>Requirements:</p>
                        <ul>
                          <li>A PhD in physics, mathematics, or a related field.</li>
                          <li>Strong communication skills.</li>
                          <li>Experience in any of the following areas is highly desirable: quantum networks, quantum computation, percolation theories, tensor networks, open quantum systems, conformal field theories, brain networks, or network resilience.</li>
                        </ul>
                        <p>We strongly encourage applications from members of underrepresented groups.</p>
                        <p>If you are interested in a position, please send the following:</p>
                        <ol>
                          <li>a current CV with publication list,</li>
                          <li>a brief statement of research experience and interests, and</li>
                          <li>two letters of recommendation sent separately.</li>
                        </ol>
                        <p>Graduate students:</p>
                        <p>
                          Current graduate students should contact Prof. Meng to schedule a meeting.
                        </p>
                        <p>Graduate students:</p>
                        <p>
                          RPI undergraduates who are interested in earning credits
                          through the Undergraduate Research Program (URP) or seeking paid summer positions
                          in the full-time Undergraduate Research Summer Program (SURP)
                          are encouraged to reach out to Prof. Meng.
                        </p>
                      </div>
                    </div>
                  </mypadding>
                </div>
              </div>
            </div>
          </div>
        </div>
"""
people_html += open_positions_html

tips_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-12">
                <div class="row">
                  <mypadding>
                    <div id = "tips" style='cursor: zoom-in;' onclick="myClickExpand(this)">
                      <div class="service-content">
                        <h2 class="s-title text-center">
                          <p class = "text-left">
                            Tips for graduates and undergraduates (expand)
                          </p>
                        </h2>
                      </div>
                    </div>
                  </mypadding>
                </div>
              </div>
              <div class="col-md-12">
                <div class="row">
                  <mypadding>
                    <div class="service-content">
                      <div id="expand-tips" style="display: none;">
                        <ol>
                          <li>...</li>
                          <li>
                            (graduates and senior undergraduates only)
                            Be open to everything but focus on one direction
                            -- either quantum information, or complex networks, but not both.
                          </li>
                          <li>
                            Thinking too much/working too little is way more harmful than
                            working too much/thinking too little.
                          </li>
                        </ol>
                      </div>
                    </div>
                  </mypadding>
                </div>
              </div>
            </div>
          </div>
        </div>
"""
people_html += tips_html

current_members_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-12">
                <div class="row">
                  <mypadding>
                    <div id = "current-members" style='cursor: zoom-in;' onclick="myClickExpand(this)">
                      <div class="service-content">
                        <h2 class="s-title text-center">
                          <p class = "text-left">
                            Current members
                          </p>
                        </h2>
                        <p>
                          X, Y, Z
                        </p>
                      </div>
                    </div>
                  </mypadding>
                </div>
              </div>
            </div>
          </div>
        </div>
"""
people_html += current_members_html

alumni_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-12">
                <div class="row">
                  <mypadding>
                    <div id = "alumni" style='cursor: zoom-in;' onclick="myClickExpand(this)">
                      <div class="service-content">
                        <h2 class="s-title text-center">
                          <p class = "text-left">
                            Alumni
                          </p>
                        </h2>
                        <p>
                          Jing Ma
                        </p>
                      </div>
                    </div>
                  </mypadding>
                </div>
              </div>
            </div>
          </div>
        </div>
"""
people_html += alumni_html

collaborators_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-12">
                <div class="row">
                  <mypadding>
                    <div id = "collaborators" style='cursor: zoom-in;' onclick="myClickExpand(this)">
                      <div class="service-content">
                        <h2 class="s-title text-center">
                          <p class = "text-left">
                            Key collaborators
                          </p>
                        </h2>
                        <p>
                          Jianxi
                        </p>
                      </div>
                    </div>
                  </mypadding>
                </div>
              </div>
            </div>
          </div>
        </div>
"""
people_html += collaborators_html

with open(tgt_filename, "a") as tgt_file:
    tgt_file.write(people_html)

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
