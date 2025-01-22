class multiplefunction():
    
    
    def subfields(fields):
        print("Subfields inAIare:")
        fields=["Macine Learning","Neurel Networks","Vision","Robotics","Speech Processing","Natural Laguage Processing"]
        for field in fields:
            print(field)
            
    def oddeven():
         num=int(input("Enter a number:"))
         if num%2==1:
            print(f"{num} is Odd number")
         else:
            print(f"{num} is Even number")

    def Eligible():
         Gender=input("Your Gender:")
         age=int(input("Your Age:"))
         if(age>=21):
            print("ELIGIBLE")
         else:
            print("NOT ELIGIBLE")

    def percentage():
         s1=int(input("Subject1:"))
         s2=int(input("Subject2:"))
         s3=int(input("Subject3:"))
         s4=int(input("Subject4:"))
         s5=int(input("Subject5:"))
         total=s1+s2+s3+s4+s5
         percentage=(total/500)*100
         print("Total:",total)
         print("Percentage:",percentage)

    def triangle():
         a1=int(input("Height:"))
         b1=int(input("Breadth:"))
         Areaformula="(Height*Breadth)/2"
         Area=(a1*b1)/2
         print("Area formula:",Areaformula)
         print("Area of Traingle:",Area)
         a2=int(input("Height1:"))
         b2=int(input("Height2:"))
         c=int(input("Breadth:"))
         Perimeterformula="Height1+Height2+Breadth"
         perimeter=a2+b2+c
         print("Perimeterformula:",Perimeterformula)
         print("Permeter of Traingle:",perimeter)
          
    
    
            
            
            
            
          
    

        