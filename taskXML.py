import xml.etree.ElementTree as ET

# Use a context manager for file I/O
with open('movie.xml', 'r') as f:
    tree = ET.parse(f)
root = tree.getroot()

# List all the child tags of the movie element using iter() function
for child in root.iter('movie'):
    print(list(child))

# Print out the movie descriptions using itertext() function
for desc in root.iter('description'):
    print(desc.text)

# Count the number of movies that are favourites and not favourites
fav_count = 0
not_fav_count = 0
for movie in root.iter('movie'):
    if movie.get('favorite') == 'True':
        fav_count += 1
    else:
        not_fav_count += 1

print("Number of favourite movies:", fav_count)
print("Number of non-favourite movies:", not_fav_count)
