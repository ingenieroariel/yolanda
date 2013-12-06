wget -r http://downloads.noah.dost.gov.ph/downloads/
mv downloads.noah.dost.gov.ph/downloads/* .
rm -rf downloads.noah.dost.gov.ph
rename -v 's/ /_/g' * */* */*/* */*/*/*
rename -v 's/ /_/g' * */* */*/* */*/*/* */*/*/*/*
rename -v 's/ /_/g' * */* */*/* */*/*/*
rename -v 's/\]/_/g' * */* */*/* */*/*/*
rename -v 's/\[/_/g' * */* */*/* */*/*/*
for a in `find . -name *.html`; do rm $a; done
for a in `find . -iname *.kmz`; do cd $(dirname $a); unzip $(basename $a); mv doc.kml $(basename $a.kml); cd -; done
for a in `find . -iname *.kmz`; do rm $a; done
for a in `find . -iname *.kml`; do cd $(dirname $a); ogr2ogr $(basename $a.shp) $(basename $a); cd -; done
