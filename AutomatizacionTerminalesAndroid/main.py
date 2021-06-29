import json

a = open("pagina_principal.json", "r")
b = a.read()
pantallaPrincipal = json.loads(b)

a = open("pantalla_cuotas.json", "r")
b = a.read()
pantallaCuotas = json.loads(b)

print(pantallaPrincipal["btn_numerico_nueve"]["value_id"])
print(pantallaCuotas["btn_aceptar"]["value_id"])