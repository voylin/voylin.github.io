import shutil
import os
from time import process_time

pages = {}

main_template = ''
elements = {
  '{{head}}': 'head.html',
  '{{sidebar}}': 'sidebar.html',
  '{{page-title}}': 'page-title.html',
  '{{footer}}': 'footer.html',

  '{{main_menu}}': 'main_menu.html',
  '{{blog_link_menu}}': 'blog_link_menu.html',
  '{{sns-icons}}': 'sns-icons.html',
}


def clear_build():
  for x in os.listdir('docs'):
    if os.path.isdir('docs/' + x):
      shutil.rmtree('docs/' + x)
    else:
      os.remove('docs/' + x)


def prepare_defaults():
  shutil.copyfile('coding-stuff/style.css', 'docs/style.css')
  os.mkdir('docs/posts')
  os.mkdir('docs/images')
  os.mkdir('docs/category')
  for _image in os.listdir('coding-stuff/images'):
    shutil.copyfile('coding-stuff/images/' + _image, 'docs/images/' + _image)


def create_main_template():
  # Creating the main template file.
  global main_template
  file = open('coding-stuff/main_template.html', 'r')
  main_template = file.read()
  file.close()
  for key, value in elements.items():
    element_data = open('coding-stuff/elements/' + value)
    element_string = element_data.read()
    main_template = main_template.replace(key, element_string)
    element_data.close()

def get_breadcrumb(type, page):
  print("Creating breadcrumb for type '{}' and page '{}'".format(type, page))
  breadcrumb = '<a href="index.html"><svg width="12" height="12" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M575.8 255.5C575.8 273.5 560.8 287.6 543.8 287.6H511.8L512.5 447.7C512.5 450.5 512.3 453.1 512 455.8V472C512 494.1 494.1 512 472 512H456C454.9 512 453.8 511.1 452.7 511.9C451.3 511.1 449.9 512 448.5 512H392C369.9 512 352 494.1 352 472V384C352 366.3 337.7 352 320 352H256C238.3 352 224 366.3 224 384V472C224 494.1 206.1 512 184 512H128.1C126.6 512 125.1 511.9 123.6 511.8C122.4 511.9 121.2 512 120 512H104C81.91 512 64 494.1 64 472V360C64 359.1 64.03 358.1 64.09 357.2V287.6H32.05C14.02 287.6 0 273.5 0 255.5C0 246.5 3.004 238.5 10.01 231.5L266.4 8.016C273.4 1.002 281.4 0 288.4 0C295.4 0 303.4 2.004 309.5 7.014L564.8 231.5C572.8 238.5 576.9 246.5 575.8 255.5L575.8 255.5z"/></svg></a>/'
  if type == 'main_pages':
    if page != 'index.html':
      breadcrumb += '<a href="{}">{}</a>'.format(page, page[:-5])
  return breadcrumb

def load_posts():
  # Load all posts and get their main categories and sub categories
  print("Still need to load posts...")

  for x in os.listdir('coding-stuff/posts'):
    post_path = 'posts/' + x
    post_file = open('coding-stuff/' + post_path)
    post_data = post_file.read()
    post_file.close()

    pages['docs/' + post_path] = post_data


def load_pages():
  for x in os.listdir('coding-stuff/main_pages'):
    _origin = 'coding-stuff/main_pages/' + x
    _path = 'docs/' + x
    page = main_template
  
    page_file = open(_origin, 'r')
    page_data = page_file.read().split('#######')
    page_file.close()
  
    page_info = page_data[0].splitlines()
    page_content = page_data[1]
    page = page.replace('{{page_title_text}}', _page_title(page_info))
    page = page.replace('{{content}}', page_content)
    breadcrumb = get_breadcrumb('main_pages', x)
    page = page.replace('{{breadcrumbs}}', breadcrumb)

    if x == '404.html':
      page = '---\npermalink: /404.html\n---\n' + page

    new_page = open(_path, 'w')
    new_page.write(page)
    new_page.close()


def load_blog_category_pages():
  for x in os.listdir('coding-stuff/blog_categories'):
    _origin = 'coding-stuff/blog_categories/' + x
    _path = 'docs/category/' + x
    page = main_template
  
    page_file = open(_origin, 'r')
    page_data = page_file.read().split('#######')
    page_file.close()
  
    page_info = page_data[0].splitlines()
    page_content = page_data[1]
    page = page.replace('{{page_title_text}}', _page_title(page_info))
    page = page.replace('{{content}}', page_content)
    breadcrumb = get_breadcrumb('main_pages', x)
    page = page.replace('{{breadcrumbs}}', breadcrumb)

    page = page.replace('href="style.css"', 'href="../style.css"')
    page = page.replace('src="images', 'src="../images')

    new_page = open(_path, 'w')
    new_page.write(page)
    new_page.close()


def _page_title(page_info):
  page_title_line = 'page_title: '
  for line in page_info:
    if page_title_line in line:
      return line[page_title_line.__len__():]
  return '{{page_title_text}}'


def prepare_site():
  clear_build()
  prepare_defaults()
  create_main_template()
  load_posts()
  load_pages()
  load_blog_category_pages()

prepare_site() 
