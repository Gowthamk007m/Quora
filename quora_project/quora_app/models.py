from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from django.template.defaultfilters import truncatechars

# Create your models here.

    

class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return truncatechars(self.content,50)
    
    def time_since_created(self):
        now = timezone.now()
        delta = now - self.created_at

        if delta.days > 0:
            if delta.days == 1:
                return "1 day ago"
            else:
                return f"{delta.days} days ago"
        elif delta.seconds >= 3600:
            hours = delta.seconds // 3600
            if hours == 1:
                return "1 hour ago"
            else:
                return f"{hours} hours ago"
        elif delta.seconds >= 60:
            minutes = delta.seconds // 60
            if minutes == 1:
                return "1 minute ago"
            else:
                return f"{minutes} minutes ago"
        else:
            return "just now"

class Answer(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='answer_like',blank=True)
    
    def __str__(self):
        return f"Answer to '{self.question.title}' by {self.user.username}"
    
    def number_of_likes(self):
        return self.likes.count()
    
    def time_since_created(self):
        now = timezone.now()
        delta = now - self.created_at

        if delta.days > 0:
            if delta.days == 1:
                return "1 day ago"
            else:
                return f"{delta.days} days ago"
        elif delta.seconds >= 3600:
            hours = delta.seconds // 3600
            if hours == 1:
                return "1 hour ago"
            else:
                return f"{hours} hours ago"
        elif delta.seconds >= 60:
            minutes = delta.seconds // 60
            if minutes == 1:
                return "1 minute ago"
            else:
                return f"{minutes} minutes ago"
        else:
            return "just now"

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='likes')
    
#     def __str__(self):
#         return f"Like by {self.user.username} on {self.answer.user.username}'s answer"
