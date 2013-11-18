Yolanda
========================

Setup notes
===========

Installed GeoNode

.. code-block:: bash

    sudo apt-get update
    sudo add-apt-repository ppa:geonode/testing
    sudo apt-get install geonode
    sudo geonode-updateip 54.254.204.189


Created a custom project

.. code-block:: bash

    cd /usr/src
    sudo django-admin startproject yolanda --template=https://github.com/GeoNode/geonode-project/archive/master.zip -epy,rst
    sudo chown -R ubuntu:ubuntu yolanda


Put it under version control
.. code-block:: bash
 sudo apt-get install git
 cd /usr/src/yolanda
 git init
 git add *
 git commit -m "Initial commit"
 sudo pip install -e .

Made it access '''/etc/geonode/local_settings'''
.. code-block:: bash
 sudo ln -s /etc/geonode/local_settings.py /usr/src/yolanda/yolanda/local_settings.py
 
Modified local_settings.py to access this project's templates and static files
.. code-block:: python
 LOCAL_ROOT = os.path.abspath('/usr/src/yolanda/yolanda')
 GEONODE_ROOT = os.path.dirname(geonode.__file__)
 
 TEMPLATE_DIRS = (
 '/etc/geonode/templates',
 os.path.join(LOCAL_ROOT, 'templates'),
 os.path.join(GEONODE_ROOT, 'templates'),
 )
 
 STATICFILES_DIRS = [
 '/etc/geonode/media',
 os.path.join(LOCAL_ROOT, 'static'),
 os.path.join(GEONODE_ROOT, 'static'),
 ]

Modified /var/www/geonode/wsgi/geonode.wsgi to use this project's settings
.. code-block:: python
 os.environ['DJANGO_SETTINGS_MODULE'] = 'yolanda.settings'

Restarted Apache for the changes to take effect:
.. code-block:: bash
 sudo service apache2 restart
