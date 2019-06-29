import random

menu = ["순남시레기", "멀티캠퍼스 20층", "양자강", "강남목장", "시골집"]
menu_detail = {"순남시레기": "시레기국, 보쌈", "멀티캠퍼스 20층": "오늘의 메뉴",
               "양자강": "차돌짬뽕", "강남목장": "뚝배기불고기", "시골집": "쌈밥정식"}

select = random.randrange(0, 5)
lunch = menu[select]

choice = random.choice(menu)
print(choice)

print(random.sample(range(5), 2))

select_menu = menu_detail[lunch]
last = select_menu[-1]

if (last == "뉴" or last == "기"):
  print(lunch + "에서는 " + select_menu + "가 먹을 만합니다.")  
else:
  print(lunch + "에서는 " + select_menu + "이 먹을 만합니다.")