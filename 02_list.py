# Python列表类型不同操作的时间效率

from timeit import Timer

# append
def t1():
	li = []
	for i in range(10000):
		li.append(i)


# +
def t2():
	li = []
	for i in range(10000):
		# li += [i]
		li = li + [i]


# 列表生成器
def t3():
	li = [i for i in range(10000)]


# 列表转换
def t4():
	li = list(range(10000))


# extend
def t5():
	li = []
	for i in range(10000):
		li.extend([i])


# insert[0]
def t6():
	li = []
	for i in range(10000):
		li.insert(0, i)


timer1 = Timer("t1()", "from __main__ import t1")
print("append:", timer1.timeit(1000))

timer2 = Timer("t2()", "from __main__ import t2")
print("+:", timer2.timeit(1000))

timer3 = Timer("t3()", "from __main__ import t3")
print("[i for i in range]:", timer3.timeit(1000))

timer4 = Timer("t4()", "from __main__ import t4")
print("list(range):", timer4.timeit(1000))

timer5 = Timer("t5()", "from __main__ import t5")
print("extend:", timer5.timeit(1000))

timer6 = Timer("t6()", "from __main__ import t6")
print("insert[0]:", timer6.timeit(1000))