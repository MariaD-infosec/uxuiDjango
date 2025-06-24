from django.contrib import admin
from .models import GeneralStatistics, DemandStatistics, Geography, Skills, Vacancy


# Регистрируем модель в админке
@admin.register(GeneralStatistics)
class GeneralStatisticsAdmin(admin.ModelAdmin):
    list_display = ('title', 'html_table', 'graph_image')
    search_fields = ('title',)


@admin.register(DemandStatistics)
class DemandStatisticsAdmin(admin.ModelAdmin):
    list_display = ('title', 'html_table', 'graph_image')
    search_fields = ('title',)

@admin.register(Geography)
class GeographyAdmin(admin.ModelAdmin):
    list_display = ('title', 'html_table', 'graph_image')
    search_fields = ('title',)

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('title', 'html_table', 'graph_image')
    search_fields = ('title',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'region', 'salary', 'published_at')
    search_fields = ('title', 'company', 'region')
    list_filter = ('published_at', 'region')
