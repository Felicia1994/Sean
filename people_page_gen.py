try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import re
from pub_parser import PubParser
import csv
import json

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

################ open positions #################

people_html = ""
open_positions_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-12">
                <div class="row">
                  <narrow-padding>
                    <!-- <div id = "open-positions" style='cursor: zoom-in;' onclick="myClickExpand(this)"> -->
                    <div id = "open-positions">
                      <div class="service-content">
                        <h2 class="s-title text-center">
                          <p class = "text-left">
                            <!-- Open Positions (expand) -->
                            Open Positions
                          </p>
                        </h2>
                      </div>
                    </div>
                  </narrow-padding>
                </div>
              </div>
              <div class="col-md-12">
                <div class="row">
                  <wide-padding>
                    <div class="service-content">
                      <!-- <div id="expand-open-positions" style="display: none;"> -->
                      <div id="expand-open-positions">
                        <p><b>Postdoctoral Researchers:</b></p>
                        <p>
                          The X-Meng Group, part of the Department of Physics,
                          Applied Physics, and Astronomy at RPI,
                          is actively seeking postdoctoral researchers who are strongly motivated
                          and have a robust publication record.
                          Ideal candidates will bring fresh, synergistic ideas
                          that align with our research focus in quantum information, statistical physics,
                          and network science.
                          The initial contract will last for two years (upon renewal),
                          with the possibility of extension to three years.
                        </p>
                        <p>
                          As part of RPI's quantum campaign,
                          our group will have access to RPI's newly acquired
                          <a href="https://research.ibm.com/blog/rpi-ibm-quantum-system-one-installed" target="_blank">
                          IBM 127-qubit processor</a>,
                          which is the world's first IBM Quantum System One on a university campus.
                        </p>
                        <p>Requirements:</p>
                        <ul>
                          <li>A PhD in physics, mathematics, or a related field.</li>
                          <li>Strong communication skills.</li>
                          <li>Proficiency in coding, particularly with Qiskit, Mathematica, Python, and C++.</li>
                          <li>Experience in any of the following areas is highly desirable: quantum networks, quantum computation, percolation theories, tensor networks, open quantum systems, network resilience, or brain networks.</li>
                        </ul>
                        <p>Duties:</p>
                        <ul>
                          <li>Primary and secondary projects (50-60%).</li>
                          <li>Supervision of undergraduate projects (20-30%).</li>
                          <li>Writing grant proposals (10-20%).</li>
                          <li>Academic travels with full support (5%).</li>
                        </ul>
                        <p>We strongly encourage applications from members of underrepresented groups.</p>
                        <p>If you are interested in a position, please send the following to (xmenggroup at gmail.com):</p>
                        <ol>
                          <li>a current CV with publication list,</li>
                          <li>a 1-2 page statement of research experience and interests, and</li>
                          <li>two letters of recommendation sent separately.</li>
                        </ol>
                        <p><b>Graduate students:</b></p>
                        <p>
                          Current graduate students with strong research motivations in quantum information,
                          statistical physics, and network science should contact Prof. Meng to schedule a meeting.
                        </p>
                        <p><b>Undergraduate students:</b></p>
                        <p>
                          RPI undergraduates who are interested in earning credits
                          through the Undergraduate Research Program (URP) or seeking paid summer positions
                          in the full-time Undergraduate Research Summer Program (SURP)
                          are encouraged to reach out to Prof. Meng.
                        </p>
                        <p><b>What can we offer?</b></p>
                        <ul>
                          <li>
                            <b>Career Support:</b>
                            An important criterion for tenure evaluation of junior professors
                            is helping students and postdocs secure ideal academic or industry positions.
                            With this motivation in mind,
                            I can offer significant assistance that senior professors
                            might find challenging to provide.
                            This includes networking, writing papers
                            and grant applications, job referrals,
                            and facilitating interactions.
                            (I have personally benefited greatly from such support in the past as well.)
                          </li>
                          <li>
                            <b>Inclusive Environment:</b>
                            We emphasize an inclusive and free environment
                            that encourages independent thinking and innovative ideas.
                            We prioritize first-author contributions
                            while encouraging collaboration and communication within the group.
                          </li>
                          <li>
                            <b>Regular Mentorship:</b>
                            We have one regular group meeting and one-on-one sessions each week for guidance.
                            I am committed to dedicating my energy to support you:
                            It is my responsibility to ensure our success together!
                          </li>
                        </ul>
                      </div>
                    </div>
                  </wide-padding>
                </div>
              </div>
            </div>
          </div>
        </div>
"""
people_html += open_positions_html

##################### tips #####################

tips_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-12">
                <div class="row">
                  <narrow-padding>
                    <div id = "tips" style='cursor: zoom-in;' onclick="myClickExpand(this)">
                      <div class="service-content">
                        <h2 class="s-title text-center">
                          <p class = "text-left">
                            Tips for graduates and undergraduates (expand)
                          </p>
                        </h2>
                      </div>
                    </div>
                  </narrow-padding>
                </div>
              </div>
              <div class="col-md-12">
                <div class="row">
                  <wide-padding>
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
                  </wide-padding>
                </div>
              </div>
            </div>
          </div>
        </div>
"""
# people_html += tips_html

################# people parser #################

people_filename = "data/people.json"
with open(people_filename, 'r') as people_file:
    people = json.load(people_file)


def people_compare(p1, p2):
    if p1["lastname"] < p2["lastname"]:
        return -1
    if p1["lastname"] > p2["lastname"]:
        return 1
    if p1["firstname"] < p2["firstname"]:
        return -1
    if p1["firstname"] > p2["firstname"]:
        return 1
    return 0

############### current members ################

current_members_html = ""
for category_id, category in [("postdocs", "Postdoctoral Researchers"), ("graduates", "Graduate Students"), ("undergraduates", "Undergraduate Students")]:
  current_members_html += """
          <div class="col-sm-12">
            <div class="service-box">
              <div class="row">
                <div class="col-md-12">
                  <div class="row">
                    <wide-padding>
                      <div id = "current-members-{}">
                        <div class="service-content">
                          <h2 class="s-title text-center">
                            <p class = "text-left">
                              {}
                            </p>
                          </h2>
                        </div>
                      </div>
                    </wide-padding>
                  </div>
                </div>
  """.format(category_id, category)

  current_members = sorted(
      people["current"][category_id], key=lambda p: (p["lastname"], p["firstname"]))

  for current_member in current_members:
      current_members_html += """
                <div class="col-md-12">
                  <div class="row">
                    <div class="col-sm-1 col-md-1"></div>
                    <div class="col-sm-2 col-md-2">
                      <div class="about-img">
                        <img src="img/people/{}" class="img-fluid rounded b-shadow-a" alt="">
                      </div>
                    </div>
                    <div class="col-sm-8 col-md-8">
                      <div class="text-center" style="margin-top: 5px; margin-bottom: 15px;">
                        <b>{}</b>
                      </div>
                      <div class="text-center" style="margin-top: 5px; margin-bottom: 15px;">
                        {}
                      </div>
                    </div>
                    <div class="col-sm-1 col-md-1"></div>
                  </div>
                </div>
                <div class="col-md-12">
                  <p>
                  </p>
                </div>
    """.format(current_member["picture"], current_member["firstname"] + " " + current_member["lastname"], current_member["description"])

  current_members_html += """
              </div>
            </div>
          </div>
  """
people_html += current_members_html

################ group pictures ################

group_pitures_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-12">
                <div class="row">
                  <wide-padding>
                    <div id = "group-pictures">
                      <div class="service-content">
                        <h2 class="s-title text-center">
                          <p class = "text-left">
                            Group pictures
                          </p>
                        </h2>
                      </div>
                    </div>
                  </wide-padding>
                </div>
              </div>
"""

group_pitures = []
people_filename = "data/people.csv"
with open(people_filename, 'r') as people_file:
    people_reader = csv.DictReader(people_file)
    for person in people_reader:
        if person["display"] == "true" and person["category"] == "group":
            group_pitures.append(person)

for group_piture in group_pitures:
    group_pitures_html += """
              <div class="col-md-6">
                <div class="row">
                  <div class="col-sm-1 col-md-1"></div>
                  <div class="col-sm-10 col-md-10">
                    <div class="about-img">
                      <img src="img/people/{}" class="img-fluid rounded b-shadow-a" alt="">
                    </div>
                  </div>
                  <div class="col-sm-1 col-md-1"></div>
                </div>
                <div class="row">
                  <div class="col-sm-1 col-md-1"></div>
                  <div class="col-sm-10 col-md-10">
                    <div class="text-center" style="margin-top: 5px; margin-bottom: 15px;">
                      {}
                    </div>
                  </div>
                  <div class="col-sm-1 col-md-1"></div>
                </div>
              </div>
  """.format(group_piture["img"], group_piture["name"])

group_pitures_html += """
            </div>
          </div>
        </div>
"""
people_html += group_pitures_html

#################### alumni ####################

alumni_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-12">
                <div class="row">
                  <wide-padding>
                    <div id = "alumni">
                      <div class="service-content">
                        <h2 class="s-title text-center">
                          <p class = "text-left">
                            Alumni
                          </p>
                        </h2>
                      </div>
                    </div>
                  </wide-padding>
                </div>
              </div>
"""

alumni = []
people_filename = "data/people.csv"
with open(people_filename, 'r') as people_file:
    people_reader = csv.DictReader(people_file)
    for person in people_reader:
        if person["display"] == "true" and person["category"] == "alumnus":
            alumni.append(person)

for alumnus in alumni:
    alumni_html += """
              <div class="col-md-3">
                <div class="row">
                  <div class="col-sm-1 col-md-1"></div>
                  <div class="col-sm-10 col-md-10">
                    <div class="about-img">
                      <img src="img/people/{}" class="img-fluid rounded b-shadow-a" alt="">
                    </div>
                  </div>
                  <div class="col-sm-1 col-md-1"></div>
                </div>
                <div class="row">
                  <div class="col-sm-1 col-md-1"></div>
                  <div class="col-sm-10 col-md-10">
                    <div class="text-center" style="margin-top: 5px; margin-bottom: 15px;">
                      {}
                    </div>
                  </div>
                  <div class="col-sm-1 col-md-1"></div>
                </div>
              </div>
  """.format(alumnus["img"], alumnus["name"])

alumni_html += """
            </div>
          </div>
        </div>
"""
# people_html += alumni_html

################ collaborators #################

################# first layout #################
collaborators_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-12">
                <div class="row">
                  <wide-padding>
                    <div id = "collaborators">
                      <div class="service-content">
                        <h2 class="s-title text-center">
                          <p class = "text-left">
                            Key collaborators
                          </p>
                        </h2>
"""

collaborators = []
collaborators_filename = "data/collaborators.csv"
with open(collaborators_filename) as collaborators_file:
    collaborators_reader = csv.reader(collaborators_file)
    for collaborator in collaborators_reader:
        collaborators.append(collaborator)
collaborators.sort(key=lambda c: c[0].split()[-1])

for name, affiliation in collaborators:
    collaborators_html += """
                        <p>
                          {}, {}
                        </p>
  """.format(name, affiliation)

collaborators_html += """
                      </div>
                    </div>
                  </wide-padding>
                </div>
              </div>
            </div>
          </div>
        </div>
"""
# people_html += collaborators_html

################ second layout #################
collaborators_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-12">
                <div class="row">
                  <wide-padding>
                    <div id = "collaborators">
                      <div class="service-content">
                        <h2 class="s-title text-center">
                          <p class = "text-left">
                            Collaborating Institutions
                          </p>
                        </h2>
                      </div>
                    </div>
                  </wide-padding>
                </div>
              </div>
"""

collaborators = ["bar-ilan.png", "bu.png", "icl.jpg",
                 "kth.png", "nordita.png", "neu.png", "nwu.png", "oist.jpg", "oxford.jpg"]

for collaborator in collaborators:
    collaborators_html += """
              <img src="img/logos/{}" style="width: 18%; height: 18%; margin: auto;">
  """.format(collaborator)

collaborators_html += """
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
