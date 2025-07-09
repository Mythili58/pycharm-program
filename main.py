import gradecal
if __name__ == "__main__":
    l=[]
    for i in range(5):
        marks=int(input("Enter marks:"))
        if marks>=0 and marks<=100:
            l.append(marks)
        else:
            print("Invalid marks")
    avg=sum(l)/len(l)
    print("Your Grade is:")
    gradecal.grade(avg)