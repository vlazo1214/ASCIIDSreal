# ASCIIDS

import asyncio

import os
import time
import ctypes
import discord
import youtube_dl

from discord.ext import commands

# Load hidden .env variables
from dotenv import load_dotenv
load_dotenv()

ffmpeg_options = {
	'options': '-vn',
}


gerberGifLink = 'https://github.com/vlazo1214/gerberSmash/blob/main/gerberSmash.gif?raw=true'
helpTxt = 'https://github.com/vlazo1214/gerberSmash/blob/main/help.txt?raw=true'

myList =[]
array = []

class SimpleCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def gerberSmash(self, ctx):
		await ctx.send(str(gerberGifLink))

	@commands.command()
	async def lst(self, ctx):
		msg = ["```\nLinked List: &LLprintMenu```", "```\nArray: &ARprintMenu```"]
		ret = "".join(msg)
		await ctx.send(ret)

	# --------------------------- linked list stuff -----------------------------------------

	# linked list aux functions
	def printNode(self, val):
		msg = ["+-----+\n",
		f"|  {val}  |\n",
		"+-----+\n",
		"   |\n",
		"   v\n"
		]
		ret = "".join(msg)
		return ret

	@commands.command()
	async def LLprintMenu(self, ctx):
		msg = [
			"```\nWhat Linked List operation would you like to perform? (only integers supported)\n", 
			"Head Insert: &insertHead [value]\n",
			"Tail Insert: &insertTail [value]\n",
			"Delete: &delete [value]\n",
			"Print current list: &printList\n",
			"Clear list: &CLEARALL```"
			]
		ret = "".join(msg)
		await ctx.send(ret)

	@commands.command()
	async def insertHead(self, ctx, val: int):
		# if not myList:
		# 	await ctx.send("```Nothing in list!```")
		# 	return
		myList.insert(0, val)
		ret = "".join(f'```\ninserted {val} at head of list!\n```')
		await ctx.send(ret)

	@commands.command()
	async def insertTail(self, ctx, val: int):
		# if not myList:
		# 	await ctx.send("```Nothing in list!```")
		# 	return
		myList.append(val)
		ret = "".join(f'```\ninserted {val} at tail of list!\n```')
		await ctx.send(ret)

	@commands.command()
	async def delete(self, ctx, val: int):
		# if not myList:
		# 	await ctx.send("```Nothing in list!```")
		# 	return
		if val not in myList:
			await ctx.send(f'```\nValue not in list!```')
			return
		myList.remove(val)
		ret = "".join(f"```deleted {val}!\n```")
		await ctx.send(ret)

	@commands.command()
	async def printList(self, ctx):
		if not myList:
			ret = "".join("```Nothing in list!```")
			await ctx.send(ret)
			return
		msg = ["```\n"]
		
		for index, val in enumerate(myList):
			if val == myList[0]:
				msg.append('\n')
			msg.append(f'index: {index}\n')
			msg.append(self.printNode(val))
		msg.append("   X```")
		ret = "".join(msg)
		await ctx.send(ret)

	@commands.command()
	async def CLEARALL(self, ctx):
		if not myList:
			await ctx.send("```Nothing in list!```")
			return
		
		myList.clear()
		ret = "".join("```\nCleared!\n```")
		await ctx.send(ret)

	# --------------------------------- end linked list stuff ------------------------------------

	# -------------------------------------- array stuff -----------------------------------------

	# array aux functions
	def printEmptyCell(self, index):
		msg = ["+-----+\n",
			f"|     |  index: {index}\n"
		]

		ret = "".join(msg)
		return ret
	
	def printCell(self, index, val):
		msg = ["+-----+\n",
			f"|  {val}  |  index: {index}\n"
		]

		ret = "".join(msg)
		return ret

	@commands.command()
	async def ARprintMenu(self, ctx):
		msg = ["```\nWhat Array operation would you like to perform? (only integers supported)\n",
		"Allocate memory: &allocate [size]\n",
		# msg += "Insert: &insert [value]\n"
		"Insert at index: &insertAtIndex [index] [element]\n",
		"Delete at index: &deleteAtIndex [index]\n",
		"Print current array: &printArray\n",
		"Clear array: &EMPTYARRAY\n",
		"Destroy array: &DESTROYARRAY```"
		]

		ret = "".join(msg)
		await ctx.send(ret)

	@commands.command()
	async def allocate(self, ctx, size: int):
		if not size:
			await ctx.send("```Please enter a size.```")
			return
		if size < 1:
			await ctx.send("```Can't have negative/ 0 size!```")
			return
		for _ in range(size):
			array.append(None)
		msg = [f"```\nallocated {size} cells!\n```"]
		ret = "".join(msg)
		await ctx.send(ret)

	@commands.command()
	async def insertAtIndex(self, ctx, index: int, element: int):
		if not array:
			await ctx.send("```Must allocate space!```")
			return
		elif index >= len(array) or index < 0:
			# SEGFAULT!!!!
			await ctx.send("```Index is out of range! (Segfault!)```")
			return
		array[index] = element
		msg = [f"```\ninserted {element} at index {index}!\n```"]
		ret = "".join(msg)
		await ctx.send(ret)

	@commands.command()
	async def deleteAtIndex(self, ctx, index: int):
		if not array:
			await ctx.send("```Must allocate space!```")
			return
		elif index >= len(array) or index < 0:
			await ctx.send("```Index is out of range!```")
			return
		elif array[index] == None:
			await ctx.send("```Nothing to delete!```")
			return

		array[index] = None
		msg = f"```\ndeleted element at index {index}!\n"
		ret = "".join(msg)
		await ctx.send(ret)
	
	@commands.command()
	async def printArray(self, ctx):
		if not array:
			await ctx.send("```Nothing in array!```")
			return
		
		msg = ["```\n"]

		for index, element in enumerate(array):
			if element == None:
				msg.append[self.printEmptyCell(index)]
			else:
				msg.append[self.printCell(index, element)]
		msg.append("+-----+```")
		ret = "".join(msg)
		await ctx.send(ret)

	@commands.command()
	async def EMPTYARRAY(self, ctx):
		if not array:
			# array is NULL
			await ctx.send("```Nothing in array!```")
			return
		
		for index, val in enumerate(array):
			array[index] = None
		msg = ["```emptied!```"]
		ret = "".join(msg)
		await ctx.send(ret)

	@commands.command()
	async def DESTROYARRAY(self, ctx):
		if not array:
			await ctx.send("```Nothing in array!```")
			return
		
		array.clear()
		msg = "```destroyed!\n```"
		await ctx.send(msg)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
	command_prefix=commands.when_mentioned_or("&"),
	description='Relatively simple music bot example',
	intents=intents,
)


@bot.event
async def on_ready():
	print(f'Logged in as {bot.user} (ID: {bot.user.id})')
	print('------')


async def main():
	async with bot:
		await bot.add_cog(SimpleCommands(bot))
		await bot.start(os.getenv('BOT_TOKEN'))


asyncio.run(main())
