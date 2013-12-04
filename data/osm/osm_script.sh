time geogit osm download --bbox 4.58748 116.928 21.1215 126.606 --saveto ./yolanda-osm.xml --keep-files
time geogit osm import ./yolanda-osm.xml
time geogit add
time geogit commit -m "Initial add PH OSM"
