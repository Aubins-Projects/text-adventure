import os.path
import string
import random


contents={}
response=""
holder=list
multiplier=1

class player:
  def __init__(self,name):
    self.name=name
    self.contents=list()
    self.pokedex=list()
    self.pokemon=list()
    self.fainted=list()
  def __str__(self):
    return str(self.name)
  def __eq__(self,other):
    return self.name == other
    
class pokemon:
  def __init__ (self,name,type,health,level,experience,attack,defense,speed,item):
    self.name=name
    self.health=health
    self.level=level
    self.experience=experience
    self.attack=attack
    self.defense=defense
    self.speed=speed
    self.item=item
    self.type=type
    self.ability=list()
    self.hp=level*health
    self.atk=level*attack
    
  def __str__(self):
    return str(self.name)
  def __eq__(self,other):
    return self.name == other    
    
class pokeball:
  def __init__(self,name,chance):
    self.name=name
    self.chance=chance
  def __str__(self):
    return str(self.name)
  def __eq__(self,other):
    return self.name == other
    
class trainor:
  def __init__(self,name,money):
    self.name=name
    self.money=money
    self.contents=list()
    self.dialogueStart=""
    self.dialogueWin=""
    self.dialogueLoss=""
  def __str__(self):
    return str(self.name)
  def __eq__(self,other):
    return self.name == other
def pretty_printer(prompt,beginspace,endspace):
  print("*****************************************")
  i=0
  while i< beginspace:
    print("\n")
    i=i+1
  print(prompt)
  i=0
  while i< endspace:
    print("\n")
    i=i+1
  print("*****************************************")
  
def arealoc_contents_look(what):
  print("************************** \n")
  i=0
  for x in range(len(what.contents)):
    print(what.contents[i].name)
    i=1+i
  if what.trainers:
    print (what.trainers.name)
    print ("\t His pokemon: ")
    i=0
    if len(what.trainers.contents) > 0:
      for x in range(len(what.trainers.contents)):
        print("\t \t"+ str(what.trainers.contents[i].name)+"\t level: "+ str(what.trainers.contents[i].level))
        i=1+i
  
  
  if what.east== None:
    i=0
  else:
    print(str(what.east)+" is East")
  if what.north== None:
    i=0
  else:
    print(str(what.north)+" is North")
  if what.west== None:
    i=0
  else:
    print(str(what.west)+" is West")
  if what.south== None:
    i=0
  else:
    print(str(what.south)+" is South")
    print("************************** \n")

    
def coordinates(direction):
  global x
  global y
  global location
  sav_x=x
  sav_y=y
  if direction in ["east" , "e"]:
     x=x+1
  elif direction in ["west" , "w"]:
     x=x-1
  elif direction in ["north" , "n"]:
     y=y+1
  elif direction in ["south" , "s"]:
     y=y-1
  loc_finder(sav_x,sav_y)


def loc_finder(sav_x,sav_y):
  global x
  global y
  global location
  check =0
  for arealoc in level1.arealocs:
    if arealoc.x==x and arealoc.y==y:
      location= arealoc
      check=1
  if check == 0:
      x=sav_x
      y=sav_y
  print(str(name)+", you are at "+str(location))  
  
  
def map_finder(x,y):
  for arealoc in level1.arealocs:
    if arealoc.x==x and arealoc.y==y:
      return arealoc


def mapping():
  global x
  global y
  global location
  temp_location=location
  temp_x=x
  temp_y=y

  if not map_finder(temp_x-1,temp_y)==temp_location:
    location.west=map_finder(temp_x-1,temp_y)

  if not map_finder(temp_x+1,temp_y)==temp_location:
    location.east=map_finder(temp_x+1,temp_y)

  if not map_finder(temp_x,temp_y-1)==temp_location:
    location.south=map_finder(temp_x,temp_y-1)

  if not map_finder(temp_x,temp_y+1)==temp_location:
    location.north=map_finder(temp_x,temp_y+1)      
  
class arealoc:
  def __init__(self,name,north="grass",east="grass",west="grass",south="grass",description=""):
    self.name=name
    self.north=north
    self.east=east
    self.west=west
    self.south=south
    self.description=description
    self.contents=list()
    self.trainers=None
    self.baddies=list()
    self.x=0
    self.y=0
  def __str__(self):
    return str(self.name)  
    
class floor:
  def __init__(self,name,arealocs=list()):
    self.name=name
    self.arealocs=arealocs
  def __str__(self):
    return str(self.name)
    
def battle_command(holder):
  global location
  if holder[0] in ["b", "battle"]:
    print(location.baddies)
##pokemon need to have attacks

class ability:
  def __init__(self,name,power,type,description):
    self.name=name
    self.power=power
    self.type=type
    self.description=description
  def __str__(self):
    return str(self.name)
  def __eq__(self,other):
    return self.name == other    
    
class type:
  def __init__(self,name,w="",w1="",w2="",w3="",s="",s1="",s2="",s3=""):
    self.name=name
    self.w=w
    self.w1=w1
    self.w2=w2
    self.w3=w3
    self.s=s
    self.s1=s1
    self.s2=s2
    self.s3=s3
  def __str__(self):
    return str(self.name)
  def __eq__(self,other):
    return self.name == other    
       
    
def weak_strength(ability):
  global multiplier
  if ability.type.w==location.trainers.contents[0].type:
    print("not very effective")
    multiplier=0.5
  elif ability.type.s==location.trainers.contents[0].type:
    print("Super effective")
    multiplier=2
  else:
    multiplier = 1
  return multiplier
    
def experience_function(pokemon,enemy):
  pokemon.experience=100/enemy.level
  if pokemon.experience >99:
    pokemon.level=pokemon.level+1
    pokemon.experience =0
    pretty_printer(str(pokemon)+" has just leveled to "+str(pokemon.level),2,2)
    
    

def attack_command(holder):
  if holder[0] in ["a","attack"]:
    print("you are now battling: "+str(location.trainers))
    pokemon_command("p")
    choosen=1
    while choosen not in user.pokemon:
      choosen= input("pick a pokemon to battle with \n")
      if user.pokemon[int(choosen)-1]:
        choosen=user.pokemon[int(choosen)-1]
        break
    if choosen in user.pokemon:
      print("you are fighting with "+str(choosen))
      while len(location.trainers.contents)>0:
        while int(location.trainers.contents[0].hp) >0:
          print("you can use the following attacks: ")
          for x in range(0,len(user.pokemon[user.pokemon.index(choosen)].ability)):
            print("Number: "+str(x+1)+"\t \t"+str(user.pokemon[user.pokemon.index(choosen)].ability[x]))
          attack=input("pick one \n")
          if user.pokemon[user.pokemon.index(choosen)].ability[int(attack)-1]:
            attack=user.pokemon[user.pokemon.index(choosen)].ability[int(attack)-1]
          if attack in user.pokemon[user.pokemon.index(choosen)].ability or user.pokemon[user.pokemon.index(choosen)].ability[user.pokemon[user.pokemon.index(choosen)].ability.index(attack)]:
            print("you used "+ str(attack)+" on "+ str(location.trainers.contents[0]))
            print("current health of "+ str(location.trainers.contents[0])+" "+ str(location.trainers.contents[0].hp))
            attack=user.pokemon[user.pokemon.index(choosen)].ability[user.pokemon[user.pokemon.index(choosen)].ability.index(attack)]
            weak_strength(attack)
#            print(user.pokemon[user.pokemon.index(choosen)].ability[user.pokemon[user.pokemon.index(choosen)].ability.index(attack)].power)
            location.trainers.contents[0].hp=location.trainers.contents[0].hp-user.pokemon[user.pokemon.index(choosen)].ability[user.pokemon[user.pokemon.index(choosen)].ability.index(attack)].power *multiplier
            print(location.trainers.contents[0].hp)
            if location.trainers.contents[0].hp>0:
              AI_fighter(location.trainers.contents[0],user.pokemon[user.pokemon.index(choosen)])
              if user.pokemon[user.pokemon.index(choosen)].hp < 1:
                print(str(user.pokemon[user.pokemon.index(choosen)])+" has just fainted!")
                user.fainted.append(user.pokemon[user.pokemon.index(choosen)])
                user.pokemon.remove(user.pokemon[user.pokemon.index(choosen)])
                holder[0]="p"
                pokemon_command(holder)
                choosen= input("pick a pokemon to battle with \n")
        pretty_printer(str(location.trainers.contents[0])+" has just fainted",1,1)
        experience_function(user.pokemon[user.pokemon.index(choosen)],location.trainers.contents[0])
        location.trainers.contents.remove(location.trainers.contents[0])
        if len(location.trainers.contents)==0:
          print("you have defeated "+location.trainers.name)
          break
        pretty_printer(str(location.trainers.contents[0])+" has just joined the battle!",0,0)

        
def AI_fighter(pokemon,yourpokemon):
  attack=pokemon.ability[random.randrange(0,len(pokemon.ability))]
  print(str(pokemon)+" just used "+str(attack))
  weak_strength(attack)
  yourpokemon.hp=yourpokemon.hp-multiplier*attack.power
  print(str(yourpokemon)+" currently has "+str(yourpokemon.hp)+" health")


      
def look_command(holder):
  if holder[0] in ["look", "l"]:
    if holder[1] in ["east","e"]:
      print(location.east)
    elif holder[1] in ["west", "w"]:
      print(location.west)
    elif holder[1] in ["south","s"]:
      print(location.south)
    elif holder[1] in ["north", "n"]:
      print(location.north)
    elif holder[1]in ["around", "a"]:
      arealoc_contents_look(location)

def pokemon_command(holder):
  if holder[0] in ["p","pokemon"]:
    print("Your Pokemon: \n")
    print("********************************************")
    i=0
    for x in range(len(user.pokemon)):
      print("Number: "+str(i+1)+"\t \t"+ str(user.pokemon[i].name)+"\t level: "+ str(user.pokemon[i].level))
      i=1+i
    print("*********************************************")
    print("Your fainted Pokemon")
    i=0
    for x in range(len(user.fainted)):
      print("\t \t"+ str(user.fainted[i].name)+"\t level: "+ str(user.fainted[i].level))
      i=1+i
      
def what_you_do(holder):
  global location
  if holder[0]=="go":
    coordinates(holder[1])
  pokemon_command(holder)
  look_command(holder)
  attack_command(holder)
  if holder[0]=="points":
    scorecheck()

    
    

'''
type goes here
class type:
  def __init__(self,name,w="",w1="",w2="",w3="",s="",s1="",s2="",s3=""):

'''
electric=type("electric")
electric.w="ground"
electric.s="water"

ground=type("ground")
ground.w="water"
ground.s="electric"

fire=type("fire")
fire.w="water"
fire.s="grass"

grass=type("grass")
grass.w="fire"
grass.s="water"

normal=type("normal")

'''
ability goes here
class ability:
  def __init__(self,name,power,type,action):

'''
scratch=ability("scratch",5,normal,"you scratch the opponent")
thunderbolt=ability("Thunder Bolt",100,electric,"thunder smites your opponent")
solarbeam=ability("Solar Beam", 10000,normal,"epic attack")
    
'''
Pokemon go here:

class pokemon:
  def __init__ (self,name,type,health,level,experience,attack,defense,speed,item):

'''
pikachu=pokemon("pikachu",electric,100,1,0,2,1,4,"")
pikachu.ability.append(scratch)
pikachu.ability.append(thunderbolt)

onix=pokemon("onix",ground,100,1,0,2,6,3,"")
onix.ability.append(scratch)


jiggly=pokemon("jiggly puff",normal,100,1,0,3,3,3,"")
jiggly.ability.append(solarbeam)


bulbasaur=pokemon("bulbasaur",grass,100,1,0,2,1,4,"")
charmander=pokemon("charmander",fire,100,1,0,2,1,4,"")
'''
trainers

class trainor:
  def __init__(self,name,money):
    self.name=name
    self.money=money
    self.contents=list()
    self.dialogueStart=""
    self.dialogueWin=""
    self.dialogueLoss=""
    
'''    
Nick_Clawson=trainor("Nick Clawson",100)
Nick_Clawson.contents.append(onix)
Nick_Clawson.contents.append(jiggly)



  
'''
arealoc
def __init__(self,name,north="grass",east="grass",west="grass",south="grass",description="")
'''
pallet_town=arealoc("Pallet Town","Your home town! Say hi to Professor Oak")
pallet_town.trainers=Nick_Clawson
pallet_town.x=10
pallet_town.y=10

route_1=arealoc("Route 1","Welcome to the first trail of your adventure")
route_1.x=11
route_1.y=10

 
level1= floor("Kanto")
level1.arealocs.append(pallet_town)
level1.arealocs.append(route_1)


location=pallet_town
x=10
y=10

name= "Aubin"

user=player("Aubin")
user.pokemon.append(pikachu)
user.fainted.append(charmander)



while not response  == "dfhsergghj":
  response=input("\nCommand: ")
  if response == "quit":
    ask_ok("You are about to quit, type no to quit")
    if relive==0:
      response="dfhsergghj"
#  try:
  holder=(response.split())
  mapping()
  what_you_do(holder)
#  except:
#    print("type a command please")






