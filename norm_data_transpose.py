#import and transpose data

import pandas as pd
import numpy as np


normData = np.loadtxt('normData.txt', delimiter = '\t', dtype = 'string')
normData = normData.T

my_df = pd.DataFrame(data=normData[1:,1:],    # values                   
              index=range(1,len(normData[1:,0])+1),    # 1st column as index
                  columns=normData[0,1:]) 


          
