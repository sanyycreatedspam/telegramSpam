from telethon import TelegramClient, events
import asyncio

api_id = 20098943
api_hash = '11cfa0038b2cb8e4a7bd214d6c1c26c4'
phone_number = '+995575757547'

client = TelegramClient('user_session', api_id, api_hash)

stop_flag = False

@client.on(events.NewMessage(outgoing=True, pattern=r'/start'))
async def handler(event):
    global stop_flag
    stop_flag = False
    n = 1000
    await event.respond("DEV:@kartveli_official\nНачинаю спам 1000−7−7...")
    while n > 7 and not stop_flag:
        next_n = n - 7
        await client.send_message(await event.get_input_chat(), f"{n}-7={next_n}")
        n = next_n
        await asyncio.sleep(0.1)
    if not stop_flag:
        await client.send_message(await event.get_input_chat(), "Готово!")
    else:
        await client.send_message(await event.get_input_chat(), "⛔ Остановлено командой /stop.")

@client.on(events.NewMessage(outgoing=True, pattern=r'/stop'))
async def stop_handler(event):
    global stop_flag
    stop_flag = True
    await event.respond("🛑 Команда /stop получена. Останавливаю спам.")

async def main():
    await client.start(phone=phone_number)
    await client.run_until_disconnected()

client.loop.run_until_complete(main())