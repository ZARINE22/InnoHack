from aiogram import Bot,types,Dispatcher, executor 
#from aiogram.dispatcher import Dispatcher 
##from aiorgram.utils import executor 
bot=Bot(token='5447138819:AAGTHryc2sA8Kuy-yI7eMVTZEb0XTN_Dd5g') 
dp=Dispatcher(bot) 
@dp.message_handler(commands={'start'}) 
async def start (message: types.Message):    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1=types.KeyboardButton("поле 1") 
    btn2=types.KeyboardButton("поле 2") 
    await message.answer("поле 1 - тепловые люки, поле 2 - центральная дождевая установка ", reply_markup=keyboard) 
    @dp.message_handler(content_types=["text"]) 
    async def type (message: types.Message): 
         
        if message.text.strip() == 'поле 1' : 
            answer = text ="тут есть: люк 1,люк 2, люк 3, люк 4,люк 5" 
            await message.answer(text=text) 
        
        elif message.text.strip() == 'поле 2': 
            answer = text ="названия оборудования дождевой установки: насосная станция,  центральная шарнирная башня, пролёты, разбрызгиватель, электродвигатели" 
            await message.answer(text=text) 
             
@dp.message_handler(text='насосная станция') 
async def gлk (message: types.Message): 
        chat_id = message.chat.id 
        text = 'качает воду' 
        await bot.send_message(chat_id = chat_id, text=text) 
         
@dp.message_handler(text='центральная шарнирная башня') 
async def gолk (message: types.Message): 
        chat_id = message.chat.id 
        text = 'работвет исправна' 
        await bot.send_message(chat_id = chat_id, text=text) 
         
@dp.message_handler(text='пролёты') 
async def gщйk (message: types.Message): 
        chat_id = message.chat.id 
        text = 'вылетела гайка в 6 пролёте' 
        await bot.send_message(chat_id = chat_id, text=text) 
         
@dp.message_handler(text='разбрызгиватели') 
async def gьчk (message: types.Message): 
        chat_id = message.chat.id 
        text = '25,30, 48, 64 разбрызгиватель забился' 
        await bot.send_message(chat_id = chat_id, text=text) 
         
@dp.message_handler(text='электродвигатели') 
async def gяиk (message: types.Message): 
        chat_id = message.chat.id 
        text = 'работают исправно' 
        await bot.send_message(chat_id = chat_id, text=text) 
         
@dp.message_handler(text='люк 1') 
async def g1jk (message: types.Message): 
        chat_id = message.chat.id 
        text = 'залит водой' 
        await bot.send_message(chat_id = chat_id, text=text) 
         
@dp.message_handler(text='люк 2') 
async def gлиk (message: types.Message): 
        chat_id = message.chat.id 
        text = 'работвет исправна' 
        await bot.send_message(chat_id = chat_id, text=text) 
         
@dp.message_handler(text='люк 3') 
async def gщk (message: types.Message): 
        chat_id = message.chat.id 
        text = 'заливается водой' 
        await bot.send_message(chat_id = chat_id, text=text) 
         
@dp.message_handler(text='люк 4') 
async def gьдk (message: types.Message): 
        chat_id = message.chat.id 
        text = 'работает исправно' 
        await bot.send_message(chat_id = chat_id, text=text) 
         
@dp.message_handler(text='люк 5') 
async def gядлоk (message: types.Message): 
        chat_id = message.chat.id 
        text = 'работает исправно' 
        await bot.send_message(chat_id = chat_id, text=text) 
                 
executor.start_polling(dp, skip_updates=True)
