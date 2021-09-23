import sqlite3



def ingresarNombre():
     print("hola")
     #nombre = input()
     #print("bienvenido", nombre)




def newEmployee(nameEmp,payEmp):
    cur.execute("INSERT INTO employees VALUES (:name,:pay)", {'name':nameEmp, 'pay':payEmp})
    con.commit()



con = sqlite3.connect('ejemplopy.db')
cur = con.cursor()
#cur.execute("DROP TABLE employees")
#cur.execute("""CREATE TABLE employees (
#                name TEXT,
#                pay INTEGER)
#                """)
con.commit()


print("Bienvenido, ingrese una opcion:")
print("1.Crear empleado")
print("2.Listar empleados")
print("3.Borrar empleado")
print("4.Salir")
opt = input()

if(opt == "1"):
    print("ingrese el nombre")
    name = input()
    print("ingrese el salario")
    pay = input()
    newEmployee(name,pay)
elif(opt == "2"):
    cur.execute("SELECT * FROM employees")
    con.commit()
    print(cur.fetchall())
elif(opt == "3"):
    print("Ingrese el id del empleado a eliminar:")
    idToDelete = input()
    cur.execute("DROP * FROM employees WHERE id = idToDelete")
    con.commit()
elif(opt == "4"):
    cur.execute("DROP TABLE employee")
    con.commit()
else:
    print("error")

#cur.execute("DROP TABLE employees")
con.commit()



con.close()
#ingresarNombre()