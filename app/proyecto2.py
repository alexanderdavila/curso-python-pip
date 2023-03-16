import csv
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

def generate_pie_chart(labels, values):
  fig, ax =plt.subplots()
  ax.pie(values,labels=labels)
  ax.axis('equal')
  plt.show()

def generate_labels_values(data):
  keys=[]
  values=[]
  for i in range(0,len(data)):
    key=data[i]['Country/Territory']
    value=data[i]['World Population Percentage'] 
    keys.append(key)
    values.append(value)
  return keys,values

if __name__=='__main__':
  data=read_csv('data.csv')
  #print(data[0]['World Population Percentaje'])
  keys,values=generate_labels_values(data)
  generate_pie_chart(keys,values)