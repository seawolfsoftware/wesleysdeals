# wesleysdeals
Website for Wesley's Red Hot Deals &amp; Steals


This website is structured as a single page application. 

The data displayed in the HTML/CSS/JS presentation is served from a Django-driven Python 3.8 back-end.

Two model objects perform the basic operations: Posts and Codes. 

A Post has a Code, which may be one-time or multi-use.
The admin can upload a Code to a Post.
A Code may or may not be associated with a Post at any given time.


Python package requirements:

asgiref==3.3.4
Django==3.2
djangorestframework==3.12.4
gunicorn==20.1.0
Pillow==8.2.0
psycopg2-binary==2.8.6
pytz==2021.1
sqlparse==0.4.1
