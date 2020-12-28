
c = 9.0e+16
# Speed of light squared

to = 3600

vo = float(input("Enter the velocity of moving object relative to you(m/s):"))


vf = vo**2

ratio_to_c= vf/c


print(vo/3.0e+8)

#gamm factor
gamma =  1/((1 - ratio_to_c) ** (0.5))

if gamma==12.257667696681581:
    print('gamma factor is:',12)

else:
         print ("gamma is: ")
         print(abs(gamma))


#gamma is used to control the  relative clock speed

