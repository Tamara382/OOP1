course1=int(input("enter grade points for course1"))
course2=int(input("enter grade points for course2"))
course3=int(input("enter grade points for course3"))
total=(course1+course2+course3)
percentile=int((total/300)*100)
if percentile <100 and percentile>=90:
    print("grade A")
elif percentile<90 and percentile>=80:
    print("grade B")
elif percentile<80 and percentile>=70:
    print("grade C")