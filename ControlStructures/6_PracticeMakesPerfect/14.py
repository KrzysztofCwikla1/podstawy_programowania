facebook = input("Do you have a Facebook account? (y/n): ")=='y'
twitter = input("Do you have a Twitter account? (y/n): ")=='y'
instagram = input("Do you have an Instagram account? (y/n): ")=='y'
accounts= facebook+twitter+instagram
if accounts>=2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")