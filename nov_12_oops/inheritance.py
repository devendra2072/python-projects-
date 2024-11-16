# // 1  inheritance 
# // i. single-level inheritance
# class a:  # base class
#      def home(self):
#           print("H.N.-SA")
#      def car(self):
#           print("Maruti-800")

# class b(a): #subclass
#      def mydata(self):
#           print("my details..")
# obj=b()
# obj.home()
# obj.car()
# obj.mydata()

# 2. maltilevel inheritance 
# class a:
#      def home(self):
#           print("H.N.-SA")
#      def car(self):
#           print("Maruti-800")

# class b(a):
#      def mydata(self):
#           print("my details..")
# class c(b):
#      def new(self):
#           print("new....")
# obj=c()
# obj.home()
# obj.car()
# obj.mydata()
# obj.new()         


# 3. maltiple inheritance  
# method resolvation oder (mro){L-R}// deafth frist // super 
# method apna ghar bnale
# overridding 
# two alag alag name ki class ke under same mathod ko overriding  kahte hai 
# class a:
#      def n1(self):
#           print("H.N.-SA")
# class b(a):
#      def n1(self):
#           super().n1()    # super method ka use karte hai 
#           print("my details..")
#           # super().n1()    # super method ka use karte hai   // method overridding ko rokne ke liye super ka use karte hai 
# obj=b()
# obj.n1()  

# 2 alag alag class uske under same name ki method and same parameter 

# ak  class ke under two same name ki method bana de to overloading