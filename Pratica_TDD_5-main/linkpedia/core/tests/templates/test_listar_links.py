from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from core.models import LinkModel


class TestListarLinks(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='gabriel',
            password='123456'
        )

        self.link = LinkModel.objects.create(
            titulo='Google',
            link='https://google.com',
            observacao='Site de busca'
        )

    def test_usuario_logado_acessa_pagina(self):

        self.client.login(
            username='gabriel',
            password='123456'
        )

        response = self.client.get(
            reverse('listar_links')
        )

        self.assertEqual(response.status_code, 200)

    def test_usuario_deslogado_redirecionado(self):

        response = self.client.get(
            reverse('listar_links')
        )

        self.assertEqual(response.status_code, 302)

    def test_template_correto(self):

        self.client.login(
            username='gabriel',
            password='123456'
        )

        response = self.client.get(
            reverse('listar_links')
        )

        self.assertTemplateUsed(
            response,
            'listar_links.html'
        )

    def test_link_aparece_na_pagina(self):

        self.client.login(
            username='gabriel',
            password='123456'
        )

        response = self.client.get(
            reverse('listar_links')
        )

        self.assertContains(
            response,
            'Google'
        )

    def test_contexto_possui_links(self):

        self.client.login(
            username='gabriel',
            password='123456'
        )

        response = self.client.get(
            reverse('listar_links')
        )

        self.assertIn(
            'links',
            response.context
        )