largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum=float(num)
    except:
        print('Invalid input')
    if fnum == "done":
        break
    if largest is None:
        largest=fnum
    elif largest<fnum:
        largest=fnum
    if smallest is None:
        smallest=fnum
    elif smallest>fnum:
        smallest=fnum
print("Maximum is", largest)
print("Minimum is", smallest)
