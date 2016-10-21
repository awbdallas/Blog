# Blog README
==================


## About
--------------

The first commit is all from the pyramid_blogr tutorial. Anything past that is
things I've added. 

Link to said tutorial: http://docs.pylonsproject.org/projects/pyramid-blogr/en/latest/


## Starting Development
---------------

##### Virtual ENV and Directory
```bash
mkdir blog
cd blog
mkdir blog_env
export VENV=$(pwd)/blog_env/env
pyvenv $VENV
git clone  https://github.com/awbdallas/Blog.git
```


##### Launching Environment

- cd to cloned directory containing setup.py

- $VENV/bin/pip install -e .

- $VENV/bin/initialize_pyramid_blogr_db development.ini

- $VENV/bin/pserve development.ini
