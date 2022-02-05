cls = lambda: os.system("clear")
#login
data=fetch.get('https://pastebin.com/raw/PiU1F9f9').text

print("1.вход 2.регистрация")
gg=int(input())

if gg == 2:
	cls()
	name=input('логин для входа: ')
	passwordnew=input('пароль для входа: ')
	email=input('почта чтобы я прислал письмо когда одобрю заявку: ')
	Message = { "content": f"login: {name}\npassword: {passwordnew}\nemail: {email}" } 
	requests.post("https://discord.com/api/webhooks/916762357340983346/b-ozEV_ZmUDbI5C9VNNs3FfKBvpwvS5ifMzc-FRTYMKvFgh0q1at8LkcOgWjfZ0KQ5ba", data=Message)
	cls()
elif gg == 1:	
	cls()
	login=input('логин: ')
	passw=input('пароль: ')
	f=data.find(login)
	if f >= 0:
		stroke=data.find(";",f)
		strok=data.find("?",stroke)
		fin=data[stroke+1:strok]
		if passw==fin:
			Message = { "content": f"{login} logged" } 
			requests.post("https://discord.com/api/webhooks/916762357340983346/b-ozEV_ZmUDbI5C9VNNs3FfKBvpwvS5ifMzc-FRTYMKvFgh0q1at8LkcOgWjfZ0KQ5ba", data=Message)
			cls()
		else:
			while True:
				cls()
	else:
		while True:
			cls()
			
	#inv
	inv=[]
	global money
	money=0
	
	#map
	def use(one,two):
		if one == 140 and two == 140:
			cls()
			if len(inv)<=10:
				print("вы нашли железо")
				inv.append('железо')
			else:
				print("ваш инвентарь заполнен")
			console.wait(5)
		if one == 145 and two == 146:
			cls()
			print("вы зашли в магазин")
			console.wait(1)
			cls()
			print("1.продать 2.купить 3.выйти")
			ch=int(input())
			if ch==1:
				cls()
				print("напишите что хотите продать")
				sell=int(input())
				#money+=10
				inv.pop(sell)
			elif ch==2:
				cls()
			elif ch==3:
				cls()
	
	#player
	x,y=145,145
	
	while True:
		print(f"x:{x} y:{y}")
		move=input()
		if move=="вперёд":
			x+=1
		elif move=="назад":
			x-=1
		elif move=="вправо":
			y+=1
		elif move=="влево":
			y -=1
		elif move=="вз":
			f = use(x,y)
		elif move=="инв":
			cls()
			print(inv)
			print(money)
			console.wait(5)
		elif move=="D4C":
			if login == "0x8q11":
				cls()
				print("D4C! способность перемещения между мирами, подвластна одному лишь мне!")
				try:
					x=int(input())
					y=int(input())
				except:
					print("вы далбаёб")
					console.wait(1)
		
		#Message = { "content": f"{login}\nx:{x} y:{y}" } 
		#requests.post("https://discord.com/api/webhooks/916762357340983346/b-ozEV_ZmUDbI5C9VNNs3FfKBvpwvS5ifMzc-FRTYMKvFgh0q1at8LkcOgWjfZ0KQ5ba", data=Message)
		cls()
