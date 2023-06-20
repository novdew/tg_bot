import random
from aiogram import Bot, Dispatcher, executor, types

# Set up the bot
bot_token = 'YOUR BOTS TOKEN'
bot = Bot(token=bot_token)
dp = Dispatcher(bot)

photos_arr = [
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fblog.depositphotos.com%2Fwp-content%2Fuploads%2F2017%2F07%2FSoothing-nature-backgrounds-2-1024x684.jpg&tbnid=BiSGXNM-5qi07M&vet=12ahUKEwij17Hw39H_AhUO6CoKHURbAFAQMyg3egQIARBQ..i&imgrefurl=https%3A%2F%2Fblog.depositphotos.com%2Ffeatured-collection-soothing-nature-backgrounds.html&docid=lGDafPXvgg44_M&w=1024&h=684&q=nature%20photos&client=firefox-b-d&ved=2ahUKEwij17Hw39H_AhUO6CoKHURbAFAQMyg3egQIARBQ",
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.cntraveller.com%2Fphotos%2F611bf0b8f6bd8f17556db5e4%2F4%3A3%2Fpass%2Fgettyimages-1146431497.jpg&tbnid=55c2RP6xQDxuXM&vet=12ahUKEwij17Hw39H_AhUO6CoKHURbAFAQMyhDegQIARBs..i&imgrefurl=https%3A%2F%2Fwww.cntraveller.com%2Fgallery%2Fnature-positive-travel&docid=qMwe4KMTKzA_DM&w=2664&h=1998&q=nature%20photos&client=firefox-b-d&ved=2ahUKEwij17Hw39H_AhUO6CoKHURbAFAQMyhDegQIARBs',
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F1766838%2Fpexels-photo-1766838.jpeg%3Fcs%3Dsrgb%26dl%3Dpexels-baskin-creative-studios-1766838.jpg%26fm%3Djpg&tbnid=jCD5hmjG1ebJhM&vet=12ahUKEwij17Hw39H_AhUO6CoKHURbAFAQMyhEegQIARBu..i&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fnature%2520background%2F&docid=8XuhtxSRxFSBCM&w=4272&h=2848&q=nature%20photos&client=firefox-b-d&ved=2ahUKEwij17Hw39H_AhUO6CoKHURbAFAQMyhEegQIARBu',
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fa-z-animals.com%2Fmedia%2Ftiger_laying_hero_background.jpg&tbnid=D9qFfSsjYyPDpM&vet=12ahUKEwi68OK_4NH_AhXWvIsKHeG5AMkQMygJegUIARDTAQ..i&imgrefurl=https%3A%2F%2Fa-z-animals.com%2Fanimals%2F&docid=oWiIrVw3qh7e7M&w=1000&h=664&q=animal%20photos&client=firefox-b-d&ved=2ahUKEwi68OK_4NH_AhXWvIsKHeG5AMkQMygJegUIARDTAQ',
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.natgeofe.com%2Fk%2Fc02b35d2-bfd7-4ed9-aad4-8e25627cd481%2Fkomodo-dragon-head-on_2x1.jpg&tbnid=AK0dcXcUVx081M&vet=12ahUKEwi68OK_4NH_AhXWvIsKHeG5AMkQMygPegUIARDfAQ..i&imgrefurl=https%3A%2F%2Fkids.nationalgeographic.com%2Fanimals&docid=-OtHMeeNhLrd7M&w=3072&h=1536&q=animal%20photos&client=firefox-b-d&ved=2ahUKEwi68OK_4NH_AhXWvIsKHeG5AMkQMygPegUIARDfAQ',
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.cbc.ca%2Fkids%2Fimages%2Fwild_and_wonderful_asian_animals_header_1140.jpg&tbnid=d8npmXW5N-7dBM&vet=12ahUKEwi68OK_4NH_AhXWvIsKHeG5AMkQMygOegUIARDdAQ..i&imgrefurl=https%3A%2F%2Fwww.cbc.ca%2Fkids%2Farticles%2Fwild-wonderful-asian-animals&docid=Y4uVvJNi4wuHXM&w=1140&h=641&q=animal%20photos&client=firefox-b-d&ved=2ahUKEwi68OK_4NH_AhXWvIsKHeG5AMkQMygOegUIARDdAQ',
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Faldf.org%2Fwp-content%2Fuploads%2F2018%2F05%2Flamb-iStock-665494268-16x9-e1559777676675.jpg&tbnid=YibnX0cR9ME3qM&vet=12ahUKEwi68OK_4NH_AhXWvIsKHeG5AMkQMygZegUIARD4AQ..i&imgrefurl=https%3A%2F%2Faldf.org%2Farticle%2Flaws-that-protect-animals%2F&docid=gn4a-gwncnPn0M&w=1600&h=900&q=animal%20photos&client=firefox-b-d&ved=2ahUKEwi68OK_4NH_AhXWvIsKHeG5AMkQMygZegUIARD4AQ',
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.newyorker.com%2Fphotos%2F62c4511e47222e61f46c2daa%2F4%3A3%2Fw_2663%2Ch_1997%2Cc_limit%2Fshouts-animals-watch-baby-hemingway.jpg&tbnid=WbC-XsfkGAc5DM&vet=12ahUKEwi68OK_4NH_AhXWvIsKHeG5AMkQMyg1egQIARBL..i&imgrefurl=https%3A%2F%2Fwww.newyorker.com%2Fhumor%2Fdaily-shouts%2Fthe-best-animals-to-watch-your-baby-according-to-hemingway&docid=PFItqC0nC-02MM&w=2663&h=1997&q=animal%20photos&client=firefox-b-d&ved=2ahUKEwi68OK_4NH_AhXWvIsKHeG5AMkQMyg1egQIARBL',
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.newyorker.com%2Fphotos%2F5a95a5b13d9089123c9fdb7e%2F1%3A1%2Fw_3289%2Ch_3289%2Cc_limit%2FPetrusich-Dont-Mess-with-the-Birds.jpg&tbnid=LPTXxhDMXxe16M&vet=12ahUKEwiW8JGH4dH_AhUJzYsKHcaPAF4QMygMegUIARDXAQ..i&imgrefurl=https%3A%2F%2Fwww.newyorker.com%2Fculture%2Fculture-desk%2Fdont-mess-with-the-birds&docid=dmNPrfx74HckwM&w=3289&h=3289&q=birds%20photos&client=firefox-b-d&ved=2ahUKEwiW8JGH4dH_AhUJzYsKHcaPAF4QMygMegUIARDXAQ',
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fnatureconservancy-h.assetsadobe.com%2Fis%2Fimage%2Fcontent%2Fdam%2Ftnc%2Fnature%2Fen%2Fphotos%2Fa%2Fm%2FAmericanGoldfinch_MattWilliams_4000x2200.jpg%3Fcrop%3D0%252C0%252C4000%252C2200%26wid%3D4000%26hei%3D2200%26scl%3D1.0&tbnid=DLilV9REgp3-NM&vet=12ahUKEwiW8JGH4dH_AhUJzYsKHcaPAF4QMygiegUIARCJAg..i&imgrefurl=https%3A%2F%2Fwww.nature.org%2Fen-us%2Fabout-us%2Fwhere-we-work%2Fpriority-landscapes%2Fgreat-lakes%2Fstories-in-the-great-lakes%2Fmidwest-backyard-birds%2F&docid=IXUIsNCFzN80nM&w=4000&h=2200&q=birds%20photos&client=firefox-b-d&ved=2ahUKEwiW8JGH4dH_AhUJzYsKHcaPAF4QMygiegUIARCJAg',
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1517960413843-0aee8e2b3285%3Fixlib%3Drb-4.0.3%26ixid%3DM3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8fA%253D%253D%26w%3D1000%26q%3D80&tbnid=9PUg7g57Bl3dPM&vet=12ahUKEwixqrqe4dH_AhUqlosKHSveDWIQMyghegUIARCPAg..i&imgrefurl=https%3A%2F%2Funsplash.com%2Fimages%2Fpeople%2Flife&docid=2O7Xdi_WWoZ7yM&w=1000&h=646&q=photos&client=firefox-b-d&ved=2ahUKEwixqrqe4dH_AhUqlosKHSveDWIQMyghegUIARCPAg',
    'https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.adobe.com%2Fcontent%2Fdam%2Fcc%2Fus%2Fen%2Fcreativecloud%2Fdesign%2Fdiscover%2Fcolorize-black-and-white-photos%2Fdesktop%2Fcolorize_black_and_white_photos_P1_900x420.jpg.img.jpg&tbnid=uHRZYiCurOpsUM&vet=10CMkBEDMoxAFqFwoTCLidy57h0f8CFQAAAAAdAAAAABAD..i&imgrefurl=https%3A%2F%2Fwww.adobe.com%2Fau%2Fcreativecloud%2Fdesign%2Fdiscover%2Fcolorize-black-and-white-photos.html&docid=xXFmNaNuDs8P5M&w=900&h=420&q=photos&client=firefox-b-d&ved=0CMkBEDMoxAFqFwoTCLidy57h0f8CFQAAAAAdAAAAABAD']


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    username = message.from_user.username
    await message.answer(f"Hello, {username}")


# Sends Sticker
@dp.message_handler(commands=['sticker'])
async def send_sticker(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAEJaP5kkXt93lIwTIRR6a7EXNGZ6j6vVgACNy4AAhhlCEhvT3UgKAbTRy8E')


# Sends random photo
@dp.message_handler(commands=['photo'])
async def send_photo(message: types.Message):
    # photo_url = 'https://source.unsplash.com/user/wsanter'
    await bot.send_photo(message.from_user.id, photo=random.choice(photos_arr))


# Answers to unknown commands or messages
@dp.message_handler()
async def send_message(message: types.Message):
    await message.reply(f"{message}❓")
    await message.answer_sticker('CAACAgIAAxkBAAEJaQ9kkX2INo-zdJIq9Qp4tnbA-32zUwACXwADto9KCRmwxQeO_UfwLwQ')


if __name__ == '__main__':
    executor.start_polling(dp)
