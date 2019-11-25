import random

#Fitness function to calculate fitness values and store in an array 'F'.
def fitness(X):
    for i in range(0, len(X)):
        F[i] = X[i]*X[i]/100   #divide by 100 because each decimal of X divide by 10

    return F

#Function to convert the variable 'x' to binary representation
def to_binary(B,X):
    for i in range(0,len(X)):
        B[i]= format(X[i],'08b')

    return B

#Function to convert the binary representation of variable 'x' to decimal representation
def to_decimal(B,X):
    for i in range(0,len(X)):
        X[i]= int(B[i],2)

    return X


#Tournament selection done by taking the best chromosome twice and rejecting the worst
def fit_exchange(X,F):
    maxx = F.index(max(F))
    minn = F.index(min(F))
    temp1 = X[maxx]
    X[minn] = temp1


    return X




#For Odd number of populations, a random index doesnt participate in cross over
#Function to select pairwise which elements mate and undergo crossover
def sel_cross(B):
    temp = [0, 0, 0, 0]
    ran = random.randrange(len(B))

    if len(B)%2!=0:

        for i in range(0,len(B)):

            j = random.randrange(len(B))
            if j!=ran:
                while j== i and temp[j]==0 :
                    j = random.randrange(len(B))

                temp[i]=j;
                temp[j]=i;
            else:
                temp[ran]=-1;

    else:
        for i in range(0, len(B)):
            j = random.randrange(len(B))
            while j == i and temp[j]==0:
                j = random.randrange(len(B))
            temp[i] = j;
            temp[j] = i;


    for i in range(0,1):
        if temp[i]!=-1:
            j = temp[i]
            b1 = B[i]
            b2 = B[j]
            temp[i]=-1
            temp[j]=-1
            crossover = random.randrange(1,8)
            s1 = str(b1)
            s2 = str(b2)
            tempS= s1[0:crossover]+s2[crossover:8]
            tempS1= s2[0:crossover]+s1[crossover:8]
            s11 = int(tempS,2)
            s22 = int(tempS1,2)
            s11 = format(s11,'08b')
            s22 = format(s22,'08b')
            B[i]=s11
            B[j]=s22
    return B





B=[[0],[0],[0],[0]]


X=[4,101,235,16]
F = [0,0,0,0]
B = to_binary(B, X)





for i in range(0,10):
    if i == 0 :
        X = to_decimal(B,X)
        F = fitness(X)
        X = fit_exchange(X,F)
        print(X)
        B = to_binary(B,X)
    else :
        B= sel_cross(B)
        X= to_decimal(B,X)
        F = fitness(X)
        X = fit_exchange(X, F)
        B = to_binary(B, X)
        print(B)
        print(X)

print(B)



