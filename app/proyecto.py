import csv
import re
import matplotlib.pyplot as plt

def read_csv(path):
  data=[]
  with open(path,'r') as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    header=next(reader)
    for row in reader:
      iterable=zip(header,row)
      create_dictionary={key:value for key,value in iterable}
      data.append(create_dictionary)

    return data

def generate_bar_chart(name, labels, values):
  fig, ax =plt.subplots()
  values=[int(x) for x in values]
  ax.bar(labels,values)
  plt.savefig(f'./img/{name}.png')
  plt.close()

def generate_info(data,index):
  newDict = dict()
  newList =[]
  for i in range(0,len(data)):
    for (key, value) in data[i].items():
       if re.match('[0-9]+ +Population', key):
           newDict[key[0:4]] = value
    newList.append(newDict)
    newDict = dict()  
  keys=[]
  values=[]
  for key, value in newList[index].items():
    keys.append(key)
    values.append(value)
  rkeys=list(reversed(keys))
  rvalues=list(reversed(values))
  return rkeys,rvalues
  
def search_country(data,name):
  for i in range(0,len(data)):
    for (key, value) in data[i].items():
      if key=='Country/Territory' and value==name:
        return i


if __name__=='__main__':
  data=read_csv('data.csv')
  name=input('Ingrese pais: ')
  index=search_country(data,name)
  keys,values=generate_info(data,index)
  generate_bar_chart(name,keys,values)