import requests
from pprint import pprint
import time
import os
import json

freq_get = 300
tick = time.time() - freq_get
fdjson = "tmp/dispositivos.json"
extraer = ["hostname","reachabilityStatus"]
list_disp_status = []

def extraer_dict_list(lista,keys):
    list_dict = []
    for x in lista:
            list_dict.append(dict((k, x[k]) for k in keys if k in x))
    return list_dict

while True:
    #Obtener lista de dispositivos cada 5 minutos
    if ((time.time()-tick) > freq_get):
        tick = time.time()
        response = requests.post(
            'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token',
            headers={'Authorization':'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='})
        response.raise_for_status()
        payload=response.json()
        pprint(payload)

        dispositivos = requests.get(
            'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device',
            headers={'X-Auth-Token': response.json()['Token']}
        )
        #Convertir la respuesta de la solicitud en una lista de diccionarios con los dispositivos y su status
        list_disp = json.loads(dispositivos.text.encode('utf8'))['response']
        list_disp_status  = extraer_dict_list(list_disp,extraer)
        list_disp_status_json = json.dumps(list_disp_status,indent=4)

        #Abrir archivo json y escribir dispositivos
        with open(fdjson,'w') as json_file:
            json_file.write(list_disp_status_json)

        #for x in dispositivos.json()['response']:
        #    print('\n\nTipo de equipo: ', x['family'], '\nHostname: ', x['hostname'], '\nDirección IP de administrador: ', x['managementIpAddress'], '\nFecha de Última Actualización: ', x['lastUpdated'], '\nEstatus del equipo: ', x['reachabilityStatus'])
        

