def main():
    print('Do I remember?')
    return 0

inty = 5
listy = [6, 7]

striny = 'Hi!'.capitalize()

import folium
azores = folium.folium.Map(location = (38, -27), zoom_start = 6)
print(folium.__file__) # Library path.
# azores.save('output.html')

# House Class.
class House:
    def __init__(self, wall_area):
        self.wall_area = wall_area

# Paint Class.
class Paint:
    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color
    
    def total_price(self):
        if self.color == 'white':
            return self.buckets*1.99
        else:
            return self.buckets*2.19

# Person Class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age