import utils
def run():
  keys,values=utils.get_population()
  
  
  print(keys,values)
  
  print(utils.A)
  
  
  data=[
  {
    'country':"Colombia",
    'population':500
  },
  {
    'country':"Bolivia",
    'population':300
  }  
  ]
  
  country=input("TYPE COUNTRY: ")
  
  result= utils.population_by_country(data,country)
  print(result)


if __name__=='__main__':
  run()