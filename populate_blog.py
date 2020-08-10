import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alina_blog.settings')

import django

django.setup()
from blog.models import Post
from datetime import datetime


def populate():
    posts = {
        "first_post": {
            "title": "Clever note",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt "
                       "ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
                       "ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
                       "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
                       "occaecat "
                       "cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "created_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },

        "second_post": {
            "title": "Not so clever",
            "content": "some jibberish",
            "created_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    }

    def add_post(title, content, created_on):
        p = Post.objects.get_or_create(title=title)[0]
        p.content = content
        p.created_on = created_on
        p.save()
        return p

    for post, post_insides in posts.items():
        p = add_post(title=post_insides["title"], content=post_insides["content"],
                     created_on=post_insides["created_on"])
        p.save()

    for p in Post.objects.all():
        print('{0}'.format(str(p)))


if __name__ == "__main__":
    print("Running alinochka blog script...")
    populate()