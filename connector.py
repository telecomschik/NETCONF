from devices import CSR1000V
from ncclient import manager
from pprint import pprint
import xmltodict

with manager.connect(**CSR1000V) as m:
    c = m.get_config(source='running').data_xml
    config_dict = xmltodict.parse(c)['data']
    int_config = config_dict['interfaces'][1]['interface']
    schema = m.get_schema('ietf-ip')
    pprint(schema)
    pprint(int_config)
    for i in int_config:
        try:
            print('----------------------------------------------')
            print('Interface: %s' % i['name'])
            print('Description:%s' % i['description'])
            print('IP:%s' % i['ipv4']['address']['ip'])
            print('Mask:%s' % i['ipv4']['address']['netmask'])
            print('----------------------------------------------')
        except KeyError:
            print('The key is not exist')

