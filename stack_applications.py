########################### 	APPLICATIONS OF STACK	 ############################

postfix_expression = []
brackop = []

####### INFIX TO POSTFIX ########
# Assuming all letters in the expression are upper case

def Infix2Postfix(expression):
	token_exp = []
	token_exp[:] = expression
	for token in token_exp:
		if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			postfix_expression.append(token)

		if token in '0123456789':
			postfix_expression.append(int(token))

		if token == '(':
			brackop.append(token)

		if token == '/' or token == '*':
			if len(brackop) == 0:
				brackop.append(token)
			else:
				if brackop[len(brackop)-1] != '/' and brackop[len(brackop)-1] != '*':
					brackop.append(token)
				else:
					for b in brackop[::-1]:
						if b != '(':
							postfix_expression.append(b)
							brackop.pop()
						if b == '(':
							brackop.pop()
					brackop.append(token)

		if token == '+' or token == '-':
			if len(brackop) == 0:
				brackop.append(token)
			else:
				if brackop[len(brackop)-1] != '/' and brackop[len(brackop)-1] != '*' and brackop[len(brackop)-1] != '+' and brackop[len(brackop)-1] != '-':
					brackop.append(token)


				else:
					for b in brackop[::-1]:
						if b != '(':
							postfix_expression.append(b)
							brackop.pop()
						if b == '(':
							brackop.pop()
					brackop.append(token)			


		if token == ')':
			for b in brackop[::-1]:
				if b != '(':
					postfix_expression.append(b)
					brackop.pop()
				if b == '(':
					brackop.pop()
					break

		# print(brackop)

	if len(brackop) != 0:
		for b in brackop[::-1]:
			postfix_expression.append(b)

	return postfix_expression

postFix = Infix2Postfix('(5+3)+ (3-3)')
print("PostFix expression --> ", postFix)

####### POSTFIX EVALUATION ########
# Assuming the expression has numbers and no letters (integers in this case).
def PostfixEval(postfix_expression):
	number_stack = []
	operator = []
	for p in postfix_expression:
		if type(p) == int:
			number_stack.append(p)

		if p == '+':
			new = number_stack[len(number_stack)-2] + number_stack[len(number_stack)-1]
			number_stack.pop()
			number_stack.pop() 
			number_stack.append(new)
		if p == '-':
			new = number_stack[len(number_stack)-2] - number_stack[len(number_stack)-1]
			number_stack.pop()
			number_stack.pop() 
			number_stack.append(new) 
		if p == '*':
			new = number_stack[len(number_stack)-2] * number_stack[len(number_stack)-1] 
			number_stack.pop()
			number_stack.pop() 
			number_stack.append(new)
		if p == '/':
			new = number_stack[len(number_stack)-2] / number_stack[len(number_stack)-1] 
			number_stack.pop()
			number_stack.pop() 
			number_stack.append(new)

	return number_stack[0]

print("The result of PostFix evaluation is ",PostfixEval(postFix))

