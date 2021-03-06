#Подключение необходимых для программы библиотек
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as anim
#from scipy.integrate import odeint

#Константы
#G = 6.67*10**(-11)   #Гравитационная постоянная
#M1 = 5.974*10**24    #Масса первого гравитирующего объекта
#M2 = 7.348*10**22    #Масса второго гравитирующего объекта
#m = 2.7*10**10       #Масса астероида (что соответствует астероиду Апофис)

def grafics(L1,E1,L2,E2):
    
    x1 = L1
    y1 = E1
    
    x2 = L2
    y2 = E2

    plt.plot(x1,y1,color='red', label='d=10000 км')
    plt.plot(x2,y2,color='blue', label='d=50000 км')
    
#    plt.subplots(figsize=(8,4))
    plt.xlabel('Расстояние до места подрыва')                      #Подпись оси Ох
    plt.ylabel('Мощность ядерного взрыва')                         #Подпись оси Оу
    plt.grid()
    plt.legend()
    plt.xlim(0, 2.1*10**8)
    plt.ylim(0, 11000)
    
L1 = [10**7, 5*10**7, 10**8, 2*10**8]
E1 = [2100, 420, 210, 105]
L2 = [10**7, 5*10**7, 10**8, 2*10**8]
E2 = [10500, 2110, 520, 210]

grafics(L1,E1,L2,E2)