import asyncio
import time
import os
from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
app = Client("client", api_id, api_hash)

def load_ids():
    try:
        with open("user_ids.txt", "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()


async def get_users(chat_ids: set[str]):
    existing_ids = load_ids()

    async with app:
        i = 1
        for chat_id in chat_ids:
            new_ids = []
            chat = await app.get_chat(int(chat_id))
            async for member in app.get_chat_members(chat.id):
                username = member.user.username
                print(f"{i}. {username}")
                i += 1
                if username and username not in existing_ids:
                    new_ids.append(username)
                    existing_ids.add(username)
            if new_ids:
                with open("user_ids.txt", "a", encoding="utf-8") as f:
                    f.write("\n".join(new_ids) + "\n")


if __name__ == "__main__":
    file = open("chat_ids.txt", "r", encoding="utf-8")
    chat_ids = set(line.strip() for line in file if line.strip()) 
    print(chat_ids)
    app.run(get_users(chat_ids))







