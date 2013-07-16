import os.path
import string
import random
'''
things to add: attack, drop (drops item in that location), better print statements for the abouts, some more monsters, and money system, maybe a store.

i really want to start attacking things soon. so we need to have a health system.

'''
#these are the global variables for the system

name=""
points=0
dead= 0
j=3
relive=1
g=0
contents={}
response=""


#This is what lets you put your name in and then checks your score
def namechecker():
  global name
  name=input("Enter your name please \n")
  if name in ('Aubin','aubin'):
    print("Welcome your highness")
  elif name in ('K','k', 'carolina', 'Carolina'):
    print("Oh...its you, well you can still play me I guess...")
    name="Smelly"
#    while(1):
#      print("Why did you break me ", name)
  else:
    print("Welcome: "+name +"\n You are only allowed to look left, or right, and move forward. \n Good Luck! \n")


def initial(name):
  answer1=input("What is your gender?\n")
  answer2=input("What is your class? \n")
  answer3=100
  name=player(name,answer3,answer1,answer2)
  print("\n")
  print(name.name)
  print(name.classs)
  print(name.gender)
  print(name.health)







#This is for looking specifically at one thing
def look(what):
  global location
  global holder
  print(what.description)


#This if for looking at the entire room
def room_contents_look(what):
  print("************************** \n")
  i=0
  for x in range(len(what.contents)):
    print(what.contents[i].name)
    i=1+i
  print(str(what.east)+" is East")
  print(str(what.north)+" is North")
  print(str(what.west)+" is West")
  print(str(what.south)+" is South")
  print("************************** \n")


#This is the reassurance for trying to quit
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
  while True:
    global relive
    ok = input( prompt + '\n')
    if ok in ('y', 'ye', 'yes'):
      print("you are alive once more!")
      relive=1
      return True
    if ok in ('n', 'no', 'nop', 'nope'):
      print("You chose to be a quitter")
      logfile = open("Highscores.txt", "a")
      logfile.write(str(points)+"\t" + name+"\n")
      logfile.close()
      relive=0
      return False
    retries = retries - 1
    if retries < 0:
      print('You cannot follow instructions')
      return False
    print(complaint)

#This is part of the reassurance from above
def infunc(what_you_want_asked):
  tobeused=input(what_you_want_asked)
  if not ask_ok(tobeused):
#    print("it was false")
    return False
  else:
    return True

#This is so you can check your score with the text file
def scorecheck():
  i=0
  logfile = open("Highscores.txt", "r")
  data=logfile.readlines()
  data.sort(key=lambda l: float(l.split("\t")[0]),reverse=True)
  logfile.close()
  logfile = open("Highscores.txt", "w")
  for x in range(len(data)):
    logfile.write(data[i])
    i=i+1
  logfile.close()
  logfile = open("Highscores.txt", "r")
  print("************************** \n")
  print("The Top Scores so far are: \n")
  for x in range(0,3):
    print(logfile.readline())
  logfile.close()

#These are generic deaths
def crzy_death(how_they_died):
  crazy_death= (name + ", because you decided to "+ how_they_died +" you have incured the wrath of Om' Alde Ashko and he has smited your SOUL!")
  return str(crazy_death)

def gen_death(how_they_died):
  gen_death= (name + ", because you decided to "+ how_they_died +" you have incured the wrath of Om' Alde Ashko and he has smited your SOUL!")
  return str(gen_death)


    
x=10
y=10

def coordinates(direction):
  global x
  global y
  global location
  sav_x=x
  sav_y=y
  if direction == "east":
     x=x+1
  elif direction == "west":
     x=x-1
  elif direction == "north":
     y=y+1
  elif direction == "south":
     y=y-1
  if x == 10 and y==10 :
     location = bedroom
  elif x== 11 and y ==10:
     location = hallway
  elif x== 11 and y == 9:
     location = lair
  else:
     x=sav_x
     y=sav_y
##  print("this is your current X and Y "+str(x)+ ", "+str(y))

#This lets you do your action using the first part of the command and then taking the second part and doing the action


#look command function
def look_command(holder):
  if holder[0]=="look":
    if holder[1] == "east":
      print(location.east)
    elif holder[1] == "west":
      print(location.west)
    elif holder[1] == "south":
      print(location.south)
    elif holder[1] == "north":
      print(location.north)
    elif holder[1]== "around":
      room_contents_look(location)
      if len(location.baddies)>0:
        print(location.baddies[0].name)
        print(location.baddies[0].health)
        

def about_command(holder):
  if holder[0]=="about":
    ff=0
    f=0
    if len(location.baddies)>0:
      if holder[1]==location.baddies[0].name:
        print(location.baddies[0].name)
        print(location.baddies[0].health)
        breaker=1
    breaker=0
    for x in range(0,len(user.contents)):
      for x in range(len(holder)):
        otherholder=str(user.contents[ff]).split()
        if len(user.contents) > 0:
          if len(holder)> f-1:
            if holder[1]==otherholder[0]:
              if len(holder)==3:
                if holder[2]==otherholder[1]:
                  print(user.contents[ff].description)
                  print(location.contents[ff].power)
                  breaker=1
                  break
              else:
                print(user.contents[ff].description)
                print(location.contents[ff].power)
                breaker=1
                break
      ff=ff+1
      if breaker==1:
        breaker=0
        break
    f=0
    ff=0
    for x in range(0,len(location.contents)):
      for x in range(len(holder)):
        otherholder=str(location.contents[ff]).split()
        if len(location.contents) > 0:
          if len(holder)> f-1:
            if holder[1]==otherholder[0]:
              if len(holder)==3:
                if holder[2]==otherholder[1]:
                  print(location.contents[ff].description)
                  print(location.contents[ff].power)
                  breaker=1
                  break
              else:
                print(location.contents[ff].description)
                print(location.contents[ff].power)
                breaker=1
                break
      ff=ff+1
      if breaker==1:
        breaker=0
        break

   
def grab_command(holder):
  check=0
  if holder[0]=="grab":
    print("************************** \n")
    ii=0
#this is where we split the words up and take the seperate words
    for x in range(len(location.contents)):
       otherhold=str(location.contents[ii]).split()
       checker=len(otherhold)
#This is the comparison of each seperate word
       f=0
       for x in range(len(otherhold)):
         if holder[f+1]== otherhold[f]:
           f=f+1
         else:
           checker=checker-1
###################################################################################################
#The input statement is seperated from above and will now make a print statement,append,and delete
##################################################################################################
       if checker==len(otherhold):
         printthis=("You just picked up: ")
         q=0
#This gives you the multiple word object printed out
         for x in range(len(otherhold)):
           printthis=printthis+" "+str(otherhold[q])
           check=1
           q=q+1
         print(printthis)         
         print(location.contents[ii].description)
#This is where you add the item then delete it from the room
         user.contents.append(location.contents[ii])
         del location.contents[ii]
#We break out if we have added an item with these two if statements
         if check==1:
           break
       if check==1:
         break
       else:
         ii=ii+1
         check=0
    if check==0:
      print("There is nothing like that here.\n")

def bag_command(holder):
  if holder[0]=="bag":
    i=0
    print("************************** \n You currently have in your bag:")
    for x in range(len(user.contents)):
      print("a(n) "+str(user.contents[i]))
      i=1+i

def drop_command(holder):
   if holder[0]=="drop":
     hholder=""
     i=1
     for x in range(1,len(holder)):
       hholder=hholder+ str(holder[i])
       i=i+1
       print(hholder)
     if hholder in user.contents:
       user.contents.remove(hholder)
       location.contents.append(hholder)
     else:
       print("found nothing to drop")

def what_you_do(holder):
  global location

#  drop_command(holder)
  try:  

    grab_command(holder)
    bag_command(holder)
    look_command(holder)
    if holder[0]=="go":
      coordinates(holder[1])
  except:
    error=1
  about_command(holder)
  




class Room:
  def __init__(self,name,north="wall",east="wall",west="wall",south="wall",description=""):
    self.name=name
    self.north=north
    self.east=east
    self.west=west
    self.south=south
    self.description=description
    self.contents=list()
    self.baddies=list()
  def __str__(self):
    return str(self.name)

class Object:
  def __init__(self, name, value, description,power):
    self.name=name
    self.value=value
    self.description=description
    self.power=power
  def __str__(self):
    return str(self.name)

class player:
  def __init__(self,name,health,gender,classs):
    self.name=name
    self.health=health
    self.gender=gender
    self.classs=classs
    self.contents=list() 
  def __str__(self):
    return str(self.name)


class monster:
  def __init__(self,name,health,color,classs):
    self.name=name
    self.health=health
    self.color=color
    self.classs=classs
    self.contents=list() 
  def __str__(self):
    return str(self.name)



#these are the Objects in the dungeon

crown = Object("crown", 15000, "a gold crown with many jewels",10)
scepter = Object("King's scepter", 10000, "a silver scepter",30)
vorpel_sword = Object("vorpel sword", 200, "a strange looking sword",1000)
bedpan = Object("bedpan", 3, "a smelly metal bowl",2)
torch= Object("torch", 1, "fire attatched to a stick",78)
shield=Object("shield",200,"will mitigate some damage",300)


#these are the monsters in the dungeon
blob=monster("blob",100,"yellow","warrior" )
blob.contents.append(shield)


commandlist = dict()

commandlist['go']="type go and then a cardinal direction"
commandlist['look']="type look and then a cardinal direction, or around to look around"
commandlist['quit']="type quit and then follow the directions to quit"
commandlist['about']="type about and then what object you want to learn about"
commandlist['bag']="type bag to see whats in your bag"

print(commandlist)





bedroom = Room("King\'s bedroom")
bedroom.description="This is a room fit for a King"
bedroom.east= Room("corridor")
bedroom.contents.append(crown)
bedroom.contents.append(scepter)
bedroom.contents.append(vorpel_sword)
bedroom.contents.append(bedpan)

hallway=Room("corridor")
hallway.description="just a long hallway"
hallway.west=bedroom
hallway.contents.append(torch)
hallway.south=Room("lair")

lair=Room("lair")
lair.description="just a long hallway"
lair.contents.append(torch)
lair.north=hallway
lair.baddies.append(blob)


#this is your player

namechecker()
#initial(name)
#name="aubin"
user=player(name,100,"male", "warrior")


location= bedroom

holder=list
while not response  == "dfhsergghj":
  response=input("Command: ")
  if response == "quit":
    ask_ok("You are about to quit, type no to quit")
    if relive==0:
      response="dfhsergghj"
  holder=(response.split())
  what_you_do(holder)







