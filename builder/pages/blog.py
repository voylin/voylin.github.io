def get_page():
  from templates.main_template import get_main_template
  return get_main_template(
    page_title='Blog',
    content="""
<h1>Welcome to our blog!</h1>
<h2>Categories:</h2>
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
<h2>All posts:</h2>
<div class="blog-card-container">
  {{blog-post-card-all}}
  {{blog-post-card-all}}
  {{blog-post-card-all}}
  {{blog-post-card-all}}
</div>
<h3 style="text-align: center;"><a href="">View all</a></h3>
""")
