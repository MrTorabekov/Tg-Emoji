import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from random import choice
from datetime import datetime

TOKEN = "7163530590:AAEQ_e86WsCKTgOxPtRdY2Vw81-n0MTFCyk"
bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message) -> None:
    emo = ["👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤‍🔥", "🌚", "🌭", "💯", "🤣", "⚡", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍", "🤗", "🫡", "🎅", "🎄", "☃", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂", "🤷", "🤷‍♀", "😡"]
    react = types.ReactionTypeEmoji(emoji=choice(emo))
    await message.react([react])
    await message.answer(f"Hello, {message.from_user.first_name}!")

async def main() -> None:
    print(f"program started at {datetime.now()}")

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"program finished at {datetime.now()}")