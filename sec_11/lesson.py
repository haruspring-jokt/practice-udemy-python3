import configparser

# config = configparser.ConfigParser()
#
# config['DEFAULT'] = {
#     'debug': True
# }
#
# with open('config.ini', 'w') as config_file:
#     config.write(config_file)

config = configparser.ConfigParser()
config.read('config.ini')
print(config['DEFAULT'])
print(config['DEFAULT']['debug'])
