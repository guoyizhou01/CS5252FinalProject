
import sys




def read_cfg(filename):
	grammar = dict()
	start = None
	with open(filename, mode ='r') as file:
		first_line = True
		for line in file:
			if line.find('//') != -1:
				line = line[0:line.find('//')]
			line = line.strip().replace(" ","").replace("~","ε")
			if len(line) == 0:
				continue
			if first_line:
				start = line
				first_line = False
				continue
			# split_line[0] is state, split_line[1] is all possible productions	
			split_line = line.split("->")
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
							while (i < len(production)-1 and production[i] != "}"):
								i = i+1
								state = state + production[i]
							# if i == len(production) and production[i-1] == "}":
								# state = state + production[i]
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

def cfg_to_pda(start,grammar,sort_grammar = False):
	index = dict()
	print('Start state: q_START')
	print("δ(q_START,ε,ε)=δ(q_{0:}_0,{{ACCEPT}})".format(start))
	state_shift = dict()
	end_of_state = dict()
	pre_accept = []
	grammar_str = []
	for key in grammar.keys():
		index[key] = 0
	for key in grammar.keys():
		for production in grammar[key]:
			isStart = True
			symbolEnd = 'ε'
			for i in range(len(production)):
				if is_state(production[i]):

					if isStart:
						grammar_str.append("δ(q_{0:}_0,ε,ε)=δ(q_{2:}_0,{0:}_{3})".format(key,index[key],production[i],index[key]+1 ))
						isStart = False
					else:
						grammar_str.append("δ(q_{0:}_{1:},ε,ε)=δ(q_{2:}_0,{0:}_{3})".format(key,index[key],production[i],index[key]+1 ))
					if not (production[i] in state_shift.keys()):
						state_shift[production[i]] = []
					state_shift[production[i]].append("{0:}_{1}".format(key,index[key]+1))

				else :
					if isStart:
						grammar_str.append("δ(q_{0:}_0,{3:},ε)=δ(q_{0:}_{2:},ε)".format(key,index[key],index[key]+1,production[i]) )
						isStart = False
					elif i == len(production) - 1:
						symbolEnd = production[i]
						index[key] = index[key]-1
					else:
						grammar_str.append("δ(q_{0:}_{1:},{3:},ε)=δ(q_{0:}_{2:},ε)".format(key,index[key],index[key]+1,production[i]) )

				index[key] = index[key]+1
			if key == start:
				pre_accept.append((index[key],symbolEnd))
			if not (key in end_of_state.keys()):
				end_of_state[key] = []
			end_of_state[key].append((index[key],symbolEnd))
	# print(index)
	for key in state_shift.keys():
		for end_pair in end_of_state[key]:
			for return_state in state_shift[key]:
				grammar_str.append("δ(q_{0:}_{1:},{3:},{2:})=δ(q_{2:},ε)".format(key,end_pair[0],return_state,end_pair[1]))
	for accept_pair in pre_accept:
		grammar_str.append("δ(q_{0:}_{1:},{2:},{{ACCEPT}})=δ(q_END,ε)".format(start,accept_pair[0],accept_pair[1]))
	if sort_grammar:
		grammar_str.sort()
	for line in grammar_str:
		print(line)
	print('Accept by empty stack only')


if __name__ == '__main__':
	filename = sys.argv[1].strip()
	(start,grammar) = read_cfg(filename)
	sort_result = False
	if len(sys.argv) > 2 and sys.argv[2] == 'sort':
		sort_result = True		
	print('start:',start)
	print('grammar:',grammar)
	cfg_to_pda(start,grammar,sort_result)