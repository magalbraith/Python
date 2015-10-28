
#import get_stop_words
#$ python setup.py install
 

countries = ["england","ireland","wales","scotland","france","italy","argentina","uruguay","tonga","samoa","new zealand","australia","namibia","south africa","fiji","japan","usa","georgia","canada","romania"]

name = raw_input('What is your name? ')
print ("Hi " + name)

reply = raw_input("Are you watching the World Cup Rugby? ")

if (reply == "Yes") or (reply == "yes"): 
    reply = raw_input("Which country do you want to win?")
    
    if reply.lower() in countries:
        print ("I want " + reply + " to win too!")
    else:
        print "That country is not in the World Cup, berk!"
    
if (reply == "No") or (reply == "no"):
    sport = raw_input ("Which sport do you follow then? ")
    sport = raw_input ("Which country is the best at " + sport + "?")
if (reply == " "):
    print "I knew that!"


   
    #if name of country is not in the list worldCupCountry, display message "That country is not in the World Cup, burke!"  If it is in the list, say, "I want" + name of country "to win too" if it is New Zealand if it is not New Zealand then print "No! Not" + name of country "they don't stand a chance"


#or (reply == "New Zealand")
    #country = raw_input ("New Zealand")
        
        
#print ("Is that " + sport + "?") 
    
#print("Do you know the National Anthem for [allCountries]?")


# import libraries:

# import countries
# import list of sports
# import list of national anthems
# import stop words
#import wikipedia
#>>> print wikipedia.summary("Wikipedia")
#C:\Python27\python.exe Rugby.py
#set variables
#   string worldCupCountry
#   string allCountries
#   string allSport
#   string sport
#   string allAnthem

#list of rugby teams in 2015 World Cup https://en.wikipedia.org/wiki/2015_Rugby_World_Cup
#list of sports that have a world competition https://en.wikipedia.org/wiki/List_of_world_sports_championships
# list of all national anthems with audio https://en.wikipedia.org/wiki/List_of_national_anthems

#>>>import py country
#>>>len(py country.countries)
#249
#>>>list(pycountries.country)[0]
#cpy country.db countryobject



#worldCupCountry 0 = Eng 1 = Ire  2 = Wal  3 = Sco 4 = Fra 5 = Ita 6 = Arg 7 = Uru 8 = Ton 9 = Sam 10 = NZ 11 = Aus 12 = Nam 13 = SA 14 = Fij 15 = Jap 16 = USA 17 = Geo 18 = Can 19 = Rom

   #>>> wikipedia.search("Rugby World Cup 2015")
    
#allSport = [0] #imported from wikipedia 
#allAnthem = [0]
#allCountries = [0]
#true = yes
#n = false



#retrieve(https://en.wikipedia.org/wiki/2015_Rugby_World_Cup[worldCupCountry, [, reporthook[, data]]])
    #worldCupCountry = [0]
#print ["worldCupcountry"]
    
#elif no =
#print ("Which sport do you follow?")
#print [allSport]

#print ("Which country is the best in the World for [allSport]?")
#print [allCountries]

#print("Do you know the National Anthem for [allCountries]?")

# if n = (play anthem)
#retrieve(https://en.wikipedia.org/wiki/2015_Rugby_World_Cup[worldCupCountry, [, reporthook[, data]]])
# if y = (find anthem)
#retrieve(https://en.wikipedia.org/wiki/List_of_#national_anthems, [, reporthook[, data]]])
