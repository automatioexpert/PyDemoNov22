
class a:
    pass

class b(a):
    pass

print(issubclass(b,a))

class Iphone13:
    Variable1="Check"
    def __init__(self,display,camera):
        self.display=display
        self.camera=camera

    def typeOfDisplay(self):
        print(f"This iphone has {self.display} type of display")

    def typeOfCamera(self):
        print(f"This iphone has {self.camera} type of camera")

class Iphone14(Iphone13):
    def __init__(self, phoneSize, audio, display, camera):
        super().__init__(display, camera)
        self.phoneSize=phoneSize
        self.audio=audio

    def typeOfPhoneSize(self):
        print(f"This iphone has {self.phoneSize} type of phoneSize")

    def typeOfAudio(self):
        print(f"This iphone has {self.audio} type of audio")

#a = Iphone13("Notchless","Cinematic")
b = Iphone14("Pro Max","Dolby","Notchless","Cinematic")

b.typeOfCamera()
b.typeOfPhoneSize()
b.typeOfCamera()
print(b.Variable1)