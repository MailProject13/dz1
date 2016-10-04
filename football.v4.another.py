import random


def sortbypoints(tmp):
    return(tmp.points)

class hismatch(object):
    def __init__(self):
		name1=team1.name
		name2=team2.name
		goals1=a
		goals2=b
	def scores (self):
		print(name1, "-", name2, goals1, ":", goals2, "\n")

class team(object):
  def __init__(self):
      self.win = 0
      self.lose = 0
      self.draw = 0
      self.pas = 0
      self.goals = 0
      self.points = 0
      self.name=self.getname()
  def getname(self):
    while (1):
        i=0
        _name = input()
        for each in teams:
            if each.name==_name:
                i=1
                print("The same name have already been registered. Enter the new one: ")
                continue
        if (i==1): continue
        return _name
  def pr(self):
    print(self.name, "\nwin ",self.win,"lose ",self.lose,"draw ",self.draw,"pass ",self.pas,"goals ",self.goals,"points ",self.points) 


def match(team1,team2):
  a = random.randint(0,10)
  b = random.randint(0,10)
  team1.goals += a
  team1.pas += b
  team2.goals += b
  team2.pas += a
  history.append(hismatch())
  if a > b : 
      team1.win += 1
      team1.points += 3
      team2.lose += 1
      return 0
  elif a==b :
      team1.draw += 1
      team1.points += 1
      team2.draw += 1
      team2.points += 1
      return 0
  team1.lose += 1
  team2.win += 1
  team2.points += 3
  return 0

y=1
while y==1:
    try: 
        count=int(input("Enter the count of teams: "))
        y=0
    except ValueError: print("It must be a number!")
	
teams=[]

for i in range(1, count+1):
    print("Enter the name of ", i, "team: ")
    teams.append(team())

history[]

for i in range(0,count):
    for j in range(i+1,count):
        match(teams[i],teams[j])

teams.sort(key=sortbypoints, reverse=True)
while 1:
	request=init("history - 'h', results table - 'rt', others - exit")
	if request=='h'
		for each in history
			each.scores()
		continue
	if request=='rt'
		for each in teams:
			each.pr()
		continue
	return 0
