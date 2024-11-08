circumference = float(input("Enter tree circumference in cm: "))
diameter = circumference / 3.14 
can_cut_down = diameter >= 50
print(f"Tree can be cut down: {can_cut_down}")
#160=true,120=false,90=false,230=true