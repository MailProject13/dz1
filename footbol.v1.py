import random
class team(object):
  win = 0
  lose = 0
  draw = 0
  pas = 0
  goals = 0
  points = 0
  def pr(self):
    print("win ",self.win,"lose ",self.lose,"draw ",self.draw,"pass ",self.pas,"goals ",self.goals,"points ",self.points) 
def match(team1,team2):
  a = random.randint(0,10)
  b = random.randint(0,10)
  team1.goals = a
  team1.pas = b
  team2.goals = b
  team2.pas = a
  if a > b : 
      team1.win += 1
      team1.point += 3
      team2.lose += 1
  elif a==b :
      team1.draw += 1
      team1.point += 1
      team2.draw += 1
      team2.point += 1
  else :
      team1.lose += 1
      team2.win += 1
      team2.points += 3



team1 = team()
team2 = team()
team3 = team()
team4 = team()
teams = (team1,team2,team3,team4)

for i in range(0,4):
    for j in range(i+1,4):
        match(teams[i],teams[j])
for i in range (0,4):
    print("team,i+1," ")
    teams[i].pr()
