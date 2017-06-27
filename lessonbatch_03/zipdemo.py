import zipfile

z = zipfile.ZipFile('c:\\users\\chris\\downloads\\zip file.zip', 'r')
print(z.comment)

for f in z.infolist():
    print(f.comment)
