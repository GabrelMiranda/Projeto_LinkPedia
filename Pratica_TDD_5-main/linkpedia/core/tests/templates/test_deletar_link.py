from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from core.models import LinkModel


class SelecionarDeleteTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="aluno",
            password="123"
        )

        self.client.login(
            username="aluno",
            password="123"
        )

        self.link = LinkModel.objects.create(
            titulo="Google",
            link="https://google.com",
            observacao="Teste"
        )

    def test_tela_selecionar_delete_carrega(self):

        response = self.client.get(
            reverse("selecionar_delete")
        )

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            "selecionar_delete.html"
        )

    def test_redireciona_para_deletar_link(self):

        response = self.client.post(
            reverse("selecionar_delete"),
            {
                "link_id": self.link.id
            }
        )

        self.assertRedirects(
            response,
            reverse(
                "deletar_link",
                kwargs={"id": self.link.id}
            )
        )


class DeletarLinkTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="aluno",
            password="123"
        )

        self.client.login(
            username="aluno",
            password="123"
        )

        self.link = LinkModel.objects.create(
            titulo="Google",
            link="https://google.com",
            observacao="Teste"
        )

    def test_tela_deletar_carrega(self):

        response = self.client.get(
            reverse(
                "deletar_link",
                kwargs={"id": self.link.id}
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_deleta_link(self):

        response = self.client.post(
            reverse(
                "deletar_link",
                kwargs={"id": self.link.id}
            )
        )

        self.assertRedirects(
            response,
            reverse("home")
        )

        self.assertFalse(
            LinkModel.objects.filter(
                id=self.link.id
            ).exists()
        )