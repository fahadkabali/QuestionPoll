from django.db import models

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	choice_text = models.CharField(max_length = 200)
	selections = models.IntegerField(default = 0)

	def __str__(self):
		return self.choice_text





# from django.db import models
# from django.conf import settings

# class Question(models.Model):
#     text = models.CharField(max_length=255, unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.text

# class Option(models.Model):
#     question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
#     text = models.CharField(max_length=255)
#     Option_list= models.IntegerField(default=0)

#     def __str__(self):
#         return self.text

# class Response(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.question.text} - {self.selected_option.text}"

# class Feedback(models.Model):
#     response = models.OneToOneField(Response, on_delete=models.CASCADE)
#     feedback_text = models.TextField()
#     satisfaction_score = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Feedback for {self.response}"
