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

# use ''.join()!!!!!

class SimpleCommands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def gerberSmash(self, ctx):
		await ctx.send(str(gerberGifLink))

	@commands.command()
	async def lst(self, ctx):
		msg = "```\nLinked List: &LLprintMenu```"
		msg += "```\nArray: &ARprintMenu```"
		await ctx.send(msg)

	# --------------------------- linked list stuff -----------------------------------------

	# linked list aux functions
	def printNode(self, val):
		msg = "+-----+\n"
		msg += f"|  {val}  |\n"
		msg += "+-----+\n"
		msg += "   |\n"
		msg += "   v\n"
		return msg

	@commands.command()
	async def LLprintMenu(self, ctx):
		msg = "```\nWhat Linked List operation would you like to perform? (only integers supported)\n"
		msg += "Head Insert: &insertHead [value]\n"
		msg += "Tail Insert: &insertTail [value]\n"
		msg += "Delete: &delete [value]\n"
		msg +="Print current list: &printList\n"
		msg += "Clear list: &CLEARALL```"
		await ctx.send(msg)

	@commands.command()
	async def insertHead(self, ctx, val: int):
		# if not myList:
		# 	await ctx.send("```Nothing in list!```")
		# 	return
		msg = f'```\ninserting {val} at head of list...\n'
		myList.insert(0, val)
		msg += f'inserted!```'
		await ctx.send(msg)

	@commands.command()
	async def insertTail(self, ctx, val: int):
		# if not myList:
		# 	await ctx.send("```Nothing in list!```")
		# 	return
		msg = f'```\ninserting {val} at tail of list...\n'
		myList.append(val)
		msg += f'inserted!```'
		await ctx.send(msg)

	@commands.command()
	async def delete(self, ctx, val: int):
		# if not myList:
		# 	await ctx.send("```Nothing in list!```")
		# 	return
		if val not in myList:
			await ctx.send(f'```\nValue not in list!```')
			return
		msg = f"```deleting {val}...\n"
		myList.remove(val)
		msg += f'deleted!```'
		await ctx.send(msg)

	@commands.command()
	async def printList(self, ctx):
		if not myList:
			await ctx.send("```Nothing in list!```")
			return
		msg = "```\n"
		
		for index, val in enumerate(myList):
			if val == myList[0]:
				msg += '\n'
			msg += f'index: {index}\n'
			msg += self.printNode(val)
		msg += "   X```"
		await ctx.send(msg)

	@commands.command()
	async def CLEARALL(self, ctx):
		if not myList:
			await ctx.send("```Nothing in list!```")
			return
		
		msg = ("```\nClearing...\n")
		myList.clear()
		msg += "Cleared!```"
		await ctx.send(msg)

	# --------------------------------- end linked list stuff ------------------------------------

	# -------------------------------------- array stuff -----------------------------------------

	# array aux functions
	def printEmptyCell(self, index):
		msg = "+-----+\n"
		msg += f"|     |  index: {index}\n"
		return msg
	
	def printCell(self, index, val):
		msg = "+-----+\n"
		msg += f"|  {val}  |  index: {index}\n"
		return msg

	@commands.command()
	async def ARprintMenu(self, ctx):
		msg = "```\nWhat Array operation would you like to perform? (only integers supported)\n"
		msg += "Allocate memory: &allocate [size]\n"
		# msg += "Insert: &insert [value]\n"
		msg += "Insert at index: &insertAtIndex [index] [element]\n"
		msg += "Delete at index: &deleteAtIndex [index]\n"
		msg += "Print current array: &printArray\n"
		msg += "Clear array: &EMPTYARRAY\n"
		msg += "Destroy array: &DESTROYARRAY```"
		await ctx.send(msg)

	@commands.command()
	async def allocate(self, ctx, size: int):
		if not size:
			await ctx.send("```Please enter a size.```")
			return
		if size < 1:
			await ctx.send("```Can't have negative/ 0 size!```")
			return
		msg = f"```\nallocating {size} cells...\n"
		for _ in range(size):
			array.append(None)
		msg += "allocated!```"
		await ctx.send(msg)

	@commands.command()
	async def insertAtIndex(self, ctx, index: int, element: int):
		if not array:
			await ctx.send("```Must allocate space!```")
			return
		elif index >= len(array) or index < 0:
			# SEGFAULT!!!!
			await ctx.send("```Index is out of range!```")
			return
		msg = f"```\ninserting {element} at index {index}...\n"
		array[index] = element
		msg += "...inserted!```"
		await ctx.send(msg)

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

		msg = f"```\ndeleting element at index {index}...\n"
		array[index] = None
		msg += "...deleted!```"
		await ctx.send(msg)
	
	@commands.command()
	async def printArray(self, ctx):
		if not array:
			await ctx.send("```Nothing in array!```")
			return
		
		msg = "```\n"

		for index, element in enumerate(array):
			if element == None:
				msg += self.printEmptyCell(index)
			else:
				msg += self.printCell(index, element)
		msg += "+-----+```"
		await ctx.send(msg)

	@commands.command()
	async def EMPTYARRAY(self, ctx):
		if not array:
			# array is NULL
			await ctx.send("```Nothing in array!```")
			return
		
		msg = "```emptying...\n"
		for index, val in enumerate(array):
			array[index] = None
		msg += "emptied!```"
		await ctx.send(msg)

	@commands.command()
	async def DESTROYARRAY(self, ctx):
		if not array:
			await ctx.send("```Nothing in array!```")
			return
		
		msg = "```destroying...\n"
		array.clear()
		msg += "destroyed!```"
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
