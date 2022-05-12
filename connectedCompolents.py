import numpy
xSize=10
ySize=10

inpImg=numpy.array([
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0,0,0,0],
    [0,0,0,1,1,0,0,0,0,0],
    [0,0,1,0,0,0,1,1,0,0],
    [0,1,1,1,0,1,1,1,1,0],
    [0,0,1,0,0,0,1,1,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
    ]
)

storedPairs=[0,0]
print("original img")
print(inpImg)
c=0
leftPix=0
upPix=0
for i in range(2):
    print(i)
    print(inpImg)

    for y in range(ySize):
        for x in range(xSize):
            if(x!=0):
                leftPix=inpImg[y,x-1]
                
            else:leftPix=0
            if(y!=0):
                upPix=inpImg[y-1,x]
            
            else:upPix=0
            
            if(inpImg[y,x]==1):

                if((upPix==0)and(leftPix==0)):
                    c=c+1
                    inpImg[y,x]=c
                elif(upPix==0):
                    inpImg[y,x]=leftPix
                elif(leftPix==0):
                    inpImg[y,x]=upPix
                else:
                    inpImg[y,x]=min(upPix,leftPix)
                    if(upPix!=leftPix):
                        storedPairs.append([leftPix,upPix])
        
    for i in storedPairs:
        print(i)
        for y in range(ySize):
            for x in range(xSize):
                if(inpImg[y,x]==i[0]):
                    inpImg[y,x]=i[1]

    print("stored pairs are")
    print(storedPairs)
print("first scan img")
print(inpImg)      
print("number of objects")
print(numpy.size(numpy.unique(inpImg))-1)      
