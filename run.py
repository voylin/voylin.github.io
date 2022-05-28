from glob import glob
import shutil
import os
from time import process_time

main_template = ''
splitter = '#######'
pages = []
sitemap = "https://voylin.github.io/\n"
categories = {
  'voylins_life': ['voylins_life.html', 'Voylin\'s Life'],
  'our_life': ['our_life.html', 'Our Life'],
  'nihongo_de': ['nihongo_de.html', '日本語で'],
  'learn_japanese': ['learn_japanese.hmtl', 'Learn Japanese'],
  'travel_advice': ['travel_advice.html', 'Travel Advice'],
}
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
  for x in ['posts', 'images']:
    os.mkdir('docs/{}'.format(x))
  for _image in os.listdir('coding-stuff/images'):
    shutil.copyfile('coding-stuff/images/' + _image, 'docs/images/' + _image)

def load_pages():
  global pages
  for x in os.listdir('coding-stuff/posts'): pages.append('posts/{}'.format(x))
  for x in os.listdir('coding-stuff/main_pages'): pages.append('main_pages/{}'.format(x))
  for x in os.listdir('coding-stuff/blog_categories'): pages.append('blog_categories/{}'.format(x))


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

def get_breadcrumb(type, page, category = ''):
  breadcrumb = '<a href="index.html"><svg width="12" height="12" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M575.8 255.5C575.8 273.5 560.8 287.6 543.8 287.6H511.8L512.5 447.7C512.5 450.5 512.3 453.1 512 455.8V472C512 494.1 494.1 512 472 512H456C454.9 512 453.8 511.1 452.7 511.9C451.3 511.1 449.9 512 448.5 512H392C369.9 512 352 494.1 352 472V384C352 366.3 337.7 352 320 352H256C238.3 352 224 366.3 224 384V472C224 494.1 206.1 512 184 512H128.1C126.6 512 125.1 511.9 123.6 511.8C122.4 511.9 121.2 512 120 512H104C81.91 512 64 494.1 64 472V360C64 359.1 64.03 358.1 64.09 357.2V287.6H32.05C14.02 287.6 0 273.5 0 255.5C0 246.5 3.004 238.5 10.01 231.5L266.4 8.016C273.4 1.002 281.4 0 288.4 0C295.4 0 303.4 2.004 309.5 7.014L564.8 231.5C572.8 238.5 576.9 246.5 575.8 255.5L575.8 255.5z"/></svg></a>/'
  if type in ['main_pages', 'blog_categories']:
    if page != 'index.html':
      breadcrumb += '<a href="{}">{}</a>'.format(page, page[:-5].replace('_', ' ').title())
  elif type == 'post':
    breadcrumb += '<a href="{}">{}</a>/<a href="{}">{}</a>'.format(categories[category][0], categories[category][1].title(), page, page[:-5].replace('_', ' ').title())

  return breadcrumb


def create_pages():
  global pages
  global sitemap
  for x in pages:
    page = main_template

    _origin = 'coding-stuff/{}'.format(x)
    _folder = x.split('/')[0]
    _filename = x.split('/')[1]
    _path = 'docs/' + _filename
    sitemap = sitemap + "https://voylin.github.io/{}\n".format(_filename)
    
    __file__ = open(_origin, 'r')
    _raw_page = __file__.read()
    __file__.close()

    page_info = {}
    page_content = 'empty'
    if splitter in _raw_page:
      for line in _raw_page.split(splitter)[0].split('\n'):
        if line != '':
          page_info[line.split(': ')[0]] = line.split(': ')[1]
      page_content = _raw_page.split(splitter)[1]
    else:
      print('ERROR for page: {}, no \'{}\'!'.format(x, splitter))
      page_content = _raw_page
    

    if 'page_title' in page_info.keys():
      page = page.replace('{{page_title_text}}', page_info['page_title'])
    else:
      print('ERROR: Page {} has no title!')
    
    page = page.replace('{{content}}', page_content)

    if _folder == 'posts':
      if 'category' in page_info.keys():
        page = page.replace('{{breadcrumbs}}', get_breadcrumb(_folder, _filename, page_info['category']))
      else: print('ERROR: Post {} has no category!')
    else:
      page = page.replace('{{breadcrumbs}}', get_breadcrumb(_folder, _filename))

    if _filename == '404.html': page = '---\npermalink: /404.html\n---\n' + page

    new_page = open(_path, 'w')
    new_page.write(page)
    new_page.close()


def create_sitemap():
  global sitemap
  new_sitemap = open('docs/sitemap.txt', 'w')
  new_sitemap.write(sitemap)
  new_sitemap.close()
  # We also need to copy the Google Search Console file
  shutil.copyfile('coding-stuff/googlea54fd002d933074e.html', 'docs/googlea54fd002d933074e.html')


def prepare_site():
  clear_build()
  prepare_defaults()
  load_pages()
  create_main_template()
  create_pages()
  create_sitemap()

prepare_site() 
