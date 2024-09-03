import pandas as pd 
import matplotlib.pyplot as plt
# * from google.colab import files
import io

# ? upload .csv file from computer in google colab

# * upload .csv file from any computer
# * uploaded = files.upload()
# * file_name = next(iter(uploaded))
# * table_1 = pd.read_csv(io.BytesIO(uploades[file_name]))

# ? Get .csv from URL

url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/faithful.csv'
table_1 = pd.read_csv(url)

# ? those imports and that url variable will be good for maybe 20 minutes, so you don't have
# ?  to repeat those steps each time. Now determinate what columns you want and convert them to numpy arrays

# print(table_1)

# ? Get the headers so you can see the column names and two rows
print(table_1.head(2))

# ? column names as a variable
col_names = table_1.columns
print(col_names)

# ?  another way to get column names
print('\n column names:')
for a in range(len(col_names)):
    print(a,' ', col_names[a])
    
# ? graph index and one other column as (x,y) points
# * convert values to numpy arrays
x = table_1['Index'].to_numpy()
y = table_1[' "Eruption length (mins)"'].to_numpy()

# * graph
xmin = x.min() - 5
xmax = x.max() + 5
ymin = y.min() - 5
ymax = y.max() + 5      

fig,ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')
plt.plot(x,y,'ro') # * scatterplot
plt.plot(x,y,'b') #  * line graph
plt.show()

# ? using variables for column names
x_name = col_names[0]
y_name = col_names[2]
x = table_1[x_name].to_numpy()
y = table_1[y_name].to_numpy()

xmin = x.min() - 5
xmax = x.max() + 5
ymin = y.min() - 5
ymax = y.max() + 5      

plt.axis([xmin,xmax,ymin,ymax])
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax],'b')
plt.plot(x,y,'ro') # * scatterplot
#plt.plot(x,y,'b') #  * line graph
plt.show()
