cities = ['mumbai', 'new york', 'paris']
countries = ['india', 'usa', 'france']

z =  zip(cities, countries)  #this zip fuinction will zip two list together

print(z)
for i in z:
    print(i)

d = {city:country for city , country in zip(cities, countries)}
print(d)
