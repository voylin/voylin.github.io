def get_page_title(page_title_text, breadcrumbs):
  return f"""
  <div id="page-title">
  <div class="title">{page_title_text}</div>
  <div id="breadcrumbs">{breadcrumbs}</div>
</div>"""
