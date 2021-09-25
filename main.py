import pickle
import sklearn
import pandas as pd

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# load the model from disk
filename = '/Users/raji/DataScienceCourse/ML-Advanced/saveModel/finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

class PredictDiabetes(Resource):
    def get(self, preg, plas, pres, skin, test, mass, pedi, age):
        # input = tuple(preg, plas, pres, skin, test, mass,  pedi, age)
        output = loaded_model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])
        print(type(output))
        return {'output': output[0]}


api.add_resource(PredictDiabetes,
                 "/predictdiabetes/<int:preg>,<int:plas>,<int:pres>,<int:skin>,<int:test>,<float:mass>,<float:pedi>,<int:age>")

if __name__ == '__main__':
    app.run(debug=True)
