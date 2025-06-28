from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Book, Review


class BookTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="reviewuser@email.com",
            password="testpass123"
        )
        self.book = Book.objects.create(
            title='Al Magrayat',
            author='DR:Ibrahim Al-Sakran',
            price='150.00'
        )
        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review="Good Book",
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Al Magrayat')
        self.assertEqual(f'{self.book.author}', 'DR:Ibrahim Al-Sakran')
        self.assertEqual(f'{self.book.price}', '150.00')

    def test_book_list_view(self):
        res = self.client.get(reverse('book_list'))
        no_res = self.client.get('/books/12345/')

        self.assertEqual(res.status_code, 200)
        self.assertEqual(no_res.status_code, 404)
        self.assertContains(res, 'Al Magrayat')
        self.assertTemplateUsed(res, 'books/book_list.html')

    def test_book_detail_view(self):
        res = self.client.get(self.book.get_absolute_url())
        no_res = self.client.get('/books/12345/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(no_res.status_code, 404)
        self.assertContains(res, 'Al Magrayat')
        self.assertTemplateUsed(res, 'books/book_detail.html')

    # def test_create_review(self)
    #     res = self.client.post(self.book.get_absolute_url())