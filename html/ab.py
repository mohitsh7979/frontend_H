 
# import pandas as pd  
    
# # Define a dictionary containing employee data  
# data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],  
#         'Age':[27, 24, 22, 32],  
#         'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],  
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']  
#        }  
# # How can you select the columns 'Name' and 'Address' using label-based indexing?

# df = pd.DataFrame(data)
# print(df.head(3))


import pandas as pd 
   
# Create the dataframe 
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'], 
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'], 
                    'Cost':[10000, 5000, 15000, 2000]})

print(df.Cost.sum())
