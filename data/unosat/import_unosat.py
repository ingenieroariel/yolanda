import lxml.html
from lxml import etree
import urllib2
import StringIO
import wget
from urlparse import urlparse
import os

url = "http://www.unitar.org/unosat/maps/PHL"

html = urllib2.urlopen(url).read()
parser = etree.HTMLParser()
tree   = etree.parse(StringIO.StringIO(html), parser)
maps = tree.xpath('//ul/li/span/span/a')
for map in maps:
    map_xpath = map.xpath
    res = {}
    map_info_url = map_xpath('@href')[0]
    map_title = map_xpath('text()')[0]
    map_html = urllib2.urlopen(map_info_url).read()
    map_tree = etree.parse(StringIO.StringIO(map_html), parser)
    map_info = map_tree.xpath("//div[@class='view-header']")[0]
    map_title = map_info.xpath("//h3/text()")[0]
    map_date = map_info.xpath("//h3/following-sibling::node()")[0]
    
    print "URL=" + map_info_url
    print "TITLE=" + map_title
    print "DATE=" + map_date

    map_attributes = map_info.xpath("//table/tr/td/text()")
    text = ""
    for attribute in map_attributes:
        attribute_text = attribute.strip()
        if len(attribute_text.split(':')) > 1:
            try:
                attribute_key, attribute_value = attribute_text.split(':')
                print "key=" + attribute_key.encode('utf-8').strip() + " value=" + attribute_value.encode('utf-8').strip()
            except ValueError:
                if attribute_text.startswith('Map Scale for A3'):
                    pass
                else:
                    text += attribute_text.strip() 
        else:
            if attribute_text.startswith('FootPrint'):
                pass
            elif attribute_text.startswith('Product Links'):
                pass 
            elif attribute_text.startswith('Analysis conducted'):
                pass
            else:
                text += attribute_text.strip()
    
    print "TEXT=" + text 

    map_links = map_info.xpath("//table/tr/td/small/a")
    for link in map_links:
        link_url = link.xpath('@href')[0]
        link_type = link.xpath('text()')[0]
        print "LINK=" + link_type.encode('utf-8').strip(), link_url.encode('utf-8').strip()
        filename = link_url.split('/')[-1]
        if os.path.exists(filename) == False:
            filename = wget.download(link_url)
        print filename
    print
