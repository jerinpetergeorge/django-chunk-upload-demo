django-chunk-upload-demo
==========================

This is a Django demo project of the `django-chunk-upload <https://github.com/jerinpetergeorge/django-chunk-upload>`__ module.

How to run the demo locally
--------------

1. Clone the repo.

::

    git clone git@github.com:jerinpetergeorge/django-chunk-upload.git
    cd django-chunk-upload/

2. Install the requirements (I suggest using a virtualenv).

::

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

3. Create the tables.

::

    ./manage.py migrate

4. Run the server.

::

    ./manage.py runserver

5. Go to `127.0.0.1:8000 <http://127.0.0.1:8000>`__ and upload a file.

Support
-------

If you find any bug or you want to propose a new feature, please use the `issues tracker <https://github.com/jerinpetergeorge/django-chunk-upload/issues>`__. I'll be happy to help you! :-)
