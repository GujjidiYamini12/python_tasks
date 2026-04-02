"""7. Student Result Generator (Method Overloading Concept)
A school system calculates student results differently depending on available data.
Create a Result class where a method can calculate the result using either two
subjects or three subject"""
class Result:
    def calResult(self,maths,sci):
        self.maths=maths
        self.sci=sci
        result=self.sci+self.maths
        print(result)
r=Result()
r.calResult(100,90)