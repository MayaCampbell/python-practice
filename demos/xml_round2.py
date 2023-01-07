#use library element tree
import xml.etree.ElementTree as ET

#create tree structure
tree= ET.parse('movies.xml')

#start from root of tree and access branchs to path system
root= tree.getroot()

#take a look and see what is in the file(see basic structure of file)
#print(ET.tostring(root,encoding='utf8').decode('utf8'))#give whole xml as a string
#print(root.tag) #giving us the name of the element tage
#print(root.attrib) #giving us the element attributes in a dictionaty
############################blank dictiontay means no attributes
#print(len(root)) #how many children the element has
#print([elem.tage for elem in root.iter()]) #gives us long list of all elements(no heirarchy)

#see list of all movies in genre
for movie in root.iter('movies'): #pass in movie tag
    #print(movie.attrib)
#get text in rating
#for rating in root.iter('rating'): #iterating and printing values
    #print(rating.text)
    pass

#find the rating of PG
#for rating in root.findall("./genre/decade/movie/[rating = 'PG']"): #findall() - travers immeditae children of reference element
    #print(rating.attrib)
    pass
#change title KARATE KID to Karate Kid
#kkid= root.find("./genre/decade/movie[@title= 'THE KARATE KID']") #key:value pair = attribute
#kkid.attrib['title']= "The Karate Kid"
#print(kkid.attrib) #check to see if it was changed
 #adding a new genre
anime_genre=ET.SubElement(root,'genre') #create new genre tag
#print(ET.tostring(anime_genre, encoding='utf8').decode('utf8')) #check to see if it was created

anime_genre.attrib['category']='Anime' #name anime genre attribute
#print(ET.tostring(anime_genre, encoding='utf8').decode('utf8')) #check to see if it was named
#######################################################################################################################################################################
########################################################################################################################
#Create new decade within new genre and move "Batmen Returns" into decade in Anime
add= root.find("./genre[@category= 'Anime']")
#print(add)

new_decade = ET.SubElement(add,'decade')
#print(new_decade)

new_decade.attrib['years'] = '2020s'
#for genre in root.findall("./genre"): 
    #print(genre.attrib)

#print(ET.tostring(add, encoding='utf8').decode('utf8'))

batman = root.find("./genre/decade/movie[@title='Batman Returns']")
print(batman)
decade2020= root.find("./genre[@category='Batman Returns']/decade[@years='2020s']")
decade2020.append(batman)
#decade1990 = root.find("./genre[@category='Action']/decade[@years='1990s']")
#decade1990.remove(batman)

print(ET.tostring(add, encoding='utf8').decode('utf8'))