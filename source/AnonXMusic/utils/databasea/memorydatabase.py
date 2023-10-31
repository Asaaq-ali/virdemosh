
from config import PRIVATE_BOT_MODE
from AnonXMusic.core.mongo import mongodb


commanddb = mongodb.commands



# Shifting to memory [ mongo sucks often]

command = []





async def is_commanddelete_on(chat_id: int) -> bool:
    if chat_id not in command:
        return True
    else:
        return False


async def commanddelete_off(chat_id: int):
    if chat_id not in command:
        command.append(chat_id)


async def commanddelete_on(chat_id: int):
    try:
        command.remove(chat_id)
    except:
        pass
