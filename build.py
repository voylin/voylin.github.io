from distutils.command.build import build
from genericpath import isdir, isfile
from pickletools import read_int4
import shutil
import os

# Constants
homepage_title = "Voylin's Life"


pages = []
class page_template:
  title = ''
  content = ''
  destination = ''

  def __init__(self, title, content, destination):
    self.title = title
    self.content = content
    self.destination = destination
    


# Loading block layouts
head = ''
with open('blocks/head.html') as f: head = f.read()
header = ''
with open('blocks/header.html') as f: header = f.read()
footer = ''
with open('blocks/footer.html') as f: footer = f.read()
single = ''
with open('blocks/single.html') as f: single = f.read()



print("Building site")
def cleanup():
  if os.path.isdir('docs'):
    print("Cleaning previous site build ...")
    shutil.rmtree('docs')
    os.mkdir('docs')


print("Copying resources ...")
def copy_resources():
  for file_name in os.listdir('res'):
    source = 'res/' + file_name
    destination = 'docs/' + file_name
    if os.path.isfile(source):
      shutil.copy(source, destination)
      print('copied', file_name)
    elif os.path.isdir(source):
      shutil.copytree(source, destination)
      print('copied', file_name)


print("Building pages ...")
def page_dest(dest, old_name):
  return dest + old_name.replace('.md', '.html')

def page_title(source_name):
  source_name = source_name.removesuffix('.md')
  if source_name == 'index':
    return homepage_title
  return ''


def page_collection():
  # Page collection
  main_dir = 'content/'
  dest_dir = 'docs/'
  for source in os.listdir(main_dir):
    content = ''

    if os.path.isfile(main_dir + source):
      with open(main_dir + source) as f:
        content = f.read()
      pages.append(page_template(page_title(source), content, page_dest(dest_dir, source)))
    else:
      source += '/'
      for sub_source in os.listdir(main_dir + source):
        with open(main_dir + source + sub_source) as f:
          content = f.read()
        pages.append(page_template(page_title(sub_source), content, page_dest(dest_dir, sub_source)))



def page_creation():
  # Page creation
  for page in pages:
    # Single page creation
    final = single
    final = final.replace('{{ Head }}', head)
    final = final.replace('{{ Header }}', header)
    final = final.replace('{{ Content }}', page.content)
    final = final.replace('{{ Footer }}', footer)

    final = final.replace('{{ CSS_Link}}', 'style.css')

    # Replace {{ Title }} by the site top bar title
    final = final.replace('{{ Title }}', page.title)

    with open(page.destination, "w") as file:
      file.write(final) 


cleanup()
copy_resources()
page_collection()
page_creation()