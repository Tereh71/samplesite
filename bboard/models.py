from django.db import models

#Створення класу оголошень
class Bb(models.Model):
    #заголовок оголошення
    title = models.CharField(max_length=50)
    #текст оголошення. (null=True, blank=True) - необов'язкове для заповнення поле'
    content = models.TextField(null=True, blank=True)
    #вартість товару
    price = models.FloatField(null=True, blank=True)
    #дата публикации (тип — временнáя отметка, значение по умолчанию — текущие дата и время, индексированное).
    published = models.DateTimeField(auto_now_add=True, db_index=True)
