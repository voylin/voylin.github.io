import importlib
import os
import shutil
import Types

from templates.main_template import get_main_template

BUILD_LOCATION = '../docs/'
pages = []
posts = {'all': []}  # Add all categories here


def create_site():
  print('Started building site ...')
  
  print('Cleaning previous build...')
  for x in os.listdir(BUILD_LOCATION):
    if os.path.isdir(BUILD_LOCATION + x):
      shutil.rmtree(BUILD_LOCATION + x)
    else:
      os.remove(BUILD_LOCATION + x)
  print('Cleaned previous build!')
  
  print('Copying resources...')
  shutil.copytree('resources', BUILD_LOCATION, dirs_exist_ok=True)
  print('Resources copied!')
  
  print('Creating pages + posts ...')
  page_paths = []
  post_paths = []
  print(os.listdir('pages'))
  for page in os.listdir('pages'):
    if page not in ["__pycache__", "blog_categories"]:
      page_paths.append('pages/' + page)
  for page in os.listdir('pages/blog_categories'):
    if page not in ["__pycache__"]:
      page_paths.append('pages/blog_categories/' + page)
  for page in os.listdir('posts'):
    if page not in ["__pycache__"]:
      post_paths.append('posts/' + page)
      
  for page in page_paths:  # FOR NORMAL PAGES
    python_file_name = page[:-3].replace('/', '.')
    python_file = importlib.import_module(python_file_name)
    # Create a html page with this data
    page_file = open(BUILD_LOCATION + page.split('/')[-1].replace('.py', '.html'), 'w')
    page_file.write(python_file.get_page())
    page_file.close()
    print('Created html page for page: ' + page + '!')
    
  for page in post_paths:  # FOR POST PAGES
    python_file_name = page[:-3].replace('/', '.')
    python_file = importlib.import_module(python_file_name)
    # Create a html page with this data
    page_file = open(BUILD_LOCATION + page.split('/')[-1].replace('.py', '.html'), 'w')
    page_file.write(python_file.get_post().content)
    page_file.close()
    print('Created html page for page: ' + page + '!')
  print('Pages created!')
  
  print('Finished building site!')


create_site()
