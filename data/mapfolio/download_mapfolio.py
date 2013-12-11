import os
import simplejson as json
import wget
from django.core.files import File
from geonode.documents.models import Document
from django.contrib.auth.models import User
from datetime import datetime

base_dir = os.getcwd()
base_url = "https://s3-us-west-2.amazonaws.com/arcmaps/haiyan/"
permissions_string='{"anonymous":"document_readonly","authenticated":"document_readwrite","users":[]}'
csrftoken=''

with open('centroids.json', 'r') as f:
    maps = json.load(f)
    for map in maps:
        url = base_url + map['filename'] + '.pdf'
        print url
        filename = wget.download(url)
        print filename
        file = open(filename)
        djangofile = File(file)
        doc = Document()
        doc.title = map['title']
        doc.abstract = map['description']
        doc.doc_file = djangofile
        doc.owner = User.objects.all()[0]
        doc.date =  datetime.strptime(map['date'], '%m/%d/%Y')
        doc.bbox_x0 = map['longitude']
        doc.bbox_y0 = map['latitude']
        doc.bbox_x1 = map['longitude'] 
        doc.bbox_y1 = map['latitude']
        doc.save()
