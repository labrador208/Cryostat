import parser as par
import math
from math import *
import matplotlib.pyplot as plt
import random
import numpy as np
random.seed(5)

#Code has almost all functionality required. Last function required is to compare the heat output of a blackbody over the entire spectrum of wavelengths to a specific wavelength
#This will allow the calcHeatLoads() function to determine the heat load over a specific wavelength. Will likely copy and paste a large part of the filter() code 


#This function can plot an equation over a range. Make sure to use Python notation. Originally had a filter function attached but 
#it is no longer updated and needs to be brought over from the filter() function. Make sure to get all essential parts (There are a lot)

def plot():
    code = str(input("Input eq(Use Python Notation, Use x as variable) y="))
    xLowerBound=int(input("Input Lower Bound: "))
    xUpperBound=int(input("Input Upper Bound: "))
    fil=int(input("Include Filter? 0 for no, 1 for yes: "))

    #if fil==0:
    #    filter="1"
    #else:
    #    filterFn=str(input("Input the function of the filter (Type 'HDPE' or 'ZOTEFOAM' for presets): "))
    #    if filterFn=="HDPE":
    #        filterFn="0.04871+(1.335e4*x)-(8.05e7*(x**2))+(2.138e11*(x**3))-(2.493e14*(x**4))+(1.036e17*(x**5))"
    #        filter=par.expr(filterFn).compile()
    #    if filterFn=="ZOTEFOAM":
    #        numLayers=int(input("How many layers are being used? (1, 6, 10 supported): "))        #Add dictionary of filters
    formula = par.expr(code).compile()
    #filter=par.expr(filter).compile()
    x=xLowerBound
    xarr=[]
    yarr=[]
    while x<xUpperBound:
        pt=eval(formula)*eval(filter)
        yarr.append(pt)
        xarr.append(x)
        x=x+0.1

    plt.plot(xarr,yarr)
    plt.show()


#This function can be called to see a blackbody curve and compare it to the curve after a filter has been applied, filtering out certain wavelengths
#Will ask for a second confirmation that you want to add a filter.
#Asks for a function of the curve. Presets for Zotefoam and HDPE have been added because I already worked with them.
def filter(temp):
    
    Etop=2*(6.63e-34)*((3e8)*(3e8))
    

    lower=float(input("Input Lower Wavelength in Meters: "))
    upper=float(input("Input Upper Wavelength in Meters: "))
    filter=int(input("Include Filter? 0 for no, 1 for yes: "))

    
    #Add dictionary of filters. As new filters are used, add their functions below so they can be repeatedly used easily.
    #Zotefoam required a lot of special rearranging of code because I could not figure out how to input an Inverse Exponent graph using Python notation and no special modules
    #If someone figures out, a lot of the code can be reworked so there aren't as many variables 
        
    
    yMax=0
    yFilter=0
    
    x=lower
    if filter==0:
        filterFn="1"
        filter=par.expr(filterFn).compile()

    else:
        filterFn=str(input("Input the function of the filter (Type 'HDPE' or 'ZOTEFOAM' for presets, otherwise ): "))
        if filterFn=="HDPE":
            filterFn="0.04871+(1.335e4*x)-(8.05e7*(x**2))+(2.138e11*(x**3))-(2.493e14*(x**4))+(1.036e17*(x**5))"
            filter=par.expr(filterFn).compile()
        if filterFn=="ZOTEFOAM":
            numLayers=int(input("How many layers are being used? (1, 4, 6, 10 supported): "))
        #If you can figure out how to input an inverse exponent function, if statements like the one below can be deleted

        if filterFn!="HDPE":
            if filterFn!="ZOTEFOAM":
                    filter=par.expr(filterFn).compile()

      

        
        #Add dictionary of filters

    yMax=0
    yFilter=0

    #Automatically calculates the maximum value of both the blackbody curve and the filtered curve.
    #This will be useful for when the Monte Carlo integration function is used later

    x=lower
    while x<upper:
        exponentTerm3=(6.63e-34*3.00e8)/((x*1.3805e-23)*temp)
        Ebot=math.pow(x,5)*(np.exp(exponentTerm3)-1)
        E=Etop/Ebot
        
        #Can be moved outside of the loop and reworked if you can input these equations using Python Notation and not np
        if filterFn=="ZOTEFOAM":

            if numLayers==10:
                
                fil=0.961*(1-np.exp(-4693*x))+0
                temp=167.5
            if numLayers==6:
                fil=0.97*(1-np.exp(-5600*x))
                temp=184
            if numLayers==1:
                fil=-1.297*(np.exp(-5900*x))+1.3
                temp=300
            if numLayers==4:
                fil=0.993*(np.exp(-6020*x))
                temp=198        
        if numLayers==10:
            if x>0.003:
                fil=1
        if numLayers==6:
            if x>0.001:
                fil=1
        if numLayers==1:
            if x>0.00066621:
                fil=1
        if numLayers==4:
            if x>0.00119917:
                fil=1
        
        if filterFn!="ZOTEFOAM":
            Efilter=E*eval(filter)
        else:
            Efilter=E*fil


        if E>yMax:
            yMax=E
        if Efilter>yFilter:
            yFilter=Efilter
        
        x=x+0.00000005
    #print(yMax)
    #print(yFilter)


    yTop=yFilter*1.2
    yTopUnfiltered=yMax*1.2


    #Uses Monte Carlo integration to integrate the curves of both the filtered and unfiltered curves. Outputs the ratio of the radiances.
    #
    xCoordIn=[]
    yCoordIn=[]
    xCoordOut=[]
    yCoordOut=[]
    xCoordInUnfiltered=[]
    yCoordInUnfiltered=[]
    xCoordOutUnfiltered=[]
    yCoordOutUnfiltered=[]
    i=0
    count=0

    #Integrates the filtered curve
    while i<1000000:
        x=random.uniform(lower, upper)
        yCoord=random.uniform(0,yTop)
        
        exponentTerm3=(6.63*math.pow(10,-34)*3.00*math.pow(10,8))/(x*1.3805*math.pow(10,-23)*temp)
        if filterFn!="ZOTEFOAM": 
            fil=eval(filter)
        if filterFn=="ZOTEFOAM":
            if numLayers==10:
                fil=0.961*(1-np.exp(-4693*x))+0
            if numLayers==6:
                fil=0.97*(1-np.exp(-5600*x))
            if numLayers==1:
                fil=-1.297*(np.exp(-5900*x))+1.3
            if numLayers==4:
                fil=0.993*(np.exp(-6020*x))
        if numLayers==10:
            if x>0.003:
                fil=1
        if numLayers==6:
            if x>0.001:
                fil=1
        if numLayers==1:
            if x>0.00066621:
                fil=1
        if numLayers==4:
            if x>0.00119917:
                fil=1
        Ebot=(x**5)*(np.exp(exponentTerm3)-1)
        functionValue=Etop/Ebot*fil
        i=i+1
    
        if yCoord<=functionValue:
            count=count+1

        
            xCoordIn.append(x)
            yCoordIn.append(yCoord)
        else:
            xCoordOut.append(x)
            yCoordOut.append(yCoord)
    ratio=count/i
    result=(upper-lower)*(yTop)*ratio
    #print(result)
    #plt.plot(xCoordIn,yCoordIn,'.',color='red')
    #plt.plot(xCoordOut,yCoordOut,'.', color='blue')
    #plt.show()
    count=0
    j=0

    #Integrates the unfiltered curve
    while j<1000000:
        #Generates two random numbers using the bounds determined above. The random numbers will be x and y coordinates
        xCoord=random.uniform(lower, upper)
        yCoord=random.uniform(0,yTopUnfiltered)
        
        
        exponentTerm3=(6.63*math.pow(10,-34)*3.00*math.pow(10,8))/(xCoord*1.3805*math.pow(10,-23)*temp)
        Ebot=(xCoord**5)*(np.exp(exponentTerm3)-1)
        
        functionValue=Etop/Ebot
        
        
        j=j+1
        #print(xCoord, yCoord, functionValue)
        
        #The if statement compares the x and y coordinates generated to the points on the function curve. If they are below the curve they will be "counted".
        if yCoord<=functionValue:
            count=count+1
            #print(xCoord, yCoord, functionValue)

            #print (count)
            #print (x)
            xCoordInUnfiltered.append(xCoord)
            yCoordInUnfiltered.append(yCoord)
        else:
            xCoordOutUnfiltered.append(xCoord)
            yCoordOutUnfiltered.append(yCoord)

        #Calculates how many "counts" have been counted relative to the total number of sets of coordinates generated. Then multiplies this ratio by the total area of integration to output the integrated value.
    
    ratio=count/j
    #print("Ratio: ", ratio)
    resultUnfiltered=(upper-lower)*(yTopUnfiltered)*ratio

    
    #print(resultUnfiltered)
    #plt.plot(xCoordInUnfiltered,yCoordInUnfiltered,'.', color='orange')
    #plt.plot(xCoordOutUnfiltered, yCoordOutUnfiltered,'.', color='blue')
    #plt.show()
    
    #print(result)
    #print(resultUnfiltered)
    #print(result/resultUnfiltered)
    return(result/resultUnfiltered)


#Main function. Meant to calculate the heat transfer from stage to stage of a cylindrical cryostat. Requires input of temperature, height, diameter, and aperture diameter
#Option to calculate the heat transfer with a filter attached
def calcHeatLoads():
    heights=[]
    cylDiameters=[]
    apDiameters=[]

    temps=[]
    while True:
        Temperature=float(input("Enter the temperature in Kelvin of next stage (Enter 0 if no more stages): "))
        if (Temperature==0):
            break
        temps.append(Temperature)

    r=0


    while r<len(temps):
        print(temps[r], ' K')
        height=int(input("Enter height of cylinder in this stage in inches: "))
        heights.append((height/39.37))
        diameter=int((input("Enter diameter of cylinder in this stage in inches:")))
        cylDiameters.append(diameter/39.37)
        apDiameter=int((input("Enter diameter of aperture in this stage in inches: ")))
        apDiameters.append(apDiameter/39.37)
        r=r+1
    

        




    print(len(temps))
    print(len(heights))
    print(len(cylDiameters))
    print(len(apDiameters))
    print(temps)
    print(heights)
    print(cylDiameters)
    print(apDiameters)

    m=1
    emissivities=[0.2]
    #Check this line. Assumes temp1 is 300K. If using a colder initial temperature, input the first stage at 300K, 
    # then set the second stage as the first you want to use. Disregard first heat transfer

    while m<len(temps):
        emissivity=(emissivities[m-1]*(temps[m]/temps[m-1]))
        emissivities.append(emissivity)
        m=m+1
    print(len(emissivities))
    print(emissivities)

    #integrate()

    #Calculates heat transfer between stages using all inputs given. See attached Excel spreadsheet for details on calculation

    d=0
    while d<len(heights)-1:
        outerStageDiameter=cylDiameters[d]
        outerStageHeight=heights[d]
        innerStageDiameter=cylDiameters[d+1]
        innerStageHeight=heights[d+1]

        outerApertureDiameter=apDiameters[d]
        innerApertureDiameter=apDiameters[d+1]
        SAaperture=(outerApertureDiameter/2)**2*3.14159
        Xout=(outerApertureDiameter/2)/(0.5/39.37)
        Xin=(innerApertureDiameter/2)/(0.5/39.37)
        Xfin=(1+((1+Xin**2)/Xout**2))
        F12Aperture=0.5*(Xfin-(Xfin**2-4*(Xin/Xout)**2)**0.5)
        Thot=temps[d]
        Tcool=temps[d+1]
        
        qAperture=5.67*10**-8*(Thot**4-Tcool**4)*(SAaperture)*F12Aperture
        #print("qAperture: ", qAperture)
        #print(Thot, " K")
        hasFilter=int(input("Would you like to add a filter? 1 for yes, 0 for no: "))

        if hasFilter==1:
            qApertureFiltered=qAperture*(filter(Thot))
            #print("qApertureFiltered: ", qApertureFiltered)


        F12Cylinder=(innerStageDiameter/2)/(outerStageDiameter/2)
        #print("F12 Cylinder: ", F12Cylinder)
        #print(innerStageDiameter)
        #print(outerStageDiameter)
        SAcylinderOut=3.14159*(outerStageDiameter)*outerStageHeight+3.14159*(outerStageDiameter/2)**2
        #print("Surface Area: ", SAcylinderOut)
        SAcylinderIn=3.14159*(innerStageDiameter)*innerStageHeight+3.14159*(innerStageDiameter/2)**2
        #print ("Surface Area Cylinder in: ", SAcylinderIn)
        Ecool=emissivities[d+1]
        Ehot=emissivities[d]
        qCylinder=((5.67*10**-8)*SAcylinderOut*(Thot**4-Tcool**4))*F12Cylinder/((1/Ecool)+((SAcylinderIn/SAcylinderOut)*((1/Ehot)-1)))
        #print("qCylinder " , qCylinder)

        OuterDiskOuterRadius=outerStageDiameter/2
        OuterDiskInnerRadius=outerApertureDiameter/2
        InnerDiskOuterRadius=innerStageDiameter/2
        InnerDiskInnerRadius=innerApertureDiameter/2

        SAdiskOuter=3.14159*OuterDiskOuterRadius**2-3.14159*OuterDiskInnerRadius**2
        SAdiskInner=3.14159*InnerDiskOuterRadius**2-3.14159*InnerDiskInnerRadius**2
        #print(SAdiskOuter)
        dis=0.5/39.37

        H=dis/InnerDiskInnerRadius
        R2=InnerDiskOuterRadius/InnerDiskInnerRadius
        R3=OuterDiskInnerRadius/InnerDiskInnerRadius
        R4=OuterDiskOuterRadius/InnerDiskInnerRadius
        #print(H)
        #print(R2)
        #print(R3)
        #print(R4)

        F12Disk=(1/(2*(R2**2-1)))*(((R2**2+R3**2+H**2)**2-(2*R3*R2)**2)**0.5-((R2**2+R4**2+H**2)**2-(2*R2*R4)**2)**0.5+((1+R4**2+H**2)**2-(2*R4)**2)**0.5-((1+R3**2+H**2)**2-(2*R3)**2)**0.5)

        #print("F12Disk: ", F12Disk)


        F21Disk=(SAdiskInner/SAdiskOuter)*F12Disk
        #print(F21Disk)
        qDiskpre=5.67*10**-8*(Thot**4-Tcool**4)*SAdiskOuter*F21Disk
        #print(qDiskpre)
        #print(SAdiskOuter)
        #print(SAdiskInner)
        qDisk=qDiskpre*(Ehot*(SAdiskOuter/(SAdiskOuter+SAdiskInner))+Ecool*(SAdiskInner/(SAdiskOuter+SAdiskInner)))/2
        #print("qDisk: ", qDisk)
        if hasFilter==1:
            qFinal=qApertureFiltered+qDisk+qCylinder
        else:
            qFinal=qDisk+qAperture+qCylinder
        print("Heat Transfer in Watts from Layer to Layer: ",qFinal)

        d=d+1

#Simple integration function for any basic curve
def integrate():
    #xUpperBound=(3.00*math.pow(10,8))/(1.25*(10**11))
    #xLowerBound=(3.00*math.pow(10,8))/(1.65*(10**11))

    code = str(input("Input eq(Use Python Notation, Use x as variable) y="))
    #Etop=2*(6.63e-34)*((3e8)*(3e8))
    

    lower=float(input("Input Lower X Bound: "))
    upper=float(input("Input Upper X Bound: "))
    #filter=int(input("Include Filter? 0 for no, 1 for yes: "))
    formula=par.expr(code).compile()

    
        #Add dictionary of filters
        
    
    yMax=0
    #yFilter=0
    
    x=lower
    
      

        
        #Add dictionary of filters
    x=lower
    while x<upper:
        #j=i*math.pow(10,6)
        if eval(formula)>yMax:
            yMax=eval(formula)
        x=x+1
        
        x=x+0.00000005
    #print(yMax)


    yTop=yMax*1.8

    xCoordIn=[]
    yCoordIn=[]
    xCoordOut=[]
    yCoordOut=[]
    
    i=0
    count=0

    while i<100000000:
        x=random.uniform(lower, upper)
        yCoord=random.uniform(0,yTop)
        if yCoord<=eval(formula):
            count=count+1
            xCoordIn.append(x)
            yCoordIn.append(yCoord)
        else:
            xCoordOut.append(x)
            yCoordOut.append(yCoord)
        i=i+1
    ratio=count/i
    result=(upper-lower)*(yTop)*ratio
    print(result)
    plt.plot(xCoordIn,yCoordIn,'.',color='red')
    plt.plot(xCoordOut,yCoordOut,'.', color='blue')
    plt.show()
    
question=int(input("Hi! What would you like to do? 1 for calculate the heat load of a cryostat, 2 for plot a function, 3 for integrate a function, 4 for compare a black body curve to a filtered curve "))

if question==1:
    calcHeatLoads()
if question==2: 
    plot()
if question==3:
    integrate()
if question==4:
    t=int(input("What is the temperature you want to graph the curve at?: "))
    filter(t)
#plot()
#integrate(300)
#calcHeatLoads()
#integrate()