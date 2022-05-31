score=input('Enter score')
try:
    score=float(score)
except:
    print('Enter score between 0.0 to 1.0')
    quit()
if score < 0.0 or score > 1.0:
    print('enter score between 0.0 to 1.0')
    quit()
else:
    if score>=0.9:
        grade='A'
    elif score>=0.8:
        grade='B'
    elif score>=0.7:
        grade='C'
    elif score>=0.6:
        grade='D'
    elif score<0.6:
        grade='F'
print(grade)
