import json


print("***********************")
print("*     MUNDO LIBRO     *")
print("***********************")

{       [1] - 'Mantenedor de Usuarios'
        [2] - 'Reportes'
        [3] - 'Salir'
        }





bibloteca = {
    "Ficcion": 1,
    "Realismo Magico": 0,
    "Poesia": 10,
    "Ciencia Ficcion": 5

}

print("******************************")
print("*     MANTENEDOR USUARIO     *")
print("******************************")

{       [1] - 'Agregar Usuario'
        [2] - 'Editar Usuario'
        [3] - 'Eliminar Usuario'
        [4] - 'Buscar usuario'
        [5] - 'Volver'
        }
       

with open('archivo.json', 'w') as archivo:
    json.dump(bibloteca, archivo)
