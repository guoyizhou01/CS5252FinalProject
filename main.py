
import sys




def read_cfg(filename):
	grammar = dict()
	start = None
	with open(filename, mode ='r') as file:
		first_line = True
		for line in file:
			if first_line:
				start = line.strip().replace(" ","")
				first_line = False
				continue
			# split_line[0] is state, split_line[1] is all possible productions	
			split_line = line.strip().replace(" ","").split("->")
			productions = split_line[1].split("|")
			for production in productions:
				single_prod = []
				i=0
				while i < len(production):
					if production[i] == "%":
						state = "%"
						if i == len(production)-1:
							print("ERROR: Syntax Error in %s: %s!"%(filename,split_line))
							exit(1)
						if production[i+1] == "{":
							while (i < len(production) and production[i] != "}"):
								i = i+1
								state = state + production[i]
							if i < len(production) and production[i] == "}":
								state = state + production[i]
							if state[-1] != "}":
								print("ERROR: Syntax Error in %s: %s!"%(filename,split_line))
								exit(1)

						else:
							i = i+1
							state = state + production[i]
						single_prod.append(state)
					else:
						single_prod.append(production[i])
					i = i+1
				if not (split_line[0] in grammar.keys()):
					grammar[split_line[0]] = []
				grammar[split_line[0]].append(single_prod)
		if not (start in grammar.keys()):
			print("ERROR: No production for %s exists!"%(start))	
			exit(1)

	return (start,grammar)

def is_state(string):
	return string[0] == "%"

def cfg_to_pda(start,grammar):
	index = dict()
	print("δ(q0,ε,ε)=δ(q_{0:}_0,{0:})".format(start))
	for key in grammar.keys():
		index[key] = 0
	for key in grammar.keys():
		production = grammar[key]
		for i in range(len(production)):
			if is_state(production[i]):
				print("δ(q_{0:}_{1:},ε,ε)=δ(q_{2:}_0,{0:}_{1})".format(key,index[key],production[i]) )
			elif :
				print("δ(q_{0:}_{1:},ε,ε)=δ(q_{2:}_0,{0:}_{1})".format(key,index[key],production[i]) )



if __name__ == '__main__':
	filename = sys.argv[1].strip()
	(start,grammar) = read_cfg(filename)
	print(start)
	print(grammar)
	cfg_to_pda(start,grammar)