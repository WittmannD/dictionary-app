from django.conf import settings
from django.db import models

# Create your models here.
class Dictionary_language(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=250)

class Part_of_speech(models.Model):
    name = models.CharField(max_length=250)

class Dictionary_word(models.Model):
    word_text = models.TextField()
    definition = models.TextField()
    frequency = models.DecimalField(max_digits=6, decimal_places=2)
    part_of_speech = models.ForeignKey(
        "Part_of_speech", on_delete=models.DO_NOTHING)
    language = models.ForeignKey(
        "Dictionary_language", on_delete=models.DO_NOTHING)

class Dictionary_word_modification(models.Model):
    type = models.TextField()
    value = models.TextField()
    word = models.ForeignKey(
        "Dictionary_word", on_delete=models.DO_NOTHING)

class Dictionary_synonym(models.Model):
    type = models.TextField()
    value = models.TextField()
    synonym_word_1 = models.ForeignKey(
        "Dictionary_word", on_delete=models.DO_NOTHING, related_name='%(class)s_synonym_word_1')
    synonym_word_2 = models.ForeignKey(
        "Dictionary_word", on_delete=models.DO_NOTHING, related_name='%(class)s_synonym_word_2')

class Dictionary_translation(models.Model):
    type = models.TextField()
    value = models.TextField()
    source_word = models.ForeignKey(
        "Dictionary_word", on_delete=models.DO_NOTHING, related_name='%(class)s_source_word')
    translated_word = models.ForeignKey(
        "Dictionary_word", on_delete=models.DO_NOTHING, related_name='%(class)s_translated_word')
    part_of_speech = models.ForeignKey(
        "Part_of_speech", on_delete=models.DO_NOTHING)
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    is_published = models.BooleanField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

class Dictionary_translation_synonym(models.Model):
    translation = models.ForeignKey(
        "Dictionary_translation", on_delete=models.DO_NOTHING)
    synonym_word_1 = models.ForeignKey(
        "Dictionary_word", on_delete=models.DO_NOTHING, related_name='%(class)s_synonym_word_1')
    synonym_word_2 = models.ForeignKey(
        "Dictionary_word", on_delete=models.DO_NOTHING, related_name='%(class)s_synonym_word_2')

class User_comment(models.Model):
    content = models.TextField()
    parent = models.ForeignKey(
        "User_comment", on_delete=models.DO_NOTHING, blank=True, null=True)
    translation = models.ForeignKey(
        "Dictionary_translation", on_delete=models.DO_NOTHING)
    is_published = models.BooleanField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

class User_vote(models.Model):
    translation = models.ForeignKey(
        "Dictionary_translation", on_delete=models.DO_NOTHING)
    vote = models.BooleanField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)