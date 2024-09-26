import pickle 
import json 
import numpy as np 
import pandas as pd   
import warnings
warnings.filterwarnings('ignore')
import config

class MedicalInsurance():
    
    def __init__(self,age,sex,bmi,children,smoker,region):
        
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        
        self.region_col = 'region_'+region 
        
    def load_models(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f :
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH,'r') as f :
            self.save_data = json.load(f)
            
    def get_predicted_charges(self):
        
        self.load_models()
        
        region_index = list(self.save_data['column_names']).index(self.region_col)
        
        array = np.zeros(len(self.save_data['column_names']))
        
        array[0] = self.age
        array[1] = self.save_data['sex'][self.sex]
        array[2] = self.bmi 
        array[3] = self.children
        array[4] = self.save_data['smoker'][self.smoker]
        array[region_index] = 1
        
        print('Array :',array)
        
         