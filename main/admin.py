from django.contrib import admin
from .models import Contact, Project, Skill, TimelineEntry, AIMLArea, LearningItem, Certification, Achievement, Resume
from django.contrib import messages as django_messages


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display  = ('name', 'email', 'created_at')
    list_filter   = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    ordering      = ('-created_at',)

    def has_add_permission(self, request):
        return False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('title', 'category', 'is_featured', 'order')
    list_editable = ('order', 'is_featured')
    list_filter   = ('category', 'is_featured')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'category', 'order', 'is_featured')
        }),
        ('Content', {
            'fields': ('description', 'long_description', 'features')
        }),
        ('Technologies', {
            'fields': ('technologies',),
            'description': 'Enter as comma-separated values: Django, React, PostgreSQL'
        }),
        ('Links', {
            'fields': ('github', 'live')
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ('name', 'category', 'icon', 'color', 'order')
    list_editable = ('order', 'color')
    list_filter   = ('category',)
    search_fields = ('name',)
    ordering      = ('category', 'order')


@admin.register(TimelineEntry)
class TimelineAdmin(admin.ModelAdmin):
    list_display  = ('year', 'title', 'is_current', 'order')
    list_editable = ('order', 'is_current')
    ordering      = ('order',)


@admin.register(AIMLArea)
class AIMLAreaAdmin(admin.ModelAdmin):
    list_display  = ('title', 'icon', 'order')
    list_editable = ('order',)


@admin.register(LearningItem)
class LearningItemAdmin(admin.ModelAdmin):
    list_display  = ('name', 'icon', 'order')
    list_editable = ('order',)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display  = ('title', 'issuer', 'date', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'issuer')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display  = ('title', 'date', 'order')
    list_editable = ('order',)
    search_fields = ('title',)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display   = ('__str__', 'is_active', 'uploaded_at')
    list_editable  = ('is_active',)

    def save_model(self, request, obj, form, change):
        if obj.is_active:
            Resume.objects.exclude(pk=obj.pk).update(is_active=False)
        try:
            super().save_model(request, obj, form, change)
        except Exception as e:
            self.message_user(request, f'Error saving file: {e}. Use Cloudinary for persistent storage.', level='error')

    def get_queryset(self, request):
        try:
            return super().get_queryset(request)
        except Exception:
            return Resume.objects.none()
