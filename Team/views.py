from django.shortcuts import render, redirect
from django.http import HttpResponse
from Team.models import Desarrolladore
from django.db.models import Q


# Create your views here.
def otro(request):
    return render(request,"formTeam.html")
    

def team(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            cantidad=[]
            for i in range(6):
                #compruebo que no venga vacio
                if request.POST["cant%s"%(i+1)]:
                    #cantidad.append([int(request.POST["cant%s"%(i+1)]),request.POST["area%s"%(i+1)],request.POST["leng%s"%(i+1)] ])
                    print(request.POST["leng%s"%(i+1)].split(","))
                    area=request.POST["area%s"%(i+1)]
                    print(area)
                    lenguajes=request.POST["leng%s"%(i+1)].split(",")
                    consulta = Q()
                    for lenguaje in lenguajes:
                        consulta|= Q(lenguajes__icontains=lenguaje)
                    desarrollador=Desarrolladore.objects.filter(consulta,rating__gte=10,area__icontains=area).order_by("-rating")[0:int(request.POST["cant%s"%(i+1)])]
                    cantidad.append([desarrollador])
                    for dev in desarrollador:
                        print(dev.nombre)
                        print(dev.lenguajes)
                    
                else:
                    cantidad.append(0)
            
            if len(cantidad)!=0:
                print(cantidad)
                return render(request,"teamArmado.html",{"cant":cantidad})
            else:
                return HttpResponse("no hizo ninguna busqueda")
        return render(request,"formTeam.html")
    else :
        return redirect('/login')



#Updateo de datos
# 
# p=Desarrolladore.objects.get(nombre="Javier Vassallo")
#p.nombre="Jose Oscar"
#p.save()
#
#Para hacer una busqueda que me devuelve varias filas
#
#desarrollador=Desarrolladore.objects.filter(email="jev.vassallo@gmail.com")
#In [18]: desarrollador[0].nombre
#Out[18]: 'Javier Vassallo'
#desarrollador=Desarrolladore.objects.filter(lenguajes__icontains="Java")
#
#Lo siguiente es un order by, descendiente, con el menos delante de la columna que se va a ordenar
# desarrollador=Desarrolladore.objects.filter(lenguajes__icontains="Java").order_by("-rating")
#Dos filtros, y mayor que, __gte mayor que __lte menor que
#
#desarrollador=Desarrolladore.objects.filter(lenguajes__icontains="Java",rating__gte=15).order_by("-rating")
#{% with ''|center:cantidad as range %}  esto es para hacer un for en rango pasando un numero entero como valor, por ejemplo cantidad = 5
#{% for i in range %}
#    {{ forloop.counter }}
#{% endfor %}
#{% endwith %}
#