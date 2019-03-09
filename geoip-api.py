import requests
import json
apiurl='http://ip-api.com/json/'
parametros='city,country,countryCode,isp,org,regionName,lat,lon,timezone,zip'
data={'fields':parametros}
def ip_scrap(ip=''):
    res=requests.get(apiurl+ip, data=data)
    apires=json.loads(res.content)
    return apires
if __name__ == '__main__':
    ip=input('Ingrese la dirección IP: ')
#llamamos la funcion ip_scrap y mostramos resultados
par=parametros.split(',')
for x in par:
    print(x.upper(), ':')
    print(ip_scrap(ip)[x])
    print('\n')
