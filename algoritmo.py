galones = float(input("cantidad"))
galon_litro=3.78
precio=20
litros=galon_litro*galones
total=litros*precio_litro
print("total a pagar:",total)


#coordenada
x1=float(input("x1"))
x2=float(input("y1"))
y1=float(input("x2"))
y2=float(input("y2"))
distancia=((x1-x2)**2+(y1-y2)**2)**(1/2)
print ("la distancia es",distancia)


#bar
hora_e=int(input("hora entrada"))
min_e=int(input("minutos entrada"))
hora_s=int(input("hora salida"))
min_s=int(input("minuto salida"))
min_totales=(hora_s-hota_e)*60+min_s-min_e
hora_completa=min_totales//60
min_sub=min_totales%60
total_pagar=hora_completa*50+min_sub*1.5
print("tiempo a pagar",tiempo_a_pagar)



N=int(input("numero de cajas"))
area=ancho_base*largo_base+ancho_base*altura*2+largo_base*altura*2+ancho_base*altura_sup*2+largo_base*altura_tr
precio=0.5
tatal_pagar=area*precio*N
print("total",total_pagar)



#condicionales
boletos=int(input("Boleto"))
precio=350
total=precio*boletos
if boletos >10:
    total=total*0.9
elif boletos >=5:
    total=total*0.95

#2
b_m=int(input("Boleto menores"))
b_M=int(input("Boleto mayores"))
n_b=b_m+b_M
precio_m=250
precio_M=350
pago_m=precio_m*b_m
if b_m>=5:
    pago_m*=0.9
pago_M=precio_M*b_M
total=pago_M+pago_m
if n_b>=10:
    total*=0.9
elif n_b>=5:
    total*=0.95
print (f"boletos menores: {b_m}"
f"subtotal= {pago_m}\n"
f"boleto mayores: {b_M}"
f"subtotal mayores= {pago_M}"
f"total= {total}\n"
f"total+iva= {total_iva}")