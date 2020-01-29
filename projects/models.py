from django.db import models
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Project title.', help_text='Max: 100 chars.')
    prev_description = models.TextField(max_length=200,
                                        verbose_name='Short description.',
                                        help_text='Max: 200 chars.')
    description = models.TextField(max_length=10000, verbose_name='Description.', help_text='Max: 10000 chars.')
    
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

    path_to_img = 'projects/static/img/projects/'

    sm_img = models.ImageField(upload_to=path_to_img, editable=True, help_text="572x360px", null=True,
                               verbose_name="Small image (thumbnail for mobile devices)")
    md_img = models.ImageField(upload_to=path_to_img, editable=True, help_text="1149x370px", null=True,
                               verbose_name="Medium image (thumbnail for screens)")
    lg_img = models.ImageField(upload_to=path_to_img, editable=True, help_text="1680x1050px", null=True,
                               verbose_name="Large image (background for the project detail page)")

    # Side note for editing each of the images (GIMP).
    #   Apply desaturation;
    #   Apply CIE ich Noise filter (dulling set from 4 to 6 depending on the image)
    #   Create black layer (visibility: 75% - depending on the image)
    #   ** md_img, apply gradient from the top (~10% above) to the bottom (~10% below)
    #   ** lg_img, must be a little bit darker than the others
    #   Further adjust brightness and contrast
    #   ** lg_img, 3D centered effect - duplicate the layer, remove red/green&blue from layers, scale the red one up
    #      and merge them down
    # Naming convention should follow: {size}_project_name.jpg, where {size} = sm, md, lg.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])

    def get_sm_img_path(self):
        return self.sm_img.name.replace('projects/static/', '')

    def get_md_img_path(self):
        return self.md_img.name.replace('projects/static/', '')

    def get_lg_img_path(self):
        return self.lg_img.name.replace('projects/static/', '')
