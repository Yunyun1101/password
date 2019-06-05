password = 'a123456'
count = 3

while count > 0:
	user_input = input('請輸入密碼')
	count = count - 1
	if user_input == password:
		print('登入成功！')
		break
	else:
		print('還有', count, '次機會')

	print('登入失敗')