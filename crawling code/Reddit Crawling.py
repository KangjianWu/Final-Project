import praw
import re
import requests
import os
from datetime import datetime, timedelta
import spacy
import geopy
from geopy.geocoders import Nominatim
from collections import Counter

reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     username='your_username',
                     password='your_password',
                     user_agent='your_user_agent')

subreddit = reddit.subreddit('your_subreddit')

nlp = spacy.load('en_core_web_sm')

geolocator = Nominatim(user_agent="your_user_agent")

hot_posts = subreddit.hot(limit=10)

for post in hot_posts:
    print("Title:", post.title)
    print("URL:", post.url)
    print("Score:", post.score)
    print("Number of comments:", post.num_comments)

    post_time = datetime.fromtimestamp(post.created_utc)
    month_ago = datetime.now() - timedelta(days=30)

    if post_time > month_ago:
        post_content = post.selftext

        urls = re.findall('(?P<url>https?://[^\s]+)', post_content)

        for url in urls:
            print("URL in post:", url)

            if url.endswith('.jpg') or url.endswith('.jpeg') or url.endswith('.png'):
                response = requests.get(url)
                with open(os.path.basename(url), 'wb') as f:
                    f.write(response.content)
                print("Image downloaded:", os.path.basename(url))

            elif url.endswith('.mp4'):
                response = requests.get(url)
                with open(os.path.basename(url), 'wb') as f:
                    f.write(response.content)
                print("Video downloaded:", os.path.basename(url))

        comments = post.comments.list()

        for comment in comments:
            print("Author:", comment.author)
            print("Content:", comment.body)
            print("Upvotes:", comment.score)
            print("Replies:", len(comment.replies))

            # Check if comment contains keyword
            if 'keyword' in comment.body.lower():
                print("Keyword found in comment:", comment.body)
                reply = "Thank you for mentioning the keyword! Here's some information on it: ..."
                comment.reply(reply)
                print("Replied to comment")

        doc = nlp(post_content)
        keywords = []
        for token in doc:
            if not token.is_stop and token.is_alpha and len(token.text) > 3:
                keywords.append(token.lemma_)

        keyword_counts = Counter(keywords)
        print("Keyword counts:", keyword_counts)

        locations = []
        for ent in doc.ents:
            if ent.label_ == 'GPE':
                locations.append(ent.text)
        for location in locations:
            try:
                geocode = geolocator.geocode(location)
                print("Location:", location)
                print("Latitude:", geocode.latitude)
                print("Longitude:", geocode.longitude)
            except:
                print("Error geocoding location:", location)

        # Automatically post to subreddit
        if 'keyword' in post.title.lower():
            title = "New information on the keyword"
            content = "Here's some new information on the keyword: ..."
            subreddit.submit(title, selftext=content)
            print("Posted to subreddit")

        print("=====================================")

        # Save post and comment data to file
        with open('post_data.txt', 'a') as f:
            f.write(f"Title: {post.title}\n")
            f.write(f"URL: {post.url}\n")
            f.write(f"Score: {post.score}\n")
            f.write(f"Number of comments: {post.num_comments}\n")
            f.write(f"Post content: {post_content}\n")
            f.write(f"Keyword counts: {keyword_counts}\n")
            f.write(f"Locations: {locations}\n")
            f.write("=====================================\n")

        for comment in comments:
            with open('comment_data.txt', 'a') as f:
                f.write(f"Author: {comment.author}\n")
                f.write(f"Content: {comment.body}\n")
                f.write(f"Upvotes: {comment.score}\n")
                f.write(f"Replies: {len(comment.replies)}\n")
                f.write("=====================================\n")
