import xml.etree.ElementTree as ET

# Read in the movie.xml file
tree = ET.parse('movie.xml')
root = tree.getroot()

# List all the child tags of the movie element using iter() function
for child in root.iter('movie'):
    print(list(child))

# Print out the movie descriptions
for desc in root.findall('.//description'):
    print(desc.text)

# Use a dictionary to count the number of favourites
fav_count = 0
counts = {'True': 0, 'False': 0}

for movie in root.iter('movie'):
    is_fav = movie.get('favorite') == 'True'
    counts[str(is_fav)] += 1
    if is_fav:
        fav_count += 1

print("Number of favourite movies:", counts['True'])
print("Number of non-favourite movies:", counts['False'])
