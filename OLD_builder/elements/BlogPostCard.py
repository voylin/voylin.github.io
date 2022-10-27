def get_blog_link_menu(category_title, category_url, date, url, description, thumb, title):
  return f"""
<div class="blog-post-block">
  <a href="{url}"><img src='{thumb}' alt="post-image"></a>
  <a class="blog-card-title" href="{url})"><p>{title}</p></a>
  <p><a href="{category_url}">{category_title}</a> <span style="float:right;" class="blog-card-date">{date}</span></p>
  <p>{description}<a href="{url}">... (read more)</a></p>
</div>"""
