import discord
from discord.ext import commands
import random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 🌱 Banco completo de ideias
ideias = {
    "lata": [
        "🎨 Porta-lápis personalizado",
        "🌱 Vaso para suculentas",
        "🕯 Porta-vela decorativo",
        "🎧 Amplificador de som para celular",
        "🍴 Organizador de talheres",
        "🎁 Embalagem criativa para presente"
    ],

    "pote de vidro": [
        "💡 Luminária com pisca-pisca",
        "🌾 Porta-temperos ou grãos",
        "🧁 Pote para sobremesas",
        "🕯 Porta-velas aromáticas",
        "💰 Cofrinho sustentável",
        "🖌 Porta-pincéis",
        "🧴 Dispenser de sabonete líquido"
    ],

    "caixa de papelão": [
        "📚 Organizador de livros",
        "🐱 Casinha para pet",
        "🎮 Suporte para notebook",
        "🗂 Divisórias de gaveta",
        "🎭 Fantasia criativa",
        "🎁 Caixa decorada para presente",
        "🎨 Mural de fotos"
    ],

    "garrafa pet": [
        "🌱 Vaso estiloso para plantas",
        "💡 Luminária criativa",
        "🖊 Organizador de lápis",
        "🐷 Cofrinho ecológico",
        "🚿 Regador caseiro",
        "🧴 Porta-objetos"
    ],

    "camiseta velha": [
        "👜 Transformar em ecobag",
        "🛏 Capa de almofada personalizada",
        "🎨 Customizar e reinventar",
        "🧹 Pano reutilizável",
        "🧶 Tapete trançado",
        "🎀 Faixa ou acessório"
    ]
}

# 🎮 Desafios
desafios = [
    "🔥 Desafio da semana: reutilize algo da sua casa e conte no chat!",
    "🌎 Tire foto de algo reciclado por você!",
    "💚 Passe 1 dia sem usar plástico descartável!",
    "♻️ Transforme uma lata em algo útil!",
    "🌱 Reutilize uma garrafa PET de forma criativa!"
]

# 🏆 Sistema de pontos
pontos = {}

@bot.event
async def on_ready():
    print(f"🌿 EcoBot conectado como {bot.user}")

# 💡 Comando reutilizar
@bot.command()
async def reutilizar(ctx, *, material: str):
    material = material.lower()

    if material in ideias:
        embed = discord.Embed(
            title="♻️ Ideias Sustentáveis",
            description=f"Aqui vão ideias para **{material}**:",
            color=0x00ff88
        )

        for ideia in ideias[material]:
            embed.add_field(name=" Ideia", value=ideia, inline=False)

        await ctx.send(embed=embed)
    else:
        await ctx.send("😢 Ainda não tenho ideias para esse material... tente outro!")

# 🎲 Desafio
@bot.command()
async def desafio(ctx):
    desafio_escolhido = random.choice(desafios)
    await ctx.send(f"🎯 {desafio_escolhido}")

# 🏆 Ganhar ponto
@bot.command()
async def ganhar_ponto(ctx):
    usuario = ctx.author.id
    pontos[usuario] = pontos.get(usuario, 0) + 10
    await ctx.send(f"🏆 {ctx.author.mention} ganhou 10 pontos ecológicos!")

# 🌱 Ver pontos
@bot.command()
async def meus_pontos(ctx):
    usuario = ctx.author.id
    total = pontos.get(usuario, 0)
    await ctx.send(f"🌿 {ctx.author.mention} você tem {total} pontos ecológicos!")

bot.run("MTQ3NjMxMzMzNzYxNTg3NjIwNw.GAut8E.cl2K4lZaIcdxa6MlaLf895xQxmhBJRD7QtSqvw")