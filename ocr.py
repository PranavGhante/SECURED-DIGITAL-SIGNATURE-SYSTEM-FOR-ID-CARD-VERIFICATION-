# Extracting text from Image
import ocrspace


api = ocrspace.API()

info = api.ocr_file("newid.jpeg")
words = info.split()

print(info)
print(words)
print(words[24] + words[25])
print(words[15])

key = words[24]
if len(key) < 4:
    key = key + words[25]
print(key)
