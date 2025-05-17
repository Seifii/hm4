class one:
    power = 10
    sadness = 9
    def pow(self):
        print(one.power)
        print(one.sadness)
class two:
    calmness = 5
    def calm(self):
        print(two.calmness)
class three:
    speed = 7
    skill = 15
    def spp(self):
        print(three.speed)
        print(three.skill)
class last(one, two, three):
    happiness = 11
    def hap(self):
        print(last.happiness)
    def yo(self):
        print("Yooyoyoyoyoy")

result = last()
result.pow()
result.calm()
result.spp()
result.hap()
result.yo()


