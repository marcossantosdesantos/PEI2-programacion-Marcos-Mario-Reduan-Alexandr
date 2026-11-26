import numpy as np 


# 1. Matriz de acoplamiento del acelerometro 3D y voltajes medidos (mV)
M_calib = np . array ([[1.05 ,0.02 , -0.01] , [0.01 ,0.98 ,0.03] , [ -0.02 ,0.01 ,1.02]])
V_medido = np . array ([15.2 , -4.5 , 98.1])

# 2. Ensayos en tunel de viento : Presion dinamica (Pa) y Fuerza Drag (N)
q_tunel = np . array ([500 , 1000 , 1500 , 2000 , 2500 , 3000])
F_drag_tunel = np . array ([12.1 , 25.3 , 37.8 , 51.0 , 62.5 , 76.2])

# 3. Atmosfera Estandar (ISA): Altitud (m) y Densidad (kg/m^3)
altitudes_isa = np . array ([0 , 500 , 1000 , 1500 , 2000 , 2500])
densidades_isa = np . array ([1.225 , 1.167 , 1.112 , 1.058 , 1.007 , 0.957])

# 4. Telemetria del Radar : Tiempo (s), Posicion X (m) y Posicion Y (m)
t_tel = np . linspace (0 , 8 , 17)
x_tel = np . array([0 ,48 ,93 ,137 ,178 ,218 ,256 ,292 ,326 ,359 ,390 ,419 ,448 ,474 ,500 ,524 ,547])
y_tel = np . array([0 ,85 ,160 ,225 ,280 ,325 ,360 ,385 ,400 ,405 ,400 ,385 ,360 ,325 ,280 ,225 ,160])


a = np.linalg.solve (M_calib, V_medido)
print (a)