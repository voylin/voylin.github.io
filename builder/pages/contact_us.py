def get_page():
  from templates.main_template import get_main_template
  return get_main_template(
    page_title='Contact us',
    content="""
<p>We can not promise that we will reply within a day, nor a week. We have a busy life full of adventures. But we will reply if needed and we will try our best to not let you wait too long.</p>
<iframe src="https://docs.google.com/forms/d/e/1FAIpQLScmYKh0BMBI9r4H4Es2xI0Npd2-V1ZbthEDmx-IrPvLAKKCcw/viewform?embedded=true" width="100%" height="1000" frameborder="0" marginheight="0" marginwidth="0">Loading form …</iframe>
""")