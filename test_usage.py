from danbooru.danbooru import Danbooru

api = Danbooru(username='USERNAME_HERE', api_key="API_KEY_HERE")


posts = api.search_posts(tags='DUMMY TAGS HERE', rating='s', limit=5)

if posts:
    for post in posts:
        print(post['file_url'])
else:
    print("No posts found.")