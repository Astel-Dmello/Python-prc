class Degree:
    def getDegree(self):
        print("I got a degree")

class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate")

class Postgraduate(Degree):
    def getDegree(self):
        print("I am a Postgraduate")

# Example usage:
degree_obj = Degree()
degree_obj.getDegree()

undergraduate_obj = Undergraduate()
undergraduate_obj.getDegree()

postgraduate_obj = Postgraduate()
postgraduate_obj.getDegree()
