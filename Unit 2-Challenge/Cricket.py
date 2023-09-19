#Base Class
class Player:
  def play(self):
    print("The Player is playing Cricket")
#Derived Class
class Batsman(Player):
  def play(self):
   print("The Batsman is Batting")
#Derived Class
class Bowler(Player):
  def play(self):
   print("The Bowler is Bowling")
#Object Creation
batsman=Batsman()
bowler=Bowler()
#Method Calling
batsman.play()
bowler.play()
