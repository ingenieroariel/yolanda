import os
import simplejson as json
import wget

base_dir = os.getcwd()
base_url = "https://s3-us-west-2.amazonaws.com/arcmaps/haiyan/"
permissions_string='{"anonymous":"document_readonly","authenticated":"document_readwrite","users":[]}'
csrftoken=''

with open('centroids.json', 'r') as f:
    maps = json.load(f)
    for map in maps:
        url = base_url + map['filename'] + '.pdf'
        #print url
        #filename = wget.download(url)
        #print filename 
        os.system('curl -X POST -F permissions=\'%s\' -F title="%s" -F file=@%s -F csrfmiddlewaretoken=%s -v -c cookies.txt -b cookies.txt http://localhost:8000/documents/upload/' % (permissions_string, map['title'], str(base_dir + '/pdf/' + map['filename'].replace('(', '\(').replace(')', '\)') + '.pdf'), csrftoken))
