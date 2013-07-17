import os.path
import string
import random
'''
things to add: attack, better print statements for the abouts, some more monsters, and money system, maybe a store.

i really want to start attacking things soon. so we need to have a health system.

'''
#these are the global variables for the system

name=""
points=0
lives=3
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
  print("************************** \n")
  print("The your score is: "+ str(points))
  
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
  elif x== 11 and y == 8:
     location = keep
  else:
     x=sav_x
     y=sav_y
  print("this is your current X and Y "+str(x)+ ", "+str(y))

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
      if location.baddies:
          print(location.baddies.name)
          print(location.baddies.health)
          print(location.baddies.damage)

def about_command(holder):
  if holder[0]=="about":
    if location.baddies:
      if holder[1]==location.baddies.name:
        print(location.baddies.name)
        print(location.baddies.health)
        print(location.baddies.damage)
    holder.remove("about")
    otherholder=' '.join(holder) 
    if otherholder in user.contents:
      print("in my bag")
      print(user.contents[user.contents.index(otherholder)].description)
    if otherholder in location.contents:
      print("in this room")
      print(location.contents[location.contents.index(otherholder)].description) 
      
def grab_command(holder):
  if holder[0]=="grab":
    holder.remove("grab")
    otherholder=' '.join(holder) 
    if otherholder in location.contents:
      user.contents.append(location.contents[location.contents.index(otherholder)])
      location.contents.remove(otherholder)
      print(user.contents[user.contents.index(otherholder)].description)

def equip_command(holder):
  if holder[0]=="equip":
    holder.remove("equip")
    otherholder=' '.join(holder)     
    if otherholder in user.contents:
      if user.contents[user.contents.index(otherholder)].equip == "shield":
        user.shield = user.contents[user.contents.index(otherholder)]
        user.contents.remove(otherholder)
        print("you just equipped a(n) "+str(otherholder)+" which "+str(user.shield.description))
      elif user.contents[user.contents.index(otherholder)].equip == "weapon":
        user.weapon = user.contents[user.contents.index(otherholder)]
        user.contents.remove(otherholder)
        print("you just equipped a(n) "+str(otherholder)+" which "+str(user.shield.description))

def unequip_command(holder):
  if holder[0]=="unequip":
    holder.remove("unequip")
    otherholder=' '.join(holder)     
    if otherholder == user.weapon:
        user.contents.append(user.weapon)
        user.weapon=""
        print("you just took off a(n) "+str(otherholder))
    elif otherholder == user.shield:
        user.contents.append(user.shield)
        user.shield=""
        print("you just took off a(n) "+str(otherholder))

        
      
def bag_command(holder):
  if holder[0]=="bag":
    i=0
    print("************************** \n You currently have in your bag:")
    for x in range(len(user.contents)):
      print("a(n) "+str(user.contents[i]))
      i=i+1
    print("************************** \n You currently have equipped:")
    print("a(n) "+str(user.shield)+" as your shield")
    print("a(n) "+str(user.weapon)+" as your weapon")

def drop_command(holder):
  if holder[0]=="drop":
    holder.remove("drop")
    otherholder=' '.join(holder)
    if otherholder in user.contents:
      location.contents.append(user.contents[user.contents.index(otherholder)])
      user.contents.remove(otherholder)
      print("you just dropped "+ otherholder + " in the " +str(location))
def help_command(holder):
  if holder[0]=="help":
    if len(holder)>1:
      holder.remove("help")
      otherholder=' '.join(holder)
      if otherholder in commandlist:
        print(commandlist[otherholder])
    else:
      print(commandlist)
      
      
def attack_command(holder):
  global response
  global lives
  global points
  if holder[0]=="attack":
    holder.remove("attack")
    otherholder=' '.join(holder)
    neitherdead=0
    if otherholder == location.baddies:
      yourhealth=int(user.health) + int(user.shield.power)
      yourdamage=int(user.weapon.power)
      monsterdamage=int(location.baddies.damage)
      monsterhealth=int(location.baddies.health)
    while neitherdead==0:
      monsterhealth=monsterhealth-yourdamage
      print("you just attacked "+str(location.baddies.name) +" with: "+ str(user.weapon.name))
      if monsterhealth<1:
        print("you have just killed "+str(location.baddies.name))
        print("you have found :")
        points=points+int(location.baddies.health)
        for item in location.baddies.contents:
          print(item)
          print(item.description)
          user.contents.append(item)
          location.baddies=None
        break
      yourhealth=yourhealth-monsterdamage
      print(str(location.baddies.name)+" just attacked you")
      if yourhealth<1:
        print("you have just been killed by "+str(location.baddies.name))
        lives=lives-1
        if lives<0:
          response="dfhsergghj"
          break
        print("you only have: "+str(lives)+" lives/life left")
        break
      print(yourhealth)
      print(monsterhealth)
      
    
    
def what_you_do(holder):
  global location
  if holder[0]=="go":
    coordinates(holder[1])
  help_command(holder)
  unequip_command(holder)
  drop_command(holder)  
  equip_command(holder)
  grab_command(holder)
  bag_command(holder)
  look_command(holder)
  about_command(holder)
  attack_command(holder)
  if holder[0]=="points":
    scorecheck()



class Room:
  def __init__(self,name,north="wall",east="wall",west="wall",south="wall",description=""):
    self.name=name
    self.north=north
    self.east=east
    self.west=west
    self.south=south
    self.description=description
    self.contents=list()
    self.baddies=None
  def __str__(self):
    return str(self.name)

class Object:
  def __init__(self, name, value, description, power, equip="item"):
    self.name=name
    self.value=value
    self.description=description
    self.power=power
    self.equip=equip

  def __str__(self):
    return str(self.name)

  def __eq__(self,other):
    return self.name == other
    
  
  
class player:
  def __init__(self,name,health,gender,classs):
    self.name=name
    self.health=health
    self.gender=gender
    self.classs=classs
    self.contents=list() 
    self.shield=""
    self.weapon=""
  def __str__(self):
    return str(self.name)


class monster:
  def __init__(self,name,health,color,classs):
    self.name=name
    self.health=health
    self.color=color
    self.classs=classs
    self.damage=10
    self.contents=list() 
  def __str__(self):
    return str(self.name)
  def __eq__(self,other):
    return self.name == other

#these are the Objects in the dungeon

crown = Object("crown", 15000, "a gold crown with many jewels",10)
scepter = Object("King's scepter", 10000, "a silver scepter",30)
vorpel_sword = Object("vorpel sword", 200, "a strange looking sword",1000)
bedpan = Object("bedpan", 3, "a smelly metal bowl",2)
torch= Object("torch", 1, "fire attatched to a stick",78)
shield=Object("shield",200,"will mitigate some damage",300)
broken_shield=Object("broken shield",100,"will mitigate some damage",300, "shield")
broken_weapon=Object("broken weapon",100,"will cause some damage",300, "weapon")
perfect_w=Object("water tower",10000,"will mitigate some damage",30000, "weapon")
perfect_s=Object("best shield",10000,"will mitigate some damage",30000, "shield")
mighty_skull = Object("skull", 15000, "a giant blob skull",100)
talon = Object("talon", 1500, "a giant dragon talon",100)
lint = Object("skull", 100, "a piece of lint",100)

#these are the monsters in the dungeon
blob=monster("blob",10000,"yellow","warrior" )
blob.contents.append(shield)
blob.damage=1000
blob.contents.append(mighty_skull)

dragon=monster("dragon",1000,"yellow","warrior" )
dragon.contents.append(lint)
dragon.damage=1000
dragon.contents.append(talon)


commandlist = dict()

commandlist['points']="type points to get your current points"
commandlist['go']="type go and then a cardinal direction"
commandlist['look']="type look and then a cardinal direction, or around to look around"
commandlist['quit']="type quit and then follow the directions to quit"
commandlist['about']="type about [item] and then what object you want to learn about"
commandlist['bag']="type bag to see whats in your bag"
commandlist['drop']="type drop [item] to drop the item from you bag"
commandlist['equip']="type equip [item] to equip whats in your bag"
commandlist['unequip']="type unequip [item] to take off what you are wearing"
commandlist['help']="type help [command] learn about command"
commandlist['attack']="type attack [monster] to attack monster"
print(commandlist)





bedroom = Room("King\'s bedroom")
bedroom.description="This is a room fit for a King"
bedroom.east= Room("corridor")
bedroom.contents.append(crown)
bedroom.contents.append(scepter)
bedroom.contents.append(vorpel_sword)
bedroom.contents.append(bedpan)
bedroom.contents.append(broken_shield)
bedroom.contents.append(broken_weapon)

hallway=Room("corridor")
hallway.description="just a long hallway"
hallway.west=bedroom
hallway.contents.append(torch)
hallway.south=Room("lair")

lair=Room("lair")
lair.description="just a long hallway"
lair.contents.append(torch)
lair.north=hallway
lair.baddies=blob
lair.south=Room("keep")

keep=Room("keep")
keep.north=lair
keep.baddies=dragon


#this is your player

#namechecker()
#initial(name)
name="aubin"
user=player(name,100,"male", "warrior")
user.shield=perfect_s
user.weapon=perfect_w

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







