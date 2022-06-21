class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


pol = BlogPost(user_name='Pol', text='Hi Pol', number_of_likes=1)
jack = BlogPost(user_name='Jack', text='Hi Jack', number_of_likes=2)

jack.number_of_likes = 100

print(pol.user_name, pol.text, pol.number_of_likes)
print(jack.user_name, jack.text, jack.number_of_likes)
