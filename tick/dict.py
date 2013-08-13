

def menu():
	"""displays a menu for the user \
	and returns users choice """
	
	print " "	
	print "Welcome to the phonebook.\n Press \n"
	print "1 - To Enter new a contact \
	\n2 - To view the contacts available \
	\n3 - To delete a contact \
	\n4 - To quit"
	
	print " "
	choice = input("Enter your choice: ")  # prompt user for their choice
	return choice

def main():
	""" the main function """

	contacts = {}   # the phonebook is empty 
	
	while 1:
		choice = menu() # display a menu for the user
		if choice == 0:
			print "Not allowed"
			break
		elif choice == 1:
			name = raw_input("Enter the name: ")
			number = input("Enter the number: ")
			contacts[name] = number  	
		elif choice == 2:
			if len(contacts) == 0:
				print "The phonbook is empty"
			else: 
				print contacts.keys()
		elif choice == 3:
			if len(contacts) > 0:
				name = raw_input("Enter name to delete: ")
				del contacts[name]
				print contacts.keys()
			else:
				print "The phonbook is empty"
		else:
			break  # exit the program 


if __name__ == '__main__':
	main()
			

	
