def get_footer():
  from elements.SnsIcons import get_sns_icons
  return f"""
  <footer>
  <div id="bottom-bar">
    <div class="left">
      <h3 style="margin: 0; padding-top: 5px;">Categories</h3>
      <ul>
        <li><a href="">Voylin's Life</a></li>
        <li><a href="">Our Life</a></li>
        <li><a href="">日本語で</a></li>
        <li><a href="">Learn Japanese</a></li>
        <li><a href="">Travel Advice</a></li>
      </ul>
    </div>
    <div class="right">
      <p style="padding-top: 5px; padding-bottom: 3px; font-size: 18px; text-align: center;"><strong>Welcome to our site!</strong></p>
      <p style="text-align: center;">This site is made by hand and without ad's, for this I thank the people who support us on Patreon for helping us out!</p>
      <br>
      {get_sns_icons()}
    </div>
  </div>
  <div id="copyright">
    <small><strong>©</strong> Copyright of <a href="https://youtube.com/voylin">Voylin's Life</a></small>
  </div>
</footer>
"""