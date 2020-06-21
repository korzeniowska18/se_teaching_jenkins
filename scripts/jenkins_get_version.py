import jenkins

server = jenkins.Jenkins('http://localhost:8080',
                         username='admin',
                         password='92046d8a89df4e009962a2f51ce484dc')  # place password here


user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['Natalia'], version))
