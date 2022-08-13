from functions import *

while True:
    
    print("\n1)Addition\n2)Subtraction\n3)multiplication\n4)inverse\n5)Transpose\n6)Encrypt a String\n7)Decrypt an Encrypted String\n8)Quit\n")
    
    try:
        
        n = int(input("Choose the operation number: "))
        
    except:
        
        print('\nPlease Enter a Valid Number..\n')
        
        continue
    
    op = Matrix_Operations()
    
    prnt = Matrix_Print()
    
    val = Matrix_Validator()
    
    encdec = Matrix_Enc_Dec()
    
    if n == 1:
        
        x = op.matrix_input()
        
        y = op.matrix_input()
        
        val.Checker(x,y,n)
        
    elif n == 2:
        
        x = op.matrix_input()
        
        y = op.matrix_input()
        
        val.Checker(x,y,n)
        
    elif n == 3:
        
        x = op.matrix_input()
        
        y = op.matrix_input()
        
        val.CheckerMul(x,y,n)
        
    elif n == 4:
        
        x = op.matrix_input()
        
        print('\nthe result is :\n')
        
        z = op.inverse(x)
        
        if z == str(z):
            
            print(z)
        
        else:
            
            prnt.matprnt(z)
        
    elif n == 5:
        
        x = op.matrix_input()
        
        print('\nthe result is :\n')
        
        op.transpose(x)
        
    elif n == 6:
        
        String = input("Enter The String You Want to Encrypt: \n\n")
        
        encdec.encrypt(String,n)
        
    elif n == 7:
        
        x = op.matrix_input()
        
        encdec.decrypt(x)
    
    elif n==8:
        
        break 

