import os
#clear screen
os.system('cls')

#make variable account
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

#make variable user
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

#make user list & count elements
user_list = [user1, user2, user3, user4]
count_list = len(user_list)

# input key
key = input('Введите ключ (name или account): ')
# small letters in key
key = key.lower()
# make user key
user_key = {'name': 'name', 'account': 'account'}

#Part 1 check name & account info about all users
# check input key
try:
  key = user_key[key]
  # print user's names or accounts
  i = 0
  for i in range(count_list):
      user = user_list [i]
      print('значение ключа {} для юзера {} = {}'.format(key, str(i+1), user [key]))
      i = i+1
#print error      
except KeyError:
  print('Введенный ключ не найден')

#Part 2 information about user
#input number of user
number = input('Введите порядковый номер: ')

# check input key
try:
  #make index from number
  index = int(number)-1
  #create variable from dictionaries
  user =user_list [index]
  account = user['account']
  #print data
  print(
  'Данные по юзеру № {}:\nимя: {}\nвозраст: {}\nлогин: {}\nпароль: {}'.format(number, user['name'], user['age'], account['login'], account['password']))
  #print average age
  average_age = 0
  i = 0
  for i in range(count_list):
    user = user_list [i]
    average_age = average_age + user['age']
    i = i+1
  average_age = average_age/count_list
  print('Среднй возраст пользователей:'+ str(average_age))
#print error     
except:
  print('Пользователь с указанным номером не найден')


#Part3 move users
#input number of user
number = input('Введите номер пользователя, которого нужно переместить в конец: ')

# check input key
try:
  #make index from number
  index = int(number)-1
  #create variable from dictionaries
  user = user_list [index]
  #print old list
  print('Список до изменения:\n{}\nПользователь с именем {} перемещен в конец.\nСписок после изменения:'.format(user_list,user['name']))
  #make & print new list
  user = user_list.pop(index)
  user_list.append(user)
  print(user_list)

except:
  print('Пользователь с указанным номером не найден')
