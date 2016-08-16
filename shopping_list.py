target_list = ["socks", "soap", "detergent", "sponges"]
safeway_list = ["butter", "cake", "cookies", "bread"]

list_dictionary = {"target": target_list, "safeway": safeway_list}


def menu_prompt():
	options = "0-Main Menu\n1-Show all lists\n2-Show specific list\n3-add new item\n4-add item to shopping list\n5-remove an item from shopping list\n6-Remove a list by nickname\n7-Exit when you are done:"
	#get user input
	option = int(raw_input(options))
	return option
	pass

def show_all_lists():
	print list_dictionary.items()
	

def show_specific_list(key):
	print list_dictionary[key] 
	

def add_new_list(key):
	initial_list=[]
	list_dictionary[key]=initial_list
	# print list_dictionary

def add_new_item(key,item):
	initial_list = list_dictionary[key]
	initial_list.append(item)
	# print list_dictionary

def remove_item(key,item):
	initial_list = list_dictionary[key]
	initial_list.remove(item)
	# print list_dictionary

def remove_list(key):
	del list_dictionary[key]
	print list_dictionary

def exit():
	pass


def main():
	option = menu_prompt()
	if option == 0:
		menu_prompt()
	if option ==1: 
		show_all_lists()
	if option ==2:
		shopping_list = raw_input("What list would you like to see: ")
		print shopping_list
		show_specific_list(shopping_list)

if __name__ == "__main__":
	main()