import simplejson as json
import wget

base_url = "https://s3-us-west-2.amazonaws.com/arcmaps/haiyan/"

with open('centroids.json', 'r') as f:
    maps = json.load(f)
    for map in maps:
        url = base_url + map['thumb'][:-10] + '.pdf'
        filename = wget.download(url)
        print filename 
        
