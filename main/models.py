from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'{self.name} <{self.email}> — {self.created_at.strftime("%Y-%m-%d %H:%M")}'


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('backend',   'Backend'),
        ('fullstack', 'Full Stack'),
        ('aiml',      'AI / ML'),
        ('frontend',  'Frontend'),
    ]

    title           = models.CharField(max_length=200)
    category        = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='backend')
    description     = models.TextField(help_text='Short description shown on the card.')
    long_description= models.TextField(help_text='Longer description shown in the details modal.')
    technologies    = models.CharField(max_length=500, help_text='Comma-separated list, e.g. Django, React, PostgreSQL')
    features        = models.TextField(blank=True, help_text='One feature per line.')
    github          = models.URLField(blank=True)
    live            = models.URLField(blank=True, help_text='Leave blank if no live demo.')
    image           = models.ImageField(upload_to='projects/', blank=True, null=True,
                                        help_text='Upload a screenshot. Leave blank to use the placeholder.')
    order           = models.PositiveIntegerField(default=0, help_text='Lower number = shown first.')
    is_featured     = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    def get_features_list(self):
        return [f.strip() for f in self.features.splitlines() if f.strip()]

    def get_category_label(self):
        return dict(self.CATEGORY_CHOICES).get(self.category, self.category)

    def get_image_url(self):
        if self.image:
            return self.image.url
        return None  # view will fall back to placeholder


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Programming',  'Programming'),
        ('Backend',      'Backend'),
        ('Frontend',     'Frontend'),
        ('Database',     'Database'),
        ('Tools',        'Tools'),
        ('AI / ML',      'AI / ML'),
    ]

    name     = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Programming')
    icon     = models.CharField(max_length=100, help_text='Bootstrap icon or devicon class, e.g. bi-cpu or devicon-django-plain')
    color    = models.CharField(max_length=20, default='#3b82f6', help_text='Hex color for the icon.')
    order    = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f'{self.category} — {self.name}'


class TimelineEntry(models.Model):
    year        = models.CharField(max_length=20, help_text='e.g. 2023 or 2025–2026 or Current')
    title       = models.CharField(max_length=200)
    description = models.TextField()
    is_current  = models.BooleanField(default=False, help_text='Marks this entry as the current/active one.')
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Timeline Entry'
        verbose_name_plural = 'Timeline Entries'

    def __str__(self):
        return f'{self.year} — {self.title}'


class AIMLArea(models.Model):
    title       = models.CharField(max_length=100)
    icon        = models.CharField(max_length=100, help_text='Bootstrap icon class, e.g. bi-cpu')
    description = models.TextField()
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'AI/ML Area'
        verbose_name_plural = 'AI/ML Areas'

    def __str__(self):
        return self.title


class LearningItem(models.Model):
    name  = models.CharField(max_length=100)
    icon  = models.CharField(max_length=100, help_text='Bootstrap icon or devicon class')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Learning Item'
        verbose_name_plural = 'Currently Learning'

    def __str__(self):
        return self.name


class Certification(models.Model):
    title       = models.CharField(max_length=200)
    issuer      = models.CharField(max_length=200, help_text='e.g. Coursera, Google, Udemy')
    date        = models.CharField(max_length=50, blank=True, help_text='e.g. June 2025')
    credential_url = models.URLField(blank=True, help_text='Link to verify the certificate.')
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-date']
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'

    def __str__(self):
        return f'{self.title} — {self.issuer}'


class Achievement(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date        = models.CharField(max_length=50, blank=True, help_text='e.g. 2025')
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

    def __str__(self):
        return self.title


class Resume(models.Model):
    file       = models.FileField(upload_to='resume/', help_text='Upload your resume PDF.')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active  = models.BooleanField(default=True, help_text='Only one resume should be active at a time.')

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Resume'
        verbose_name_plural = 'Resume'

    def __str__(self):
        return f'Resume uploaded {self.uploaded_at.strftime("%Y-%m-%d %H:%M")}'
