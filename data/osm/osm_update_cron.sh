cd /geovol/osm/download
mv philippines-latest.osm.pbf philippines-latest.osm.pbf.old
wget http://download.geofabrik.de/asia/philippines-latest.osm.pbf
cd /geovol/osm/geofabrik
time geogit osm import ../download/philippines-latest.osm.pbf
time geogit add
time geogit commit -m "Update PH OSM from geofabrik"
time geogit osm map ../mapping.json
rm -rf *
time geogit shp export buildings_osm buildings_osm.shp
time geogit shp export damage_lines damage_lines.shp
time geogit shp export damage_polygons damage_polygons.shp
time geogit shp export hospital_points hospital_points.shp
time geogit shp export hospital_polygons hospital_polygons.shp
time geonode importlayers -u boundless -o *.shp
