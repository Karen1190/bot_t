import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_token
import sqlite3

bot = telebot.TeleBot(API_token)

con = sqlite3.connect("at.db", check_same_thread=False)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS aot(
ID int,
name_c varchar(225),
image text,
m text)''')



cur.execute('''CREATE TABLE IF NOT EXISTS a2ot(
ID int,
name_c varchar(225),
image text,
massage text)''')


# sql = '''
# INSERT INTO aot VALUES (1,'Levi Ackermann','https://vignette.wikia.nocookie.net/shingekinokyojin/images/b/b1/Levi_Ackermann_%28Anime%29_character_image.png/revision/latest/scale-to-width-down/350?cb=20180815192508');
# INSERT INTO aot VALUES (2,'Eren Jaeger','https://vignette.wikia.nocookie.net/shingekinokyojin/images/a/a1/Eren_Jaeger_%28Anime%29_character_image.png/revision/latest/scale-to-width-down/350?cb=20210308023541')'''
# cur.executescript(sql)


@bot.callback_query_handler(func=lambda call: call.data == 'Levi Ackermann')
def view(call):
    cur.execute("SELECT * from aot")
    sk0 = cur.fetchall()
    if sk0:
        for record in sk0:
             message_photo = record[2]
             #massage_massage = record[3]
             bot.send_photo(call.message.chat.id, message_photo,caption=('[[['))


def view(call):
    cur.execute("SELECT * from a2ot")
    sk1 = cur.fetchall()
    if sk1:
        for record in sk1:
             t_message_photo = record[2]
             t_massage_massage = record[3]
             bot.send_photo(call.message.chat.id, t_message_photo,caption=(f'{t_massage_massage}'))


#             # @bot.callback_query_handler(func=lambda call: call.data('expert_'))
# # def show_expert_info(call):
def main_menu():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("attack on titan", callback_data='menu1')
    markup.add(button1)
    return markup


def submenu1():
    markup = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('titans', callback_data='titans')
    button2 = InlineKeyboardButton('characters', callback_data='characters')

    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(button1, button2, return_button)
    return markup


def characters():
    markup = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton('Levi Ackermann', callback_data='Levi Ackermann')
    button2 = InlineKeyboardButton('Eren Jaeger', callback_data='Eren Jaeger')
    button3 = InlineKeyboardButton('Mikasa Ackermann', callback_data='Mikasa Ackermann')
    button4 = InlineKeyboardButton('Armin Arlert', callback_data='Armin Arlert')
    button5 = InlineKeyboardButton('Zeke Jaeger', callback_data='Zeke Jaeger')
    button6 = InlineKeyboardButton('Karl Fritz', callback_data='Karl Fritz')
    button7 = InlineKeyboardButton('Ymir', callback_data='Ymir')
    button8 = InlineKeyboardButton('Annie Leonhart', callback_data='Annie Leonhart')
    button9 = InlineKeyboardButton('Reiner Braun', callback_data='Reiner Braun')
    button10 = InlineKeyboardButton('Eren Kruger', callback_data='Eren Kruger')
    button11 = InlineKeyboardButton('Bertholdt Hoover', callback_data='Bertholdt Hoover')
    button12 = InlineKeyboardButton('Frieda Reiss', callback_data='Frieda Reiss')
    button13 = InlineKeyboardButton('Grisha Jaeger', callback_data='Grisha Jaeger')
    button14 = InlineKeyboardButton('Hange Zoër', callback_data='Hange Zoë')
    button15 = InlineKeyboardButton('Kenny Ackermann', callback_data='Kenny Ackermann')
    button16 = InlineKeyboardButton('Erwin Smith', callback_data='Erwin Smith')
    button17 = InlineKeyboardButton('Uri Reiss', callback_data='Uri Reiss')
    button18 = InlineKeyboardButton('Porco Galliard', callback_data='Porco Galliard')
    button19 = InlineKeyboardButton('Sasha Braus', callback_data='Sasha Braus')
    button20 = InlineKeyboardButton('Gabi Braun', callback_data='Gabi Braun')
    button21 = InlineKeyboardButton('Lara Tybur', callback_data='Lara Tybur')
    button22 = InlineKeyboardButton('Falco Grice', callback_data='Falco Grice')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
               button12, button13, button14, button15, button16, button17, button18, button19, button20, button21,
               button22, return_button)
    return markup


def titan():
    markup = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('Fundamental Titan', callback_data='Fundamental Titan')
    button2 = InlineKeyboardButton('Attack Titan', callback_data='Attack Titan')
    button3 = InlineKeyboardButton('Colossus Titan', callback_data='Colossus Titan')
    button4 = InlineKeyboardButton('War Hammer Titan', callback_data='War Hammer Titan')
    button5 = InlineKeyboardButton('Armored Titan', callback_data='Armored Titan')
    button6 = InlineKeyboardButton('Female Titan', callback_data='Female Titan')
    button7 = InlineKeyboardButton('Beast Titan', callback_data='Beast Titan')
    button8 = InlineKeyboardButton('Cart Titan', callback_data='Cart Titan')
    button9 = InlineKeyboardButton('Jaw Titan', callback_data='Jaw Titan')
    return_button = InlineKeyboardButton('Return', callback_data='return_to_main')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, return_button)
    return markup

# def view():
#     cur.execute("SELECT * from at")
#     sk0 = cur.fetchall()
#    if sk0:
#        for record in sk0:
#             message_photo = record[3]
#             bot.send_photo(call.message.chat.id, message_photo,


            # @bot.callback_query_handler(func=lambda call: call.data('expert_'))
# def show_expert_info(call):

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "You are in main menu. Choose an option:", reply_markup=main_menu())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'menu1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="گزینه مورد نظر را انتخاب کنید",
                              reply_markup=submenu1())

    elif call.data == 'characters':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="شخصیت مورد نظر را انتخاب کنید", reply_markup=characters())

    elif call.data == 'titans':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="تایتان مورد نظر را انتخاب کنید", reply_markup=titan())

    elif call.data == 'return_to_main':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="You are in return_to_main", reply_markup=main_menu())

    elif call.data == 'Levi Ackermann':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="hghfhgfhjfh", reply_markup=view())

    #
    # elif call.data == 'Eren Jaeger':
    #     bot.send_message(message.chat.id, "لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    # elif call.data == 'Mikasa Ackermann':
    #     bot.send_message(message.chat.id, "لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    # elif call.data == 'Armin Arlert':
    #     bot.send_message(message.chat.id, "لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    # elif call.data == 'Zeke Jaeger':
    #     bot.send_message(message.chat.id, "لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    # elif call.data == 'Karl Fritz':
    #     bot.send_message(message.chat.id, "لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    # elif call.data == 'Ymir':
    #     bot.send_message(message.chat.id, "لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    # elif call.data == 'Annie Leonhart':
    #     bot.send_message(message.chat.id, "لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    # elif call.data == 'Reiner Braun':
    #     bot.send_message(message.chat.id, "لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    # elif call.data == 'Eren Kruger':
    #     bot.send_message(message.chat.id, "لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    # elif call.data == 'Bertholdt Hoover':
    #     bot.send_message(message.chat.id,"لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    # elif call.data == 'Frieda Reiss':
    #     bot.send_message(message.chat.id, "لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    # elif call.data == 'Grisha Jaeger':
    #     bot.send_message(message.chat.id, "لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    # elif call.data == 'Hange Zoër':
    #     bot.send_message(message.chat.id, "لیوای آکرمن که بیشتر با نام کاپیتان لیوای شناخته می‌شود، کاپیتان جوخه‌ی عملیات‌هاییژه از دسته دیدبانی است. گفته می‌شود او قدرتمندترین سرباز بشری است", reply_markup=view())
    #
    #


bot.polling()
