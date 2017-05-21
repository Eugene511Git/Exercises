# cook_book = {
      # 'яйчница': [
        # {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
        # {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
        # ],
      # 'стейк': [
        # {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
        # {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
        # {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
        # ],
      # 'салат': [
        # {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
        # {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
        # {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
        # {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
        # ]
      # }

# with open('cookBook.txt', 'w') as book:
	# for key, ingridient_list in cook_book.items():
		# book.write('\n{}\n'.format(key))
		# book.write('{}\n'.format(len(ingridient_list)))
		# for ingridient in ingridient_list:
			# book.write('{ingridient_name} | {quantity} | {measure}\n'.format(**ingridient))
			
def get_shop_list_by_dishes(dishes, person_count):
  cook_book = read_book()
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=\
					new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
	for shop_list_item in shop_list.values():
		print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], \
			shop_list_item['measure']))

def create_shop_list():
	person_count = int(input('Введите количество человек: '))
	dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
		.lower().split(', ')
	shop_list = get_shop_list_by_dishes(dishes, person_count)
	print_shop_list(shop_list)
	
def read_book():
	title = ['ingridient_name', 'quantity', 'measure']
	dishes = list()
	ingridients_lists = list()
	with open('cookBook.txt') as book:
		for line in book:
			if line == '\n': continue
			dish = line.strip()
			ingridients_list = list()
			for i in range(int(book.readline())):
				ingridients_list.append(dict(zip(title, book.readline().strip().split('|'))))
				ingridients_list[i]['quantity'] = int(ingridients_list[i]['quantity'])
			dishes.append(dish)
			ingridients_lists.append(ingridients_list)
	return dict(zip(dishes, ingridients_lists))
	#print(cook_book)

create_shop_list()


