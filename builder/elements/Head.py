def get_head(page_title):
  function_showBlogLinks = """
  function showBlogLinks() {
    var button = document.getElementById("blogMenuButton");
    var blog_link_items = document.getElementById("blog_menu_items");
    if (blog_link_items.style.display === "none") {
      blog_link_items.style.display = "block";
      button.innerText = "-";
    } else {
      blog_link_items.style.display = "none";
      button.innerText = "+";
    }
  }
  """
  function_showMobileMenu = """
  function showMobileMenu() {
    var button = document.getElementById("mobile-menu-button");
    var mobile_menu = document.getElementById("sidebar-content");
    var blog_link_items = document.getElementById("blog_menu_items");
    if (mobile_menu.style.display === "block") {
      mobile_menu.style.display = "none";
      blog_link_items.style.display = "none";
      document.getElementById("blogMenuButton").innerText = "+"
    } else { mobile_menu.style.display = "block"; }
  }
  """
  
  return f"""
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="A site made by the yt channel Voylin's Life. With blog posts of learning Japanese, my Youtube channel, our life, travel advice, ...">
<link rel="icon" type="image/svg+xml" href="images/favicon.svg">
<link href="style.css" rel="stylesheet" type="text/css" />
<title>Voylin's site - {page_title}</title>
<script>
  {function_showBlogLinks}
  {function_showMobileMenu}
</script>
</head>
"""

