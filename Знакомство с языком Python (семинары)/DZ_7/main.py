import pandas as pd
import random 
lst = ['robot'] * 10  
lst += ['human'] * 10  
random.shuffle(lst)  
data = pd.DataFrame({'whoAmI':lst})
data.head(10)
    
pd.get_dummies(data['whoAmI']).head(10)

pd.DataFrame({'human': data['whoAmI'] == 'human',
              'robot': data['whoAmI'] == 'robot'}).astype(int).head(10)

