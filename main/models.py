from django.db import models

# Модель для хранения статистики с HTML-таблицей и графиком
class GeneralStatistics(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название раздела")
    html_table = models.TextField(verbose_name="HTML таблица")  # Сохраняем HTML-код таблицы
    graph_image = models.ImageField(upload_to="graphs/", null=True, blank=True, verbose_name="График (PNG)")  # График

    objects = models.Manager()

    class Meta:
        verbose_name = "Раздел статистики"
        verbose_name_plural = "Разделы статистики"

    def __str__(self):
        return self.title


class DemandStatistics(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название раздела")
    html_table = models.TextField(verbose_name="HTML таблица")  # Сохраняем HTML-код таблицы
    graph_image = models.ImageField(upload_to="graphs/", null=True, blank=True, verbose_name="График (PNG)")  # График

    objects = models.Manager()

    class Meta:
        verbose_name = "Статистика востребованности"
        verbose_name_plural = "Статистика востребованности"

    def __str__(self):
        return self.title

class Geography(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название раздела")
    html_table = models.TextField(verbose_name="HTML таблица")  # Сохраняем HTML-код таблицы
    graph_image = models.ImageField(upload_to="graphs/", null=True, blank=True, verbose_name="График (PNG)")  # График

    objects = models.Manager()

    class Meta:
        verbose_name = "География"
        verbose_name_plural = "География"

    def __str__(self):
        return self.title

class Skills(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название раздела")
    html_table = models.TextField(verbose_name="HTML таблица")  # Сохраняем HTML-код таблицы
    graph_image = models.ImageField(upload_to="graphs/", null=True, blank=True, verbose_name="График (PNG)")  # График

    objects = models.Manager()

    class Meta:
        verbose_name = "Навыки"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.title



class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название вакансии")
    description = models.TextField(verbose_name="Описание вакансии", null=True, blank=True)
    skills = models.TextField(verbose_name="Навыки", null=True, blank=True)
    company = models.CharField(max_length=255, verbose_name="Компания")
    salary = models.CharField(max_length=100, verbose_name="Оклад", null=True, blank=True)
    region = models.CharField(max_length=255, verbose_name="Регион")
    published_at = models.DateTimeField(verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ['-published_at']

    def __str__(self):
        return self.title
