from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from core.models import LinkModel


class TestCadastrarLink(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='gabriel',
            password='123456'
        )

    def test_usuario_logado_acessa_pagina(self):

        self.client.login(
            username='gabriel',
            password='123456'
        )

        response = self.client.get(
            reverse('cadastrar_link')
        )

        self.assertEqual(response.status_code, 200)

    def test_usuario_deslogado_redirecionado(self):

        response = self.client.get(
            reverse('cadastrar_link')
        )

        self.assertEqual(response.status_code, 302)

    def test_cadastrar_link_post(self):

        self.client.login(
            username='gabriel',
            password='123456'
        )

        response = self.client.post(
            reverse('cadastrar_link'),
            {
                'titulo': 'Google',
                'link': 'https://google.com',
                'observacao': 'Site de busca'
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            LinkModel.objects.count(),
            1
        )

    def test_link_salvo_corretamente(self):

        self.client.login(
            username='gabriel',
            password='123456'
        )

        self.client.post(
            reverse('cadastrar_link'),
            {
                'titulo': 'YouTube',
                'link': 'https://youtube.com',
                'observacao': 'Vídeos'
            }
        )

        link = LinkModel.objects.first()

        self.assertEqual(link.titulo, 'YouTube')
        self.assertEqual(link.link, 'https://youtube.com')