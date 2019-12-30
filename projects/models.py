from django.db import models
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Project title.', help_text='Max: 100 chars.')
    prev_description = models.TextField(max_length=300,
                                        verbose_name='Short description.',
                                        help_text='Max: 300chars.')
    description = models.TextField(max_length=2500, verbose_name='Description.', help_text='Max: 2500 chars.')
    
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    PHASE = (
        ('p', 'Planning'),
        ('i', 'Implementation'),
        ('m', 'Maintenance'),
        ('c', 'Completion'),
    )

    phase = models.CharField(
        max_length=1,
        choices=PHASE,
        blank=True,
        default='p',
        help_text='Project phase.'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])
