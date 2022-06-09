#!/bin/bash

echo 'File_name: (date_title)'
read filename
cp coding-stuff/post_content_template.html coding-stuff/posts/$filename.html
