 
from django.db import madels

class Question(models.Model):
	class Meta:
		verbose_name = '質問'
		verbose_name_plural = '質問の複数形'
		ordering = ['-pub_date']

	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

    	def __str__(self):
        	return self.question_text

class Choice(models.Model):
	class Meta:
		verbose_name = '選択'
		verbose_name_plural = '選択の複数形'

	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
