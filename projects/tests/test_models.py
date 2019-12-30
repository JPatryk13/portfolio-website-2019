from django.test import TestCase

from projects.models import Project


class ProjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(title="Title of the test project.")

    def test_label_title(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Project title.')

    def test_label_prev_description(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('prev_description').verbose_name
        self.assertEquals(field_label, 'Short description.')

    def test_label_description(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Description.')

    def test_max_length_title(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_max_length_prev_description(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('prev_description').max_length
        self.assertEquals(max_length, 300)


    def test_max_length_description(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('description').max_length
        self.assertEquals(max_length, 2500)

    def test_max_length_phase(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('phase').max_length
        self.assertEquals(max_length, 1)

    def test_object_name(self):
        project = Project.objects.get(id=1)
        expected_name = project.title
        self.assertEquals(expected_name, str(project))

    def test_get_absolute_url(self):
        project = Project.objects.get(id=1)
        self.assertEquals(project.get_absolute_url(), '/project/1')
