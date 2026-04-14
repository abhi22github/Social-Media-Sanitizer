#Social Media Content Sanitizer
posts = ["User123 : Whites are toxic people",
         "User455 : HI World",
         "User197 :Enjoy !! htpp://www.helper.com",
         "User123 : I hate this society",
         "User455 : I bought my first car today",
         "User197 : I am a bad guy"]

banned_words = ["hate","toxic","bad"]
links_found=[]
moderator_dict={}

Total_posts = len(posts)
cleaned = 0
blocked = 0

for post in posts:
    user,content= post.split(":",1)
    if user not in moderator_dict:
        moderator_dict[user]=0
    flag = False
    for word in banned_words:
        if word in content:
            content = content.replace(word,"******")
            cleaned+=1
            flag = True
    if flag:
        blocked+=1
        moderator_dict[user]+=1
    
    words = content.split()
    for wrd in words:
        if wrd.startswith("http"):
            links_found.append(wrd)

with open("links_found.txt","w") as file:
    for links in links_found:
        file.write(links+"\n")

print("-------------------Posts Report-------------------")
print("Total Posts:",Total_posts)
print("Cleaned :",cleaned)
print("Blocked:",blocked)
print("Moderation Report:")
print(moderator_dict)