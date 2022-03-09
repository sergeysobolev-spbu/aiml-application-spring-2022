import numpy as np
#from scipy import optimize
from scipy.optimize import basinhopping
import matplotlib.pyplot as plt

#длина пути по заданному маршруту
def distance_along_the_route(points,route):
  distance = 0
  quantity_points = len(route)
  #route = route[:len(route)-1]
  for i in range(quantity_points-1):
    distance = distance + np.sqrt((points[route[i]][0]-points[route[i+1]][0])**2+(points[route[i]][1]-points[route[i+1]][1])**2)

  return distance

#большое расстояние - большая ошибка
def error(points,route): 
  return distance_along_the_route(points,route)# - 16


#смежный маршрут - меняет местами два случайных индекса
def adjacent(route, rnd):
  n = len(route)
  result = np.copy(route)
  i = rnd.randint(n) 
  j = rnd.randint(n)
  tmp = result[i]
  result[i] = result[j] 
  result[j] = tmp
  return result

#основная функция
def solve(n_cities, rnd, max_iter, start_temperature, alpha, points):
  # решить с помощью имитации отжига
  curr_temperature = start_temperature
  soln = np.arange(n_cities, dtype=np.int64)
  rnd.shuffle(soln)
  #print("Первоначальное предположение: ")
  #print(soln)

  err = error(points,soln)
  iteration = 0
  interval = (int)(max_iter / 10)     #частота отображения сообщений о ходе выполнения
  while iteration < max_iter and err > 0.0:
    adj_route = adjacent(soln, rnd)
    adj_err = error(points,adj_route)
    if adj_err < err:  # лучший маршрут
      soln = adj_route
      err = adj_err
    else:          # соседние хуже
      accept_p = np.exp((err - adj_err) / curr_temperature) #принять вероятность
      p = rnd.random()
      if p < accept_p:  # все равно принять
        soln = adj_route
        err = adj_err 
      # иначе не принимать

    if iteration % interval == 0:
      print("iteration = %6d | error = %7.2f | temperature = %10.4f " % (iteration, err, curr_temperature))
    if curr_temperature < 0.00001:
      curr_temperature = 0.00001
    else:
      curr_temperature *= alpha
    iteration += 1


  return soln

#отрисовка
def rendering(x,y,render):
  if render != 0:
    plt.plot(x, y)
    plt.scatter(x, y, s=20, c='r')
    plt.show()

#filename = 'C:/python11/spbgu/input.txt'
filename = 'input.txt'
render = 1

x=[]
y=[]
points =[]
quantity_points = 0

#чтение из файла
with open(filename, 'r') as f:
    for line in f:
        if quantity_points == 0:
          quantity_points = int(line) 
        else:
          points.append([int(line.split()[0]),int(line.split()[1])])
          x.append(int(line.split()[0]))
          y.append(int(line.split()[1]))

route = list(range(0,quantity_points))

#начальная отрисовка точек
rendering(x,y,render)
################################################################   

print("Начальный маршрут:") 
print(route) 
print("Начальный маршрут имеет общее расстояние = %0.3f" % distance_along_the_route(points,route)) 
rnd = np.random.RandomState(4) 
max_iter = 2500 
start_temperature = 10000.0 
alpha = 0.99    #Снижение температуры контролируется значением альфа: T=T*alpha
print("\nНастройки: ") 
print("max_iter = %d " % max_iter) 
print("start_temperature = %0.1f " % start_temperature) 
print("alpha = %0.2f " % alpha)

#new_route=route
print("\n")
new_route = solve(quantity_points,rnd,max_iter,start_temperature,alpha,points) 

print("\nНайдено лучшее решение:") 
print(new_route) 
dist = distance_along_the_route(points,new_route)
print("Общее расстояние = %0.3f " % dist) 

#запись результата в файл
#f = open('C:/python11/spbgu/output.txt', 'w')
f = open('output.txt', 'w')
f.write(str(dist)+'\n')
stri = ''
for i in new_route:
  stri = stri + str(i) + ' '
f.write(stri)
f.close()

#конечная отрисовка точек
new_x = []
new_y = []
for i in range(len(new_route)):
  new_x.append(x[new_route[i]])
  new_y.append(y[new_route[i]])

rendering(new_x,new_y,render)