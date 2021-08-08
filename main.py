import instaloader

bot = instaloader.Instaloader()

username = "username"

print(bot.download_profile(username, profile_pic_only=True))

