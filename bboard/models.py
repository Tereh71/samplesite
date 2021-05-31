from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Назва")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ='Рубрики'
        verbose_name ='Рубрика'
        ordering = ['name']


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
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name = 'Рубрика')

    class Meta:
        verbose_name_plural ='Оголошення'
        verbose_name ='Оголошення'
        ordering = ['-published']
