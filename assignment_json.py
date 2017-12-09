import urllib.request, urllib.parse, urllib.error
import json

address = input('Enter location: ')
print("Retrieving", address)
uh = urllib.request.urlopen(address)
data = uh.read();
print("Retrieved", len(data), " characters")

info = json.loads(data)
count_sum = 0
count = 0
for items in info["comments"]:
    count_sum += int(items["count"])
    count += 1

print("Count", count)
print("Sum:", count_sum)
