def get_main_menu(blog_link_menu):
  return f"""
  <nav id="sidebar-nav">
  <ul>
    <a href="index.html"><li>Homepage</li></a>
    <li style="display: flex;">
      <a style="display: inline-flex; width: 100%;" href="blog.html">Blog</a>
      <a onclick="showBlogLinks()" id="blogMenuButton"  style="width: 60px; text-align: center;">+</a>
      <!--<button style="display: inline-flex;" class="blog_menu_button" id="blogMenuButton" onclick="showBlogLinks()">+</button>-->
    </li>
    {blog_link_menu}
    <a href="who_we_are.html"><li>Who we are</li></a>
    <a href="contact_us.html"><li>Contact us</li></a>
  </ul>
</nav>"""