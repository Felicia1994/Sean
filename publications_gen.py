import re
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

with open("publications.html", "w") as tgt_file:
    pass

header_html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>DevFolio Bootstrap Template</title>
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <meta content="" name="keywords">
  <meta content="" name="description">

  <!-- Favicons -->
  <link href="img/favicon.png" rel="icon">
  <link href="img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Bootstrap CSS File -->
  <link href="lib/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Libraries CSS Files -->
  <link href="lib/font-awesome/css/font-awesome.min.css" rel="stylesheet">
  <link href="lib/animate/animate.min.css" rel="stylesheet">
  <link href="lib/ionicons/css/ionicons.min.css" rel="stylesheet">
  <link href="lib/owlcarousel/assets/owl.carousel.min.css" rel="stylesheet">
  <link href="lib/lightbox/css/lightbox.min.css" rel="stylesheet">

  <!-- Main Stylesheet File -->
  <link href="css/style.css" rel="stylesheet">

  <!-- =======================================================
    Theme Name: DevFolio
    Theme URL: https://bootstrapmade.com/devfolio-bootstrap-portfolio-html-template/
    Author: BootstrapMade.com
    License: https://bootstrapmade.com/license/
  ======================================================= -->
</head>

<body id="page-top">

  <!--/ Nav Star /-->
  <nav class="navbar navbar-b navbar-trans navbar-expand-md fixed-top" id="mainNav">
    <div class="container">
      <a class="navbar-brand js-scroll" href="#page-top">DevFolio</a>
      <button class="navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#navbarDefault"
        aria-controls="navbarDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span></span>
        <span></span>
        <span></span>
      </button>
      <div class="navbar-collapse collapse justify-content-end" id="navbarDefault">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link js-scroll active" href="index.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link js-scroll" href="research.html">Research</a>
          </li>
          <li class="nav-item">
            <a class="nav-link js-scroll" href="publications.html">Publications</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <!--/ Nav End /-->

  <div id="content"><br><br><br><br><br></div>

  <!--/ Section Services Star /-->
  <section class="services-mf route">
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <div class="title-box text-center">
            <h3 class="title-a">
              Publications
            </h3>
            <div class="line-mf"></div>
          </div>
        </div>
      </div>
      <div id="publications" class="row">
"""
with open("publications.html", "a") as tgt_file:
    tgt_file.write(header_html)
publications_html = ""
with open("data/publications.html", "r") as src_file:
    src_html = src_file.read()
parsed_src_html = BeautifulSoup(src_html, "lxml")
print(type(parsed_src_html))
publications = parsed_src_html.body.find_all('ul', recursive=False)[0].find_all('li', recursive=False)
print(type(publications))
for pub in publications:
    title = pub.find('h2', recursive=False).text
    info = pub.find('table').find('tbody')
    authors = []
    abstract = ""
    year = ""
    url = ""
    volume = ""
    pages = ""
    journal = ""
    doi = ""
    issue = ""
    journal_abbr = ""
    for item in info.find_all('tr', recursive=False):
        if item.find("th").text=="Author":
            authors.append(item.find("td").text)
        elif item.find("th").text=="Abstract":
            abstract = item.find("td").text
        elif item.find("th").text=="Date":
            date = item.find("td").text
            date = re.split(' |/|-', date)
            print(date)
            for x in date:
                if len(x)==4 and x.isdigit():
                    year = x
        elif item.find("th").text=="URL":
            url = item.find("td").text        
        elif item.find("th").text=="Volume":
            volume = item.find("td").text        
        elif item.find("th").text=="Pages":
            pages = item.find("td").text        
        elif item.find("th").text=="Publication":
            journal = item.find("td").text
        elif item.find("th").text=="DOI":
            doi = item.find("td").text
        elif item.find("th").text=="Issue":
            issue = item.find("td").text
        elif item.find("th").text=="Journal Abbr":
            journal_abbr = item.find("td").text
    try:
        img = pub.find_all('ul', class_="notes")[0].find('img')["src"]
    except:
        img = ""
    pub_html = """
        <div class="col-sm-12">
          <div class="service-box">
            <div class="row">
              <div class="col-md-1"></div>
              <div class="col-md-2">
                <div class="row">
                  <div class="about-img">
                    <img src="{}" class="img-fluid rounded b-shadow-a" alt="">
                  </div>
                </div>
              </div>
              <div class="col-md-1"></div>
              <div class="col-md-7">
                <div class="row">
                  <div class="service-content">
                    <div>
                      {}
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-md-1"></div>
            </div>
          </div>
        </div>
    """.format(img, ", ".join(authors)+". "+title+". "+journal_abbr+" "+volume+", "+pages+" ("+year+"). doi: <a href='"+doi+"'><u>"+doi+"</u></a>" )
    publications_html += pub_html

with open("publications.html", "a") as tgt_file:
    tgt_file.write(publications_html)
footer_html = """
  <a href="#" class="back-to-top"><i class="fa fa-chevron-up"></i></a>
  <div id="preloader"></div>

  <!-- JavaScript Libraries -->
  <script src="lib/jquery/jquery.min.js"></script>
  <script src="lib/jquery/jquery-migrate.min.js"></script>
  <script src="lib/popper/popper.min.js"></script>
  <script src="lib/bootstrap/js/bootstrap.min.js"></script>
  <script src="lib/easing/easing.min.js"></script>
  <script src="lib/counterup/jquery.waypoints.min.js"></script>
  <script src="lib/counterup/jquery.counterup.js"></script>
  <script src="lib/owlcarousel/owl.carousel.min.js"></script>
  <script src="lib/lightbox/js/lightbox.min.js"></script>
  <script src="lib/typed/typed.min.js"></script>
  <!-- Contact Form JavaScript File -->
  <script src="contactform/contactform.js"></script>

  <!-- Template Main Javascript File -->
  <script src="js/main.js"></script>

</body>
</html>
"""
with open("publications.html", "a") as tgt_file:
    tgt_file.write(footer_html)
