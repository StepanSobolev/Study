from aiogram import types, executor, Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
import sqlite3


storage = MemoryStorage()
bot = Bot(token="1521325076:AAFfDO4zU6ZQcN1HxaUh1y6BNtkGYLEDvzs")
dp = Dispatcher(bot, storage=storage)

class ProfileState(StatesGroup):
    photo = State()
    name = State()
    age = State()
    description = State()


db = sqlite3.connect('base.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS articles(
        photo text,
        name text,
        age text,
        description text
    )""")

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Welcome')

@dp.message_handler(commands=['create'])
async def cmd_create(message: types.Message):
    await message.answer('Отправь мне фото')
    await ProfileState.photo.set()

@dp.message_handler(content_types=['photo'], state=ProfileState.photo)
async def cmd_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await message.reply('Отправь имя')
    await ProfileState.next()

@dp.message_handler(state=ProfileState.name)
async def cmd_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.reply('Отправь возраст')
    await ProfileState.next()

@dp.message_handler(state=ProfileState.age)
async def cmd_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await message.reply('Отправь описание')
    await ProfileState.next()

@dp.message_handler(state=ProfileState.description)
async def cmd_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        cur.execute("INSERT INTO articles VALUES (?,?,?,?)", (data.get('photo'), data.get('name'), data.get('age'), data.get('description')))
        db.commit()
        print(data)


    await message.reply('Ура все вийшло')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True)