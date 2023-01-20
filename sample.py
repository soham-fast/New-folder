class Review:
  def __init__(self,m,s,a,r):
    self.movie=m
    self.story=s
    self.actor=a
    self.music=r
    self.avg=int((s+a+r)/3)
    self.myratings={'MovieName':m,'StoryRatings':s,'ActorRatings':a,'MusicRatings':r,'AverageRatings':self.avg}
  def display(self):
    print("THANKS FOR YOUR RATINGS",end=' ')
    for i in range(0,self.avg):
      print("*" ,end=' ')
    print()  
    print(self.myratings)
p1=Review('Circus',8,9,7)
p1.display()