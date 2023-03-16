import csv


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
     
    


if __name__=='__main__':
  data=read_csv('./app/data.csv')
  print(data[0])