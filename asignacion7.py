import requests
from pprint import pprint

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

for x in dispositivos.json()['response']:
    print('\n\nTipo de equipo: ', x['family'], '\nHostname: ', x['hostname'], '\nDirección IP de administrador: ', x['managementIpAddress'], '\nFecha de Última Actualización: ', x['lastUpdated'], '\nEstatus del equipo: ', x['reachabilityStatus'])