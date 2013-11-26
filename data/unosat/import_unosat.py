import lxml.html
from lxml import etree
import urllib2
import StringIO

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
    
    print map_info_url
    print map_title
    print map_title
    print map_date

    map_attributes = map_info.xpath("//table/tr/td/text()")
    for attribute in map_attributes:
        print attribute.strip()
    
    print
