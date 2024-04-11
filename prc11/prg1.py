def prime(num):
    for x in range(2,num):
     if num%x ==0 :
        return False
    return True
print("Parameter is Prime",prime(2))
