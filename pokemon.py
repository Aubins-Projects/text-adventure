import os.path
import string
import random
import pygame, sys

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
    
class abilities:
  def __init__(self,name,power,effect,cat,type,description):
    self.name=name
    self.power=power
    self.effect=effect
    self.cat=cat
    self.type=type
    self.description=description
  def __str__(self):
    return str(self.name)
  def __eq__(self,other):
    return self.name == other
    
class pokemon:
  def __init__ (self,name,species,hp,atk,deff,spatk,spdef,speed,type1,type2,a1,l1,a2,l2,a3,l3,a4,l4,a5,l5,a6,l6,a7,l7,a8,l8,a9,l9,a10,l10,a11,l11,a12,l12,a13,l13,a14,l14,a15,l15,a16,l16,a17,l17,a18,l18,a19,l19,a20,l20,a21,l21,a22,l22,a23,l23,a24,l24,a25,l25,a26,l26,a27,l27,a28,l28,a29,l29):
    level=1
    self.name=name
    self.hp=hp
    self.atk=atk
    self.ability=list()
    self.level=level
    self.experience=0
    self.deff=deff
    self.spatk=spatk
    self.speed=speed
    self.spdef=spdef
    self.type1=type1
    self.type2=type2
    self.health=level*hp
    self.species=species
    self.a1=a1
    self.a2=a2
    self.a3=a3
    self.a4=a4
    self.a5=a5
    self.a6=a6
    self.a7=a7
    self.a8=a8
    self.a9=a9
    self.a10=a10
    self.a11=a11
    self.a12=a12
    self.a13=a13
    self.a14=a14
    self.a15=a15
    self.a16=a16
    self.a17=a17
    self.a18=a18
    self.a19=a19
    self.a20=a20
    self.a21=a21
    self.a22=a22
    self.a23=a23
    self.a24=a24
    self.a25=a25
    self.a26=a26
    self.a27=a27
    self.a28=a28
    self.a29=a29
    self.l1=l1
    self.l2=l2
    self.l3=l3
    self.l4=l4
    self.l5=l5
    self.l6=l6
    self.l7=l7
    self.l8=l8
    self.l9=l9
    self.l10=l10
    self.l11=l11
    self.l12=l12
    self.l13=l13
    self.l14=l14
    self.l15=l15
    self.l16=l16
    self.l17=l17
    self.l18=l18
    self.l19=l19
    self.l20=l20
    self.l21=l21
    self.l22=l22
    self.l23=l23
    self.l24=l24
    self.l25=l25
    self.l26=l26
    self.l27=l27
    self.l28=l28
    self.l29=l29
    self.moves=list()
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
    self.dialoguestart=""
    self.dialoguewin=""
    self.dialogueloss=""
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
    print ("\t his pokemon: ")
    i=0
    if len(what.trainers.contents) > 0:
      for x in range(len(what.trainers.contents)):
        print("\t \t"+ str(what.trainers.contents[i].name)+"\t level: "+ str(what.trainers.contents[i].level))
        i=1+i
  
  
  if what.east== None:
    i=0
  else:
    print(str(what.east)+" is east")
  if what.north== None:
    i=0
  else:
    print(str(what.north)+" is north")
  if what.west== None:
    i=0
  else:
    print(str(what.west)+" is west")
  if what.south== None:
    i=0
  else:
    print(str(what.south)+" is south")
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

   
    
class type:
  def __init__(self,name,modifier1,amount1,modifier2,amount2,modifier3,amount3,modifier4,amount4,modifier5,amount5,modifier6,amount6,modifier7,amount7,modifier8,amount8,modifier9,amount9,modifier10,amount10,modifier11,amount11):
    self.name=name
    self.modifier1=modifier1
    self.modifier2=modifier2
    self.modifier3=modifier3
    self.modifier4=modifier4
    self.modifier5=modifier5
    self.modifier6=modifier6
    self.modifier7=modifier7
    self.modifier8=modifier8
    self.modifier9=modifier9
    self.modifier10=modifier10
    self.amount1=amount1
    self.amount2=amount2
    self.amount3=amount3
    self.amount4=amount4
    self.amount5=amount5
    self.amount6=amount6
    self.amount7=amount7
    self.amount8=amount8
    self.amount9=amount9
    self.amount10=amount10
    
  def __str__(self):
    return str(self.name)
  def __eq__(self,other):
    return self.name == other    
       
    
def weak_strength(ability, pokemon):
  global multiplier
  if ability.type.modifier1 == pokemon.type1:
    multiplier=ability.type.amount1
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier2 == pokemon.type1:
    multiplier=ability.type.amount2
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier3 == pokemon.type1:
    multiplier=ability.type.amount3
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier4 == pokemon.type1:
    multiplier=ability.type.amount4
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier5 == pokemon.type1:
    multiplier=ability.type.amount5
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier6 == pokemon.type1:
    multiplier=ability.type.amount6
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier7 == pokemon.type1:
    multiplier=ability.type.amount7
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier8 == pokemon.type1:
    multiplier=ability.type.amount8
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier9 == pokemon.type1:
    multiplier=ability.type.amount9
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier10 == pokemon.type1:
    multiplier=ability.type.amount10
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier10 == pokemon.type1:
    multiplier=ability.type.amount10
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier1 == pokemon.type2:
    multiplier=ability.type.amount1
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier2 == pokemon.type2:
    multiplier=ability.type.amount2
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier3 == pokemon.type2:
    multiplier=ability.type.amount3
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier4 == pokemon.type2:
    multiplier=ability.type.amount4
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier5 == pokemon.type2:
    multiplier=ability.type.amount5
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier6 == pokemon.type2:
    multiplier=ability.type.amount6
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier7 == pokemon.type2:
    multiplier=ability.type.amount7
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier8 == pokemon.type2:
    multiplier=ability.type.amount8
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier9 == pokemon.type2:
    multiplier=ability.type.amount9
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier10 == pokemon.type2:
    multiplier=ability.type.amount10
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  elif ability.type.modifier10 == pokemon.type2:
    multiplier=ability.type.amount10
    if multiplier < 1:
       print(str(ability)+" was not very effective")
    elif multiplier > 1:
       print(str(ability)+" was very effective")
  else:
    multiplier=1
    
def experience_function(pokemon,enemy):
  pokemon.experience=100/enemy.level+pokemon.experience
  if pokemon.experience >99:
    pokemon.level=pokemon.level+1
    pokemon.experience =0
    pretty_printer(str(pokemon)+" has just leveled to "+str(pokemon.level),2,2)
    


def attack_command(holder):
  global choosen
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
        while int(location.trainers.contents[0].health) >0:
          
          print(str(choosen)+" can use the following attacks: ")
         
          for x in range(0,len(choosen.ability)):
            print("number: "+str(x+1)+"\t \t"+str(choosen.ability[x]))
          print("\n\nPokemon - p\n\n")
          attack=input("pick one \n")
          battle_options(attack)
          yourpokemon=user.pokemon[user.pokemon.index(choosen)]
          if user.pokemon[user.pokemon.index(choosen)].ability[int(attack)-1]:
            attack=user.pokemon[user.pokemon.index(choosen)].ability[int(attack)-1]
            print(attack)
          if attack in user.pokemon[user.pokemon.index(choosen)].ability or user.pokemon[user.pokemon.index(choosen)].ability[user.pokemon[user.pokemon.index(choosen)].ability.index(attack)]:
            print("you used "+ str(attack)+" on "+ str(location.trainers.contents[0]))
            print("current health of "+ str(location.trainers.contents[0])+" "+ str(location.trainers.contents[0].health))
#            attack=user.pokemon[user.pokemon.index(choosen)].ability[user.pokemon[user.pokemon.index(choosen)].ability.index(attack)]
            weak_strength(attack, location.trainers.contents[0])
#            print(user.pokemon[user.pokemon.index(choosen)].ability[user.pokemon[user.pokemon.index(choosen)].ability.index(attack)].power)
            location.trainers.contents[0].health=location.trainers.contents[0].health-user.pokemon[user.pokemon.index(choosen)].ability[user.pokemon[user.pokemon.index(choosen)].ability.index(attack)].effect *multiplier/5
            print(user.pokemon[user.pokemon.index(choosen)].ability[user.pokemon[user.pokemon.index(choosen)].ability.index(attack)].effect *multiplier/5)
            damage=(((((2 *yourpokemon.level/5+2)*yourpokemon.atk*attack.effect/location.trainers.contents[0].deff)/50)+2)*multiplier*random.randrange(85,100)/100)
            print(damage)
            print("^^^^")
            print(multiplier)
            print(user.pokemon[user.pokemon.index(choosen)].ability[user.pokemon[user.pokemon.index(choosen)].ability.index(attack)].effect)
            if location.trainers.contents[0].health>0:
              ai_fighter(location.trainers.contents[0],user.pokemon[user.pokemon.index(choosen)])
              if user.pokemon[user.pokemon.index(choosen)].health < 1:
                print(str(user.pokemon[user.pokemon.index(choosen)])+" has just fainted!")
                user.fainted.append(user.pokemon[user.pokemon.index(choosen)])
                user.pokemon.remove(user.pokemon[user.pokemon.index(choosen)])
                if len(user.pokemon) ==0:
                  for faint in user.fainted:
                    faint.health=faint.hp*faint.level
                    user.pokemon.append(faint)
                  user.fainted=list()
                holder[0]="p"
                pokemon_command(holder)
                choosen= input("pick a pokemon to battle with \n")
                choosen=user.pokemon[int(choosen)-1]
            
        pretty_printer(str(location.trainers.contents[0])+" has just fainted",1,1)
        experience_function(user.pokemon[user.pokemon.index(choosen)],location.trainers.contents[0])
        location.trainers.contents.remove(location.trainers.contents[0])
        if len(location.trainers.contents)==0:
          print("you have defeated "+location.trainers.name)
          break
        pretty_printer(str(location.trainers.contents[0])+" has just joined the battle!",0,0)
        ability_keeper(yourpokemon)

        
def ai_fighter(pokemon,ypokemon):
  attack=pokemon.ability[random.randrange(0,len(pokemon.ability))]
  print(str(pokemon)+" just used "+str(attack))
  weak_strength(attack,ypokemon)
  ypokemon.health=ypokemon.health-multiplier*attack.effect*attack.power/200
  print(str(ypokemon)+" currently has "+str(ypokemon.health)+" health")


      
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
    print("your pokemon: \n")
    print("********************************************")
    i=0
    for x in range(len(user.pokemon)):
      print("number: "+str(i+1)+"\t \t"+ str(user.pokemon[i].name)+"\t level: "+ str(user.pokemon[i].level))
      i=1+i
    print("*********************************************")
    print("your fainted pokemon")
    i=0
    for x in range(len(user.fainted)):
      print("\t \t"+ str(user.fainted[i].name)+"\t level: "+ str(user.fainted[i].level))
      i=1+i
def battle_options(previous_command):
  global choosen
  if previous_command=="p":
    pokemon_command(previous_command)
    choosen= input("pick a pokemon to battle with \n")
    choosen=user.pokemon[int(choosen)-1]
    print(str(choosen)+" can use the following attacks: ")
    for x in range(0,len(choosen.ability)):
      print("number: "+str(x+1)+"\t \t"+str(choosen.ability[x]))
    attack=input("pick one ")
        
    
def moves_maker(pokemon):
  pokemon.moves.append(pokemon.a1)
  pokemon.moves.append(pokemon.l1)
  pokemon.moves.append(pokemon.a2)
  pokemon.moves.append(pokemon.l2)
  pokemon.moves.append(pokemon.a3)
  pokemon.moves.append(pokemon.l3)
  pokemon.moves.append(pokemon.a4)
  pokemon.moves.append(pokemon.l4)
  pokemon.moves.append(pokemon.a5)
  pokemon.moves.append(pokemon.l5)
  pokemon.moves.append(pokemon.a6)
  pokemon.moves.append(pokemon.l6)
  pokemon.moves.append(pokemon.a7)
  pokemon.moves.append(pokemon.l7)
  pokemon.moves.append(pokemon.a8)
  pokemon.moves.append(pokemon.l8)
  pokemon.moves.append(pokemon.a9)
  pokemon.moves.append(pokemon.l9)
  pokemon.moves.append(pokemon.a10)
  pokemon.moves.append(pokemon.l10)
  pokemon.moves.append(pokemon.a11)
  pokemon.moves.append(pokemon.l11)
  pokemon.moves.append(pokemon.a12)
  pokemon.moves.append(pokemon.l12)
  pokemon.moves.append(pokemon.a13)
  pokemon.moves.append(pokemon.l13)
  pokemon.moves.append(pokemon.a14)
  pokemon.moves.append(pokemon.l14)
  pokemon.moves.append(pokemon.a15)
  pokemon.moves.append(pokemon.l15)
  pokemon.moves.append(pokemon.a16)
  pokemon.moves.append(pokemon.l16)
  pokemon.moves.append(pokemon.a17)
  pokemon.moves.append(pokemon.l17)
  pokemon.moves.append(pokemon.a18)
  pokemon.moves.append(pokemon.l18)
  pokemon.moves.append(pokemon.a19)
  pokemon.moves.append(pokemon.l19)
  pokemon.moves.append(pokemon.a20)
  pokemon.moves.append(pokemon.l20)
  pokemon.moves.append(pokemon.a21)
  pokemon.moves.append(pokemon.l21)
  pokemon.moves.append(pokemon.a22)
  pokemon.moves.append(pokemon.l22)
  pokemon.moves.append(pokemon.a23)
  pokemon.moves.append(pokemon.l23)
  pokemon.moves.append(pokemon.a24)
  pokemon.moves.append(pokemon.l24)
  pokemon.moves.append(pokemon.a25)
  pokemon.moves.append(pokemon.l25)
  pokemon.moves.append(pokemon.a26)
  pokemon.moves.append(pokemon.l26)
  pokemon.moves.append(pokemon.a27)
  pokemon.moves.append(pokemon.l27)
  pokemon.moves.append(pokemon.a28)
  pokemon.moves.append(pokemon.l28)
  pokemon.moves.append(pokemon.a29)
  pokemon.moves.append(pokemon.l29)
  
def ability_keeper(pokemon):
#make this for loop a one time thing
#  for pokemon in user.pokemon:
  i=1
  if pokemon.level in pokemon.moves:
    while i<int(len(pokemon.moves)):
      if pokemon.level-1 == pokemon.moves[i]:
        print(str(pokemon)+" has just learned "+str(pokemon.moves[i-1]))
        pokemon.ability.append(pokemon.moves[i-1])
        pokemon.moves.remove(pokemon.moves[i-1])       
      i=i+1
  
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
normal=type("normal","rock",1/2,"ghost",0,"steel",1/2,"steel",1/2,"steel",1/2,"steel",1/2,"steel",1/2,"steel",1/2,"steel",1/2,"steel",1/2,"steel",1/2)
fighting=type("fighting","normal",2,"flying",1/2,"poison",1/2,"rock",2,"bug",1/2,"ghost",0,"steel",2,"psychic",1/2,"ice",2,"dark",2,"dark",2)
flying=type("flying","fighting",2,"rock",1/2,"bug",2,"steel",1/2,"grass",2,"electric",1/2,"electric",1/2,"electric",1/2,"electric",1/2,"electric",1/2,"electric",1/2)
poison=type("poison","poison",1/2,"ground",1/2,"rock",1/2,"ghost",1/2,"steel",0,"grass",2,"grass",2,"grass",2,"grass",2,"grass",2,"grass",2)
ground=type("ground","flying",0,"poison",2,"rock",2,"bug",1/2,"steel",2,"fire",2,"grass",1/2,"electric",2,"electric",2,"electric",2,"electric",2)
rock=type("rock","fighting",1/2,"flying",2,"ground",1/2,"bug",2,"steel",1/2,"fire",1/2,"ice",2,"ice",2,"ice",2,"ice",2,"ice",2)
bug=type("bug","fighting",1/2,"flying",1/2,"poison",1/2,"ghost",1/2,"steel",1/2,"fire",1/2,"grass",2,"psychic",2,"dark",2,"dark",2,"dark",2)
ghost=type("ghost","normal",0,"ghost",2,"steel",1/2,"psychic",2,"dark",1/2,"dark",1/2,"dark",1/2,"dark",1/2,"dark",1/2,"dark",1/2,"dark",1/2)
steel=type("steel","rock",2,"steel",1/2,"fire",1/2,"water",1/2,"electric",1/2,"ice",2,"ice",2,"ice",2,"ice",2,"ice",2,"ice",2)
fire=type("fire","rock",1/2,"bug",2,"steel",2,"fire",1/2,"water",1/2,"grass",2,"ice",2,"dragon",1/2,"dragon",1/2,"dragon",1/2,"dragon",1/2)
water=type("water","ground",2,"rock",2,"fire",2,"water",1/2,"grass",1/2,"dragon",1/2,"dragon",1/2,"dragon",1/2,"dragon",1/2,"dragon",1/2,"dragon",1/2)
grass=type("grass","flying",1/2,"poison",1/2,"ground",2,"rock",2,"bug",1/2,"steel",1/2,"fire",1/2,"water",2,"grass",1/2,"dragon",1/2,"dragon",1/2)
electric=type("electric","flying",2,"ground",0,"water",2,"grass",1/2,"electric",1/2,"dragon",1/2,"dragon",1/2,"dragon",1/2,"dragon",1/2,"dragon",1/2,"dragon",1/2)
psychic=type("psychic","fighting",2,"poison",2,"steel",1/2,"psychic",1/2,"dark",0,"dark",0,"dark",0,"dark",0,"dark",0,"dark",0,"dark",0)
ice=type("ice","flying",2,"ground",2,"steel",1/2,"fire",1/2,"water",1/2,"grass",2,"ice",1/2,"dragon",2,"dragon",2,"dragon",2,"dragon",2)
dragon=type("dragon","steel",1/2,"dragon",2,"dragon",2,"dragon",2,"dragon",2,"dragon",2,"dragon",2,"dragon",2,"dragon",2,"dragon",2,"dragon",2)
dark=type("dark","fighting",1/2,"ghost",2,"steel",1/2,"psychic",2,"dark",1/2,"dark",1/2,"dark",1/2,"dark",1/2,"dark",1/2,"dark",1/2,"dark",1/2)





'''
ability goes here
class abilities:
  def __init__(self,name,power,effect,cat,type,description):

'''
absorb=abilities("absorb",3,20,"special",grass,"an attack that absorbs half the damage it inflicted to restore hp.")
acid=abilities("acid",69,40,"special",poison,"the foe is sprayed with a harsh, hide- melting acid that may lower defense.")
acid_armor=abilities("acid armor",51,0,"status",poison,"the user alters its cells to liquefy itself and sharply raise defense.")
aerial_ace=abilities("aerial ace",17,60,"physical",flying,"an extremely fast attack against one target. it can't be evaded.")
aeroblast=abilities("aeroblast",43,100,"special",flying,"a vortex of air is shot at the foe. it has a high critical-hit ratio.")
agility=abilities("agility",52,0,"status",psychic,"the user relaxes and lightens its body to sharply boost its speed.")
air_cutter=abilities("air cutter",43,55,"special",flying,"the foe is hit with razor-like wind. it has a high critical-hit ratio.")
amnesia=abilities("amnesia",54,0,"status",psychic,"forgets about something and sharply raises sp. def.")
ancientpower=abilities("ancientpower",140,60,"physical",rock,"an ancient power is used to attack. it may also raise all the user's stats.")
arm_thrust=abilities("arm thrust",29,15,"physical",fighting,"a quick flurry of straight-arm punches that hit two to five times.")
aromatherapy=abilities("aromatherapy",102,0,"status",grass,"a soothing scent is released to heal all status problems in the user's party.")
assist=abilities("assist",180,0,"status",normal,"the user randomly picks and uses a move of an allied pok{ae}mon.")
astonish=abilities("astonish",150,30,"physical",ghost,"an attack using a startling shout. it also may make the foe flinch.")
attract=abilities("attract",120,0,"status",normal,"if it is the other gender, the foe is made infatuated and unlikely to attack.")
aurora_beam=abilities("aurora beam",68,65,"special",ice,"a rainbow-colored attack beam. it may lower the foe's attack stat.")
barrage=abilities("barrage",29,15,"special",normal,"round objects are hurled at the foe to strike two to five times.")
barrier=abilities("barrier",51,0,"status",psychic,"the user creates a sturdy wall that sharply raises its defense stat.")
baton_pass=abilities("baton pass",127,0,"status",normal,"the user switches out, passing along any stat changes to the new battler.")
beat_up=abilities("beat up",154,10,"special",dark,"all party pok{ae}mon join in the attack. the more allies, the more damage.")
belly_drum=abilities("belly drum",142,0,"status",normal,"the user maximizes its attack stat at the cost of half its full hp.")
bide=abilities("bide",26,1,"physical",normal,"the user endures attacks for two turns, then strikes back double.")
bind=abilities("bind",42,15,"physical",normal,"a long body or tentacles are used to bind the foe for two to five turns.")
bite=abilities("bite",31,60,"physical",dark,"the user bites with vicious fangs. it may make the foe flinch.")
blast_burn=abilities("blast burn",80,150,"special",fire,"the foe is hit with a huge explosion. the user can't move on the next turn.")
blaze_kick=abilities("blaze kick",200,85,"physical",fire,"a fiery kick with a high critical-hit ratio. it may also burn the foe.")
blizzard=abilities("blizzard",5,120,"special",ice,"the foe is blasted with a blizzard. it may freeze the foe solid.")
block=abilities("block",106,0,"status",normal,"the user blocks the foe's way with arms spread wide to prevent escape.")
body_slam=abilities("body slam",6,85,"physical",normal,"the user drops its full body on the foe. it may leave the foe paralyzed.")
bonemerang=abilities("bonemerang",44,50,"special",ground,"the user throws a bone that hits the foe once, then once again on return.")
bone_club=abilities("bone club",31,65,"special",ground,"the foe is clubbed with a bone held in hand. it may make the foe flinch.")
bone_rush=abilities("bone rush",29,25,"special",ground,"the user strikes the foe with a bone in hand two to five times.")
bounce=abilities("bounce",155,85,"physical",flying,"the user bounces on the foe on the 2nd turn. it may paralyze the foe.")
brick_break=abilities("brick break",186,75,"physical",fighting,"an attack that also breaks any barrier like light screen and reflect.")
bubble=abilities("bubble",70,20,"special",water,"a spray of bubbles hits the foe. it may lower the foe's speed stat.")
bubblebeam=abilities("bubblebeam",70,65,"special",water,"a spray of bubbles strikes the foe. it may lower the foe's speed stat.")
bulk_up=abilities("bulk up",208,0,"status",fighting,"the user bulks up its body to boost both its attack and defense stats.")
bullet_seed=abilities("bullet seed",29,10,"special",grass,"the user shoots seeds at the foe. two to five seeds are shot at once.")
calm_mind=abilities("calm mind",211,0,"status",psychic,"the user focuses its mind to raise the sp. atk and sp. def stats.")
camouflage=abilities("camouflage",213,0,"status",normal,"alters the user's type depending on the location's terrain.")
charge=abilities("charge",174,0,"status",electric,"the user charges power to boost the electric move it uses next.")
charm=abilities("charm",58,0,"status",normal,"the foe is charmed by the user's cute appeals, sharply cutting its attack.")
clamp=abilities("clamp",42,35,"physical",water,"the foe is clamped and squeezed by the user's shell for two to five turns.")
comet_punch=abilities("comet punch",29,18,"physical",normal,"the foe is hit with a flurry of punches that strike two to five times.")
confuse_ray=abilities("confuse ray",49,0,"status",ghost,"the foe is exposed to a sinister ray that triggers confusion.")
confusion=abilities("confusion",76,50,"special",psychic,"a weak telekinetic attack that may also leave the foe confused.")
constrict=abilities("constrict",70,10,"physical",normal,"the foe is attacked with long tentacles or vines. it may lower speed.")
conversion=abilities("conversion",30,0,"status",normal,"the user changes its type to match the type of one of its moves.")
conversion_2=abilities("conversion 2",93,0,"status",normal,"the user changes type to make itself resistant to the last attack it took.")
cosmic_power=abilities("cosmic power",206,0,"status",psychic,"the user absorbs a mystic power to raise its defense and sp. def.")
cotton_spore=abilities("cotton spore",60,0,"status",grass,"cotton-like spores cling to the foe, sharply reducing its speed stat.")
counter=abilities("counter",89,1,"physical",fighting,"a retaliation move that counters any physical hit with double the damage.")
covet=abilities("covet",105,40,"special",normal,"a cutely executed attack that also steals the foe's hold item.")
crabhammer=abilities("crabhammer",43,90,"physical",water,"a large pincer is used to hammer the foe. it has a high critical-hit ratio.")
cross_chop=abilities("cross chop",43,100,"physical",fighting,"the foe is hit with double chops. it has a high critical-hit ratio.")
crunch=abilities("crunch",72,80,"physical",dark,"the foe is crunched with sharp fangs. it may lower the foe's sp. def.")
crush_claw=abilities("crush claw",69,75,"physical",normal,"the foe is attacked with sharp claws. it may also lower the foe's defense.")
curse=abilities("curse",109,0,"status",ghost,"a move that works differently for the ghost-type and all the other types.")
cut=abilities("cut",0,50,"physical",normal,"a basic attack. it can be used to cut down thin trees and grass.")
defense_curl=abilities("defense curl",156,0,"status",normal,"the user curls up to conceal weak spots and raise its defense stat.")
destiny_bond=abilities("destiny bond",98,0,"status",ghost,"if the user faints, the foe delivering the final hit also faints.")
detect=abilities("detect",111,0,"status",fighting,"enables the user to evade all attacks. it may fail if used in succession.")
dig=abilities("dig",155,60,"physical",ground,"an attack that hits on the 2nd turn. can also be used to exit dungeons.")
disable=abilities("disable",86,0,"status",normal,"for a few turns, it prevents the foe from using the move it last used.")
dive=abilities("dive",155,60,"physical",water,"the user dives underwater on the first turn and strikes next turn.")
dizzy_punch=abilities("dizzy punch",76,70,"physical",normal,"the foe is hit with a rhythmic punch that may leave it confused.")
doom_desire=abilities("doom desire",148,120,"special",steel,"a move that attacks the foe with a blast of light two turns after use.")
double_edge=abilities("double-edge",198,120,"physical",normal,"a reckless, life- risking tackle that also hurts the user a little.")
doubleslap=abilities("doubleslap",29,15,"physical",normal,"the foe is slapped repeatedly, back and forth, two to five times.")
double_kick=abilities("double kick",44,30,"physical",fighting,"two legs are used to quickly kick the foe twice in one turn.")
double_team=abilities("double team",16,0,"status",normal,"the user creates illusory copies of itself to raise its evasiveness.")
dragonbreath=abilities("dragonbreath",6,60,"special",dragon,"the foe is hit with an incredible blast of breath that may also paralyze.")
dragon_claw=abilities("dragon claw",0,80,"physical",dragon,"sharp, huge claws hook and slash the foe quickly and with great power.")
dragon_dance=abilities("dragon dance",212,0,"status",dragon,"a mystic, powerful dance that boosts the user's attack and speed stats.")
dragon_rage=abilities("dragon rage",41,1,"special",dragon,"the foe is hit with a shock wave that always inflicts 40- hp damage.")
dream_eater=abilities("dream eater",8,100,"special",psychic,"absorbs half the damage it inflicted on a sleeping foe to restore hp.")
drill_peck=abilities("drill peck",0,80,"physical",flying,"a corkscrewing attack with the sharp beak acting as a drill.")
dynamicpunch=abilities("dynamicpunch",76,100,"physical",fighting,"the foe is punched with the user's full power. it confuses the foe if it hits.")
earthquake=abilities("earthquake",147,100,"special",ground,"an earthquake that strikes all pok{ae}mon in battle excluding the user.")
egg_bomb=abilities("egg bomb",0,100,"special",normal,"a large egg is hurled with great force at the foe to inflict damage.")
ember=abilities("ember",4,40,"special",fire,"the foe is attacked with small flames. the foe may suffer a burn.")
encore=abilities("encore",90,0,"status",normal,"makes the foe use the move it last used repeatedly for two to six turns.")
endeavor=abilities("endeavor",189,1,"physical",normal,"gains power the fewer hp the user has compared with the foe.")
endure=abilities("endure",116,0,"status",normal,"the user endures any hit with 1 hp left. it may fail if used in succession.")
eruption=abilities("eruption",190,150,"special",fire,"the higher the user's hp, the more powerful this attack becomes.")
explosion=abilities("explosion",7,250,"special",normal,"the user explodes to inflict terrible damage even while fainting itself.")
extrasensory=abilities("extrasensory",150,80,"special",psychic,"the user attacks with an odd power that may make the foe flinch.")
extremespeed=abilities("extremespeed",103,80,"physical",normal,"a blindingly speedy charge attack that always goes before any other.")
facade=abilities("facade",169,70,"physical",normal,"an attack that is boosted if user is burned, poisoned, or paralyzed.")
faint_attack=abilities("faint attack",17,60,"special",dark,"the user draws up close to the foe disarmingly, then hits without fail.")
fake_out=abilities("fake out",158,40,"special",normal,"an attack that hits first and causes flinching. usable only on 1st turn.")
fake_tears=abilities("fake tears",62,0,"status",dark,"the user feigns crying to sharply lower the foe's sp. def stat.")
false_swipe=abilities("false swipe",101,40,"physical",normal,"a restrained attack that always leaves the foe with at least 1 hp.")
featherdance=abilities("featherdance",58,0,"status",flying,"the foe is covered with a mass of down that sharply cuts the attack stat.")
fire_blast=abilities("fire blast",4,120,"special",fire,"the foe is hit with an intense flame. it may leave the target with a burn.")
fire_punch=abilities("fire punch",4,75,"physical",fire,"the foe is punched with a fiery fist. it may leave the foe with a burn.")
fire_spin=abilities("fire spin",42,15,"special",fire,"the foe is trapped in an intense spiral of fire that rages two to five turns.")
fissure=abilities("fissure",38,1,"special",ground,"the foe is dropped into a fissure. the foe faints if it hits.")
flail=abilities("flail",99,1,"physical",normal,"a desperate attack that becomes more powerful the less hp the user has.")
flamethrower=abilities("flamethrower",4,95,"special",fire,"the foe is scorched with intense flames. the foe may suffer a burn.")
flame_wheel=abilities("flame wheel",125,60,"physical",fire,"the user makes a fiery charge at the foe. it may cause a burn.")
flash=abilities("flash",23,0,"status",normal,"a blast of light that cuts the foe's accuracy. it also illuminates caves.")
flatter=abilities("flatter",166,0,"status",dark,"flattery is used to confuse the foe, but its sp. atk also rises.")
fly=abilities("fly",155,70,"physical",flying,"a 2-turn move that hits on the 2nd turn. use it to fly to any known town.")
focus_energy=abilities("focus energy",47,0,"status",normal,"the user takes a deep breath and focuses to raise its critical-hit ratio.")
focus_punch=abilities("focus punch",170,150,"physical",fighting,"an attack that is executed last. the user flinches if hit beforehand.")
follow_me=abilities("follow me",172,0,"status",normal,"the user draws attention to itself, making foes attack only the user.")
foresight=abilities("foresight",113,0,"status",normal,"completely negates the foe's efforts to heighten its abilities to evade.")
frenzy_plant=abilities("frenzy plant",80,150,"special",grass,"the foe is hit with an enormous branch. the user can't move on the next turn.")
frustration=abilities("frustration",123,1,"physical",normal,"this attack move grows more powerful the less the user likes its trainer.")
fury_attack=abilities("fury attack",29,15,"physical",normal,"the foe is jabbed repeatedly with a horn or beak two to five times.")
fury_cutter=abilities("fury cutter",119,10,"physical",bug,"an attack that grows stronger on each successive hit.")
fury_swipes=abilities("fury swipes",29,18,"physical",normal,"the foe is raked with sharp claws or scythes two to five times.")
future_sight=abilities("future sight",148,80,"special",psychic,"two turns after this move is used, the foe is attacked psychically.")
giga_drain=abilities("giga drain",3,60,"special",grass,"a harsh attack that absorbs half the damage it inflicted to restore hp.")
glare=abilities("glare",67,0,"status",normal,"the user intimidates the foe with the design on its belly to cause paralysis.")
grasswhistle=abilities("grasswhistle",1,0,"status",grass,"a pleasant melody is played to lull the foe into a deep sleep.")
growl=abilities("growl",18,0,"status",normal,"the user growls in a cute way, making the foe lower its attack stat.")
growth=abilities("growth",13,0,"status",normal,"the user's body is forced to grow, raising the sp. atk stat.")
grudge=abilities("grudge",194,0,"status",ghost,"if the user faints, this move deletes the pp of the move that finished it.")
guillotine=abilities("guillotine",38,1,"physical",normal,"a vicious tearing attack with pincers. the foe will faint if it hits.")
gust=abilities("gust",149,40,"special",flying,"strikes the foe with a gust of wind whipped up by wings.")
hail=abilities("hail",164,0,"status",ice,"a hailstorm lasting five turns damages all pok{ae}mon except the ice-type.")
harden=abilities("harden",11,0,"status",normal,"the user stiffens all the muscles in its body to raise its defense stat.")
haze=abilities("haze",25,0,"status",ice,"eliminates all stat changes among all pok{ae}mon engaged in battle.")
headbutt=abilities("headbutt",31,70,"physical",normal,"the user sticks its head out and rams. it may make the foe flinch.")
heal_bell=abilities("heal bell",102,0,"status",normal,"a soothing bell chimes to heal the status problems of all allies.")
heat_wave=abilities("heat wave",4,100,"special",fire,"the user exhales a heated breath to attack. it may also inflict a burn.")
helping_hand=abilities("helping hand",176,0,"status",normal,"a move that boosts the power of the ally's attack in a battle.")
hidden_power=abilities("hidden power",135,1,"special",normal,"an attack that varies in type and intensity depending on the user.")
hi_jump_kick=abilities("hi jump kick",45,85,"physical",fighting,"a strong jumping knee kick. if it misses, the user is hurt.")
horn_attack=abilities("horn attack",0,65,"physical",normal,"the foe is jabbed with a sharply pointed horn to inflict damage.")
horn_drill=abilities("horn drill",38,1,"physical",normal,"the horn is rotated like a drill to ram. the foe will faint if it hits.")
howl=abilities("howl",10,0,"status",normal,"the user howls to raise its spirit and boost its attack stat.")
hydro_cannon=abilities("hydro cannon",80,150,"special",water,"the foe is hit with a watery cannon. the user can't move on the next turn.")
hydro_pump=abilities("hydro pump",0,120,"special",water,"a high volume of water is blasted at the foe under great pressure.")
hyper_beam=abilities("hyper beam",80,150,"special",normal,"a severely damaging attack that makes the user rest on the next turn.")
hyper_fang=abilities("hyper fang",31,80,"physical",normal,"the foe is attacked with sharp fangs. it may make the foe flinch.")
hyper_voice=abilities("hyper voice",0,90,"special",normal,"the user lets loose a horribly loud shout with the power to damage.")
hypnosis=abilities("hypnosis",1,0,"status",psychic,"hypnotic suggestion is used to make the foe fall into a deep sleep.")
ice_ball=abilities("ice ball",117,30,"physical",ice,"a 5-turn rolling attack that becomes stronger each time it rolls.")
ice_beam=abilities("ice beam",5,95,"special",ice,"the foe is struck with an icy beam. it may freeze the foe solid.")
ice_punch=abilities("ice punch",5,75,"physical",ice,"the foe is punched with an icy fist. it may leave the foe frozen.")
icicle_spear=abilities("icicle spear",29,10,"special",ice,"sharp icicles are fired at the foe. it strikes two to five times.")
icy_wind=abilities("icy wind",70,55,"special",ice,"a chilling wind is used to attack. it also lowers the speed stat.")
imprison=abilities("imprison",192,0,"status",psychic,"prevents foes from using any move that is also known by the user.")
ingrain=abilities("ingrain",181,0,"status",grass,"the user lays roots that restore hp on every turn. it can't switch out.")
iron_defense=abilities("iron defense",51,0,"status",steel,"the user hardens its body's surface to sharply raise its defense stat.")
iron_tail=abilities("iron tail",69,100,"physical",steel,"an attack with a steel-hard tail. it may lower the foe's defense stat.")
jump_kick=abilities("jump kick",45,70,"physical",fighting,"the user jumps up high, then kicks. if it misses, the user hurts itself.")
karate_chop=abilities("karate chop",43,50,"physical",fighting,"the foe is attacked with a sharp chop. it has a high critical-hit ratio.")
kinesis=abilities("kinesis",23,0,"status",psychic,"the user distracts the foe by bending a spoon. it may lower accuracy.")
knock_off=abilities("knock off",188,20,"physical",dark,"knocks down the foe's held item to prevent its use during the battle.")
leaf_blade=abilities("leaf blade",43,70,"physical",grass,"the foe is slashed with a sharp leaf. it has a high critical-hit ratio.")
leech_life=abilities("leech life",3,20,"physical",bug,"an attack that absorbs half the damage it inflicted to restore hp.")
leech_seed=abilities("leech seed",84,0,"status",grass,"a seed is planted on the foe to steal some hp for the  user on every turn.")
leer=abilities("leer",19,0,"status",normal,"the foe is given an intimidating look that lowers its defense stat.")
lick=abilities("lick",6,20,"physical",ghost,"the foe is licked and hit with a long tongue. it may also paralyze.")
light_screen=abilities("light screen",35,0,"status",psychic,"a wall of light cuts damage from sp. atk attacks for five turns.")
lock_on=abilities("lock-on",94,0,"status",normal,"the user locks on to the foe, making the next move sure to hit.")
lovely_kiss=abilities("lovely kiss",1,0,"status",normal,"the user forces a kiss on the foe with a scary face that induces sleep.")
low_kick=abilities("low kick",196,1,"physical",fighting,"a low, tripping kick that inflicts more damage on heavier foes.")
luster_purge=abilities("luster purge",72,70,"special",psychic,"a burst of light injures the foe. it may also lower the foe's sp. def.")
mach_punch=abilities("mach punch",103,40,"physical",fighting,"a punch thrown at blinding speed. it is certain to strike first.")
magical_leaf=abilities("magical leaf",17,60,"special",grass,"the foe is attacked with a strange leaf that cannot be evaded.")
magic_coat=abilities("magic coat",183,0,"status",psychic,"reflects back the foe's leech seed and any status- damaging move.")
magnitude=abilities("magnitude",126,1,"special",ground,"a ground-shaking attack against all standing pok{ae}mon. its power varies.")
mean_look=abilities("mean look",106,0,"status",normal,"the foe is fixed with a mean look that prevents it from escaping.")
meditate=abilities("meditate",10,0,"status",psychic,"the user meditates to awaken its power and raise its attack stat.")
megahorn=abilities("megahorn",0,120,"physical",bug,"a brutal ramming attack delivered with a tough and impressive horn.")
mega_drain=abilities("mega drain",3,40,"special",grass,"a tough attack that drains half the damage it inflicted to restore hp.")
mega_kick=abilities("mega kick",0,120,"physical",normal,"the foe is attacked by a kick fired with muscle-packed power.")
mega_punch=abilities("mega punch",0,80,"physical",normal,"the foe is slugged by a punch thrown with muscle-packed power.")
memento=abilities("memento",168,0,"status",dark,"the user faints, but sharply lowers the foe's attack and sp. atk.")
metal_claw=abilities("metal claw",139,50,"physical",steel,"the foe is attacked with steel claws. it may also raise the user's attack.")
metal_sound=abilities("metal sound",62,0,"status",steel,"a horrible metallic screech is used to sharply lower the foe's sp. def.")
meteor_mash=abilities("meteor mash",139,100,"physical",steel,"the foe is hit with a hard, fast punch. it may also raise the user's attack.")
metronome=abilities("metronome",83,0,"status",normal,"waggles a finger and stimulates the brain into using any move at random.")
milk_drink=abilities("milk drink",157,0,"status",normal,"heals the user by up to half its full hp. it can be used to heal an ally.")
mimic=abilities("mimic",82,0,"status",normal,"the user copies the move last used by the foe for the rest of the battle.")
mind_reader=abilities("mind reader",94,0,"status",normal,"the user predicts the foe's action to ensure its next attack hits.")
minimize=abilities("minimize",108,0,"status",normal,"the user compresses all the cells in its body to raise its evasiveness.")
mirror_coat=abilities("mirror coat",144,1,"special",psychic,"a retaliation move that pays back the foe's special attack double.")
mirror_move=abilities("mirror move",9,0,"status",flying,"the user counters the move last used by the foe with the same move.")
mist=abilities("mist",46,0,"status",ice,"the ally party is protected by a mist that prevents stat reductions.")
mist_ball=abilities("mist ball",71,70,"special",psychic,"a flurry of down hits the foe. it may also lower the foe's sp. atk.")
moonlight=abilities("moonlight",134,0,"status",normal,"restores the user's hp. the amount of hp regained varies with the weather.")
morning_sun=abilities("morning sun",132,0,"status",normal,"restores the user's hp. the amount of hp regained varies with the weather.")
mud_slap=abilities("mud-slap",73,20,"special",ground,"mud is hurled in the foe's face to inflict damage and lower its accuracy.")
muddy_water=abilities("muddy water",73,95,"special",water,"the user attacks with muddy water. it may also lower the foe's accuracy.")
mud_shot=abilities("mud shot",70,55,"special",ground,"the user attacks by hurling mud. it also reduces the foe's speed.")
mud_sport=abilities("mud sport",201,0,"status",ground,"weakens electric- type attacks while the user is in the battle.")
nature_power=abilities("nature power",173,0,"status",normal,"an attack that changes type depending on the user's location.")
needle_arm=abilities("needle arm",150,60,"physical",grass,"an attack using thorny arms. it may make the foe flinch.")
nightmare=abilities("nightmare",107,0,"status",ghost,"a sleeping foe is shown a nightmare that inflicts some damage every turn.")
night_shade=abilities("night shade",87,1,"special",ghost,"an attack with a mirage that inflicts damage matching the user's level.")
octazooka=abilities("octazooka",73,65,"special",water,"ink is blasted in the foe's face or eyes to damage and lower accuracy.")
odor_sleuth=abilities("odor sleuth",113,0,"status",normal,"completely negates the foe's efforts to heighten its abilities to evade.")
outrage=abilities("outrage",27,90,"physical",dragon,"the user thrashes about for two to three turns, then becomes confused.")
overheat=abilities("overheat",204,140,"physical",fire,"an intense attack that also sharply reduces the user's sp. atk stat.")
pain_split=abilities("pain split",91,0,"status",normal,"the user adds its hp to the foe's hp, then equally shares the total hp.")
pay_day=abilities("pay day",34,40,"special",normal,"numerous coins are hurled at the foe. money is earned after battle.")
peck=abilities("peck",0,35,"physical",flying,"the foe is jabbed with a sharply pointed beak or horn.")
perish_song=abilities("perish song",114,0,"status",normal,"any battler that hears this faints in three turns unless it switches.")
petal_dance=abilities("petal dance",27,70,"physical",grass,"the user attacks with petals for two to three turns, then gets confused.")
pin_missile=abilities("pin missile",29,14,"special",bug,"sharp pins are shot at the foe and hit two to five times at once.")
poisonpowder=abilities("poisonpowder",66,0,"status",poison,"a cloud of toxic dust is scattered. it may poison the foe.")
poison_fang=abilities("poison fang",202,50,"physical",poison,"the foe is bitten with toxic fangs. it may also badly poison the foe.")
poison_gas=abilities("poison gas",66,0,"status",poison,"the foe is sprayed with a cloud of toxic gas that may poison the foe.")
poison_sting=abilities("poison sting",2,15,"special",poison,"the foe is stabbed with a toxic barb, etc. it may poison the foe.")
poison_tail=abilities("poison tail",209,50,"physical",poison,"an attack with a high critical-hit ratio. it may also poison the foe.")
pound=abilities("pound",0,40,"physical",normal,"a physical attack delivered with a long tail or a foreleg, etc.")
powder_snow=abilities("powder snow",5,40,"special",ice,"blasts the foe with a snowy gust. it may cause freezing.")
present=abilities("present",122,1,"special",normal,"the foe is given a booby-trapped gift. it restores hp sometimes, however.")
protect=abilities("protect",111,0,"status",normal,"enables the user to evade all attacks. it may fail if used in succession.")
psybeam=abilities("psybeam",76,65,"special",psychic,"a peculiar ray is shot at the foe. it may leave the foe confused.")
psychic=abilities("psychic",72,90,"special",psychic,"a strong telekinetic attack. it may also lower the foe's sp. def stat.")
psycho_boost=abilities("psycho boost",204,140,"special",psychic,"an intense attack that also sharply reduces the user's sp. atk stat")
psych_up=abilities("psych up",143,0,"status",normal,"the user hypnotizes itself into copying any stat change made by the foe.")
psywave=abilities("psywave",88,1,"special",psychic,"the foe is attacked with an odd, hot energy wave that varies in intensity.")
pursuit=abilities("pursuit",128,40,"physical",dark,"an attack move that works especially well on a foe that is switching out.")
quick_attack=abilities("quick attack",103,40,"physical",normal,"an almost invisibly fast attack that is certain to strike first.")
rage=abilities("rage",81,20,"physical",normal,"an attack that becomes stronger each time the user is hit in battle.")
rain_dance=abilities("rain dance",136,0,"status",water,"a heavy rain falls for five turns, powering up water- type moves.")
rapid_spin=abilities("rapid spin",129,20,"physical",normal,"an attack that frees the user from bind, wrap, leech seed, and spikes.")
razor_leaf=abilities("razor leaf",43,55,"special",grass,"the foe is hit with a cutting leaf. it has a high critical-hit ratio.")
razor_wind=abilities("razor wind",39,80,"special",normal,"blades of wind hit the foe on the 2nd turn. it has a high critical-hit ratio.")
recover=abilities("recover",32,0,"status",normal,"a self-healing move that restores hp by up to half of the user's maximum hp.")
recycle=abilities("recycle",184,0,"status",normal,"a move that recycles a used item for use once more.")
reflect=abilities("reflect",65,0,"status",psychic,"a wall of light cuts damage from physical attacks for five turns.")
refresh=abilities("refresh",193,0,"status",normal,"a self-healing move that cures the user of a poisoning, burn, or paralysis.")
rest=abilities("rest",37,0,"status",psychic,"the user sleeps for two turns to fully restore hp and heal any status problem.")
return_=abilities("return",121,1,"physical",normal,"this attack move grows more powerful the more the user likes its trainer.")
revenge=abilities("revenge",185,60,"physical",fighting,"an attack move that gains in intensity if the target has hurt the user.")
reversal=abilities("reversal",99,1,"physical",fighting,"an all-out attack that becomes more powerful the less hp the user has.")
roar=abilities("roar",28,0,"status",normal,"the foe is made to switch out with an ally. in the wild, the battle ends.")
rock_blast=abilities("rock blast",29,25,"special",rock,"the user hurls two to five hard rocks at the foe to attack.")
rock_slide=abilities("rock slide",31,75,"special",rock,"large boulders are hurled at the foe. it may make the foe flinch.")
rock_smash=abilities("rock smash",69,20,"physical",fighting,"an attack that may also cut defense. it can also smash cracked boulders.")
rock_throw=abilities("rock throw",0,50,"special",rock,"the foe is attacked with a shower of small, easily thrown rocks.")
rock_tomb=abilities("rock tomb",70,50,"special",rock,"boulders are hurled at the foe. it also lowers the foe's speed if it hits.")
role_play=abilities("role play",178,0,"status",psychic,"the user mimics the foe completely and copies the foe's abilities.")
rolling_kick=abilities("rolling kick",31,60,"physical",fighting,"a quick kick from a rolling spin. it may make the foe flinch.")
rollout=abilities("rollout",117,30,"physical",rock,"a 5-turn rolling attack that becomes stronger each time it hits.")
sacred_fire=abilities("sacred fire",125,100,"special",fire,"a mystical and powerful fire attack that may inflict a burn.")
safeguard=abilities("safeguard",124,0,"status",normal,"it protects the user's party from all status problems for five turns.")
sand_attack=abilities("sand-attack",23,0,"status",ground,"a lot of sand is hurled in the foe's face, reducing its accuracy.")
sandstorm=abilities("sandstorm",115,0,"status",rock,"a 5-turn sandstorm that damages all types except rock, ground, and steel.")
sand_tomb=abilities("sand tomb",42,15,"special",ground,"the foe is trapped inside a painful sandstorm for two to five turns.")
scary_face=abilities("scary face",60,0,"status",normal,"frightens the foe with a scary face to sharply reduce its speed.")
scratch=abilities("scratch",0,40,"physical",normal,"hard, pointed, and sharp claws rake the foe.")
screech=abilities("screech",59,0,"status",normal,"an ear-splitting screech is emitted to sharply reduce the foe's defense.")
secret_power=abilities("secret power",197,70,"special",normal,"an attack that may have an additional effect that varies with the terrain.")
seismic_toss=abilities("seismic toss",87,1,"physical",fighting,"a gravity-fed throw that causes damage matching the user's level.")
selfdestruct=abilities("selfdestruct",7,200,"special",normal,"the user blows up to inflict severe damage, even making itself faint.")
shadow_ball=abilities("shadow ball",72,80,"special",ghost,"a shadowy blob is hurled at the foe. may also lower the foe's sp. def.")
shadow_punch=abilities("shadow punch",17,60,"physical",ghost,"the user throws a punch from the shadows. it cannot be evaded.")
sharpen=abilities("sharpen",10,0,"status",normal,"the user reduces its polygon count to sharpen edges and raise attack.")
sheer_cold=abilities("sheer cold",38,1,"special",ice,"the foe is attacked with ultimate cold that causes fainting if it hits.")
shock_wave=abilities("shock wave",17,60,"special",electric,"a rapid jolt of electricity strikes the foe. it can't be evaded.")
signal_beam=abilities("signal beam",76,75,"special",bug,"the foe is hit with a flashing beam that may also cause confusion.")
silver_wind=abilities("silver wind",140,60,"special",bug,"the foe is attacked with a silver dust. it may raise all the user's stats.")
sing=abilities("sing",1,0,"status",normal,"a soothing song in a calming voice lulls the foe into a deep slumber.")
sketch=abilities("sketch",95,0,"status",normal,"this move copies the move last used by the foe, then disappears.")
skill_swap=abilities("skill swap",191,0,"status",psychic,"the user employs its psychic power to swap abilities with the foe.")
skull_bash=abilities("skull bash",145,100,"physical",normal,"the user raises its defense in the 1st turn, then attacks in the 2nd turn.")
sky_attack=abilities("sky attack",75,140,"special",flying,"a 2nd-turn attack move with a high critical-hit ratio. the foe may flinch.")
sky_uppercut=abilities("sky uppercut",207,85,"physical",fighting,"the user attacks with an uppercut thrown skywards with force.")
slack_off=abilities("slack off",32,0,"status",normal,"the user slacks off and restores its hp by half its full hp.")
slam=abilities("slam",0,80,"physical",normal,"the foe is struck with a long tail, vines, etc.")
slash=abilities("slash",43,70,"physical",normal,"the foe is slashed with claws, etc. it has a high critical-hit ratio.")
sleep_powder=abilities("sleep powder",1,0,"status",grass,"a sleep-inducing dust is scattered in high volume around a foe.")
sleep_talk=abilities("sleep talk",97,0,"status",normal,"while asleep, the user randomly uses one of the moves it knows.")
sludge=abilities("sludge",2,65,"special",poison,"toxic sludge is hurled at the foe. it may poison the target.")
sludge_bomb=abilities("sludge bomb",2,90,"special",poison,"filthy sludge is hurled at the foe. it may poison the target.")
smellingsalt=abilities("smellingsalt",171,60,"physical",normal,"doubly effective on a paralyzed foe, but it also cures the foe's paralysis.")
smog=abilities("smog",2,20,"special",poison,"the foe is attacked with exhaust gases. it may also poison the foe.")
smokescreen=abilities("smokescreen",23,0,"status",normal,"an obscuring cloud of smoke or ink reduces the foe's accuracy.")
snatch=abilities("snatch",195,0,"status",dark,"steals the effects of the foe's healing or status- changing move.")
snore=abilities("snore",92,40,"special",normal,"an attack that can be used only while asleep. it may cause flinching.")
softboiled=abilities("softboiled",157,0,"status",normal,"heals the user by up to half its full hp. it can be used to heal an ally.")
solarbeam=abilities("solarbeam",151,120,"special",grass,"a 2-turn move that blasts the foe with absorbed energy in the 2nd turn.")
sonicboom=abilities("sonicboom",130,1,"special",normal,"the foe is hit with a shock wave that always inflicts 20- hp damage.")
spark=abilities("spark",6,65,"physical",electric,"an electrically charged tackle that may also paralyze the foe.")
spider_web=abilities("spider web",106,0,"status",bug,"ensnares the foe  with sticky string so it doesn't flee or switch out.")
spikes=abilities("spikes",112,0,"status",ground,"a trap of spikes is laid around the foe's party to hurt foes switching in.")
spike_cannon=abilities("spike cannon",29,20,"special",normal,"sharp spikes are fired at the foe to strike two to five times.")
spite=abilities("spite",100,0,"status",ghost,"a move that cuts 2 to 5 pp from the move last used by the foe.")
spit_up=abilities("spit up",161,100,"special",normal,"the power built using stockpile is released at once for attack.")
splash=abilities("splash",85,0,"status",normal,"the user just flops and splashes around without having any effect.")
spore=abilities("spore",1,0,"status",grass,"the user scatters bursts of fine spores that induce sleep.")
steel_wing=abilities("steel wing",138,70,"physical",steel,"the foe is hit with wings of steel. it may also raise the user's defense.")
stockpile=abilities("stockpile",160,0,"status",normal,"the user charges up power for use later. it can be used three times.")
stomp=abilities("stomp",150,65,"physical",normal,"the foe is stomped with a big foot. it may make the foe flinch.")
strength=abilities("strength",0,80,"physical",normal,"the foe is slugged at maximum power. can also be used to move boulders.")
string_shot=abilities("string shot",20,0,"status",bug,"the foe is bound with strings shot from the mouth to reduce its speed.")
struggle=abilities("struggle",48,50,"physical",normal,"an attack that is used only if there is no pp. it also hurts the user.")
stun_spore=abilities("stun spore",67,0,"status",grass,"paralyzing dust is scattered wildly. it may paralyze the foe.")
submission=abilities("submission",48,80,"physical",fighting,"a reckless, full- body throw attack that also hurts the user a little.")
substitute=abilities("substitute",79,0,"status",normal,"the user creates a decoy using one- quarter of its full hp.")
sunny_day=abilities("sunny day",137,0,"status",fire,"the sun blazes for five turns, powering up fire-type moves.")
superpower=abilities("superpower",182,120,"physical",fighting,"a powerful attack, but it also lowers the user's attack and defense stats.")
supersonic=abilities("supersonic",49,0,"status",normal,"the user generates odd sound waves. it may confuse the foe.")
super_fang=abilities("super fang",40,1,"physical",normal,"the user attacks with sharp fangs and halves the foe's hp.")
surf=abilities("surf",0,95,"special",water,"a big wave crashes down on the foe. can also be used for crossing water.")
swagger=abilities("swagger",118,0,"status",normal,"a move that makes the foe confused, but also sharply raises its attack.")
swallow=abilities("swallow",162,0,"status",normal,"the energy it built using stockpile is absorbed to restore hp.")
sweet_kiss=abilities("sweet kiss",49,0,"status",normal,"the user kisses the foe with sweet cuteness that causes confusion.")
sweet_scent=abilities("sweet scent",24,0,"status",normal,"allures the foe to reduce evasiveness. it also attracts wild pok{ae}mon.")
swift=abilities("swift",17,60,"special",normal,"star-shaped rays that never miss are fired at all foes in battle.")
swords_dance=abilities("swords dance",50,0,"status",normal,"a frenetic dance of fighting. it sharply raises the attack stat.")
synthesis=abilities("synthesis",133,0,"status",grass,"restores the user's hp. the amount of hp regained varies with the weather.")
tackle=abilities("tackle",0,35,"physical",normal,"a physical attack in which the user charges, full body, into the foe.")
tail_glow=abilities("tail glow",53,0,"status",bug,"the user flashes a light that sharply raises its sp. atk stat.")
tail_whip=abilities("tail whip",19,0,"status",normal,"the user wags its tail cutely, making the foe lower its defense stat.")
take_down=abilities("take down",48,90,"physical",normal,"a reckless, full- body charge attack that also hurts the user a little.")
taunt=abilities("taunt",175,0,"status",dark,"the foe is taunted into a rage that allows it to use only attack moves.")
teeter_dance=abilities("teeter dance",199,0,"status",normal,"a wobbly dance that confuses all the pok{ae}mon in battle.")
teleport=abilities("teleport",153,0,"status",psychic,"use it to flee from any wild pok{ae}mon. also warps to the last poke center.")
thief=abilities("thief",105,40,"physical",dark,"an attack that may take the foe's held item if the user isn't holding one.")
thrash=abilities("thrash",27,90,"physical",normal,"the user rampages about for two to three turns, then becomes confused.")
thunder=abilities("thunder",152,120,"special",electric,"a brutal lightning attack that may also leave the foe paralyzed.")
thunderbolt=abilities("thunderbolt",6,95,"special",electric,"a strong electrical attack that may also leave the foe paralyzed.")
thunderpunch=abilities("thunderpunch",6,75,"physical",electric,"the foe is punched with an electrified fist. it may leave the foe paralyzed.")
thundershock=abilities("thundershock",6,40,"special",electric,"an electric shock attack that may also leave the foe paralyzed.")
thunder_wave=abilities("thunder wave",67,0,"status",electric,"a weak electric shock that is sure to cause paralysis if it hits.")
tickle=abilities("tickle",205,0,"status",normal,"the foe is made to laugh, reducing its attack and defense stats.")
torment=abilities("torment",165,0,"status",dark,"it enrages the foe, making it incapable of using the same move successively.")
toxic=abilities("toxic",33,0,"status",poison,"a move that badly poisons the foe. its poison damage worsens every turn.")
transform=abilities("transform",57,0,"status",normal,"the user transforms into a copy of the foe with even the same move set.")
trick=abilities("trick",177,0,"status",psychic,"a move that tricks the foe into trading held items with the user.")
triple_kick=abilities("triple kick",104,10,"physical",fighting,"a 3-kick attack that becomes more powerful with each successive hit.")
tri_attack=abilities("tri attack",36,80,"special",normal,"a simultaneous 3-beam attack that may paralyze, burn, or freeze the foe.")
twineedle=abilities("twineedle",77,25,"special",bug,"the foe is stabbed twice with foreleg stingers. it may poison the foe.")
twister=abilities("twister",146,40,"special",dragon,"a vicious twister attacks the foe. it may make the foe flinch.")
uproar=abilities("uproar",159,50,"special",normal,"the user attacks in an uproar that prevents sleep for two to five turns.")
vicegrip=abilities("vicegrip",0,55,"physical",normal,"huge, impressive pincers grip and squeeze the foe.")
vine_whip=abilities("vine whip",0,35,"physical",grass,"the foe is struck with slender, whip- like vines.")
vital_throw=abilities("vital throw",78,70,"physical",fighting,"makes the user attack after the foe. in return, it will not miss.")
volt_tackle=abilities("volt tackle",198,120,"physical",electric,"the user throws an electrified tackle. it hurts the user a little.")
waterfall=abilities("waterfall",0,80,"physical",water,"a powerful charge attack. it can also be used to climb a waterfall.")
water_gun=abilities("water gun",0,40,"special",water,"the foe is struck with a lot of water expelled forcibly from the mouth.")
water_pulse=abilities("water pulse",76,60,"special",water,"an attack with a pulsing blast of water. it may also confuse the foe.")
water_sport=abilities("water sport",210,0,"status",water,"weakens fire-type attacks while the user is in the battle.")
water_spout=abilities("water spout",190,150,"special",water,"the higher the user's hp, the more powerful this attack becomes.")
weather_ball=abilities("weather ball",203,50,"special",normal,"an attack that varies in power and type depending on the weather.")
whirlpool=abilities("whirlpool",42,15,"special",water,"the foe is trapped in a fast, vicious whirlpool for two to five turns.")
whirlwind=abilities("whirlwind",28,0,"status",normal,"the foe is made to switch out with an ally. in the wild, the battle ends.")
will_o_wisp=abilities("will-o-wisp",167,0,"status",fire,"a sinister, bluish white flame is shot at the foe to inflict a burn.")
wing_attack=abilities("wing attack",0,60,"physical",flying,"the foe is struck with large, imposing wings spread wide.")
wish=abilities("wish",179,0,"status",normal,"a self-healing move that restores half the full hp on the next turn.")
withdraw=abilities("withdraw",11,0,"status",water,"the user withdraws its body in its hard shell, raising its defense stat.")
wrap=abilities("wrap",42,15,"physical",normal,"a long body or vines are used to wrap the foe for two to five turns.")
yawn=abilities("yawn",187,0,"status",normal,"a huge yawn lulls the foe into falling asleep on the next turn.")
zap_cannon=abilities("zap cannon",6,100,"special",electric,"an electric blast is fired like a cannon to inflict damage and paralyze.")

    
'''
pokemon go here:

class pokemon:
  def __init__ (self,name,species,hp,atk,def,spatk,spdef,speed,type,type1=none,a1,l1,a2,l2,a3,l3,a4,l4,a5,l5,a6,l6,a7,l7,a8,l8,a9,l9,a10,l10,a11,l11,a12,l12,a13,l13,a14,l14,a15,l15,a16,l16,a17,l17,a18,l18,a19,l19,a20,l20,a21,l21,a22,l22,a23,l23,a4,l24,a25,l25,a26,l26,a27,l27,a28,l28,a29,l29):

'''
abra=pokemon("abra","psi",25,20,15,105,55,90,psychic,psychic,teleport,0,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
aerodactyl=pokemon("aerodactyl","fossil",80,105,65,60,75,130,rock,flying,wing_attack,0,bite,1,supersonic,2,ancientpower,2,scary_face,3,take_down,4,hyper_beam,5,agility,8,bite,15,supersonic,22,ancientpower,29,scary_face,36,take_down,43,hyper_beam,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
aipom=pokemon("aipom","long tail",55,70,55,40,55,85,normal,normal,scratch,0,tail_whip,0,mist,1,baton_pass,1,drill_peck,2,fury_swipes,3,swift,3,screech,4,agility,5,sand_attack,6,mist,13,baton_pass,18,drill_peck,25,fury_swipes,31,swift,38,screech,43,agility,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
alakazam=pokemon("alakazam","psi",55,50,45,135,85,120,psychic,psychic,teleport,0,kinesis,0,confusion,0,confusion,1,disable,1,psybeam,2,reflect,2,recover,2,future_sight,3,dig,3,psychic,3,cut,4,confusion,16,disable,18,psybeam,21,reflect,23,recover,25,future_sight,30,dig,33,psychic,36,cut,43,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
ampharos=pokemon("ampharos","light",90,75,75,115,90,55,electric,electric,tackle,0,growl,0,thundershock,0,thunder_wave,0,thunder_wave,1,cotton_spore,2,thunderpunch,3,light_screen,4,thunder,5,thundershock,9,thunder_wave,18,cotton_spore,27,thunderpunch,30,light_screen,42,thunder,57,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
arbok=pokemon("arbok","cobra",60,85,69,65,79,80,poison,poison,wrap,0,leer,0,poison_sting,0,bite,0,bite,1,glare,2,screech,2,acid,3,stockpile,4,psycho_boost,4,spit_up,4,haze,5,poison_sting,8,bite,13,glare,20,screech,28,acid,38,stockpile,46,psycho_boost,46,spit_up,46,haze,56,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
arcanine=pokemon("arcanine","legendary",90,110,80,100,80,95,fire,fire,bite,0,roar,0,ember,0,psybeam,0,extremespeed,4,extremespeed,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
ariados=pokemon("ariados","long leg",70,90,70,60,60,40,bug,poison,poison_sting,0,string_shot,0,scary_face,0,constrict,0,constrict,1,night_shade,1,leech_life,2,fury_swipes,3,spider_web,4,agility,5,scary_face,6,psychic,6,constrict,11,night_shade,17,leech_life,25,fury_swipes,34,spider_web,43,agility,53,psychic,63,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
articuno=pokemon("articuno","freeze",90,85,100,95,125,85,ice,flying,gust,0,powder_snow,0,mist,1,agility,2,mind_reader,3,ice_beam,4,reflect,6,blizzard,7,leech_seed,8,mist,13,agility,25,mind_reader,37,ice_beam,49,reflect,61,blizzard,73,leech_seed,85,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
azumarill=pokemon("azumarill","aqua rabbit",100,50,80,50,80,50,water,water,tackle,0,defense_curl,0,tail_whip,0,water_gun,0,water_gun,1,rollout,1,bubblebeam,2,defense_curl,3,double_edge,3,rain_dance,4,hydro_pump,5,tail_whip,6,water_gun,10,rollout,15,bubblebeam,24,double_edge,34,rain_dance,45,hydro_pump,57,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
bayleef=pokemon("bayleef","leaf",60,62,80,63,80,60,grass,grass,tackle,0,growl,0,razor_leaf,0,reflect,0,reflect,1,poisonpowder,1,synthesis,2,body_slam,3,light_screen,3,safeguard,4,solarbeam,5,razor_leaf,8,reflect,12,poisonpowder,15,synthesis,23,body_slam,31,light_screen,39,safeguard,47,solarbeam,55,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
beedrill=pokemon("beedrill","poison bee",65,80,40,45,80,75,bug,poison,fury_attack,0,fury_attack,1,focus_energy,1,twineedle,2,rage,2,pursuit,3,pin_missile,3,agility,4,rolling_kick,4,fury_attack,10,focus_energy,15,twineedle,20,rage,25,pursuit,30,pin_missile,35,agility,40,rolling_kick,45,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
bellossom=pokemon("bellossom","flower",75,80,85,90,100,50,grass,grass,absorb,0,sweet_scent,0,stun_spore,0,earthquake,0,petal_dance,4,solarbeam,5,petal_dance,44,solarbeam,55,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
bellsprout=pokemon("bellsprout","flower",50,75,35,70,30,40,grass,poison,vine_whip,0,wrap,1,sleep_powder,1,poisonpowder,1,stun_spore,1,acid,2,sweet_scent,3,razor_leaf,3,slam,4,growth,6,wrap,11,sleep_powder,15,poisonpowder,17,stun_spore,19,acid,23,sweet_scent,30,razor_leaf,37,slam,45,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
blastoise=pokemon("blastoise","shellfish",79,83,100,85,105,78,water,water,tackle,0,tail_whip,0,bubble,0,withdraw,0,withdraw,1,water_gun,1,bite,1,rapid_spin,2,protect,3,tail_whip,4,rain_dance,4,skull_bash,5,hydro_pump,6,bubble,7,withdraw,10,water_gun,13,bite,19,rapid_spin,25,protect,31,rain_dance,42,skull_bash,55,hydro_pump,68,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
blissey=pokemon("blissey","happiness",255,10,10,75,135,55,normal,normal,pound,0,growl,0,softboiled,1,doubleslap,1,minimize,1,sing,2,egg_bomb,2,defense_curl,3,tail_whip,4,light_screen,4,double_edge,4,fury_attack,7,softboiled,10,doubleslap,13,minimize,18,sing,23,egg_bomb,28,defense_curl,33,light_screen,40,double_edge,47,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
bulbasaur=pokemon("bulbasaur","seed",45,49,49,65,65,45,grass,poison,tackle,0,vine_whip,1,poisonpowder,1,sleep_powder,1,razor_leaf,2,sweet_scent,2,growth,3,synthesis,3,growl,4,solarbeam,4,leech_seed,7,vine_whip,10,poisonpowder,15,sleep_powder,15,razor_leaf,20,sweet_scent,25,growth,32,synthesis,39,solarbeam,46,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
butterfree=pokemon("butterfree","butterfly",60,45,50,80,80,70,bug,flying,confusion,0,confusion,1,poisonpowder,1,stun_spore,1,sleep_powder,1,supersonic,1,whirlwind,2,gust,2,psybeam,3,safeguard,4,aurora_beam,4,confusion,10,poisonpowder,13,stun_spore,14,sleep_powder,15,supersonic,18,whirlwind,23,gust,28,psybeam,34,safeguard,40,aurora_beam,47,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
caterpie=pokemon("caterpie","worm",45,30,35,20,20,45,bug,bug,tackle,0,string_shot,0,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
celebi=pokemon("celebi","time travel",100,100,100,100,100,100,psychic,grass,leech_seed,0,confusion,0,recover,0,heal_bell,0,safeguard,1,ancientpower,2,future_sight,3,baton_pass,4,perish_song,5,safeguard,10,ancientpower,20,future_sight,30,baton_pass,40,perish_song,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
chansey=pokemon("chansey","egg",250,5,5,35,105,50,normal,normal,pound,0,growl,0,softboiled,1,doubleslap,1,minimize,2,sing,2,egg_bomb,3,defense_curl,4,light_screen,4,tail_whip,5,double_edge,5,fury_attack,9,softboiled,13,doubleslap,17,minimize,23,sing,29,egg_bomb,35,defense_curl,41,light_screen,49,double_edge,57,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
charizard=pokemon("charizard","flame",78,84,78,109,85,100,fire,flying,pound,0,scratch,0,growl,0,ember,0,metal_claw,0,metal_claw,1,smokescreen,2,scary_face,2,flamethrower,3,wing_attack,3,slash,4,dragon_rage,5,fire_spin,6,ember,7,metal_claw,13,smokescreen,20,scary_face,27,flamethrower,34,wing_attack,36,slash,44,dragon_rage,54,fire_spin,64,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
charmander=pokemon("charmander","lizard",39,52,43,60,50,65,fire,fire,scratch,0,growl,0,metal_claw,1,smokescreen,1,scary_face,2,flamethrower,3,slash,3,dragon_rage,4,fire_spin,4,ember,7,metal_claw,13,smokescreen,19,scary_face,25,flamethrower,31,slash,37,dragon_rage,43,fire_spin,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
charmeleon=pokemon("charmeleon","flame",58,64,58,80,65,80,fire,fire,scratch,0,growl,0,ember,0,metal_claw,1,smokescreen,2,scary_face,2,flamethrower,3,slash,4,dragon_rage,4,fire_spin,5,ember,7,metal_claw,13,smokescreen,20,scary_face,27,flamethrower,34,slash,41,dragon_rage,48,fire_spin,55,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
chikorita=pokemon("chikorita","leaf",45,49,65,49,65,45,grass,grass,tackle,0,growl,0,reflect,1,poisonpowder,1,synthesis,2,body_slam,2,light_screen,3,safeguard,4,solarbeam,5,razor_leaf,8,reflect,12,poisonpowder,15,synthesis,22,body_slam,29,light_screen,36,safeguard,43,solarbeam,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
chinchou=pokemon("chinchou","angler",75,38,38,56,56,67,water,electric,bubble,0,thunder_wave,0,flail,1,water_gun,1,spark,2,confuse_ray,2,take_down,3,hydro_pump,4,guillotine,4,supersonic,5,flail,13,water_gun,17,spark,25,confuse_ray,29,take_down,37,hydro_pump,41,guillotine,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
clefable=pokemon("clefable","fairy",95,70,73,85,90,60,normal,normal,sing,0,doubleslap,0,minimize,0,metronome,0,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
clefairy=pokemon("clefairy","fairy",70,45,48,60,65,35,normal,normal,pound,0,growl,0,doubleslap,1,scratch,1,minimize,2,defense_curl,2,metronome,2,submission,3,moonlight,3,light_screen,4,flamethrower,4,encore,5,sing,9,doubleslap,13,scratch,17,minimize,21,defense_curl,25,metronome,29,submission,33,moonlight,37,light_screen,41,flamethrower,45,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
cleffa=pokemon("cleffa","star shape",50,25,28,45,55,15,normal,normal,pound,0,charm,0,sweet_kiss,1,earthquake,1,encore,4,sing,8,sweet_kiss,13,earthquake,17,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
cloyster=pokemon("cloyster","bivalve",50,95,180,85,45,70,water,ice,withdraw,0,supersonic,0,aurora_beam,0,protect,0,spikes,3,spike_cannon,4,spikes,36,spike_cannon,43,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
corsola=pokemon("corsola","coral",55,55,85,65,85,35,water,rock,tackle,0,bubble,1,recover,1,fury_attack,1,bubblebeam,2,spike_cannon,2,psychic,3,mirror_coat,3,ancientpower,4,harden,6,bubble,12,recover,17,fury_attack,17,bubblebeam,23,spike_cannon,28,psychic,34,mirror_coat,39,ancientpower,45,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
crobat=pokemon("crobat","bat",85,90,80,70,80,130,poison,flying,screech,0,leech_life,0,mist,0,supersonic,0,supersonic,1,bite,1,wing_attack,2,confuse_ray,2,ice_beam,3,mean_look,4,sonicboom,4,haze,5,mist,6,supersonic,11,bite,16,wing_attack,21,confuse_ray,28,ice_beam,35,mean_look,42,sonicboom,49,haze,56,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
croconaw=pokemon("croconaw","big jaw",65,80,80,59,63,58,water,water,scratch,0,leer,0,rage,0,water_gun,1,bite,2,scary_face,2,slash,3,screech,4,hydro_pump,5,rage,7,water_gun,13,bite,21,scary_face,28,slash,37,screech,45,hydro_pump,55,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
cubone=pokemon("cubone","lonely",50,50,95,40,50,35,ground,ground,growl,0,headbutt,1,leer,1,focus_energy,2,bonemerang,2,rage,2,false_swipe,3,thrash,3,bone_rush,4,double_edge,4,tail_whip,5,bone_club,9,headbutt,13,leer,17,focus_energy,21,bonemerang,25,rage,29,false_swipe,33,thrash,37,bone_rush,41,double_edge,45,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
cyndaquil=pokemon("cyndaquil","fire mouse",39,52,43,60,50,65,fire,fire,tackle,0,leer,0,ember,1,quick_attack,1,flame_wheel,2,swift,3,flamethrower,4,smokescreen,6,ember,12,quick_attack,19,flame_wheel,27,swift,36,flamethrower,46,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
delibird=pokemon("delibird","delivery",45,55,45,65,45,75,ice,flying,present,0,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
dewgong=pokemon("dewgong","sea lion",90,70,80,70,95,70,water,ice,counter,0,headbutt,0,growl,0,icy_wind,0,aurora_beam,0,icy_wind,1,aurora_beam,2,rest,2,leech_seed,3,take_down,4,ice_beam,5,safeguard,6,growl,9,icy_wind,17,aurora_beam,21,rest,29,leech_seed,34,take_down,42,ice_beam,51,safeguard,64,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
diglett=pokemon("diglett","mole",10,55,25,35,45,95,ground,ground,sand_attack,0,scratch,0,dig,1,fury_swipes,2,mud_slap,2,slash,3,earthquake,4,fissure,4,growl,5,magnitude,9,dig,17,fury_swipes,21,mud_slap,25,slash,33,earthquake,41,fissure,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
ditto=pokemon("ditto","transform",48,48,48,48,48,48,normal,normal,transform,0,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
dodrio=pokemon("dodrio","triple bird",60,110,70,60,60,100,normal,flying,peck,0,growl,0,pursuit,0,fury_attack,0,fury_attack,1,tri_attack,2,rage,2,uproar,3,drill_peck,4,agility,6,pursuit,9,fury_attack,13,tri_attack,21,rage,25,uproar,38,drill_peck,47,agility,60,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
doduo=pokemon("doduo","twin bird",35,85,45,35,35,75,normal,flying,peck,0,growl,0,fury_attack,1,tri_attack,2,rage,2,uproar,3,drill_peck,3,agility,4,pursuit,9,fury_attack,13,tri_attack,21,rage,25,uproar,33,drill_peck,37,agility,45,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
donphan=pokemon("donphan","armor",90,120,120,60,60,50,ground,ground,psybeam,0,horn_attack,0,growl,0,flail,1,fury_attack,2,rollout,3,rapid_spin,4,earthquake,4,defense_curl,9,flail,17,fury_attack,25,rollout,33,rapid_spin,41,earthquake,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
dragonair=pokemon("dragonair","dragon",61,84,65,70,70,70,dragon,dragon,wrap,0,leer,0,thunder_wave,0,twister,0,twister,1,dragon_rage,2,slam,2,agility,3,safeguard,4,outrage,5,hyper_beam,6,thunder_wave,8,twister,15,dragon_rage,22,slam,29,agility,38,safeguard,47,outrage,56,hyper_beam,65,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
dragonite=pokemon("dragonite","dragon",91,134,95,100,100,80,dragon,flying,wrap,0,leer,0,thunder_wave,0,twister,0,twister,1,dragon_rage,2,slam,2,agility,3,safeguard,4,wing_attack,5,outrage,6,hyper_beam,7,thunder_wave,8,twister,15,dragon_rage,22,slam,29,agility,38,safeguard,47,wing_attack,55,outrage,61,hyper_beam,75,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
dratini=pokemon("dratini","dragon",41,64,45,50,50,50,dragon,dragon,wrap,0,leer,0,twister,1,dragon_rage,2,slam,2,agility,3,safeguard,4,outrage,5,hyper_beam,5,thunder_wave,8,twister,15,dragon_rage,22,slam,29,agility,36,safeguard,43,outrage,50,hyper_beam,57,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
drowzee=pokemon("drowzee","hypnosis",60,48,45,43,90,42,psychic,psychic,pound,0,hypnosis,0,confusion,1,headbutt,1,poison_gas,2,meditate,2,psychic,3,psych_up,3,swagger,4,future_sight,4,disable,7,confusion,11,headbutt,17,poison_gas,21,meditate,27,psychic,31,psych_up,37,swagger,41,future_sight,47,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
dugtrio=pokemon("dugtrio","mole",35,80,50,50,70,120,ground,ground,tri_attack,0,scratch,0,sand_attack,0,growl,0,dig,1,fury_swipes,2,mud_slap,2,mega_drain,2,slash,3,growl,5,earthquake,5,fissure,6,magnitude,9,dig,17,fury_swipes,21,mud_slap,25,mega_drain,26,slash,38,earthquake,51,fissure,64,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
dunsparce=pokemon("dunsparce","land snake",100,70,70,65,65,45,normal,normal,rage,0,mega_kick,1,glare,1,rollout,2,spite,2,pursuit,3,screech,3,defense_curl,4,take_down,4,flail,4,rolling_kick,5,mega_kick,11,glare,14,rollout,21,spite,24,pursuit,31,screech,34,take_down,41,flail,44,rolling_kick,51,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
eevee=pokemon("eevee","evolution",55,55,50,45,65,55,normal,normal,tackle,0,tail_whip,0,swords_dance,0,growl,1,quick_attack,2,bite,3,baton_pass,3,take_down,4,sand_attack,8,growl,16,quick_attack,23,bite,30,baton_pass,36,take_down,42,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
ekans=pokemon("ekans","snake",35,60,44,40,54,55,poison,poison,wrap,0,leer,0,bite,1,glare,2,screech,2,acid,3,stockpile,3,psycho_boost,3,spit_up,3,haze,4,poison_sting,8,bite,13,glare,20,screech,25,acid,32,stockpile,37,psycho_boost,37,spit_up,37,haze,44,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
electabuzz=pokemon("electabuzz","electric",65,83,57,95,85,105,electric,electric,quick_attack,0,leer,0,thunderpunch,0,light_screen,1,swift,2,screech,3,thunderbolt,4,thunder,5,thunderpunch,9,light_screen,17,swift,25,screech,36,thunderbolt,47,thunder,58,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
electrode=pokemon("electrode","ball",60,50,70,80,80,140,electric,electric,guillotine,0,tackle,0,screech,0,sonicboom,0,sonicboom,1,spark,2,selfdestruct,2,rollout,3,light_screen,4,swift,4,explosion,5,mirror_coat,5,screech,8,sonicboom,15,spark,21,selfdestruct,27,rollout,34,light_screen,41,swift,48,explosion,54,mirror_coat,59,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
elekid=pokemon("elekid","electric",45,63,37,65,55,95,electric,electric,quick_attack,0,leer,0,light_screen,1,swift,2,screech,3,thunderbolt,4,thunder,4,thunderpunch,9,light_screen,17,swift,25,screech,33,thunderbolt,41,thunder,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
entei=pokemon("entei","volcano",115,115,85,90,75,100,fire,fire,bite,0,leer,0,ember,1,roar,2,fire_spin,3,stomp,4,flamethrower,5,swagger,6,fire_blast,7,dig,8,ember,11,roar,21,fire_spin,31,stomp,41,flamethrower,51,swagger,61,fire_blast,71,dig,81,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
espeon=pokemon("espeon","sun",65,65,60,130,95,110,psychic,psychic,tackle,0,tail_whip,0,swords_dance,0,confusion,1,quick_attack,2,swift,3,psybeam,3,psych_up,4,psychic,4,morning_sun,5,sand_attack,8,confusion,16,quick_attack,23,swift,30,psybeam,36,psych_up,42,psychic,47,morning_sun,52,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
exeggcute=pokemon("exeggcute","egg",60,40,80,60,45,40,grass,psychic,barrage,0,uproar,0,hypnosis,0,leech_seed,1,confusion,1,stun_spore,2,poisonpowder,3,sleep_powder,3,solarbeam,4,reflect,7,leech_seed,13,confusion,19,stun_spore,25,poisonpowder,31,sleep_powder,37,solarbeam,43,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
exeggutor=pokemon("exeggutor","coconut",95,95,85,125,65,55,grass,psychic,barrage,0,hypnosis,0,confusion,0,stomp,1,egg_bomb,3,stomp,19,egg_bomb,31,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
farfetchd=pokemon("farfetch'd","wild duck",52,65,55,58,62,60,normal,flying,peck,0,leer,1,fury_attack,1,jump_kick,2,fury_cutter,2,swords_dance,3,agility,3,slash,4,false_swipe,4,sand_attack,6,leer,11,fury_attack,16,jump_kick,21,fury_cutter,26,swords_dance,31,agility,36,slash,41,false_swipe,46,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
fearow=pokemon("fearow","beak",65,90,65,61,61,100,normal,flying,peck,0,growl,0,leer,0,fury_attack,0,fury_attack,1,pursuit,2,mirror_move,3,drill_peck,4,agility,4,leer,7,fury_attack,13,pursuit,26,mirror_move,32,drill_peck,40,agility,47,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
feraligatr=pokemon("feraligatr","big jaw",85,105,100,79,83,78,water,water,scratch,0,leer,0,rage,0,water_gun,0,water_gun,1,bite,2,scary_face,2,slash,3,screech,4,hydro_pump,5,rage,7,water_gun,13,bite,21,scary_face,28,slash,38,screech,47,hydro_pump,58,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
flaaffy=pokemon("flaaffy","wool",70,55,55,80,60,45,electric,electric,tackle,0,growl,0,thundershock,0,thunder_wave,1,cotton_spore,2,light_screen,3,thunder,4,thundershock,9,thunder_wave,18,cotton_spore,27,light_screen,36,thunder,45,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
flareon=pokemon("flareon","flame",65,130,60,95,110,65,fire,fire,tackle,0,tail_whip,0,swords_dance,0,ember,1,quick_attack,2,bite,3,fire_spin,3,smog,4,leer,4,flamethrower,5,sand_attack,8,ember,16,quick_attack,23,bite,30,fire_spin,36,smog,42,leer,47,flamethrower,52,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
forretress=pokemon("forretress","bagworm",75,90,140,60,60,40,bug,steel,tackle,0,protect,0,selfdestruct,0,take_down,1,rapid_spin,2,bide,2,zap_cannon,3,explosion,3,spikes,4,double_edge,5,selfdestruct,8,take_down,15,rapid_spin,22,bide,29,zap_cannon,31,explosion,39,spikes,49,double_edge,59,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
furret=pokemon("furret","long body",85,76,64,45,55,90,normal,normal,scratch,0,defense_curl,0,quick_attack,0,fury_swipes,1,swords_dance,1,slam,2,scratch,3,defense_curl,4,rest,4,amnesia,5,quick_attack,7,fury_swipes,12,swords_dance,19,slam,28,scratch,37,rest,48,amnesia,59,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
gastly=pokemon("gastly","gas",30,35,30,100,35,80,ghost,poison,hypnosis,0,lick,0,curse,1,night_shade,1,confuse_ray,2,dream_eater,2,destiny_bond,3,shadow_ball,3,nightmare,4,mean_look,4,spite,8,curse,13,night_shade,16,confuse_ray,21,dream_eater,28,destiny_bond,33,shadow_ball,36,nightmare,41,mean_look,48,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
gengar=pokemon("gengar","shadow",60,65,60,130,75,110,ghost,poison,hypnosis,0,lick,0,spite,0,curse,1,night_shade,1,confuse_ray,2,seismic_toss,2,dream_eater,3,destiny_bond,3,shadow_ball,4,nightmare,5,mean_look,6,spite,8,curse,13,night_shade,16,confuse_ray,21,seismic_toss,25,dream_eater,31,destiny_bond,39,shadow_ball,45,nightmare,53,mean_look,64,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
geodude=pokemon("geodude","rock",40,80,100,30,30,20,rock,ground,tackle,0,defense_curl,0,rock_throw,1,magnitude,1,selfdestruct,2,rollout,2,psychic,3,earthquake,3,explosion,4,double_edge,4,bite,6,rock_throw,11,magnitude,16,selfdestruct,21,rollout,26,psychic,31,earthquake,36,explosion,41,double_edge,46,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
girafarig=pokemon("girafarig","long neck",70,80,65,90,65,85,normal,psychic,tackle,0,growl,0,confusion,1,stomp,1,psybeam,2,agility,3,baton_pass,3,psybeam,4,crunch,4,mist,7,confusion,13,stomp,19,psybeam,25,agility,31,baton_pass,37,psybeam,43,crunch,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
gligar=pokemon("gligar","flyscorpion",65,75,105,35,65,85,ground,flying,poison_sting,0,harden,1,quick_attack,2,faint_attack,2,slash,3,screech,4,guillotine,5,sand_attack,6,harden,13,quick_attack,20,faint_attack,28,slash,36,screech,44,guillotine,52,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
gloom=pokemon("gloom","weed",60,65,70,85,75,40,grass,poison,absorb,0,sweet_scent,0,poisonpowder,0,poisonpowder,1,stun_spore,1,sleep_powder,1,acid,2,moonlight,3,petal_dance,4,sweet_scent,7,poisonpowder,14,stun_spore,16,sleep_powder,18,acid,24,moonlight,35,petal_dance,44,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
golbat=pokemon("golbat","bat",75,80,70,65,75,90,poison,flying,screech,0,leech_life,0,mist,0,supersonic,0,supersonic,1,bite,1,wing_attack,2,confuse_ray,2,ice_beam,3,mean_look,4,sonicboom,4,haze,5,mist,6,supersonic,11,bite,16,wing_attack,21,confuse_ray,28,ice_beam,35,mean_look,42,sonicboom,49,haze,56,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
goldeen=pokemon("goldeen","goldfish",45,67,60,35,50,63,water,water,peck,0,tail_whip,0,fissure,0,supersonic,1,horn_attack,1,flail,2,fury_attack,2,waterfall,3,horn_drill,4,agility,5,megahorn,5,supersonic,10,horn_attack,15,flail,24,fury_attack,29,waterfall,38,horn_drill,43,agility,52,megahorn,57,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
golduck=pokemon("golduck","duck",80,82,78,95,80,85,water,water,fissure,0,scratch,0,tail_whip,0,disable,0,disable,1,confusion,1,screech,2,psych_up,3,fury_swipes,4,tail_whip,5,hydro_pump,5,disable,10,confusion,16,screech,23,psych_up,31,fury_swipes,44,hydro_pump,58,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
golem=pokemon("golem","megaton",80,110,130,55,65,45,rock,ground,tackle,0,defense_curl,0,bite,0,rock_throw,0,rock_throw,1,magnitude,1,selfdestruct,2,rollout,2,psychic,3,earthquake,4,explosion,5,bite,6,double_edge,6,rock_throw,11,magnitude,16,selfdestruct,21,rollout,29,psychic,37,earthquake,45,explosion,53,double_edge,62,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
granbull=pokemon("granbull","fairy",90,120,75,60,60,45,normal,normal,tackle,0,scary_face,0,bite,1,lick,1,roar,2,rage,3,tail_whip,4,take_down,4,crunch,6,charm,8,bite,13,lick,19,roar,28,rage,38,take_down,49,crunch,61,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
graveler=pokemon("graveler","rock",55,95,115,45,45,35,rock,ground,tackle,0,defense_curl,0,bite,0,rock_throw,0,rock_throw,1,magnitude,1,selfdestruct,2,rollout,2,psychic,3,earthquake,4,explosion,5,bite,6,double_edge,6,rock_throw,11,magnitude,16,selfdestruct,21,rollout,29,psychic,37,earthquake,45,explosion,53,double_edge,62,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
grimer=pokemon("grimer","sludge",80,80,50,40,50,25,poison,poison,poison_gas,0,pound,0,sludge,1,minimize,1,screech,2,acid_armor,3,harden,4,sludge_bomb,4,pay_day,5,disable,8,sludge,13,minimize,19,screech,26,acid_armor,34,sludge_bomb,43,pay_day,53,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
growlithe=pokemon("growlithe","puppy",55,70,45,70,50,60,fire,fire,bite,0,roar,0,leer,1,psybeam,1,take_down,2,flame_wheel,3,swords_dance,3,agility,4,flamethrower,4,ember,7,leer,13,psybeam,19,take_down,25,flame_wheel,31,swords_dance,37,agility,43,flamethrower,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
gyarados=pokemon("gyarados","atrocious",95,125,79,60,100,81,water,flying,thrash,0,bite,2,dragon_rage,2,leer,3,twister,3,hydro_pump,4,rain_dance,4,confusion,5,hyper_beam,5,bite,20,dragon_rage,25,leer,30,twister,35,hydro_pump,40,rain_dance,45,confusion,50,hyper_beam,55,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
haunter=pokemon("haunter","gas",45,50,45,115,55,95,ghost,poison,hypnosis,0,lick,0,spite,0,curse,1,night_shade,1,confuse_ray,2,seismic_toss,2,dream_eater,3,destiny_bond,3,shadow_ball,4,nightmare,5,mean_look,6,spite,8,curse,13,night_shade,16,confuse_ray,21,seismic_toss,25,dream_eater,31,destiny_bond,39,shadow_ball,45,nightmare,53,mean_look,64,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
heracross=pokemon("heracross","single horn",80,125,75,40,95,85,bug,fighting,tackle,0,leer,0,endure,1,fury_attack,1,double_kick,2,counter,3,take_down,3,reversal,4,megahorn,5,horn_attack,6,endure,11,fury_attack,17,double_kick,23,counter,30,take_down,37,reversal,45,megahorn,53,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
hitmonchan=pokemon("hitmonchan","punching",50,105,79,35,110,76,fighting,fighting,stomp,0,comet_punch,0,pursuit,1,mach_punch,2,thunderpunch,2,ice_punch,2,fire_punch,2,absorb,3,mega_punch,3,detect,4,counter,5,agility,7,pursuit,13,mach_punch,20,thunderpunch,26,ice_punch,26,fire_punch,26,absorb,32,mega_punch,38,detect,44,counter,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
hitmonlee=pokemon("hitmonlee","kicking",50,120,53,35,110,87,fighting,fighting,stomp,0,double_kick,0,rolling_kick,1,jump_kick,1,double_kick,2,focus_energy,2,hi_jump_kick,2,mind_reader,3,foresight,3,endure,4,mega_kick,4,reversal,5,meditate,6,rolling_kick,11,jump_kick,16,double_kick,20,focus_energy,21,hi_jump_kick,26,mind_reader,31,foresight,36,endure,41,mega_kick,46,reversal,51,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
hitmontop=pokemon("hitmontop","handstand",50,95,95,35,110,70,fighting,fighting,stomp,0,rolling_kick,0,pursuit,1,quick_attack,1,triple_kick,2,rapid_spin,2,counter,3,agility,3,detect,4,rolling_kick,4,focus_energy,7,pursuit,13,quick_attack,19,triple_kick,20,rapid_spin,25,counter,31,agility,37,detect,43,rolling_kick,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
ho_oh=pokemon("ho_oh","rainbow",106,130,90,110,154,90,fire,flying,whirlwind,0,safeguard,1,gust,2,recover,3,fire_blast,4,sunny_day,5,swift,6,sacred_fire,7,ancientpower,8,future_sight,9,safeguard,11,gust,22,recover,33,fire_blast,44,sunny_day,55,swift,66,sacred_fire,77,ancientpower,88,future_sight,99,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
hoothoot=pokemon("hoothoot","owl",60,30,30,36,56,50,normal,flying,tackle,0,growl,0,peck,1,hypnosis,1,reflect,2,take_down,2,confusion,3,dream_eater,4,foresight,6,peck,11,hypnosis,16,reflect,22,take_down,28,confusion,34,dream_eater,48,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
hoppip=pokemon("hoppip","cottonweed",35,35,40,35,55,50,grass,flying,splash,0,tackle,1,poisonpowder,1,stun_spore,1,sleep_powder,1,leech_seed,2,cotton_spore,2,mega_drain,3,synthesis,5,tail_whip,5,tackle,10,poisonpowder,13,stun_spore,15,sleep_powder,17,leech_seed,20,cotton_spore,25,mega_drain,30,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
horsea=pokemon("horsea","dragon",30,40,70,70,25,60,water,water,bubble,0,leer,1,water_gun,2,twister,2,agility,3,hydro_pump,4,confusion,5,smokescreen,8,leer,15,water_gun,22,twister,29,agility,36,hydro_pump,43,confusion,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
houndoom=pokemon("houndoom","dark",75,90,50,110,80,95,dark,fire,leer,0,ember,0,petal_dance,0,smog,1,roar,1,bite,2,psybeam,3,faint_attack,4,flamethrower,5,crunch,5,petal_dance,7,smog,13,roar,19,bite,27,psybeam,35,faint_attack,43,flamethrower,51,crunch,59,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
houndour=pokemon("houndour","dark",45,60,30,80,50,65,dark,fire,leer,0,ember,0,smog,1,roar,1,bite,2,psybeam,3,faint_attack,3,flamethrower,4,crunch,4,petal_dance,7,smog,13,roar,19,bite,25,psybeam,31,faint_attack,37,flamethrower,43,crunch,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
hypno=pokemon("hypno","hypnosis",85,73,70,73,115,67,psychic,psychic,nightmare,0,pound,0,hypnosis,0,disable,0,confusion,0,confusion,1,headbutt,1,poison_gas,2,meditate,2,psychic,3,psych_up,4,swagger,4,future_sight,5,disable,7,confusion,11,headbutt,17,poison_gas,21,meditate,29,psychic,35,psych_up,43,swagger,49,future_sight,57,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
igglybuff=pokemon("igglybuff","balloon",90,30,15,40,20,15,normal,normal,sing,0,charm,0,sweet_kiss,1,defense_curl,4,pound,9,sweet_kiss,14,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
ivysaur=pokemon("ivysaur","seed",60,62,63,80,80,60,grass,poison,tackle,0,growl,0,leech_seed,0,vine_whip,1,poisonpowder,1,sleep_powder,1,razor_leaf,2,sweet_scent,2,growth,3,growl,4,synthesis,4,solarbeam,5,leech_seed,7,vine_whip,10,poisonpowder,15,sleep_powder,15,razor_leaf,22,sweet_scent,29,growth,38,synthesis,47,solarbeam,56,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
jigglypuff=pokemon("jigglypuff","balloon",115,45,20,45,25,20,normal,normal,sing,0,disable,1,rollout,1,doubleslap,2,rest,2,body_slam,3,mimic,3,defense_curl,4,supersonic,4,double_edge,4,pound,9,disable,14,rollout,19,doubleslap,24,rest,29,body_slam,34,mimic,39,supersonic,44,double_edge,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
jolteon=pokemon("jolteon","lightning",65,65,60,110,95,130,electric,electric,tackle,0,tail_whip,0,swords_dance,0,thundershock,1,quick_attack,2,double_kick,3,pin_missile,3,thunder_wave,4,agility,4,thunder,5,sand_attack,8,thundershock,16,quick_attack,23,double_kick,30,pin_missile,36,thunder_wave,42,agility,47,thunder,52,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
jumpluff=pokemon("jumpluff","cottonweed",75,55,70,55,85,110,grass,flying,splash,0,synthesis,0,tail_whip,0,tackle,0,tackle,1,poisonpowder,1,stun_spore,1,sleep_powder,1,leech_seed,2,cotton_spore,3,mega_drain,4,synthesis,5,tail_whip,5,tackle,10,poisonpowder,13,stun_spore,15,sleep_powder,17,leech_seed,22,cotton_spore,33,mega_drain,44,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
jynx=pokemon("jynx","human shape",65,50,35,115,95,95,ice,psychic,pound,0,lick,0,lovely_kiss,0,powder_snow,0,powder_snow,1,doubleslap,2,ice_punch,2,mean_look,3,surf,4,body_slam,5,perish_song,5,blizzard,6,lovely_kiss,9,powder_snow,13,doubleslap,21,ice_punch,25,mean_look,35,surf,41,body_slam,51,perish_song,57,blizzard,67,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
kabuto=pokemon("kabuto","shellfish",30,80,90,55,45,55,rock,water,scratch,0,harden,0,absorb,1,leer,1,thunderbolt,2,sand_attack,3,endure,3,hyper_beam,4,mega_drain,4,ancientpower,5,absorb,13,leer,19,thunderbolt,25,sand_attack,31,endure,37,hyper_beam,43,mega_drain,49,ancientpower,55,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
kabutops=pokemon("kabutops","shellfish",60,115,105,65,70,80,rock,water,fury_cutter,0,scratch,0,harden,0,absorb,0,leer,0,absorb,1,leer,1,thunderbolt,2,sand_attack,3,endure,3,slash,4,hyper_beam,4,mega_drain,5,ancientpower,6,absorb,13,leer,19,thunderbolt,25,sand_attack,31,endure,37,slash,40,hyper_beam,46,mega_drain,55,ancientpower,65,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
kadabra=pokemon("kadabra","psi",40,35,30,120,70,105,psychic,psychic,teleport,0,kinesis,0,confusion,0,confusion,1,disable,1,psybeam,2,reflect,2,recover,2,future_sight,3,gust,3,psychic,3,cut,4,confusion,16,disable,18,psybeam,21,reflect,23,recover,25,future_sight,30,gust,33,psychic,36,cut,43,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
kakuna=pokemon("kakuna","cocoon",45,25,50,25,25,35,bug,poison,harden,0,harden,7,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
kangaskhan=pokemon("kangaskhan","parent",105,95,80,40,80,90,normal,normal,comet_punch,0,leer,0,tail_whip,1,fake_out,1,mega_punch,2,rage,3,endure,3,dizzy_punch,4,reversal,4,bite,7,tail_whip,13,fake_out,19,mega_punch,25,rage,31,endure,37,dizzy_punch,43,reversal,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
kingdra=pokemon("kingdra","dragon",75,95,95,95,95,85,water,dragon,bubble,0,smokescreen,0,leer,0,water_gun,0,leer,1,water_gun,2,twister,2,agility,4,hydro_pump,5,confusion,6,smokescreen,8,leer,15,water_gun,22,twister,29,agility,40,hydro_pump,51,confusion,62,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
kingler=pokemon("kingler","pincer",55,130,115,50,50,75,water,water,metal_claw,0,bubble,0,leer,0,vicegrip,0,harden,0,vicegrip,1,harden,1,thunderbolt,2,stomp,2,guillotine,3,protect,4,leer,5,crabhammer,5,flail,6,vicegrip,12,harden,16,thunderbolt,23,stomp,27,guillotine,38,protect,42,crabhammer,57,flail,65,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
koffing=pokemon("koffing","poison gas",40,65,95,60,45,35,poison,poison,poison_gas,0,tackle,0,selfdestruct,1,sludge,2,smokescreen,2,haze,3,explosion,4,destiny_bond,4,pay_day,4,smog,9,selfdestruct,17,sludge,21,smokescreen,25,haze,33,explosion,41,destiny_bond,45,pay_day,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
krabby=pokemon("krabby","river crab",30,105,90,25,25,50,water,water,bubble,0,vicegrip,1,harden,1,thunderbolt,2,stomp,2,guillotine,3,protect,3,crabhammer,4,flail,4,leer,5,vicegrip,12,harden,16,thunderbolt,23,stomp,27,guillotine,34,protect,38,crabhammer,45,flail,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
lanturn=pokemon("lanturn","light",125,58,58,76,76,67,water,electric,bubble,0,thunder_wave,0,supersonic,0,flail,1,water_gun,1,spark,2,confuse_ray,3,take_down,4,supersonic,5,hydro_pump,5,guillotine,6,flail,13,water_gun,17,spark,25,confuse_ray,32,take_down,43,hydro_pump,50,guillotine,61,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
lapras=pokemon("lapras","transport",130,85,80,85,95,60,water,ice,water_gun,0,growl,0,sing,0,body_slam,1,confuse_ray,1,perish_song,2,ice_beam,3,rain_dance,3,safeguard,4,hydro_pump,4,leech_seed,5,mist,7,body_slam,13,confuse_ray,19,perish_song,25,ice_beam,31,rain_dance,37,safeguard,43,hydro_pump,49,leech_seed,55,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
larvitar=pokemon("larvitar","rock skin",50,64,50,45,50,41,rock,ground,bite,0,leer,0,screech,1,rock_slide,2,thrash,2,scary_face,3,crunch,4,earthquake,5,hyper_beam,5,sandstorm,8,screech,15,rock_slide,22,thrash,29,scary_face,36,crunch,43,earthquake,50,hyper_beam,57,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
ledian=pokemon("ledian","five star",55,35,50,55,110,85,bug,flying,tackle,0,supersonic,0,comet_punch,1,light_screen,2,reflect,2,safeguard,2,baton_pass,3,swift,4,agility,5,double_edge,6,supersonic,8,comet_punch,15,light_screen,24,reflect,24,safeguard,24,baton_pass,33,swift,42,agility,51,double_edge,60,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
ledyba=pokemon("ledyba","five star",40,20,30,40,80,55,bug,flying,tackle,0,comet_punch,1,light_screen,2,reflect,2,safeguard,2,baton_pass,2,swift,3,agility,4,double_edge,5,supersonic,8,comet_punch,15,light_screen,22,reflect,22,safeguard,22,baton_pass,29,swift,36,agility,43,double_edge,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
lickitung=pokemon("lickitung","licking",90,55,75,60,75,30,normal,normal,lick,0,defense_curl,1,jump_kick,1,stomp,2,wrap,2,disable,3,slam,4,screech,4,fury_attack,5,supersonic,7,defense_curl,12,jump_kick,18,stomp,23,wrap,29,disable,34,slam,40,screech,45,fury_attack,51,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
lugia=pokemon("lugia","diving",106,90,130,90,154,110,psychic,flying,whirlwind,0,safeguard,1,gust,2,recover,3,hydro_pump,4,rain_dance,5,swift,6,aeroblast,7,ancientpower,8,future_sight,9,safeguard,11,gust,22,recover,33,hydro_pump,44,rain_dance,55,swift,66,aeroblast,77,ancientpower,88,future_sight,99,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
machamp=pokemon("machamp","superpower",90,130,80,65,85,55,fighting,fighting,low_kick,0,leer,0,focus_energy,0,karate_chop,1,seismic_toss,1,foresight,2,stomp,2,vital_throw,3,submission,4,cross_chop,4,scary_face,5,dynamicpunch,5,focus_energy,7,karate_chop,13,seismic_toss,19,foresight,22,stomp,25,vital_throw,33,submission,41,cross_chop,46,scary_face,51,dynamicpunch,59,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
machoke=pokemon("machoke","superpower",80,100,70,50,60,45,fighting,fighting,low_kick,0,leer,0,focus_energy,0,karate_chop,1,seismic_toss,1,foresight,2,stomp,2,vital_throw,3,submission,4,cross_chop,4,scary_face,5,dynamicpunch,5,focus_energy,7,karate_chop,13,seismic_toss,19,foresight,22,stomp,25,vital_throw,33,submission,41,cross_chop,46,scary_face,51,dynamicpunch,59,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
machop=pokemon("machop","superpower",70,80,50,35,35,35,fighting,fighting,low_kick,0,leer,0,karate_chop,1,seismic_toss,1,foresight,2,stomp,2,vital_throw,3,submission,3,cross_chop,4,scary_face,4,dynamicpunch,4,focus_energy,7,karate_chop,13,seismic_toss,19,foresight,22,stomp,25,vital_throw,31,submission,37,cross_chop,40,scary_face,43,dynamicpunch,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
magby=pokemon("magby","live coal",45,75,37,70,55,83,fire,fire,ember,0,smog,1,fire_punch,1,smokescreen,2,sunny_day,3,flamethrower,3,confuse_ray,4,fire_blast,4,leer,7,smog,13,fire_punch,19,smokescreen,25,sunny_day,31,flamethrower,37,confuse_ray,43,fire_blast,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
magcargo=pokemon("magcargo","lava",50,50,120,80,80,30,fire,rock,mega_kick,0,smog,0,ember,0,rock_throw,0,rock_throw,1,harden,2,amnesia,2,flamethrower,3,rock_slide,4,body_slam,6,ember,8,rock_throw,15,harden,22,amnesia,29,flamethrower,36,rock_slide,48,body_slam,60,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
magikarp=pokemon("magikarp","fish",20,10,55,15,20,80,water,water,splash,0,tackle,1,flail,3,tackle,15,flail,30,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
magmar=pokemon("magmar","spitfire",65,95,57,100,85,93,fire,fire,ember,0,leer,0,smog,0,fire_punch,0,smog,1,fire_punch,1,smokescreen,2,sunny_day,3,flamethrower,4,confuse_ray,4,fire_blast,5,leer,7,smog,13,fire_punch,19,smokescreen,25,sunny_day,33,flamethrower,41,confuse_ray,49,fire_blast,57,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
magnemite=pokemon("magnemite","magnet",25,35,70,95,55,45,electric,steel,hyper_beam,0,tackle,0,supersonic,1,sonicboom,1,thunder_wave,2,spark,2,lock_on,3,swift,3,screech,4,zap_cannon,5,thundershock,6,supersonic,11,sonicboom,16,thunder_wave,21,spark,26,lock_on,32,swift,38,screech,44,zap_cannon,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
magneton=pokemon("magneton","magnet",50,60,95,120,70,70,electric,steel,hyper_beam,0,tackle,0,thundershock,0,supersonic,0,supersonic,1,sonicboom,1,thunder_wave,2,spark,2,lock_on,3,tri_attack,4,screech,5,thundershock,6,zap_cannon,6,supersonic,11,sonicboom,16,thunder_wave,21,spark,26,lock_on,35,tri_attack,44,screech,53,zap_cannon,62,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
mankey=pokemon("mankey","pig monkey",40,80,35,35,45,70,fighting,fighting,scratch,0,leer,0,karate_chop,1,fury_swipes,1,focus_energy,2,seismic_toss,2,cross_chop,3,swagger,3,screech,4,thrash,4,low_kick,6,karate_chop,11,fury_swipes,16,focus_energy,21,seismic_toss,26,cross_chop,31,swagger,36,screech,41,thrash,46,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
mantine=pokemon("mantine","kite",65,40,70,80,140,70,water,flying,tackle,0,bubble,0,bubblebeam,1,take_down,2,agility,2,wing_attack,3,meditate,4,confuse_ray,5,supersonic,8,bubblebeam,15,take_down,22,agility,29,wing_attack,36,meditate,43,confuse_ray,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
mareep=pokemon("mareep","wool",55,40,40,65,45,35,electric,electric,tackle,0,growl,0,thunder_wave,1,cotton_spore,2,light_screen,3,thunder,3,thundershock,9,thunder_wave,16,cotton_spore,23,light_screen,30,thunder,37,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
marill=pokemon("marill","aqua mouse",70,20,50,20,50,40,water,water,tackle,0,water_gun,1,rollout,1,bubblebeam,2,double_edge,2,defense_curl,3,rain_dance,3,hydro_pump,4,tail_whip,6,water_gun,10,rollout,15,bubblebeam,21,double_edge,28,rain_dance,36,hydro_pump,45,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
marowak=pokemon("marowak","bone keeper",60,80,110,50,80,45,ground,ground,growl,0,tail_whip,0,bone_club,0,headbutt,0,headbutt,1,leer,1,focus_energy,2,bonemerang,2,rage,3,false_swipe,3,thrash,4,tail_whip,5,bone_rush,5,double_edge,6,bone_club,9,headbutt,13,leer,17,focus_energy,21,bonemerang,25,rage,32,false_swipe,39,thrash,46,bone_rush,53,double_edge,61,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
meganium=pokemon("meganium","herb",80,82,100,83,100,80,grass,grass,tackle,0,growl,0,razor_leaf,0,reflect,0,reflect,1,poisonpowder,1,synthesis,2,body_slam,3,light_screen,4,safeguard,5,solarbeam,6,razor_leaf,8,reflect,12,poisonpowder,15,synthesis,23,body_slam,31,light_screen,41,safeguard,51,solarbeam,61,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
meowth=pokemon("meowth","scratch cat",40,45,35,40,40,90,normal,normal,scratch,0,growl,0,bite,1,pay_day,1,faint_attack,2,screech,3,fury_swipes,3,slash,4,fake_out,4,swagger,4,bite,10,pay_day,18,faint_attack,25,screech,31,fury_swipes,36,slash,40,fake_out,43,swagger,45,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
metapod=pokemon("metapod","cocoon",50,20,55,25,25,30,bug,bug,harden,0,harden,7,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
mew=pokemon("mew","new species",100,100,100,100,100,100,psychic,psychic,pound,0,transform,1,mega_punch,2,metronome,3,psychic,4,ancientpower,5,transform,10,mega_punch,20,metronome,30,psychic,40,ancientpower,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
mewtwo=pokemon("mewtwo","genetic",106,110,90,154,90,130,psychic,psychic,confusion,0,disable,0,barrier,1,mist,2,swift,3,recover,4,safeguard,5,psychic,6,psych_up,7,future_sight,8,amnesia,9,barrier,11,mist,22,swift,33,recover,44,safeguard,55,psychic,66,psych_up,77,future_sight,88,amnesia,99,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
miltank=pokemon("miltank","milk cow",95,80,105,40,70,100,normal,normal,tackle,0,stomp,1,milk_drink,1,bide,2,rollout,3,growl,4,body_slam,4,heal_bell,5,defense_curl,8,stomp,13,milk_drink,19,bide,26,rollout,34,body_slam,43,heal_bell,53,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
misdreavus=pokemon("misdreavus","screech",60,60,60,85,85,85,ghost,ghost,growl,0,psywave,0,mist,1,confuse_ray,1,mean_look,2,psybeam,3,pain_split,3,perish_song,4,horn_drill,5,spite,6,mist,11,confuse_ray,17,mean_look,23,psybeam,30,pain_split,37,perish_song,45,horn_drill,53,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
moltres=pokemon("moltres","flame",90,100,90,125,85,90,fire,flying,wing_attack,0,ember,0,fire_spin,1,agility,2,endure,3,flamethrower,4,safeguard,6,pound,7,sky_attack,8,fire_spin,13,agility,25,endure,37,flamethrower,49,safeguard,61,pound,73,sky_attack,85,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
mr_mime=pokemon("mr. mime","barrier",40,45,65,100,120,90,psychic,psychic,barrier,0,meditate,1,doubleslap,1,light_screen,1,reflect,1,earthquake,2,encore,2,psybeam,2,vine_whip,3,cut,3,gust,4,psychic,4,baton_pass,4,confusion,5,safeguard,5,substitute,8,meditate,12,doubleslap,15,light_screen,19,reflect,19,earthquake,22,encore,26,psybeam,29,vine_whip,33,cut,36,gust,40,psychic,43,baton_pass,47,safeguard,50)
muk=pokemon("muk","sludge",105,105,75,65,100,50,poison,poison,poison_gas,0,pound,0,harden,0,sludge,1,minimize,1,screech,2,acid_armor,3,harden,4,sludge_bomb,4,pay_day,6,disable,8,sludge,13,minimize,19,screech,26,acid_armor,34,sludge_bomb,47,pay_day,61,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
murkrow=pokemon("murkrow","darkness",60,85,42,85,42,91,dark,flying,peck,0,pursuit,1,haze,2,night_shade,2,faint_attack,3,razor_wind,4,mean_look,4,mist,9,pursuit,14,haze,22,night_shade,27,faint_attack,35,razor_wind,40,mean_look,48,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
natu=pokemon("natu","tiny bird",40,50,45,70,45,70,psychic,flying,peck,0,leer,0,night_shade,1,teleport,2,wing_attack,3,future_sight,3,confuse_ray,4,psychic,5,night_shade,10,teleport,20,wing_attack,30,future_sight,30,confuse_ray,40,psychic,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
nidoking=pokemon("nidoking","drill",81,92,77,85,75,85,poison,ground,peck,0,focus_energy,0,double_kick,0,poison_sting,0,thrash,2,megahorn,4,thrash,22,megahorn,43,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
nidoqueen=pokemon("nidoqueen","drill",90,82,87,75,85,76,poison,ground,scratch,0,tail_whip,0,double_kick,0,poison_sting,0,body_slam,2,bind,4,body_slam,22,bind,43,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
nidoranfemale=pokemon("nidoranfemale","poison pin",46,57,40,40,40,50,poison,poison,leer,0,peck,0,double_kick,1,poison_sting,1,horn_attack,2,swords_dance,2,fury_attack,3,comet_punch,3,horn_drill,4,focus_energy,8,double_kick,12,poison_sting,17,horn_attack,20,swords_dance,23,fury_attack,30,comet_punch,38,horn_drill,47,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
nidoranmale=pokemon("nidoranmale","poison pin",55,47,52,40,40,41,poison,poison,growl,0,scratch,0,double_kick,1,poison_sting,1,bite,2,swords_dance,2,fury_swipes,3,comet_punch,3,crunch,4,tail_whip,8,double_kick,12,poison_sting,17,bite,20,swords_dance,23,fury_swipes,30,comet_punch,38,crunch,47,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
nidorina=pokemon("nidorina","poison pin",70,62,67,55,55,56,poison,poison,growl,0,scratch,0,double_kick,1,poison_sting,1,bite,2,swords_dance,2,fury_swipes,3,comet_punch,4,crunch,5,tail_whip,8,double_kick,12,poison_sting,18,bite,22,swords_dance,26,fury_swipes,34,comet_punch,43,crunch,53,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
nidorino=pokemon("nidorino","poison pin",61,72,57,55,55,65,poison,poison,leer,0,peck,0,double_kick,1,poison_sting,1,horn_attack,2,swords_dance,2,fury_attack,3,comet_punch,4,horn_drill,5,focus_energy,8,double_kick,12,poison_sting,18,horn_attack,22,swords_dance,26,fury_attack,34,comet_punch,43,horn_drill,53,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
ninetales=pokemon("ninetales","fox",73,76,75,81,100,100,fire,fire,ember,0,quick_attack,0,confuse_ray,0,safeguard,0,fire_spin,4,fire_spin,45,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
noctowl=pokemon("noctowl","owl",100,50,50,76,96,70,normal,flying,tackle,0,growl,0,foresight,0,peck,0,peck,1,hypnosis,1,reflect,2,take_down,3,confusion,4,dream_eater,5,foresight,6,peck,11,hypnosis,16,reflect,25,take_down,33,confusion,41,dream_eater,57,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
octillery=pokemon("octillery","jet",75,105,75,105,75,45,water,water,water_gun,0,constrict,1,psybeam,2,aurora_beam,2,bubblebeam,2,octazooka,2,focus_energy,3,ice_beam,5,hyper_beam,7,constrict,11,psybeam,22,aurora_beam,22,bubblebeam,22,octazooka,25,focus_energy,38,ice_beam,54,hyper_beam,70,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
oddish=pokemon("oddish","weed",45,50,55,75,65,30,grass,poison,absorb,0,poisonpowder,1,stun_spore,1,sleep_powder,1,acid,2,moonlight,3,petal_dance,3,sweet_scent,7,poisonpowder,14,stun_spore,16,sleep_powder,18,acid,23,moonlight,32,petal_dance,39,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
omanyte=pokemon("omanyte","spiral",35,40,100,90,55,35,rock,water,constrict,0,withdraw,0,bite,1,water_gun,1,thunderbolt,2,leer,3,protect,3,drill_peck,4,ancientpower,4,hydro_pump,5,bite,13,water_gun,19,thunderbolt,25,leer,31,protect,37,drill_peck,43,ancientpower,49,hydro_pump,55,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
omastar=pokemon("omastar","spiral",70,60,125,115,70,55,rock,water,constrict,0,withdraw,0,bite,0,water_gun,0,bite,1,water_gun,1,thunderbolt,2,leer,3,protect,3,spike_cannon,4,drill_peck,4,ancientpower,5,hydro_pump,6,bite,13,water_gun,19,thunderbolt,25,leer,31,protect,37,spike_cannon,40,drill_peck,46,ancientpower,55,hydro_pump,65,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
onix=pokemon("onix","rock snake",35,45,160,30,45,70,rock,ground,tackle,0,screech,0,rock_throw,1,harden,1,rage,2,dragonbreath,3,sandstorm,3,slam,4,iron_tail,4,mega_drain,5,double_edge,5,bind,8,rock_throw,12,harden,19,rage,23,dragonbreath,30,sandstorm,34,slam,41,iron_tail,45,mega_drain,52,double_edge,56,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
paras=pokemon("paras","mushroom",35,70,55,45,55,25,bug,grass,scratch,0,poisonpowder,1,leech_life,1,spore,2,slash,3,growth,3,giga_drain,4,hydro_pump,4,stun_spore,7,poisonpowder,13,leech_life,19,spore,25,slash,31,growth,37,giga_drain,43,hydro_pump,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
parasect=pokemon("parasect","mushroom",60,95,80,60,80,30,bug,grass,scratch,0,stun_spore,0,poisonpowder,0,poisonpowder,1,leech_life,1,spore,2,slash,3,growth,4,giga_drain,5,hydro_pump,5,stun_spore,7,poisonpowder,13,leech_life,19,spore,27,slash,35,growth,43,giga_drain,51,hydro_pump,59,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
persian=pokemon("persian","classy cat",65,70,60,65,65,115,normal,normal,scratch,0,growl,0,bite,0,bite,1,pay_day,1,faint_attack,2,screech,3,fury_swipes,4,slash,4,fake_out,5,swagger,6,bite,10,pay_day,18,faint_attack,25,screech,34,fury_swipes,42,slash,49,fake_out,55,swagger,61,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
phanpy=pokemon("phanpy","long nose",90,60,60,40,40,40,ground,ground,psybeam,0,tackle,0,growl,0,flail,1,take_down,2,rollout,3,endure,4,double_edge,4,defense_curl,9,flail,17,take_down,25,rollout,33,endure,41,double_edge,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
pichu=pokemon("pichu","tiny mouse",20,40,15,35,35,60,electric,electric,thundershock,0,charm,0,sweet_kiss,1,tail_whip,6,thunder_wave,8,sweet_kiss,11,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
pidgeot=pokemon("pidgeot","bird",83,80,75,70,70,91,normal,flying,tackle,0,sand_attack,0,gust,0,quick_attack,0,quick_attack,1,whirlwind,2,wing_attack,2,twineedle,3,agility,4,sand_attack,5,mirror_move,6,gust,9,quick_attack,13,whirlwind,20,wing_attack,27,twineedle,34,agility,48,mirror_move,62,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
pidgeotto=pokemon("pidgeotto","bird",63,60,55,50,50,71,normal,flying,tackle,0,sand_attack,0,gust,0,quick_attack,1,whirlwind,2,wing_attack,2,twineedle,3,agility,4,sand_attack,5,mirror_move,5,gust,9,quick_attack,13,whirlwind,20,wing_attack,27,twineedle,34,agility,43,mirror_move,52,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
pidgey=pokemon("pidgey","tiny bird",40,45,40,35,35,56,normal,flying,tackle,0,quick_attack,1,whirlwind,1,wing_attack,2,twineedle,3,agility,3,mirror_move,4,sand_attack,5,gust,9,quick_attack,13,whirlwind,19,wing_attack,25,twineedle,31,agility,39,mirror_move,47,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
pikachu=pokemon("pikachu","mouse",35,55,30,50,40,90,electric,electric,thundershock,0,growl,0,quick_attack,1,double_team,1,slam,2,thunderbolt,2,agility,3,thunder,4,light_screen,5,tail_whip,6,thunder_wave,8,quick_attack,11,double_team,15,slam,20,thunderbolt,26,agility,33,thunder,41,light_screen,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
piloswine=pokemon("piloswine","swine",100,100,80,60,60,50,ice,ground,horn_attack,0,psybeam,0,powder_snow,0,endure,0,powder_snow,1,endure,1,take_down,2,fury_attack,3,mist,4,blizzard,5,amnesia,7,powder_snow,10,endure,19,take_down,28,fury_attack,33,mist,42,blizzard,56,amnesia,70,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
pineco=pokemon("pineco","bagworm",50,65,90,35,35,15,bug,bug,tackle,0,protect,0,take_down,1,rapid_spin,2,bide,2,explosion,3,spikes,4,double_edge,5,selfdestruct,8,take_down,15,rapid_spin,22,bide,29,explosion,36,spikes,43,double_edge,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
pinsir=pokemon("pinsir","stag beetle",65,125,100,55,70,85,bug,bug,vicegrip,0,focus_energy,0,seismic_toss,1,harden,1,stomp,2,double_kick,3,guillotine,3,submission,4,swords_dance,4,bind,7,seismic_toss,13,harden,19,stomp,25,double_kick,31,guillotine,37,submission,43,swords_dance,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
politoed=pokemon("politoed","frog",90,75,75,90,100,70,water,water,water_gun,0,hypnosis,0,doubleslap,0,perish_song,0,perish_song,3,swagger,5,perish_song,35,swagger,51,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
poliwag=pokemon("poliwag","tadpole",40,50,40,40,40,90,water,water,bubble,0,water_gun,1,doubleslap,1,rain_dance,2,body_slam,3,belly_drum,3,hydro_pump,4,hypnosis,7,water_gun,13,doubleslap,19,rain_dance,25,body_slam,31,belly_drum,37,hydro_pump,43,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
poliwhirl=pokemon("poliwhirl","tadpole",65,65,65,50,50,90,water,water,bubble,0,hypnosis,0,water_gun,0,water_gun,1,doubleslap,1,rain_dance,2,body_slam,3,belly_drum,4,hydro_pump,5,hypnosis,7,water_gun,13,doubleslap,19,rain_dance,27,body_slam,35,belly_drum,43,hydro_pump,51,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
poliwrath=pokemon("poliwrath","tadpole",90,85,95,70,90,70,water,fighting,water_gun,0,hypnosis,0,doubleslap,0,submission,0,submission,3,mind_reader,5,submission,35,mind_reader,51,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
ponyta=pokemon("ponyta","fire horse",50,85,55,65,65,90,fire,fire,quick_attack,0,ember,1,stomp,1,fire_spin,2,take_down,3,agility,3,thundershock,4,growl,5,fire_blast,5,tail_whip,9,ember,14,stomp,19,fire_spin,25,take_down,31,agility,38,thundershock,45,fire_blast,53,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
porygon=pokemon("porygon","virtual",65,60,70,85,75,40,normal,normal,conversion_2,0,tackle,0,conversion,0,psybeam,1,recover,2,sharpen,2,lock_on,3,tri_attack,3,vine_whip,4,zap_cannon,4,agility,9,psybeam,12,recover,20,sharpen,24,lock_on,32,tri_attack,36,vine_whip,44,zap_cannon,48,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
porygon2=pokemon("porygon2","virtual",85,80,90,105,95,60,normal,normal,conversion_2,0,tackle,0,conversion,0,psybeam,1,recover,2,defense_curl,2,lock_on,3,tri_attack,3,vine_whip,4,zap_cannon,4,agility,9,psybeam,12,recover,20,defense_curl,24,lock_on,32,tri_attack,36,vine_whip,44,zap_cannon,48,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
primeape=pokemon("primeape","pig monkey",65,105,60,60,70,95,fighting,fighting,scratch,0,leer,0,low_kick,0,rage,0,karate_chop,1,fury_swipes,1,focus_energy,2,seismic_toss,2,rage,2,cross_chop,3,swagger,4,screech,5,low_kick,6,thrash,6,karate_chop,11,fury_swipes,16,focus_energy,21,seismic_toss,26,rage,28,cross_chop,35,swagger,44,screech,53,thrash,62,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
psyduck=pokemon("psyduck","duck",50,52,48,65,50,55,water,water,fissure,0,scratch,0,disable,1,confusion,1,screech,2,psych_up,3,fury_swipes,4,tail_whip,5,hydro_pump,5,disable,10,confusion,16,screech,23,psych_up,31,fury_swipes,40,hydro_pump,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
pupitar=pokemon("pupitar","hard shell",70,84,70,65,70,51,rock,ground,bite,0,leer,0,sandstorm,0,screech,0,screech,1,rock_slide,2,thrash,2,scary_face,3,crunch,4,earthquake,5,hyper_beam,6,sandstorm,8,screech,15,rock_slide,22,thrash,29,scary_face,38,crunch,47,earthquake,56,hyper_beam,65,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
quagsire=pokemon("quagsire","water fish",95,85,85,65,65,35,water,ground,water_gun,0,tail_whip,0,slam,1,thunderbolt,1,amnesia,2,mega_kick,3,earthquake,4,rain_dance,4,mist,6,haze,6,slam,11,thunderbolt,16,amnesia,23,mega_kick,35,earthquake,42,rain_dance,49,mist,61,haze,61,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
quilava=pokemon("quilava","volcano",58,64,58,80,65,80,fire,fire,tackle,0,leer,0,smokescreen,0,ember,1,quick_attack,2,flame_wheel,3,swift,4,flamethrower,5,smokescreen,6,ember,12,quick_attack,21,flame_wheel,31,swift,42,flamethrower,54,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
qwilfish=pokemon("qwilfish","balloon",65,95,75,55,55,85,water,poison,spikes,0,tackle,0,poison_sting,0,water_gun,1,pin_missile,2,stomp,2,take_down,3,hydro_pump,3,destiny_bond,4,harden,9,minimize,9,water_gun,13,pin_missile,21,stomp,25,take_down,33,hydro_pump,37,destiny_bond,45,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
raichu=pokemon("raichu","mouse",60,90,55,90,80,100,electric,electric,thundershock,0,tail_whip,0,quick_attack,0,thunderbolt,0,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
raikou=pokemon("raikou","thunder",90,85,75,115,100,115,electric,electric,bite,0,leer,0,thundershock,1,roar,2,quick_attack,3,spark,4,reflect,5,crunch,6,thunder,7,dig,8,thundershock,11,roar,21,quick_attack,31,spark,41,reflect,51,crunch,61,thunder,71,dig,81,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
rapidash=pokemon("rapidash","fire horse",65,100,70,80,80,105,fire,fire,quick_attack,0,growl,0,tail_whip,0,ember,0,ember,1,stomp,1,fire_spin,2,take_down,3,agility,3,fury_attack,4,growl,5,thundershock,5,fire_blast,6,tail_whip,9,ember,14,stomp,19,fire_spin,25,take_down,31,agility,38,fury_attack,40,thundershock,50,fire_blast,63,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
raticate=pokemon("raticate","mouse",55,81,60,50,70,97,normal,normal,tackle,0,tail_whip,0,quick_attack,0,hyper_fang,1,scary_face,2,pursuit,3,super_fang,4,rolling_kick,5,quick_attack,7,hyper_fang,13,scary_face,20,pursuit,30,super_fang,40,rolling_kick,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
rattata=pokemon("rattata","mouse",30,56,35,25,35,72,normal,normal,tackle,0,tail_whip,0,hyper_fang,1,focus_energy,2,pursuit,2,super_fang,3,rolling_kick,4,quick_attack,7,hyper_fang,13,focus_energy,20,pursuit,27,super_fang,34,rolling_kick,41,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
remoraid=pokemon("remoraid","jet",35,65,35,65,35,65,water,water,water_gun,0,lock_on,1,psybeam,2,aurora_beam,2,bubblebeam,2,focus_energy,3,ice_beam,4,hyper_beam,5,lock_on,11,psybeam,22,aurora_beam,22,bubblebeam,22,focus_energy,33,ice_beam,44,hyper_beam,55,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
rhydon=pokemon("rhydon","drill",105,130,120,45,45,40,ground,rock,horn_attack,0,tail_whip,0,stomp,0,fury_attack,0,stomp,1,fury_attack,1,scary_face,2,psychic,2,horn_drill,3,take_down,4,earthquake,5,megahorn,6,stomp,10,fury_attack,15,scary_face,24,psychic,29,horn_drill,38,take_down,46,earthquake,58,megahorn,66,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
rhyhorn=pokemon("rhyhorn","spikes",80,85,95,30,30,25,ground,rock,horn_attack,0,tail_whip,0,stomp,1,fury_attack,1,scary_face,2,psychic,2,horn_drill,3,take_down,4,earthquake,5,megahorn,5,stomp,10,fury_attack,15,scary_face,24,psychic,29,horn_drill,38,take_down,43,earthquake,52,megahorn,57,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
sandshrew=pokemon("sandshrew","mouse",50,75,85,20,30,40,ground,ground,scratch,0,sand_attack,1,poison_sting,1,slash,2,swift,3,fury_swipes,3,mega_drain,4,sandstorm,5,defense_curl,6,sand_attack,11,poison_sting,17,slash,23,swift,30,fury_swipes,37,mega_drain,45,sandstorm,53,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
sandslash=pokemon("sandslash","mouse",75,100,110,45,55,65,ground,ground,scratch,0,defense_curl,0,sand_attack,0,sand_attack,1,poison_sting,1,slash,2,swift,3,fury_swipes,4,mega_drain,5,defense_curl,6,sandstorm,6,sand_attack,11,poison_sting,17,slash,24,swift,33,fury_swipes,42,mega_drain,52,sandstorm,62,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
scizor=pokemon("scizor","pincer",70,130,100,55,80,65,bug,steel,quick_attack,0,leer,0,pursuit,1,false_swipe,1,agility,2,metal_claw,2,slash,3,swords_dance,3,stun_spore,4,fury_cutter,4,focus_energy,6,pursuit,11,false_swipe,16,agility,21,metal_claw,26,slash,31,swords_dance,36,stun_spore,41,fury_cutter,46,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
scyther=pokemon("scyther","mantis",70,110,80,55,80,105,bug,flying,quick_attack,0,leer,0,pursuit,1,false_swipe,1,agility,2,wing_attack,2,slash,3,swords_dance,3,double_team,4,fury_cutter,4,focus_energy,6,pursuit,11,false_swipe,16,agility,21,wing_attack,26,slash,31,swords_dance,36,double_team,41,fury_cutter,46,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
seadra=pokemon("seadra","dragon",55,65,95,95,45,85,water,water,bubble,0,smokescreen,0,leer,0,water_gun,0,leer,1,water_gun,2,twister,2,agility,4,hydro_pump,5,confusion,6,smokescreen,8,leer,15,water_gun,22,twister,29,agility,40,hydro_pump,51,confusion,62,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
seaking=pokemon("seaking","goldfish",80,92,65,65,80,68,water,water,peck,0,tail_whip,0,fissure,0,supersonic,0,supersonic,1,horn_attack,1,flail,2,fury_attack,2,waterfall,4,horn_drill,4,agility,6,megahorn,6,supersonic,10,horn_attack,15,flail,24,fury_attack,29,waterfall,41,horn_drill,49,agility,61,megahorn,69,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
seel=pokemon("seel","sea lion",65,45,55,45,70,45,water,water,headbutt,0,icy_wind,1,aurora_beam,2,rest,2,take_down,3,ice_beam,4,safeguard,4,growl,9,icy_wind,17,aurora_beam,21,rest,29,take_down,37,ice_beam,41,safeguard,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
sentret=pokemon("sentret","scout",35,46,34,35,45,20,normal,normal,scratch,0,fury_swipes,1,swords_dance,1,slam,2,scratch,3,defense_curl,4,rest,4,amnesia,4,quick_attack,7,fury_swipes,12,swords_dance,17,slam,24,scratch,31,rest,40,amnesia,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
shellder=pokemon("shellder","bivalve",30,65,100,45,25,40,water,water,tackle,0,withdraw,0,supersonic,1,aurora_beam,2,protect,2,leer,3,clamp,4,ice_beam,5,poisonpowder,8,supersonic,15,aurora_beam,22,protect,29,leer,36,clamp,43,ice_beam,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
shuckle=pokemon("shuckle","mold",20,10,230,10,230,5,bug,rock,constrict,0,withdraw,0,encore,1,safeguard,2,bide,2,rest,3,wrap,9,encore,14,safeguard,23,bide,28,rest,37,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
skarmory=pokemon("skarmory","armor bird",65,80,140,40,70,70,steel,flying,leer,0,peck,0,sand_attack,1,swift,1,agility,1,fury_attack,2,ice_beam,2,steel_wing,3,spikes,4,hyper_beam,4,sand_attack,10,swift,13,agility,16,fury_attack,26,ice_beam,29,steel_wing,32,spikes,42,hyper_beam,45,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
skiploom=pokemon("skiploom","cottonweed",55,45,50,45,65,80,grass,flying,splash,0,synthesis,0,tail_whip,0,tackle,0,tackle,1,poisonpowder,1,stun_spore,1,sleep_powder,1,leech_seed,2,cotton_spore,2,mega_drain,3,synthesis,5,tail_whip,5,tackle,10,poisonpowder,13,stun_spore,15,sleep_powder,17,leech_seed,22,cotton_spore,29,mega_drain,36,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
slowbro=pokemon("slowbro","hermit crab",95,75,110,100,80,30,water,psychic,curse,0,mega_kick,0,tackle,0,growl,0,water_gun,1,confusion,1,disable,2,headbutt,2,amnesia,3,withdraw,3,psychic,4,psych_up,5,growl,6,water_gun,13,confusion,17,disable,24,headbutt,29,amnesia,36,withdraw,37,psychic,44,psych_up,55,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
slowking=pokemon("slowking","royal",95,75,80,100,110,30,water,psychic,curse,0,mega_kick,0,tackle,0,water_gun,1,confusion,1,disable,2,headbutt,2,swagger,3,psychic,4,psych_up,4,growl,6,water_gun,13,confusion,17,disable,24,headbutt,29,swagger,36,psychic,40,psych_up,47,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
slowpoke=pokemon("slowpoke","dopey",90,65,65,40,40,15,water,psychic,curse,0,mega_kick,0,tackle,0,water_gun,1,confusion,1,disable,2,headbutt,2,amnesia,3,psychic,4,psych_up,4,growl,6,water_gun,13,confusion,17,disable,24,headbutt,29,amnesia,36,psychic,40,psych_up,47,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
slugma=pokemon("slugma","lava",40,40,40,70,40,20,fire,fire,mega_kick,0,smog,0,rock_throw,1,harden,2,amnesia,2,flamethrower,3,rock_slide,4,body_slam,5,ember,8,rock_throw,15,harden,22,amnesia,29,flamethrower,36,rock_slide,43,body_slam,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
smeargle=pokemon("smeargle","painter",55,20,35,20,45,75,normal,normal,sketch,0,sketch,1,sketch,2,sketch,3,sketch,4,sketch,5,sketch,6,sketch,7,sketch,8,sketch,9,sketch,11,sketch,21,sketch,31,sketch,41,sketch,51,sketch,61,sketch,71,sketch,81,sketch,91,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
smoochum=pokemon("smoochum","kiss",45,30,15,85,65,65,ice,psychic,pound,0,lick,0,powder_snow,1,confusion,2,sing,2,mean_look,3,surf,3,psychic,4,perish_song,4,blizzard,5,sweet_kiss,9,powder_snow,13,confusion,21,sing,25,mean_look,33,surf,37,psychic,45,perish_song,49,blizzard,57,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
sneasel=pokemon("sneasel","sharp claw",55,95,55,35,75,115,dark,ice,scratch,0,leer,0,razor_wind,0,screech,1,faint_attack,2,fury_swipes,2,agility,3,icy_wind,4,slash,5,beat_up,5,metal_claw,6,quick_attack,8,screech,15,faint_attack,22,fury_swipes,29,agility,36,icy_wind,43,slash,50,beat_up,57,metal_claw,64,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
snorlax=pokemon("snorlax","sleeping",160,110,65,65,110,30,normal,normal,tackle,0,belly_drum,1,headbutt,1,mega_kick,2,rest,2,snore,2,body_slam,3,sleep_talk,3,sleep_powder,4,thunder,4,rollout,4,amnesia,5,hyper_beam,5,defense_curl,9,belly_drum,13,headbutt,17,mega_kick,21,rest,25,snore,29,body_slam,33,sleep_talk,37,sleep_powder,41,thunder,45,rollout,49,hyper_beam,53,tackle,200,tackle,200,tackle,200,tackle,200)
snubbull=pokemon("snubbull","fairy",60,80,50,40,40,30,normal,normal,tackle,0,scary_face,0,bite,1,lick,1,roar,2,rage,3,tail_whip,4,take_down,4,crunch,5,charm,8,bite,13,lick,19,roar,26,rage,34,take_down,43,crunch,53,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
spearow=pokemon("spearow","tiny bird",40,60,30,31,31,70,normal,flying,peck,0,growl,0,fury_attack,1,pursuit,1,solarbeam,2,mirror_move,3,drill_peck,3,agility,4,leer,7,fury_attack,13,pursuit,19,solarbeam,25,mirror_move,31,drill_peck,37,agility,43,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
spinarak=pokemon("spinarak","string spit",40,60,40,40,40,30,bug,poison,poison_sting,0,string_shot,0,constrict,1,night_shade,1,leech_life,2,fury_swipes,3,spider_web,3,agility,4,psychic,5,scary_face,6,constrict,11,night_shade,17,leech_life,23,fury_swipes,30,spider_web,37,agility,45,psychic,53,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
squirtle=pokemon("squirtle","tiny turtle",44,48,65,50,64,43,water,water,tackle,0,withdraw,1,water_gun,1,bite,1,rapid_spin,2,protect,2,rain_dance,3,tail_whip,4,skull_bash,4,hydro_pump,4,bubble,7,withdraw,10,water_gun,13,bite,18,rapid_spin,23,protect,28,rain_dance,33,skull_bash,40,hydro_pump,47,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
stantler=pokemon("stantler","big horn",73,95,62,85,65,85,normal,normal,tackle,0,mist,1,hypnosis,1,stomp,2,sand_attack,2,gust,3,take_down,3,confuse_ray,4,dig,4,leer,7,mist,11,hypnosis,17,stomp,21,sand_attack,27,gust,31,take_down,37,confuse_ray,41,dig,47,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
starmie=pokemon("starmie","mysterious",60,75,85,100,85,115,water,psychic,water_gun,0,rapid_spin,0,recover,0,swift,0,confuse_ray,3,confuse_ray,33,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
staryu=pokemon("staryu","star shape",30,45,55,70,55,85,water,water,tackle,0,harden,0,rapid_spin,1,recover,1,thrash,1,swift,2,bubblebeam,2,minimize,3,light_screen,3,submission,4,hydro_pump,4,water_gun,6,rapid_spin,10,recover,15,thrash,19,swift,24,bubblebeam,28,minimize,33,light_screen,37,submission,42,hydro_pump,46,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
steelix=pokemon("steelix","iron snake",75,85,200,55,65,30,steel,ground,tackle,0,screech,0,rock_throw,1,harden,1,rage,2,dragonbreath,3,sandstorm,3,slam,4,iron_tail,4,crunch,5,double_edge,5,bind,8,rock_throw,12,harden,19,rage,23,dragonbreath,30,sandstorm,34,slam,41,iron_tail,45,crunch,52,double_edge,56,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
sudowoodo=pokemon("sudowoodo","imitation",70,100,115,30,65,30,rock,rock,rock_throw,0,mimic,0,low_kick,1,rock_slide,2,sleep_powder,3,faint_attack,4,slam,4,double_edge,5,flail,9,low_kick,17,rock_slide,25,sleep_powder,33,faint_attack,41,slam,49,double_edge,57,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
suicune=pokemon("suicune","aurora",100,75,115,90,115,85,water,water,bite,0,leer,0,bubblebeam,1,rain_dance,2,gust,3,aurora_beam,4,mist,5,mirror_coat,6,hydro_pump,7,dig,8,bubblebeam,11,rain_dance,21,gust,31,aurora_beam,41,mist,51,mirror_coat,61,hydro_pump,71,dig,81,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
sunflora=pokemon("sunflora","sun",75,75,55,105,85,30,grass,grass,absorb,0,pound,0,razor_leaf,1,fly,1,razor_leaf,2,sunny_day,3,petal_dance,3,solarbeam,4,growth,6,razor_leaf,13,fly,18,razor_leaf,25,sunny_day,30,petal_dance,37,solarbeam,42,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
sunkern=pokemon("sunkern","seed",30,30,30,30,30,30,grass,grass,absorb,0,mega_drain,1,fly,1,rolling_kick,2,sunny_day,3,synthesis,3,giga_drain,4,growth,6,mega_drain,13,fly,18,rolling_kick,25,sunny_day,30,synthesis,37,giga_drain,42,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
swinub=pokemon("swinub","pig",50,50,40,30,30,50,ice,ground,tackle,0,psybeam,0,powder_snow,1,endure,1,take_down,2,mist,3,blizzard,4,amnesia,5,powder_snow,10,endure,19,take_down,28,mist,37,blizzard,46,amnesia,55,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
tangela=pokemon("tangela","vine",65,55,115,100,40,60,grass,grass,fly,0,constrict,0,absorb,1,growth,1,poisonpowder,1,vine_whip,2,bind,2,mega_drain,3,stun_spore,3,sleep_powder,4,slam,4,drill_peck,4,absorb,10,growth,13,poisonpowder,19,vine_whip,22,bind,28,mega_drain,31,stun_spore,37,slam,40,drill_peck,46,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
tauros=pokemon("tauros","wild bull",75,100,95,40,70,110,normal,normal,tackle,0,tail_whip,0,scary_face,1,pursuit,1,swagger,2,rest,3,rage,4,thrash,4,take_down,5,horn_attack,8,scary_face,13,pursuit,19,swagger,26,rest,34,thrash,43,take_down,53,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
teddiursa=pokemon("teddiursa","little bear",60,80,50,50,50,40,normal,normal,scratch,0,leer,0,fury_swipes,1,surf,1,faint_attack,2,rest,3,slash,3,snore,4,thrash,4,lick,7,fury_swipes,13,surf,19,faint_attack,25,rest,31,slash,37,snore,43,thrash,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
tentacool=pokemon("tentacool","jellyfish",40,40,35,50,100,70,water,poison,poison_sting,0,constrict,1,acid,1,bubblebeam,2,wrap,3,barrier,3,screech,4,hydro_pump,4,supersonic,6,constrict,12,acid,19,bubblebeam,25,wrap,30,barrier,36,screech,43,hydro_pump,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
tentacruel=pokemon("tentacruel","jellyfish",80,70,65,80,120,100,water,poison,poison_sting,0,supersonic,0,constrict,0,constrict,1,acid,1,bubblebeam,2,wrap,3,barrier,3,screech,4,hydro_pump,5,supersonic,6,constrict,12,acid,19,bubblebeam,25,wrap,30,barrier,38,screech,47,hydro_pump,55,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
togepi=pokemon("togepi","spike ball",35,20,65,40,65,20,normal,normal,growl,0,charm,0,mega_kick,1,encore,1,ancientpower,2,scratch,2,wing_attack,2,safeguard,3,double_edge,3,metronome,4,baton_pass,4,sweet_kiss,9,mega_kick,13,encore,17,ancientpower,21,scratch,25,wing_attack,29,safeguard,33,double_edge,37,baton_pass,41,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
togetic=pokemon("togetic","happiness",55,40,85,80,105,40,normal,flying,earthquake,0,growl,0,charm,0,metronome,0,sweet_kiss,0,mega_kick,1,encore,1,ancientpower,2,scratch,2,wing_attack,2,safeguard,3,double_edge,3,metronome,4,baton_pass,4,sweet_kiss,9,mega_kick,13,encore,17,ancientpower,21,scratch,25,wing_attack,29,safeguard,33,double_edge,37,baton_pass,41,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
totodile=pokemon("totodile","big jaw",50,65,64,44,48,43,water,water,scratch,0,leer,0,water_gun,1,bite,2,scary_face,2,slash,3,screech,4,hydro_pump,5,rage,7,water_gun,13,bite,20,scary_face,27,slash,35,screech,43,hydro_pump,52,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
typhlosion=pokemon("typhlosion","volcano",78,84,78,109,85,100,fire,fire,tackle,0,leer,0,smokescreen,0,ember,0,ember,1,quick_attack,2,flame_wheel,3,swift,4,smokescreen,6,flamethrower,6,ember,12,quick_attack,21,flame_wheel,31,swift,45,flamethrower,60,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
tyranitar=pokemon("tyranitar","armor",100,134,110,95,100,61,rock,dark,bite,0,leer,0,sandstorm,0,screech,0,screech,1,rock_slide,2,thrash,2,scary_face,3,crunch,4,earthquake,6,hyper_beam,7,sandstorm,8,screech,15,rock_slide,22,thrash,29,scary_face,38,crunch,47,earthquake,61,hyper_beam,75,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
tyrogue=pokemon("tyrogue","scuffle",35,35,35,35,35,35,fighting,fighting,tackle,0,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
umbreon=pokemon("umbreon","moonlight",95,65,110,60,130,65,dark,dark,tackle,0,tail_whip,0,swords_dance,0,pursuit,1,quick_attack,2,confuse_ray,3,faint_attack,3,mean_look,4,screech,4,moonlight,5,sand_attack,8,pursuit,16,quick_attack,23,confuse_ray,30,faint_attack,36,mean_look,42,screech,47,moonlight,52,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
unown=pokemon("unown","symbol",48,72,48,72,48,48,psychic,psychic,hidden_power,0,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
ursaring=pokemon("ursaring","hibernator",90,130,75,75,75,55,normal,normal,scratch,0,leer,0,lick,0,fury_swipes,0,fury_swipes,1,surf,1,faint_attack,2,rest,3,slash,3,snore,4,thrash,4,lick,7,fury_swipes,13,surf,19,faint_attack,25,rest,31,slash,37,snore,43,thrash,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
vaporeon=pokemon("vaporeon","bubble jet",130,65,60,110,95,65,water,water,tackle,0,tail_whip,0,swords_dance,0,water_gun,1,quick_attack,2,bite,3,aurora_beam,3,haze,4,acid_armor,4,hydro_pump,5,sand_attack,8,water_gun,16,quick_attack,23,bite,30,aurora_beam,36,haze,42,acid_armor,47,hydro_pump,52,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
venomoth=pokemon("venomoth","poison moth",70,65,60,90,75,90,bug,poison,aurora_beam,0,tackle,0,disable,0,foresight,0,supersonic,0,confusion,1,poisonpowder,2,leech_life,2,stun_spore,2,gust,3,psybeam,3,sleep_powder,4,psychic,5,supersonic,9,confusion,17,poisonpowder,20,leech_life,25,stun_spore,28,gust,31,psybeam,36,sleep_powder,42,psychic,52,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
venonat=pokemon("venonat","insect",60,55,50,40,55,45,bug,poison,tackle,0,disable,0,foresight,0,confusion,1,poisonpowder,2,leech_life,2,stun_spore,2,psybeam,3,sleep_powder,3,psychic,4,supersonic,9,confusion,17,poisonpowder,20,leech_life,25,stun_spore,28,psybeam,33,sleep_powder,36,psychic,41,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
venusaur=pokemon("venusaur","seed",80,82,83,100,100,80,grass,poison,tackle,0,growl,0,leech_seed,0,vine_whip,0,vine_whip,1,poisonpowder,1,sleep_powder,1,razor_leaf,2,sweet_scent,2,growl,4,growth,4,synthesis,5,solarbeam,6,leech_seed,7,vine_whip,10,poisonpowder,15,sleep_powder,15,razor_leaf,22,sweet_scent,29,growth,41,synthesis,53,solarbeam,65,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
victreebel=pokemon("victreebel","flycatcher",80,105,65,100,60,70,grass,poison,stockpile,0,spit_up,0,psycho_boost,0,vine_whip,0,sleep_powder,0,sweet_scent,0,razor_leaf,0,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
vileplume=pokemon("vileplume","flower",75,80,85,100,90,50,grass,poison,absorb,0,hydro_pump,0,stun_spore,0,mega_drain,0,petal_dance,4,petal_dance,44,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
voltorb=pokemon("voltorb","ball",40,30,50,55,55,100,electric,electric,guillotine,0,tackle,0,sonicboom,1,spark,2,selfdestruct,2,rollout,3,light_screen,3,swift,4,explosion,4,mirror_coat,4,screech,8,sonicboom,15,spark,21,selfdestruct,27,rollout,32,light_screen,37,swift,42,explosion,46,mirror_coat,49,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
vulpix=pokemon("vulpix","fox",38,41,40,50,65,65,fire,fire,ember,0,quick_attack,1,mega_punch,1,confuse_ray,2,horn_attack,2,flamethrower,2,safeguard,3,horn_drill,3,fire_spin,4,tail_whip,5,roar,9,quick_attack,13,mega_punch,17,confuse_ray,21,horn_attack,25,flamethrower,29,safeguard,33,horn_drill,37,fire_spin,41,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
wartortle=pokemon("wartortle","turtle",59,63,80,65,80,58,water,water,tackle,0,tail_whip,0,bubble,0,withdraw,1,water_gun,1,bite,1,rapid_spin,2,protect,3,rain_dance,3,tail_whip,4,skull_bash,4,hydro_pump,5,bubble,7,withdraw,10,water_gun,13,bite,19,rapid_spin,25,protect,31,rain_dance,37,skull_bash,45,hydro_pump,53,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
weedle=pokemon("weedle","hairy bug",40,35,30,20,20,50,bug,poison,poison_sting,0,string_shot,0,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
weepinbell=pokemon("weepinbell","flycatcher",65,90,50,85,45,55,grass,poison,vine_whip,0,growth,0,wrap,0,wrap,1,sleep_powder,1,poisonpowder,1,stun_spore,1,acid,2,sweet_scent,3,razor_leaf,4,slam,5,growth,6,wrap,11,sleep_powder,15,poisonpowder,17,stun_spore,19,acid,24,sweet_scent,33,razor_leaf,42,slam,54,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
weezing=pokemon("weezing","poison gas",65,90,120,85,70,60,poison,poison,poison_gas,0,tackle,0,smog,0,selfdestruct,0,selfdestruct,1,sludge,2,smokescreen,2,haze,3,explosion,4,destiny_bond,5,pay_day,5,smog,9,selfdestruct,17,sludge,21,smokescreen,25,haze,33,explosion,44,destiny_bond,51,pay_day,58,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
wigglytuff=pokemon("wigglytuff","balloon",140,70,45,75,50,45,normal,normal,sing,0,disable,0,defense_curl,0,doubleslap,0,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
wobbuffet=pokemon("wobbuffet","patient",190,33,58,33,58,33,psychic,psychic,counter,0,mirror_coat,0,safeguard,0,destiny_bond,0,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
wooper=pokemon("wooper","water fish",55,45,45,25,25,15,water,ground,water_gun,0,tail_whip,0,slam,1,thunderbolt,1,amnesia,2,mega_kick,3,earthquake,3,rain_dance,4,mist,5,haze,5,slam,11,thunderbolt,16,amnesia,21,mega_kick,31,earthquake,36,rain_dance,41,mist,51,haze,51,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
xatu=pokemon("xatu","mystic",65,75,70,95,70,95,psychic,flying,peck,0,leer,0,night_shade,1,teleport,2,wing_attack,3,future_sight,3,confuse_ray,5,psychic,6,night_shade,10,teleport,20,wing_attack,35,future_sight,35,confuse_ray,50,psychic,65,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
yanma=pokemon("yanma","clear wing",65,65,45,75,45,95,bug,flying,tackle,0,foresight,0,double_team,1,sonicboom,1,hypnosis,2,detect,2,uproar,3,wing_attack,3,supersonic,4,screech,5,quick_attack,6,double_team,12,sonicboom,17,hypnosis,23,detect,28,uproar,34,wing_attack,39,supersonic,45,screech,50,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
zapdos=pokemon("zapdos","electric",90,90,85,125,90,100,electric,flying,peck,0,thundershock,0,thunder_wave,1,agility,2,detect,3,drill_peck,4,guillotine,6,light_screen,7,thunder,8,thunder_wave,13,agility,25,detect,37,drill_peck,49,guillotine,61,light_screen,73,thunder,85,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)
zubat=pokemon("zubat","bat",40,45,35,30,40,55,poison,flying,leech_life,0,supersonic,1,bite,1,wing_attack,2,confuse_ray,2,ice_beam,3,mean_look,3,sonicboom,4,haze,4,mist,6,supersonic,11,bite,16,wing_attack,21,confuse_ray,26,ice_beam,31,mean_look,36,sonicboom,41,haze,46,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200,tackle,200)

'''
trainers

class trainor:
  def __init__(self,name,money):
    self.name=name
    self.money=money
    self.contents=list()
    self.dialoguestart=""
    self.dialoguewin=""
    self.dialogueloss=""
    
'''    
rick_blawson=trainor("rick blawson",100)
rick_blawson.contents.append(onix)
rick_blawson.contents.append(magikarp)
rick_blawson.contents.append(geodude)
rick_blawson.contents.append(arbok)
rick_blawson.contents.append(muk)



  
'''
arealoc
def __init__(self,name,north="grass",east="grass",west="grass",south="grass",description="")
'''
pallet_town=arealoc("pallet town","your home town! say hi to professor oak")
pallet_town.trainers=rick_blawson
pallet_town.x=10
pallet_town.y=10

route_1=arealoc("route 1","welcome to the first trail of your adventure")

route_1.x=11
route_1.y=10

 
level1= floor("kanto")
level1.arealocs.append(pallet_town)
level1.arealocs.append(route_1)


location=pallet_town
x=10
y=10

name= "aubin"

user=player("aubin")
user.pokemon.append(pikachu)
user.pokemon.append(charmander)

for pokemon in user.pokemon:
  moves_maker(pokemon)
  ability_keeper(pokemon)
for pokemon in location.trainers.contents:
  moves_maker(pokemon)
  ability_keeper(pokemon)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  

while not response  == "dfhsergghj":
  response=input("\ncommand: ")
  if response == "quit":
    ask_ok("you are about to quit, type no to quit")
    if relive==0:
      response="dfhsergghj"
#  try:
  holder=(response.split())
  mapping()
  what_you_do(holder)
#  except:
#    print("type a command please")






