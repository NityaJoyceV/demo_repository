try:
    file1=open("C:\Users\NITYA\Documents\Python\dem.txt","w")
    file1.write("The previous data got erased.")
    
    
finally:
    print("In finally block")
    file1.close()
