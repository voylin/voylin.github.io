import inspect

from Types import get_breadcrumb


def get_main_template(page_title, content=''):
  from elements.Head import get_head
  from elements.Sidebar import get_sidebar
  from elements.PageTitle import get_page_title
  from elements.Footer import get_footer
  return f"""
<!DOCTYPE html>
<html>
  {get_head(page_title)}
  <body>
    {get_sidebar()}
    {get_page_title(page_title, get_breadcrumb(inspect.stack()[1][1]))}
    <main>
      {content}
    </main>
    {get_footer()}
  </body>
</html>
"""
