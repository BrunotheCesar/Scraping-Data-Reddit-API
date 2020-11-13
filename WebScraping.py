#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Scraping New Zealand subreddit with praw


# In[1]:


import praw


# In[2]:


# Reddit Authentication
reddit = praw.Reddit(client_id='*****', client_secret='*****', user_agent='*****')

# gets 5 new zealand subreddit newest posts along with its up and downvotes count
new_posts = reddit.subreddit('Newzealand').new(limit=5)  
for post in new_posts:
    print('Title: {}, upvotes: {}, downvotes: {}'.format(post.title, post.ups, post.downs))


# In[3]:


# Get all visible commentaries on election night discussion thread
# "error" at the bottom means that there are hidden commentaries that are not showing
submission = reddit.submission(url="https://old.reddit.com/r/newzealand/comments/jcpy2z/election_night_discussion_megathread/")
comments = submission.comments
for comment in comments:
        print(15*'*' + '\n' + comment.body)


# In[4]:


# Creates parent and comment id for tracking and discussion purposes
submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
    print(15*'*')
    print('Parent ID:', comment.parent())
    print('Comment ID:', comment.id)
    print(comment.body)


# In[5]:


# gets all comments in thread and gets rid of the above "morecomments" error
submission = reddit.submission(url="https://old.reddit.com/r/newzealand/comments/jcpy2z/election_night_discussion_megathread/")
submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
    print(comment.body)

