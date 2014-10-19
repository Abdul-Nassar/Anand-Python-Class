import zipfile
import sys
a = sys.argv[1]
zip = zipfile.ZipFile(a, 'w')
for i in range(2, len(sys.argv):
	zip.write(sys.argv[i])
