from templates.main_template import *
from Types import *


def create_blog_post(page_title, thumb_path, post_date, categories, description, content):
    from elements.Head import get_head
    from elements.Sidebar import get_sidebar
    from elements.PageTitle import get_page_title
    from elements.Footer import get_footer
    
    return BlogPost(
        page_title,
        thumb_path,
        post_date,
        categories,
        description,
        content=f"""
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
    """)
    # TODO: Change this to add specific post stuff like next post, last post, recommended stuff, ...

    
    
