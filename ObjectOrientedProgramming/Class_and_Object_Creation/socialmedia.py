class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    def display_timeline(self):
        print(f"Timeline for {self.username}:")
        for i, post in enumerate(self.posts, start=1):
            print(f"{i}. {post}")
profile = SocialMediaProfile("johndoe")
profile.add_post("Hello, world!")
profile.add_post("Had a great day at the park!")
profile.add_post("What's up, Natalie? How are you?")
profile.display_timeline()

