from django.shortcuts import render
from django.urls import reverse_lazy

posts = [
    {
        "slug": "the-mountains",
        "image":"AdventureVacations.jpeg",
        "title": "Hiking Trip",
        "author":"Neil",
        "timeStamp": "09-27-2022",
        "briefDescription": "This was an adventurous trip i had back in 2019 during the pandamic along with my friends.Had lots of stories to tell and memories made. The view in the morning from the hill was simply breath-taking. You must camp atleast once in your life time.",
        "content":"""
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dicta, delectus. Hic laudantium eius placeat eum natus corrupti praesentium, a, 
        doloremque provident quod reprehenderit iusto, earum cum voluptatibus velit perspiciatis ratione!

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dicta, delectus. Hic laudantium eius placeat eum natus corrupti praesentium, a, 
        doloremque provident quod reprehenderit iusto, earum cum voluptatibus velit perspiciatis ratione!
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dicta, delectus. Hic laudantium eius placeat eum natus corrupti praesentium, a, 
        doloremque provident quod reprehenderit iusto, earum cum voluptatibus velit perspiciatis ratione!
        """
    },
    {
        "slug": "camping-trip",
        "image":"campingVacation.jpeg",
        "title": "Camping Trip",
        "author":"Neil",
        "timeStamp": "10-18-2022",
        "briefDescription": "This was an adventurous trip i had back in 2019 during the pandamic along with my friends.Had lots of stories to tell and memories made. The view in the morning from the hill was simply breath-taking. You must camp atleast once in your life time.",
        "content":"""
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dicta, delectus. Hic laudantium eius placeat eum natus corrupti praesentium, a, 
        doloremque provident quod reprehenderit iusto, earum cum voluptatibus velit perspiciatis ratione!

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dicta, delectus. Hic laudantium eius placeat eum natus corrupti praesentium, a, 
        doloremque provident quod reprehenderit iusto, earum cum voluptatibus velit perspiciatis ratione!
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dicta, delectus. Hic laudantium eius placeat eum natus corrupti praesentium, a, 
        doloremque provident quod reprehenderit iusto, earum cum voluptatibus velit perspiciatis ratione!
        """
    },
    {
        "slug": "resort",
        "image":"resort.jpeg",
        "title": "Staycation Trip",
        "author":"Neil",
        "timeStamp": "11-20-2022",
        "briefDescription": "This was an adventurous trip i had back in 2019 during the pandamic along with my friends.Had lots of stories to tell and memories made. The view in the morning from the hill was simply breath-taking. You must camp atleast once in your life time.",
        "content":"""
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dicta, delectus. Hic laudantium eius placeat eum natus corrupti praesentium, a, 
        doloremque provident quod reprehenderit iusto, earum cum voluptatibus velit perspiciatis ratione!

        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dicta, delectus. Hic laudantium eius placeat eum natus corrupti praesentium, a, 
        doloremque provident quod reprehenderit iusto, earum cum voluptatibus velit perspiciatis ratione!
        
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dicta, delectus. Hic laudantium eius placeat eum natus corrupti praesentium, a, 
        doloremque provident quod reprehenderit iusto, earum cum voluptatibus velit perspiciatis ratione!
        """
    }
]

# Create your views here.
def indexPage(request):
    displayPosts = posts[-1:]
    context = {
        "posts" : displayPosts
    }    
    return render(request,"blog/index.html", context)

def blogsPage(request):
    allPosts = posts
    context = {
        "allPosts" : allPosts
    }    
    return render(request,"blog/blogsPage.html",context)

def blogDetailPage(request, slug):
    identifiedPost = next(post for post in posts if post["slug"] == slug) # next() finds the next element that matches a certain condition. The condition that is met is list comprehension.
    context = {
        "post": identifiedPost
    }
    return render(request, "blog/singleBlogDetail.html", context)