from matplotlib import pyplot as plt
 
# years = [1950,1952,1947,1960,1970,2005,2006,2007]
# gdp= [300.2,56.2,897.2,456,145.3,158,1456.2,4788.0]

# plt.plot(years,gdp,color = 'red',marker='o',linestyle='dotted')

# plt.title("GDP FOR YEARS")

# plt.xlabel("years ")
# plt.ylabel("amount in billions")

# plt.show()

movies = ['ah','fd','ghj','df','hum hian na ']
num_koscar = [5,77,4,66,9]

plt.bar(movies,num_koscar,color='black')

plt.title("movies")
plt.xticks(range(len(movies)),movies)
plt.show()