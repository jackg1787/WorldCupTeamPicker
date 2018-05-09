import random

print("The code works by assigning each of the teams to pools based on their ranking and how many people are participating, then giving everyone one random team from each pool. This means that everyone is guarenteed a good team. Some of the worst teams will be removed in order for everyone to have an even number. You can have a maximum of 32 people participating.", "\n")

#### array of all teams, with their current ranking
TeamArray = [
["Germany" ,1],
["Brazil" ,2],
["Belgium" ,3],
["Portugal" ,4],
["Argentina" ,5],
["Switzerland" ,6],
["France" ,7],
["Spain" ,8],
["Poland" ,10],
["Peru" ,11],
["Denmark" ,12],
["England" ,13],
["Tunisia" ,14],
["Mexico" ,15],
["Colombia" ,16],
["Uruguay" ,17],
["Croatia" ,18],
["Iceland" ,22],
["Sweden" ,23],
["CostaRica" ,25],
["Senegal" ,28],
["Serbia" ,35],
["Iran" ,36],
["Australia" ,40],
["Egypt" ,46],
["Nigeria" ,47],
["Morocco" ,47],
["Panama" ,55],
["Japan" ,60],
["SouthKorea" ,61],
["Russia" ,66],
["SaudiArabia" ,70] ]


# get how many people are participating (wrapped in some exceptions to avoid bad inputs)
while True:
  try:
    NumberOfParticipants = int(input("How many people are participating? "))
    if NumberOfParticipants < 0 or NumberOfParticipants> len(TeamArray):
      print("selection not valid")
      continue
    else:
      break
    
  except ValueError:
    print("Not a number")
    continue

NumberOfPools = int(len(TeamArray)/int(NumberOfParticipants))
# remove excess teams
NumberOfDeletedTeams = len(TeamArray)- (int(NumberOfParticipants)*NumberOfPools)

# remove bottome n teams to get even numbered pools
TeamArray = TeamArray[:len(TeamArray)-NumberOfDeletedTeams]

#create list of pools
pools = []
for i in (range(1,int(NumberOfPools)+1)):
    pools.append(i)
    
#create a pool label for each team
pools2 = []
for i in (range(0,int(NumberOfParticipants))):    
    pools2.extend(pools)
    
#put labels in right order  
pools2.sort()

# append mega array with the pool labels
for j in range(0, len(pools2)):
   #print(TeamArray[j])
   #print(pools2[j])
   TeamArray[j].append(pools2[j])

# shuffle the array
random.shuffle(TeamArray)

#for each participant, print their number. then for each pool, select a team for each person. print all the pools for each person.
for i in range(NumberOfParticipants):
    print("\n", "PERSON", i+1, '\'s Teams: ')
    for k in range(1,NumberOfPools+1):
        a = [j for j in TeamArray if j[2] ==k][i]
        print(a[0])
