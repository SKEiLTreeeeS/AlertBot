import time
import logging
from bs4 import BeautifulSoup
import requests
from aiogram import Bot, Dispatcher, executor, types

Token = "5962272909:AAEXM4bM-JmDlL0hhjUl75HMU8FQYqDssA8"
bot = Bot(token=Token)
dp = Dispatcher(bot=bot)
MSG = "В настоящий момент цена биткоина - {}. Будьте аккуратны, новый ценовой диапазон!"

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}!")

    MemoryBTC = 0
    BitcoinPriceMassiv = []
    BitcoinPriceHTML = []
    BitcoinPriceCutMassiv = []

    while MemoryBTC != -1:

        url = 'https://coinmarketcap.com/currencies/bitcoin/markets/'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        BitcoinPriceHTML = soup.find("div", class_='priceValue').text
        print(BitcoinPriceHTML)

        for i in range(len(BitcoinPriceHTML)):
            if BitcoinPriceHTML[i] in '.':
                break
            else:
                if BitcoinPriceHTML[i] in '0123456789':
                    BitcoinPriceMassiv.append(BitcoinPriceHTML[i])
        print(BitcoinPriceMassiv)

        if len(BitcoinPriceMassiv) == 5:
            BitcoinPriceCutMassiv.append(BitcoinPriceMassiv[2])
            BitcoinPriceCutMassiv.append(BitcoinPriceMassiv[3])
            BitcoinPriceCutMassiv.append(BitcoinPriceMassiv[4])
        print(BitcoinPriceCutMassiv)
        BitcoinPriceCut = int(''.join(map(str, BitcoinPriceCutMassiv)))
        print(BitcoinPriceCut)
        print(MemoryBTC)

        if BitcoinPriceCut in range(0, 99) and not(MemoryBTC in range(0, 99)):
            await bot.send_message(user_id, MSG.format(BitcoinPriceHTML))
            MemoryBTC = BitcoinPriceCut
        if BitcoinPriceCut in range(100, 199) and not(MemoryBTC in range(100, 199)):
            await bot.send_message(user_id, MSG.format(BitcoinPriceHTML))
            MemoryBTC = BitcoinPriceCut
        if BitcoinPriceCut in range(200, 299) and not(MemoryBTC in range(200, 299)):
            await bot.send_message(user_id, MSG.format(BitcoinPriceHTML))
            MemoryBTC = BitcoinPriceCut
        if BitcoinPriceCut in range(300, 399) and not(MemoryBTC in range(300, 399)):
            await bot.send_message(user_id, MSG.format(BitcoinPriceHTML))
            MemoryBTC = BitcoinPriceCut
        if BitcoinPriceCut in range(400, 499) and not(MemoryBTC in range(400, 499)):
            await bot.send_message(user_id, MSG.format(BitcoinPriceHTML))
            MemoryBTC = BitcoinPriceCut
        if BitcoinPriceCut in range(500, 599) and not(MemoryBTC in range(500, 599)):
            await bot.send_message(user_id, MSG.format(BitcoinPriceHTML))
            MemoryBTC = BitcoinPriceCut
        if BitcoinPriceCut in range(600, 699) and not(MemoryBTC in range(600, 699)):
            await bot.send_message(user_id, MSG.format(BitcoinPriceHTML))
            MemoryBTC = BitcoinPriceCut
        if BitcoinPriceCut in range(700, 799) and not(MemoryBTC in range(700, 799)):
            await bot.send_message(user_id, MSG.format(BitcoinPriceHTML))
            MemoryBTC = BitcoinPriceCut
        if BitcoinPriceCut in range(800, 899) and not(MemoryBTC in range(800, 899)):
            await bot.send_message(user_id, MSG.format(BitcoinPriceHTML))
            MemoryBTC = BitcoinPriceCut
        if BitcoinPriceCut in range(900, 999) and not(MemoryBTC in range(900, 999)):
            await bot.send_message(user_id, MSG.format(BitcoinPriceHTML))
            MemoryBTC = BitcoinPriceCut
        BitcoinPriceMassiv = []
        BitcoinPriceCutMassiv = []
        time.sleep(30)

if __name__ == '__main__':
    executor.start_polling(dp)