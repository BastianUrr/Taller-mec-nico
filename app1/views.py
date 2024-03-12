from django.shortcuts import render

from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required





def vista(request):
    return render(request, 'extras/index.html')

def principal (request):
    return render(request,'extras/principal.html')

def contacto (request):
    return render(request,'contacto.html')

def registro (request):
    return render(request,'registro.html')

def limpiezaMotor (request):
    return render(request,'limpiezaMotor.html')

def cambioPastillas (request):
    return render(request,'cambioPastillas.html')

def cambioAceite (request):
    return render(request,'cambioAceite.html')

def aliniamiento (request):
    return render(request,'aliniamiento.html')








def poblarBaseDatos (request):
    User.objects.create_user(username='root', first_name='root', password='root', is_superuser=True, is_staff=True)
    User.objects.create_user(username='Pedro', first_name='Pedro', password='Pedropedro', is_staff=True)
    User.objects.create_user(username='Juan', first_name='Juan', password='Juanjuan', is_staff=True)
    User.objects.create_user(username='Diego', first_name='Diego', password='Diegodiego', is_staff=True)

    User.objects.create_user(username='Usuario', first_name='Usuario', password='Usuariousuario')
    # Material.objects.create(
    #     id = 1,
    #     nombre = 'Caucho'
    # )

    # Material.save()

    # Material.objects.create(
    #     id = 2,
    #     nombre = 'Acero'
    # )

    # Material.objects.create(
    #     nombre = ''
    # )

    # Material.save()

    return render(request,'extras/poblarBaseDatos.html')

def guardado(request):
    nom = request.POST["InNom"]
    ape = request.POST["InApe"]
    corr = request.POST["InCorr"]
    con = request.POST["InCon"]
    User.objects.create_user(username=corr, password=con, first_name = nom, last_name = ape, email=corr)

    return render(request, 'guardado.html')

@login_required
def formTrabajo(request):
    if request.user.is_staff:
        diag = Diagnostico.objects.all()
        mate = Material.objects.all()
        cate = Categoria.objects.all()

        dic = {
            'diag' : diag,
            'mate' : mate,
            'cate' : cate
        }
        return render(request, 'form_trabajo.html', dic)

def base(request):
    return render(request, 'base.html')

def extension(request):
    return render(request, 'extras/extension.html')

from django.core.files.storage import FileSystemStorage

@login_required
def guardado2(request):
    # El formulario de guardado se envía a esta funcion!!
    if request.user.is_staff:
        titulo = request.POST["titulo"]
        fecha = request.POST["fecha"]
        desc = request.POST["desc"]
        cate = request.POST["categoria"]
        diag = request.POST["diagnostico"]
        mate = request.POST["listaMateriales"]
        foto = request.FILES["foto"]

        objCliente = User.objects.get(id = request.user.id)
        objCate = Categoria.objects.get(id = cate)
        objDiag = Diagnostico.objects.get(id = diag)
        objTrabajo = Trabajo.objects.create(
            fecha = fecha,
            publicado = False,
            titulo = titulo,
            descripcion = desc,
            nombre_foto ='',
            id_categoria = objCate,
            id_diagnostico = objDiag,
            cliente = objCliente
        )
        objTrabajo.save()
        
        print("----> tipo...")
        print(foto.content_type)
        ext = foto.content_type.split(sep='/')[1]
        print(ext)
        nombre = str(objTrabajo.pk) + "." + ext
        print("-----> Nombre: ", nombre)
        fs = FileSystemStorage()
        filename = fs.save(nombre, foto)
        ruta = fs.url(filename)
        print("(---> ruta...")
        print(ruta)

        objTrabajo.nombre_foto = nombre
        objTrabajo.save()

        mate = mate.split(sep=',')
        mate.pop()
        
        for i in mate:
            objMate = Material.objects.get(id = i)
            Material_trabajo.objects.create(
                id_material = objMate,
                id_trabajo = objTrabajo
            )

        return render(request, 'guardado2.html')

def index(request):
    sql1 = 'select * from auth_user where is_superuser = false and is_staff = true;'

    objMeca = User.objects.raw(sql1)
    print('----> Mecanicos: ' + str( objMeca))
    print(objMeca)
    dicc = {
        'meca' : objMeca
    }
    return render(request, 'index.html', dicc)

def cate(request, cate):
    sql1 = 'select tra.idTrabajo, tra.fecha, tra.titulo, mec.first_name '
    sql2 = 'from app1_trabajo tra join auth_user mec on (tra.cliente_id = mec.id)'
    sql3 = 'where tra.idCategoria = ' + cate + ';'
    sql1 = sql1 + sql2 + sql3

    sqlCate = 'select * from app1_categoria where idCategoria = ' + cate + ';'
    objCate = Categoria.objects.raw(sqlCate)
    print('---> La categoria es ' + objCate[0].nombre)

    obj = Trabajo.objects.raw(sql1)
    dicc = {
        'data' : obj,
        'cate' : objCate[0].nombre
    }
    return render(request, 'categoria.html', dicc)

def trabajo(request, pk):
    sql1 = 'select * from app1_trabajo tra join auth_user mec on (tra.cliente_id = mec.id) '
    sql2 = 'where idTrabajo = ' + pk + ';'
    sql1 = sql1 + sql2

    objTrabajo = Trabajo.objects.raw(sql1)

    sql1 = 'select * from app1_material_trabajo where idTrabajo = ' + pk + ';'
    objMateriales = Material_trabajo.objects.raw(sql1)
    dicc = {
        'data': objTrabajo[0],
        'diag' : objTrabajo[0].id_diagnostico,
        'mate': objMateriales
    }
    return render(request, 'trabajo.html', dicc)

def mecanico(request, pk):
    sql1 = 'select idTrabajo, fecha, titulo from app1_trabajo '
    sql2 = 'where cliente_id = ' + pk + ';'
    sql1 = sql1 + sql2
    objtrabajo = Trabajo.objects.raw(sql1)

    sql1 = 'select id, first_name from auth_user where id = ' + pk + ';'
    objMecanico = User.objects.raw(sql1)

    total = len(objtrabajo)

    dicc = {
        'data' : objtrabajo,
        'meca2' : objMecanico[0],
        'total' : total
    }
    return render(request, 'mecanico.html', dicc)

def guardado3(request):
    email = request.POST["email"]
    msg = request.POST["mensaje"]

    objContacto = Contacto.objects.create(
        email = email,
        texto = msg
    )

    objContacto.save()
    return render(request, 'guardado3.html')










from .forms import *

def experimento1(request):
    
    form = CountryForm

    # return render_to_response('extras/experimento1.html', {'form': form},
    #                           context_instance=RequestContext(request))

    return render(request, 'extras/experimento1.html', {'form': form})
    
def guardadoXX(request):
    sel = request.POST["select"]
    print('---> Lo que llegó...')
    print(sel)
    
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            countries = form.cleaned_data.get('countries')

            print('---> Variable...')
            print(countries)
            # do something with your results

    return render(request, 'extras/guardado3.html')


