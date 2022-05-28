class zuri_student():
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score
        print("my name is", name, "I am", age, "My track is", track, "I scored", score)
    def speak (self):
        print("this is the function", self.name, "my age is", self.age, "i venture in this", self.track, "here is my score", self.score)
h = zuri_student("Esther",  20, "full stack", 10.0)
class student(zuri_student):
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score
        print("change_name", self.name)
        print("change_age", self.age)
        print("change_track", self.track)
        print("change_score", self.score)
h = student("Jayjay", 17, "UI/UX", 17.94)




# Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
#
# # Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()
