from configparser import ConfigParser
parser = ConfigParser()
parser.read('properties.conf')
username = parser.get('database_config', 'username')
password = parser.get('database_config', 'password')
hostname = parser.get('database_config', 'hostname')
port = parser.get('database_config', 'port')


print(username)
print(password)
print(hostname)
print(port)
