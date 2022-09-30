def get_sidebar():
  from elements.SnsIcons import get_sns_icons
  from elements.MainMenu import get_main_menu
  from elements.BlogLinkMenu import get_blog_link_menu
  return f"""
  <header id="sidebar">
  <div id="sidebar-banner">
    <a id="site-logo" href="index.html" target="_self">
      <img alt="Site Logo" src="images/logo-white-small.webp" style="margin: 0 auto;">
    </a>
    <a onclick="showMobileMenu()" id="mobile-menu-button"><p>Menu</p></a>
  </div>
  <div id="sidebar-content">
    {get_main_menu(get_blog_link_menu())}
    <br>
    {get_sns_icons()}
    <br>
  </div>
</header>
  """
