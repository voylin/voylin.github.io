def get_page():
  from templates.main_template import get_main_template
  return get_main_template(
    page_title='Welcome!',
    content="""
<img class="center-image" width="900" height="600" src="images/banner.webp" alt="Banner image" >
<a href="about_us.html"><h1 style="text-align: center;"><u>Who we are</u></h1></a>
<h1>Blog categories:</h1>
<div class="category-container">
  <a href="voylins_life.py">
    <img src="images/category-voylins-life.webp" alt="Voylin's life">
  </a>
  <a href="our_life.py">
    <img src="images/category-our-life.webp" alt="Our life">
  </a>
  <a href="travel_advice.py">
    <img src="images/category-travel-advice.webp" alt="Travel advice">
  </a>
  <a href="nihongo_de.py">
    <img src="images/category-nihongo-de.webp" alt="にほんごで">
  </a>
  <a href="learn_japanese.py">
    <img src="images/category-learn-japanese.webp" alt="Learn Japanese">
  </a>
</div>
<h1>Our posts:</h1>
<p>Coming soon</p>
""")