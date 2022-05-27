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
  
    new_page = open(_path, 'w')
    new_page.write(page)
    new_page.close()


def load_blog_category_pages():
  print('Still need to load blog pages...')


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
