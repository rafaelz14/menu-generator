from random import randrange
import pandas as pd

desayunos = [{

    'nombre': 'huevos con champi y jamon',
    'ingredientes': ['huevos', 'champis', 'jamon iberico'],
    'carb': False

},
    {
    'nombre': 'huevos con cebolla calabacin y jamon',
    'ingredientes': ['huevos', 'cebolla', 'calabacin', 'jamon'],
    'carb': False
},
    {

    'nombre': 'huevos con tomates asados',
    'ingredientes': ['huevos', 'tomates', 'queso feta'],
    'carb': False

},
    {

    'nombre': 'avenita',
    'ingredientes': ['avena', 'leche', 'canela', 'mantequilla de mani', 'frutas'],
    'carb': True

},

    {

    'nombre': 'panquecas de proteina',
    'ingredientes': ['avena', 'huevos', 'platano', 'chia'],
    'carb': True

},

    {

    'nombre': 'tosta de aguacate',
    'ingredientes': ['pan', 'aguacate', 'sesamo'],
    'carb': True

},

    {

    'nombre': 'huevos revueltos con pimenton asado',
    'ingredientes': ['huevos', 'pimenton rojo', 'jamon iberico'],
    'carb': False

},

    {

    'nombre': 'lomo adobado con vegetales',
    'ingredientes': ['lomo', 'champis', 'tomate'],
    'carb': False

},

    {

    'nombre': 'arepa de verduras',
    'ingredientes': ['harina pan', 'zanahoria'],
    'carb': True

},
    {

    'nombre': 'huevos con puerro',
    'ingredientes': ['huevos', 'puerro', 'jamon'],
    'carb': False

},
    {
    'nombre': 'parfait',
    'ingredientes': ['yogur', 'avena', 'almendras', 'frutas'],
    'carb': True

},
    {
    'nombre': 'fritatta de salmon',
    'ingredientes': ['huevos', 'salmon', 'puerro'],
    'carb': False

},

]
almuerzos = [{

    'nombre': 'ensalada de pollo',
    'ingredientes': ['verdes', 'manzana', 'pollo', 'almendras', 'queso brie'],
    'carb': False

},
    {
    'nombre': 'ensalada de pescado',
    'ingredientes': ['verdes', 'tomate', 'pescado', 'mostaza dijon', 'pepino'],
    'carb': False
},
    {

    'nombre': 'ensalada de camarones',
    'ingredientes': ['camarones congelados', 'verdes', 'pimenton', 'naranja', 'frutos rojos'],
    'carb': False

},
    {

    'nombre': 'ensalada de lentejas',
    'ingredientes': ['verdes', 'lentejas', 'aceitunas negras', 'pimenton', 'queso feta'],
    'carb': True

},

    {

    'nombre': 'ensalada fresca de huevo',
    'ingredientes': ['verdes', 'huevo hervido', 'jamon iberico', 'tomate', 'pepino'],
    'carb': False

},

    {

    'nombre': 'ensalada de garbanzo',
    'ingredientes': ['verdes', 'garbanzo', 'jamon iberico', 'tomate', 'pepino'],
    'carb': True

},
    {
    'nombre': 'ensalada de pollo a la parrilla',
    'ingredientes': ['verdes', 'pollo', 'tomates', 'aguacate', 'cebolla'],
    'carb': False
},

    {

    'nombre': 'hamburguesa',
    'ingredientes': ['carne picada', 'verdes', 'tomate', 'queso', 'pepinillos'],
    'carb': False

},

    {

    'nombre': 'pollo al horno con veggies',
    'ingredientes': ['muslo de pollo deshuesado', 'cebolla', 'tomate', 'calabacin', 'pimenton'],
    'carb': False

},

    {

    'nombre': 'pasta integral',
    'ingredientes': ['carne picada', 'cebolla', 'lata de tomate', 'pimenton', 'puerro', 'pasta integral'],
    'carb': True

},
    {

    'nombre': 'bistec a la pobre',
    'ingredientes': ['filetes de res', 'cebolla', 'tomate'],
    'carb': False

},

    {
    'nombre': 'lasagna de berenjena',
    'ingredientes': ['berenjena', 'tomate', 'ajo', 'cebollas', 'mozarella'],
    'carb': False

}

]
cenas = [
    
    {
    
    'nombre' : 'lomo con vegetales',
    'ingredientes' : ['lomo de cerdo', 'cebolla', 'tomate','pimenton'],
    'carb' : False
    
},
   {
       'nombre' : 'camarones creole',
       'ingredientes': ['camarones', 'cebolla', 'pimenton', 'leche de coco','curcuma','curry','pimenton de la vera','comino'],
       'carb' : False
   },
   {
    
    'nombre' : 'wok de pollo',
    'ingredientes' : ['pechuga de pollo', 'cebolla', 'pimenton','jenjibre','salsa de soja'],
    'carb' : False
    
},
   {
    
    'nombre' : 'risotto de setas',
    'ingredientes' : ['arroz', 'caldo de pollo', 'setas'],
    'carb' : True
    
},

   {
    
    'nombre' : 'trucha con esparragos',
    'ingredientes' : ['trucha', 'esparragos'],
    'carb' : False
    
},

   {
       'nombre' : 'ensalada de pescado',
       'ingredientes': ['verdes', 'tomate', 'pescado', 'mostaza dijon','pepino'],
       'carb' : False
},
    
    {
    'nombre' : 'plato italiano',
    'ingredientes' : ['jamon iberico', 'aceitunas', 'pepinillos','quesos','almendras'],
    'carb' : False 
},

   {
    
    'nombre' : 'chile de carne',
    'ingredientes' : ['carne picada', 'cebolla', 'tomate','pimenton','alubias rojas'],
    'carb' : False
    
},

   {
    
    'nombre' : 'taco destruido',
    'ingredientes' : ['alubias rojas', 'cebolla', 'tomate','pimenton'],
    'carb' : False
    
},

   {
    
    'nombre' : 'lomo de cerdo con queso y ensalada',
    'ingredientes' : ['lomo', 'queso','verdes','tomate','pepinillo'],
    'carb' : False
    
},

    {
    'nombre' : 'calabacines rellenos',
    'ingredientes' : ['calabacin', 'cebolla','queso','tomate','crema de leche'],
    'carb' : False
    
},

    {
    'nombre' : 'sopa de lentejas',
    'ingredientes' : ['lentejas', 'cebolla','pimenton'],
    'carb' : True
    
},
    
]
# to generate main menu
menu = [
    {
        'desayuno': desayunos[(randrange(0, (len(desayunos))))],
        'almuerzo': almuerzos[(randrange(0, (len(almuerzos))))],
        'cena': cenas[(randrange(0, (len(cenas))))]
    },
    {
        'desayuno': desayunos[(randrange(0, (len(desayunos))))],
        'almuerzo': almuerzos[(randrange(0, (len(almuerzos))))],
        'cena': cenas[(randrange(0, (len(cenas))))]
    },
    {
        'desayuno': desayunos[(randrange(0, (len(desayunos))))],
        'almuerzo': almuerzos[(randrange(0, (len(almuerzos))))],
        'cena': cenas[(randrange(0, (len(cenas))))]
    },
    {
        'desayuno': desayunos[(randrange(0, (len(desayunos))))],
        'almuerzo': almuerzos[(randrange(0, (len(almuerzos))))],
        'cena': cenas[(randrange(0, (len(cenas))))]
    },
    {
        'desayuno': desayunos[(randrange(0, (len(desayunos))))],
        'almuerzo': almuerzos[(randrange(0, (len(almuerzos))))],
        'cena': cenas[(randrange(0, (len(cenas))))]
    },
    {
        'desayuno': desayunos[(randrange(0, (len(desayunos))))],
        'almuerzo': almuerzos[(randrange(0, (len(almuerzos))))],
        'cena': cenas[(randrange(0, (len(cenas))))]
    }]
# to get list of all meals and compare
desayunos_list = []
almuerzos_list = []
cenas_list =[]

for comida in range (0,len(menu)):
    desayunos_list.append(menu[comida].get('desayuno').get('nombre'))
    almuerzos_list.append(menu[comida].get('almuerzo').get('nombre'))
    cenas_list.append(menu[comida].get('cena').get('nombre'))


def find_repeated(test_list):
    oc_set = set()
    res = []
    for idx, val in enumerate(test_list):
        if val not in oc_set:
            oc_set.add(val)
        else:
            res.append(idx)
    return (res)


to_replace = find_repeated(desayunos_list)
while len(to_replace)>0:
    for repeated in to_replace:
        menu[repeated]['desayuno'] = desayunos[(randrange(0,(len(desayunos))))]
        desayunos_list =[]
        for comida in range (0,len(menu)):
            desayunos_list.append(menu[comida].get('desayuno').get('nombre'))
    to_replace = find_repeated(desayunos_list)
    

to_replace = find_repeated(almuerzos_list)
while len(to_replace)>0:
    for repeated in to_replace:
        menu[repeated]['almuerzo'] = almuerzos[(randrange(0,(len(almuerzos))))]
        almuerzos_list =[]
        for comida in range (0,len(menu)):
            almuerzos_list.append(menu[comida].get('almuerzo').get('nombre'))
    to_replace = find_repeated(almuerzos_list)
    

to_replace = find_repeated(cenas_list)
while len(to_replace)>0:
    for repeated in to_replace:
        menu[repeated]['cena'] = cenas[(randrange(0,(len(cenas))))]
        cenas_list =[]
        for comida in range (0,len(menu)):
            cenas_list.append(menu[comida].get('cena').get('nombre'))
    to_replace = find_repeated(cenas_list)
        
menu_lunes = [desayunos_list[0],almuerzos_list[0],cenas_list[0]]
menu_martes = [desayunos_list[1],almuerzos_list[1],cenas_list[1]]
menu_miercoles = [desayunos_list[2],almuerzos_list[2],cenas_list[2]]
menu_jueves = [desayunos_list[3],almuerzos_list[3],cenas_list[3]]
menu_viernes = [desayunos_list[4],almuerzos_list[4],cenas_list[4]]
menu_sabado = [desayunos_list[5],almuerzos_list[5],cenas_list[5]]

fullmenu = [menu_lunes, menu_martes, menu_miercoles, menu_jueves, menu_viernes, menu_sabado]

df = pd.DataFrame(data=fullmenu)
df = df.T
df.rename(columns={0: "Lunes", 1: "Martes", 2: "Miercoles", 3: "Jueves", 4: "Viernes", 5: "Sabado"}, inplace = True)
df.rename(index={0: "Desayuno", 1: "Almuerzo", 2: "Cena"}, inplace = True)
df.to_csv('menu.csv')

