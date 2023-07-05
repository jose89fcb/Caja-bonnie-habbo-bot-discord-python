import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time

from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

slash = SlashCommand(bot, sync_commands=True)
@slash.slash(
    name="caja", description="Keko habbo Hotel",
    options=[
                create_option(
                  name="keko",
                  description="Escribe el keko",
                  option_type=3,
                  required=True
                ),
               
    
                  create_option(
                  name="fondos",
                  description="Elige él fondo",
                  option_type=3,
                  required=True,
                  choices=[
                      create_choice(
                          name="Fondo Nieve",
                          value="FondoNieve"
                         
                      ),
                      create_choice(
                          name="Fondo Palmera",
                          value="FondoPalmeras"
                          
                      ),
                      create_choice(
                          name="Fondo Rosas",
                          value="FondoRosas"
                         
                      ),
                     
                      
                    
                  ],
                  
                
               
                  
                
                  
                  
                
               
                  
                ),
                create_option(
                  name="hotel",
                  description="Elige él hotel",
                  option_type=3,
                  required=True,
                  choices=[
                      create_choice(
                          name="ES - Hotel España",
                          value="es"
                      ),
                      create_choice(
                          name="BR - Hotel Brasil",
                          value="com.br"
                      ),
                      create_choice(
                          name="COM - Hotel Estados unidos",
                          value="com"
                      ),
                      create_choice(
                          name="DE - Hotel Aleman",
                          value="de"
                      ),
                      create_choice(
                          name="FR - Hotel Frances",
                          value="fr"
                      ),
                      create_choice(
                          name="FI - Hotel Finalandia",
                          value="fi"
                      ),
                      create_choice(
                          name="IT - Hotel Italiano",
                          value="it"
                      ),
                      create_choice(
                          name="TR - Hotel Turquia",
                          value="com.tr"
                      ),
                      create_choice(
                          name="NL - Hotel Holandés",
                          value="nl"
                      )
                  ]
                
               
                  
                )
             ])

                  
                
               
                 
            


async def _caja(ctx:SlashContext, keko, hotel, fondos):
    await ctx.defer()
    
    response = requests.get(f"https://www.habbo.{hotel}/api/public/users?name={keko}")
  
   
    try:

     habbo = response.json()['figureString']
     
    except KeyError:
        await ctx.send("El keko no existe!") 
   

   
    ##
    # programado Por jose89fcb
    ###

    
    
   
    try:

     url = "https://www.habbo.com/habbo-imaging/avatarimage?size=m&figure="+ habbo +"&action=none&direction=4&head_direction=4&gesture=std&size=m"
     img1 = Image.open(io.BytesIO(requests.get(url).content))
     img1 = img1.resize((64,110), Image.ANTIALIAS)#tamaño del keko 1

  
    
    


    
    


    

   

    

    
    
    



     img2 = img1.copy()
    
    
    ###

    


     cristalDerecho = Image.open(r"imagenes/cristalDerecho.png").convert("RGBA") #imagen
     img1 = cristalDerecho.resize((138,295), Image.ANTIALIAS)#tamaño de la cristalDerecho

     cristalizquierdo = Image.open(r"imagenes/cristalizquierdo.png").convert("RGBA") #imagen
     img1 = cristalizquierdo.resize((138,295), Image.ANTIALIAS)#tamaño de la cristalizquierdo


    ###
  
    ###
     almo = Image.open(r"imagenes/caja.png").convert("RGBA") #imagen
     img1 = almo.resize((138,295), Image.ANTIALIAS)#tamaño de la caja

    ###
     fondos = Image.open(r"imagenes/" +fondos+".png").convert("RGBA") #imagen
     img1 = fondos.resize((138,295), Image.ANTIALIAS)#tamaño de los fondos

    
    

 
   
    
    
    
     
     img1.paste(fondos,(0,0), mask = fondos) #Posicion de FondoNieve.png
    
     img1.paste(img2,(35,90), mask = img2) #Posicion del keko 1
     img1.paste(almo,(0,0), mask = almo) #Posicion de la caja
    
   
     
     img1.paste(cristalDerecho,(0,0), mask = cristalDerecho) #cristalDerecho

     img1.paste(cristalizquierdo,(0,0), mask = cristalizquierdo) #cristalizquierdo
     
    
     
  

    
    ### 

    
    
   
    
   ###
   
    
   
    ###
    
   
 
    
    
  ####
   
  ###
    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
     with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(f"`{keko}`", file=discord.File(fp=image_binary, filename='keko.png'))
    except UnboundLocalError:
       habbo=":("    
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   