import re
from math import gcd
from copy import deepcopy
from collections import deque
from operator import add, mul, attrgetter

class Monkey:
	__values__ = ('items', 'op', 'op_value', 'divisor','pass_if_true', 'pass_if_false', 'inspections')

	def inspect(self):
		item = self.items.popleft()
		if self.op_value is None:
			return self.op(item, item)
		return self.op(item, self.op_value)

def lcm(*integers):
	it  = iter(integers)
	res = next(it)
	for x in it:
		res = res * x // gcd(res, x)
	return res

def simulate(monkeys, n_rounds, part2=False):
	if part2:
		modulus = lcm(*map(attrgetter('divisor'), monkeys))
	for _ in range(n_rounds):
		for monkey in monkeys:
			monkey.inspections += len(monkey.items)
			while monkey.items:
				if part2:
					item = monkey.inspect() % modulus
				else:
					item = monkey.inspect() // 3
				if item % monkey.divisor == 0:
					monkeys[monkey.pass_if_true].items.append(item)
				else:
					monkeys[monkey.pass_if_false].items.append(item)
	a, b = sorted(map(attrgetter('inspections'), monkeys), reverse=True)[:2]
	return a*b

regexp  = re.compile(r'\d+')
monkeys = []

with open('input.txt') as file:
	data = file.read().split('\n\n')
for monkey_data in data:
	lines   = monkey_data.splitlines()
	matches = regexp.findall(lines[2])
	m = Monkey()
	m.items = deque(map(int, regexp.findall(lines[1])))
	m.op = add if '+' in lines[2] else mul
	m.op_value = int(matches[0]) if matches else None
	m.divisor = int(regexp.findall(lines[3])[0])
	m.pass_if_true = int(regexp.findall(lines[4])[0])
	m.pass_if_false = int(regexp.findall(lines[5])[0])
	m.inspections = 0
	monkeys.append(m)
original = deepcopy(monkeys)
sol_1 = simulate(monkeys, 20)
print(sol_1)
sol_2 = simulate(original, 10000, True)
print(sol_2)