import pandas as pd
import os
from dotenv import load_dotenv
import openai

load_dotenv() # take environment variables from .env

openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = "YOUR_API_KEY"

copied_text = '' # insert the text here (from selenium or smth, since Twitter does not allow HTML apsring with tools like BeautifullSoup)

get_nametags_prompt = f"extract nametags from this text: {copied_text}"
fans_tags = """@savakholin
@Ioofus
@BrandonDoyle
@xxes
@GroovyNFTs
@solana_king
@MarkCrtlC
@KarlJacobs_
@ckonefilm
@crotweet
@LorettaKrypto
@ExAEye
@TheSaaSCFO
@MrBeast"""

make_fans_table_prompt = f""" 
these are twitter name tags:
{fans_tags}
put them in a table, add a columns with a links to profile and two empty columns named "sent_message" and "verified". return json"""



prompt = "Hello, how are you today?"


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": make_fans_table_prompt}]
)

print(response.choices[0].message.content)
