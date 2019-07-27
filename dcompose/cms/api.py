from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)

class HelloW(Resource) :
    def get(self):
        return {
            'products':['Ansible',
                       'Chef',
                       'Puppet',
                       'New App']

        }
api.add_resource(HelloW,'/')

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
