from datetime import date

from django.shortcuts import render

all_posts = [
  {
    "slug": "hike-in-the-mountains",
    "image": "mountains.jpg",
    "author": "Tero",
    "date": date(2022, 2, 24),
    "title": "Mountain Hiking",
    "excerpt": """There is nothing like the views you get when hiking in the 
          mountains! And i wasn't even prepared for what happened whilst I 
          was enjoying the view!""",
    "content": """
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
      quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
      consequat.
    """
  },
  {
    "slug": "programming-is-fun",
    "image": "coding.jpg",
    "author": "Tero",
    "date": date(2022, 2, 24),
    "title": "Programming is Great",
    "excerpt": """Did you ever spend hours searching that one error in your code?""",
    "content": """
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
      quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
      consequat.
    """
  },
  {
    "slug": "into-the-woods",
    "image": "woods.jpg",
    "author": "Tero",
    "date": date(2022, 2, 24),
    "title": "Nature At Its Best",
    "excerpt": """Nature is Amazing!""",
    "content": """
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
      quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
      consequat.
    """
  },
]

def get_date(post):
  return post['date']

# Create your views here.

def starting_page(request):
  sorted_posts = sorted(all_posts, key=get_date)
  latest_posts = sorted_posts[-3:]
  return render(request, "blog/index.html", {
    "posts": latest_posts
  })

def posts(request):
  return render(request, "blog/all-posts.html", {
    "all_posts": all_posts
  })

def post_detail(request, slug):
  identified_post = next(post for post in all_posts if post['slug'] == slug)
  return render(request, "blog/post-detail.html", {
    "post": identified_post
  })