import shutil
import os

main_template = ''
post_card_template = ''
splitter = '#######'
pages = []
sitemap = "https://voylin.github.io/\n"


posts = {
    'voylins_life': [],
    'our_life': [],
    'travel_advice': [],
    'learning_japanese': [],
    'nihongo_de': [],
    'all': []
    }
card_types = [
    '{{blog-post-card-all}}',
    '{{blog-post-card-voylins_life}}',
    '{{blog-post-card-our_life}}',
    '{{blog-post-card-travel-advice}}',
    '{{blog-post-card-learn-japanese}}',
    '{{blog-post-card-nihongo-de}}']



def get_breadcrumb(type, page, category = ''):
  breadcrumb = '<a href="index.html"><svg width="12" height="12" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path d="M575.8 255.5C575.8 273.5 560.8 287.6 543.8 287.6H511.8L512.5 447.7C512.5 450.5 512.3 453.1 512 455.8V472C512 494.1 494.1 512 472 512H456C454.9 512 453.8 511.1 452.7 511.9C451.3 511.1 449.9 512 448.5 512H392C369.9 512 352 494.1 352 472V384C352 366.3 337.7 352 320 352H256C238.3 352 224 366.3 224 384V472C224 494.1 206.1 512 184 512H128.1C126.6 512 125.1 511.9 123.6 511.8C122.4 511.9 121.2 512 120 512H104C81.91 512 64 494.1 64 472V360C64 359.1 64.03 358.1 64.09 357.2V287.6H32.05C14.02 287.6 0 273.5 0 255.5C0 246.5 3.004 238.5 10.01 231.5L266.4 8.016C273.4 1.002 281.4 0 288.4 0C295.4 0 303.4 2.004 309.5 7.014L564.8 231.5C572.8 238.5 576.9 246.5 575.8 255.5L575.8 255.5z"/></svg></a>/'
  if type in ['main_pages', 'blog_categories']:
    if page != 'index.html':
      breadcrumb += '<a href="{}">{}</a>'.format(page, page[:-5].replace('_', ' ').title())
  elif type == 'posts':
    breadcrumb += '<a href="{}">{}</a>/<a href="{}">{}</a>'.format(categories[category][0], categories[category][1], page, page[:-5].replace('_', ' ').title())

  return breadcrumb


def create_post_cards():
  global posts
  # We first create them but later on edit those files 
  for post_file in os.listdir('coding-stuff/posts'):
    _file = open('coding-stuff/posts/{}'.format(post_file), 'r')
    _file_data = _file.read()
    _file.close()
    post_info = {}
    for _line in _file_data.split(splitter)[0].split('\n'):
      if _line != '':
        post_info[_line.split(': ')[0]] = _line.split(': ')[1]

    temp_card = post_card_template
    temp_card = temp_card.replace('{{url}}', post_file)
    temp_card = temp_card.replace('{{title}}', post_info['page_title'])
    temp_card = temp_card.replace('{{thumb}}', 'images/posts/' + post_info['thumb'] + '.webp')
    temp_card = temp_card.replace('{{date}}', post_info['date'])
    temp_card = temp_card.replace('{{description}}', post_info['description'][:200]) # Adding a description limiter
    temp_card = temp_card.replace('{{category_url}}', categories[post_info['categories'].split(', ')[0]][0])
    temp_card = temp_card.replace('{{category_title}}', categories[post_info['categories'].split(', ')[0]][1])
    # Adding the cards to posts so we can easily add them later
    posts['all'].append(temp_card)
    for post_cat in post_info:
      posts[post_cat] = temp_card


def create_pages():
  global sitemap

  # Loading all pages
  pages = []
  for x in os.listdir('coding-stuff/posts'): pages.append('posts/{}'.format(x))
  for x in os.listdir('coding-stuff/main_pages'): pages.append('main_pages/{}'.format(x))
  for x in os.listdir('builder/pages/blog_categories'): pages.append('blog_categories/{}'.format(x))


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
          if line.split(': ')[0] == "categories":
            page_info['categories'] = page_info['categories'].split(',')
      page_content = _raw_page.split(splitter)[1]
    else:
      print('ERROR for page: {}, no \'{}\'!'.format(x, splitter))
      page_content = _raw_page
    

    if 'page_title' in page_info.keys():
      page = page.replace('{{page_title_text}}', page_info['page_title'])
    else:
      print('ERROR: Page {} has no title!')
    
    page = page.replace('{{breadcrumbs}}', get_breadcrumb(_folder, _filename,  page_info['categories'][0] if _folder == 'posts' else ''))
    page = page.replace('{{content}}', page_content)

    # Populate all post cards on pages
    for card_type in card_types:
      _type = card_type.removeprefix('{{blog-post-card-').removesuffix('}}')
      for nr in range(page.count(card_type)):
        if len(posts[_type]) > nr: 
          page = page.replace(card_type, posts[_type][nr], 1)
        else: page = page.replace(card_type, '') # If not enough posts, delete the {{...}} tags

    # Inserting youtube videos
    while page.find('{{yt-video:') != -1:
      video_id = ''
      index = page.find('{{yt-video:') + len('{{yt-video:')
      while page[index] != '}':
        video_id += page[index]
        index += 1
      _file = open('coding-stuff/extra-elements/yt-video.html', 'r')
      page = page.replace('{{yt-video:' + video_id + "}}", _file.read())
      _file.close()
      page = page.replace('{{yt-id}}', video_id)
      

    # Page exceptions
    if _filename == '404.html.html': page = '---\npermalink: /404.html.html\n---\n' + page

    # Creating the page
    new_page = open(_path, 'w')
    new_page.write(page)
    new_page.close()


def create_sitemap(): # Search engine stuff
  global sitemap
  new_sitemap = open('docs/sitemap.txt', 'w')
  new_sitemap.write(sitemap)
  new_sitemap.close()
  # We also need to copy the Google Search Console file
  shutil.copyfile('coding-stuff/googlea54fd002d933074e.html', 'docs/googlea54fd002d933074e.html')


def prepare_site():
  clear_build()
  prepare_defaults()
  create_main_template()
  create_post_card_template()
  create_post_cards()
  create_pages()
  create_sitemap()

prepare_site() 
