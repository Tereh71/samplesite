from django.db import models

#Створення класу оголошень
class Bb(models.Model):
    #заголовок оголошення
    title = models.CharField(max_length=50, verbose_name='Товар')
    #текст оголошення. (null=True, blank=True) - необов'язкове для заповнення поле'
    content = models.TextField(null=True, blank=True, verbose_name='Опис')
    #вартість товару
    price = models.FloatField(null=True, blank=True, verbose_name='Ціна')
    #дата публикации (тип — временнáя отметка, значение по умолчанию — текущие дата и время, индексированное).
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубліковано')

    class Meta:
        verbose_name_plural ='Оголошення'
        verbose_name ='Оголошення'
        ordering = ['-published']
