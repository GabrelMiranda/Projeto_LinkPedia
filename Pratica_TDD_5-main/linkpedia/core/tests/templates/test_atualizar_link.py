from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from core.models import LinkModel


class UpdateLinkTemplateTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='aluno',
            password='123'
        )

        self.link = LinkModel.objects.create(
            titulo='Google',
            link='https://google.com',
            observacao='Teste'
        )

    def test_render_update_template(self):

        self.client.login(
            username='aluno',
            password='123'
        )

        response = self.client.get(

            reverse(
                'atualizar_link',
                kwargs={'id': self.link.id}
            )

        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertTemplateUsed(
            response,
            'atualizar_link.html'
        )

        from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class SelecionarLinkTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='aluno',
            password='123'
        )

    def test_render_selecionar_link_template(self):

        self.client.login(
            username='aluno',
            password='123'
        )

        response = self.client.get(
            reverse('selecionar_link')
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertTemplateUsed(
            response,
            'selecionar_link.html'
        )