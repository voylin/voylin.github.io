def get_page():
  from templates.main_template import get_main_template
  
  return get_main_template(
    page_title='Whoops, something went wrong there!',
    content="""
    <p>Sorry about that, this page does not exist.</p>
    """)
    