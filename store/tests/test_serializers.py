from django.contrib.auth.models import User
from django.db.models import Count, Case, When, Avg
from django.test import TestCase

from store.models import Book, UserBookRelation

from store.serializers import BooksSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        user1 = User.objects.create(username='user1')
        user2 = User.objects.create(username='user2')
        user3 = User.objects.create(username='user3')

        book_1 = Book.objects.create(name="Test book 1", price=25, author_name='Author 1')
        book_2 = Book.objects.create(name="Test book 2", price=55, author_name='Author 3')
        book_3 = Book.objects.create(name="Test book Author 1", price=75, author_name='Author 2')

        UserBookRelation.objects.create(user=user1, book=book_1, like=True,
                                        rate=5)
        UserBookRelation.objects.create(user=user2, book=book_1, like=True,
                                        rate=5)
        UserBookRelation.objects.create(user=user3, book=book_1, like=True,
                                        rate=4)

        UserBookRelation.objects.create(user=user1, book=book_2, like=True,
                                        rate=3)
        UserBookRelation.objects.create(user=user2, book=book_2, like=True,
                                        rate=4)
        UserBookRelation.objects.create(user=user3, book=book_2, like=False)

        books = Book.objects.all().annotate(
            annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
            rating=Avg('userbookrelation__rate')
        ).order_by('id')
        data = BooksSerializer(books, many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': book_1.name,
                'price': '25.00',
                'author_name': book_1.author_name,
                'likes_count': 3,
                'annotated_likes': 3,
                'rating': '4.67',
            },
            {
                'id': book_2.id,
                'name': book_2.name,
                'price': '55.00',
                'author_name': book_2.author_name,
                'likes_count': 2,
                'annotated_likes': 2,
                'rating': '3.50',
            },
            {
                'id': book_3.id,
                'name': book_3.name,
                'price': '75.00',
                'author_name': book_3.author_name,
                'likes_count': 0,
                'annotated_likes': 0,
                'rating': None,
            },
        ]
        self.assertEqual(expected_data, data)