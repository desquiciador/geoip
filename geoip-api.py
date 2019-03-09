import requests
import json
#url de la api
apiurl='http://ip-api.com/json/'
#parametros a obtener
parametros='city,country,countryCode,isp,org,regionName,lat,lon,timezone,zip'
data={'fields':parametros}
def ip_scrap(ip=''):
    #conectamos con la api
    res=requests.get(apiurl+ip, data=data)
    #obtenemos y procesamos la respuesta json
    apires=json.loads(res.content)
    return apires
if __name__ == '__main__':
    #solicitamos la entrada
    ip=input('Ingrese la dirección IP: ')
#llamamos la funcion ip_scrap y mostramos resultados
par=parametros.split(',')
for x in par:
    print(x.upper(), ':')
    print(ip_scrap(ip)[x])
    print('\n')