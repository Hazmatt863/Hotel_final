#Matthew Jones CIS261#


print("#########################################################")
print("#############JONES HOTEL RESERVATION SYSTEM##############")
print('#########################################################")
      
#Calculation for main function      
class hotelfarecal:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=85,b=120,datetime.date='',datetime.timealpha='',name='',address='',cindate='',coutdate='',rno=101):

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.datetime.date=today
        self.datetime.timealpha=coutdate - cindate=timealpha
        self.a=85
        self.b=120
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
      
class inputdata(self):
      
      def __init__inputdata(self):  
        self.date=today()
        self.datetime=datetime.datetime.strptime(input(' '),['%d/%b/%Y']
        self.timedelta=datetime.timealpha.strptime(input(' '),['%d/%b/%Y']                                        
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=datetime.datetime.strptime(input("\nEnter your check in date:"), ['%d/%b/%Y']
        self.coutdate=datetime.datetime.strptime(input("\nEnter your checkout date:"), ['%d/%b/%Y']
        print("Your room no.:",self.rno,"\n")


    def month(i):
        from datetime import datetime
        from datetime import date
        from datetime import timealpha
        
        switcher={ (input(' '))
            1:'January',
            2:'Febuary',
            3:'March',
            4:'April',
            5:'May',
            6:'June',
            7:'July',
            8:'August',
            9:'September',
            10:'October',
            11:'November',
            12:'December',
            }
            
    def roomrent(self):#sel1353

        print ("We have the following options for you:-")

        print ("1.  option A---->For all the months but August = 85 PN\-")
        
        print ("2.  option B---->For the month of August = 120 PN\-")
                             
        x=int(input("Enter Your Choice Please->"))

        n=int(input("For How Many Nights Did You Stay:"), ([self.coutdate-self.cindate=timedelta])

        if(x==1):

            print ("you have selected option 1")

            self.s=85*n

        elif (x==2):

            print ("you have selected option B")

            self.s=120*n

            
        else:

            print ("please choose a room")

            print ("your room rent is = ")
#Display settings
    def display(self):
        print ("******HOTEL BILL******")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)

        self.rt = self.coutdate - self.cindate + self.a

        print ("Your sub total bill is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.rt+self.a,"\n")
        self.rno+=1

            
#MAIN APPLICATION  FUNCTION
def main():

    a=hotelfarecal()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate rommrent")

        print("3.Show total cost")

        print("4.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.showtotalcost()

        if (b==4):

            a.exit

        if (b==5):

            a.display()

        if (b==6):

           quit()

       


main()
