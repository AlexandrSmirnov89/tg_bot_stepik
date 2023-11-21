from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from token_my_bot import token


TOKEN = token

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет, я эхо-бот написанный с помощью aiogram')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Ты можешь написать мне что-то доброе, а я отвечу тем же:3')


@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)


@dp.message(F.voice)
async def send_voice_echo(message: Message):
    await message.reply_voice(message.voice.file_id)


@dp.message(F.video)
async def send_video_echo(message: Message):
    await message.reply_video(message.video.file_id)


@dp.message(F.animation)
async def send_animation_echo(message: Message):
    await message.reply_animation(message.animation.file_id)


@dp.message(F.document)
async def send_document_echo(message: Message):
    await message.reply_document(message.document.file_id)


@dp.message(F.video_note)
async def send_video_note_echo(message: Message):
    await message.reply_video_note(message.video_note.file_id)


@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)