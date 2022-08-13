import numpy as np

class Matrix_Operations:
    
    def matrix_input(self):
        
        while True:
            
            try:
                
                self.RowsNum = int(input("Enter the rows number of the matrix: "))
                
            except:
                
                print('\nPlease Enter a Vaild Number..\n')
                
                continue
            
            try:
                
                self.ColsNum = int(input("Enter the columns number of the matrix: "))
                
            except:
                
                print('\nPlease Enter a Vaild Number..\n')
                
                continue
                    
            break
                   
        print("Enter The Matrix: ")
            
        self.Processing = []
        
        self.cnt = 0
  
        while self.cnt < self.RowsNum:
            
            try:
                        
                self.Row = list(map(float,input().split()))
                
            except:
                
                print('\nPlease Enter a Vaild Number..\n')
                
                print('\nType The Matrix again\n')
                
                self.cnt = 0
                
                continue
            
            if len(self.Row) != self.ColsNum:
                
                self.cnt = 0
                
                print('\nYou Have Entered more columns than expected..\n')
                
                print('\nType The Matrix again\n')
                
                continue           
                
            self.Processing.append(self.Row)
            
            self.cnt+=1
            
        self.Final_res = [self.Processing , self.RowsNum , self.ColsNum]
               
        return self.Final_res
    
    def addition(self,F_MAT,S_MAT):

        self.Added_Mat = []
            
        self.Matrix_1 = F_MAT[0]
            
        self.Matrix_2 = S_MAT[0]
                   
        for i in range(F_MAT[1]):

            self.Processing = []
            
            for j in range(F_MAT[2]):
                
                self.m = self.Matrix_1[i][j] + self.Matrix_2[i][j]
                
                self.Processing.append(self.m)
                
            self.Added_Mat.append(self.Processing)
            
        self.Final_res = [self.Added_Mat , F_MAT[1] , F_MAT[2]]
        
        return self.Final_res

    def subtraction(self,F_MAT,S_MAT):
        
        self.SubTr_Mat = []
            
        self.Matrix_1 = F_MAT[0]
            
        self.Matrix_2 = S_MAT[0]
                    
        for i in range(F_MAT[1]):

            self.Processing = []
            
            for j in range(F_MAT[2]):
                
                self.m = self.Matrix_1[i][j] - self.Matrix_2[i][j]
                
                self.Processing.append(self.m)
                
            self.SubTr_Mat.append(self.Processing)
            
        self.Final_res = [self.SubTr_Mat , F_MAT[1] , F_MAT[2]]
        
        return self.Final_res
    
    def multiplication(self,F_MAT,S_MAT):
        
        self.MUL_Mat = []
        
        for i in range(F_MAT[1]):
            
            self.Matrix_1 = F_MAT[0]
            
            self.Matrix_2 = S_MAT[0]
            
            self.Processing = []
            
            for j in range(S_MAT[2]):
                
                self.sum = 0
                
                for k in range(F_MAT[2]):
                    
                    self.sum += (self.Matrix_1[i][k] * self.Matrix_2[k][j])
                    
                self.Processing.append(self.sum)
                
            self.MUL_Mat.append(self.Processing)
            
        self.Final_res = [ self.MUL_Mat , F_MAT[1] , S_MAT[2] ]
        
        return self.Final_res
    
    def inverse(self,Matrix):
        
        if Matrix[1] != Matrix[2]:
            
            return "The Matrix Should Be a Square Matrix"
        
        try:
            
            self.INV_Mat = list(np.linalg.inv(Matrix[0]))
            
            self.ARR_To_LIST = [list(self.INV_Mat[i][0:]) for i in range(Matrix[1])]
            
            self.Final_res = [self.ARR_To_LIST, Matrix[1], Matrix[2]]
            
        except:
            
            self.Final_res = "Cant Get Inverse, The Matrix is Singular"
        
        return self.Final_res

    def transpose(self,Matrix):
        
        self.TRANS_Mat = []
        
        self.Orig_Mat = Matrix[0]
        
        for i in range(Matrix[1]):
            
            self.Proccesing = []
            
            for j in range(Matrix[2]):
                
                self.Proccesing.append(self.Orig_Mat[j][i])
                
            self.TRANS_Mat.append(self.Proccesing)
            
        self.Final_res = [self.TRANS_Mat , Matrix[1] , Matrix[2]]
        
        Matrix_Print.matprnt(self,self.Final_res)

class Matrix_Print:
    
    def matprnt(self,Orig_Mat):
        
        self.Matrix = Orig_Mat[0]
        
        for i in range(Orig_Mat[1]):
            
            for j in self.Matrix[i]:
                
                print(round(j,3),end=' ')
                
            print('\n')
        
    def matprntforencrypt(self,Orig_Mat):
        
        self.Matrix = Orig_Mat[0]
        
        for i in range(Orig_Mat[1]):
            
            for j in self.Matrix[i]:
                
                print(j,end=' ')
                
            print()
        
        print(f"{Orig_Mat[1]} Row and {Orig_Mat[2]} Columns\n")
        
        print("Copy The Code and Send it to The Receiver..(There Will Be Automatic Send and Receive Soon..)\n\n")
        

class Matrix_Validator:
    
    def Checker(self,F_MAT,S_MAT,Operation):

            if F_MAT[1]==S_MAT[1] and F_MAT[2]==S_MAT[2]:
                
                print("\nThe result is: \n")
                
                if Operation == 1:
                    
                    self.proc = Matrix_Operations.addition(self , F_MAT , S_MAT)
                    
                    Matrix_Print.matprnt(self,self.proc)
                
                elif Operation == 2:
                    
                    self.proc = Matrix_Operations.subtraction(self , F_MAT , S_MAT)
                    
                    Matrix_Print.matprnt(self,self.proc)  
                
            else:
                
                print("\nCan't make this opertaion on two different matrices systems.\n")
                


    def CheckerMul(self,F_MAT,S_MAT,Operation):
        
        if Operation == 3:
            
            if F_MAT[2] == S_MAT[1]:
                
                print("\nThe Result is: \n")
                
                self.proc = Matrix_Operations.multiplication(self, F_MAT , S_MAT)
                
                Matrix_Print.matprnt(self,self.proc)
                
            else:
                
                print("\nCan't make this opertaion on two different matrices systems.\n")
        
        elif Operation == 6:
            
                print("\nThe Result is: \n")
                
                self.proc = Matrix_Operations.multiplication(self , F_MAT , S_MAT)
                
                Matrix_Print.matprntforencrypt(self , self.proc)
        
            
class Matrix_Enc_Dec:
    
    def encrypt(self, String , Operation ):
        
        #---Constant Matrix----
        
        self.SECRET_MATRIX = [[34646545,67234774,927246754],[556624638,457575356,7123463342],[52377435,9478565656,23533463464]]
        
        self.INDEX = 9283019346352
        
        #---Making a matrix for string---
        
        self.Mat_S = []
        
        self.rand_lst = []
        
        while len(String)%3 != 0:
            
            String += ' '    
        
        for i in range( len(String) ):

            self.rand_lst.append((ord(String[i])-62) + self.INDEX*2)
            
            
            if len(self.rand_lst) == 3:
                
                self.Mat_S.append(self.rand_lst)
                
                self.rand_lst = []                   
                
        Matrix = [self.Mat_S , len(self.Mat_S) , 3]
        
        self.SECRET_MATRIX = [self.SECRET_MATRIX , 3 , 3]
        
        return Matrix_Validator.CheckerMul(self , Matrix , self.SECRET_MATRIX , Operation )

    def decrypt(self , Matrix):
        
        self.INV_Mat = Matrix_Operations.inverse(self , [[[34646545,67234774,927246754],[556624638,457575356,7123463342],[52377435,9478565656,23533463464]],3,3])
        
        self.Mul_Mat = Matrix_Operations.multiplication(self , Matrix, self.INV_Mat)
        
        self.INDEX = 9283019346352
        
        self.Word = []
        
        for row in self.Mul_Mat[0]:
            
            self.Processing = []
            
            for col in row:
                
                self.Processing.append((round(col)+62) - self.INDEX*2)
                
            self.Word.append(self.Processing)
        
        self.String = ""
        
        for row in self.Word:
            
            for col in row:
                
                self.String+=chr(col)
                
        print(f"\n\n{self.String}\n\nDONE!!")
            
    
    
    