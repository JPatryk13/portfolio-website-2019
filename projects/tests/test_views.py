from django.test import TestCase
from django.urls import reverse

from projects.models import Project


class ProjectListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create some number of projects
        no_of_projects = 20
        for project_id in range(no_of_projects):
            Project.objects.create(title="Test project #{project_id} title.")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/projects/')
        self.assertEquals(response.status_code, 200)

    def test_vew_url_accessible_by_name(self):
        response = self.client.get(reverse('projects'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('projects'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_list.html')


class ProjectDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(title="Test project title.")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/project/1')
        self.assertEquals(response.status_code, 200)

    def test_vew_url_accessible_by_name(self):
        response = self.client.get(reverse('project-detail', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('project-detail', args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_detail.html')
