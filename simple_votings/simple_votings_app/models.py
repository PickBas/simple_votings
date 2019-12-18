# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


class modelTest(models.Model):
    question = models.CharField(max_length=50)
    click_count = models.IntegerField()


class Voting(models.Model):
    text = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    start = models.DateTimeField(auto_now=True)

    # answer =models.ManyToManyField(VotingAnswer)

    def __str__(self):
        "При добавлении будет отображатся text а не Объект"
        return "%s" % (self.text)

    def __unicode__(self):
        "При добавлении будет отображатся text а не Объект"
        return u'%s' % (self.text)

    def answers(self):
        return VotingAnswer.objects.filter(voting=self)
    # TODO: Добавить дату окончания



class VotingAnswer(models.Model):
    text = models.CharField(max_length=200)
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)

    def __unicode__(self):
        "При добавлении будет отображатся text а не Объект"
        return self.text

    def action(self):
        return "/vote/" + str(self.id)

    def votes(self):
        return Vote.objects.filter(answer=self)

    def votes_count(self):
        return len(self.votes())


class Vote(models.Model):
    answer = models.ForeignKey(to=VotingAnswer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)



# TODO: Добавить модель комментариев
class Example(models.Model):
    number = models.IntegerField(default=1)
    date = models.DateTimeField()
    text = models.CharField(max_length=200)
    galochka = models.BooleanField(blank=False)


class ExampleAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'text', 'galochka')


class VotingAdmin(admin.ModelAdmin):
    list_display = ('text', 'likes', 'start')


class VotingAnswerAdmin(admin.ModelAdmin):
    list_display = ('text', )


admin.site.register(Example, ExampleAdmin)
admin.site.register(Voting, VotingAdmin)
admin.site.register(VotingAnswer, VotingAnswerAdmin)