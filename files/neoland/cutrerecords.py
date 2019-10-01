from tabulate import tabulate
import sqlite3
conn=sqlite3.connect('albums3.db')
#conn=sqlite3.connect(':memory:')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS albums(
            name text,
            band text,
            year integer)""")

class Album:
    def __init__(self,name,band,year):
        self.name = name
        self.band = band
        self.year = year
        
def insert_album(album):
    c.execute("INSERT INTO albums VALUES (:name,:band,:year)",
              {'name':album.name,'band':album.band,'year':album.year})
        
def get_all_albums():
    c.execute("SELECT * FROM albums")
    return c.fetchall()
        
def get_albums_by_band(band):
    c.execute("SELECT * FROM albums WHERE band=:band", {'band':band})
    return c.fetchall()

def get_albums_by_year(year):
    c.execute("SELECT * FROM albums WHERE year=:year", {'year':year})
    return c.fetchall()

while True:
    print("\n \n \n")
    print("--------------- C U T R E -------R E C O R D S-----------------")
    print(""" MENÚ:
        1. Introduce un nuevo álbum.
        2. Consulta todos los álbumes.
        3. Consulta álbumes por banda.
        4. Consulta álbumes por año.
        
        X. Salir del programa.
    """)
    opcion = input('Selecciona una opción: ')
    if opcion == 'X':
        print("Fuck you")
        break
    elif opcion == '1':
        titulo = input('Título del álbum: ')
        banda =  input('Nombre de la banda: ')
        año = input('Año: ')
        album = Album(titulo, banda, año)
        insert_album(album)
    elif opcion == '2':
        albums = get_all_albums()
        print("\n \n \n")
        print(tabulate(albums,headers=['Título','Grupo', 'Año']))
        input('Pulsa ENTER para continuar')
    elif opcion == '3':
        banda = input('Introduce banda: ')
        albums = get_albums_by_band(banda)
        print("\n \n \n")
        print(tabulate(albums,headers=['Título','Grupo', 'Año']))
        input('Pulsa ENTER para continuar')
    elif opcion == '4':
        año = input('Introduce año: ')
        albums = get_albums_by_year(año)
        print("\n \n \n")
        print(tabulate(albums,headers=['Título','Grupo', 'Año']))
        input('Pulsa ENTER para continuar')
    else:
        print('Opción incorrecta')
        input('Pulsa ENTER para continuar')
        
conn.commit()
conn.close()