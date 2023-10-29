import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def bot_info(Bot):
    DOB_Bot = "21.05.23"
    INFO_Bot = "Это мой первый бот!"

    if Bot == "DOB":
        return DOB_Bot
    
    elif Bot == "INF":
        return INFO_Bot