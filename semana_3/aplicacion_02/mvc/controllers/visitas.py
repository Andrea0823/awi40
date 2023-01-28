import web
from datetime import datetime


class Visitas:
    def GET(self, nombre):
        try:
            cookie = web.cookies()
            visitas = "0"
            print(cookie)
            now = datetime.now()
            print(now)
            hora = datetime.today().strftime('%H:%M')
            
            if nombre:
                web.setcookie("nombre", nombre,expires="",domain=None)
            else:
                nombre = "Anonimo"
                web.setcookie("nombre", nombre,expires="",domain=None)

            if cookie.get("visitas"):
                visitas= int(cookie.get("visitas"))
                visitas += 1
                web.setcookie("visitas",str(visitas),expires="", domain=None)
            else:
                web.setcookie("visitas", str(1), expires="", domain=None)
                visitas = "1"
                web.setcookie("fecha",str(now),expires="", domain=None)
                web.setcookie("fecha",str(now),expires="", domain=None)
                web.setcookie("hora",hora,expires="", domain=None)
                web.setcookie("hora",hora,expires="", domain=None)
            
            return "Visitas: " + str(visitas) + " Nombre: " + nombre + " fecha: " + str(now) + " hora: " + hora
        except Exception as e:
            return "Error" + str(e.args)