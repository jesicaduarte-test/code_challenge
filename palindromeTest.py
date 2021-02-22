def palindrome(e):

	if type(e) != str:
		return False
	else:	
		e = e.replace(" ", "")
		if len(e) <= 0:
			return False
		else:	
			if str.lower(e) == str.lower(e)[::-1]:
				return True
			else:
				return False


# In this array we define the values that we want to use in our function
dataSet = [3, 2.3,'    ','999','98','ERe!eRE','Re!eRE','!!!','!!"!','mum','mun','somos o no somos','somos no somos','Somos o no soMos','Somos NO somos',' space','space ','e3e@e3e','e3e@ee','12/11/21','02/02/2020']


for e in dataSet: 
	# If the element of the data set it's a palindrome this function will print True if it's not, this function will print False

	print(palindrome(e))