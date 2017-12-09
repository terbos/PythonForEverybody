import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

address = input('Enter location: ')
print("Retrieving", address)
uh = urllib.request.urlopen(address)
data = uh.read();
print("Retrieved", len(data), " characters")

tree = ET.fromstring(data)
counts = tree.findall("comments/comment")
count_sum = 0
count = 0
for item in counts:
    count_sum += int(item.find("count").text)
    count += 1
print("Count", count)
print("Sum:", count_sum)
