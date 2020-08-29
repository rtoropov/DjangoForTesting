from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


# Create your tests here.

import os


class HomePageTest(TestCase):
    # Тест домашней страницы

    def test_root_url_resolves_to_home_page_view(self):
        # Тест: корневой url преобразуется в представление домашней страницы
        found = resolve('/') # resolve – это функция, которую Django использует внутренне для
                             # преобразования URL-адреса и нахождения функций представления,
                             # в соответствие которым они должны быть поставлены
        self.assertEqual(found.func, home_page) # Проверяем, что resolse, когда её вызывают с '/', с корня сайта, нашeла
                                                # функцию под названием home_page