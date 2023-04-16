from django.test import TestCase, Client

from network.services import main
from network.models import Post, User, Comment
from datetime import datetime


class TestServices(TestCase):
    def setUp(self) -> None:
        User.objects.create(username="kem", email="k@mail.ru", password="123")
        User.objects.create(username="lel", email="k@mail.ru", password="123")

        Comment.objects.create(creator=User.objects.get(username="kem"),
                               comment="wow")
        Comment.objects.create(creator=User.objects.get(username="lel"),
                               comment="nice")

        post1 = Post.objects.create(
            creator=User.objects.get(username="lel"),
            content="Hello",
            likes=2,
            datetime=datetime(2020, 4, 10, 11, 30),
        )
        post1.comments.set([1])

        post2 = Post.objects.create(
            creator=User.objects.get(username="kem"),
            content="Hi!",
            likes=0,
            datetime=datetime(2021, 4, 10),
        )
        post2.comments.set([2])

    def test_get_user_objets(self):
        """Test for get user kem"""
        kem = User.objects.get(username="kem")
        self.assertEqual(kem.username, "kem")

    def test_display_posts(self):
        """Test for all Post objects"""
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 2)

    def test_iterate_function(self):
        """Test for iterate function from services.main"""
        checked_post = {
            1: {
                "creator": "lel",
                "content": "Hello",
                "likes": 2,
                "datetime": "April 10, 2020, 11:30 AM",
                "comments": ["wow"],
            }
        }
        post = Post.objects.get(content="Hello")
        post_json = main.iterate_at_posts_array([post])
        self.assertEqual(post_json, checked_post)


class TestExceptions(TestCase):
    def test_invalid_get_id_post(self):
        """Test for invalid id post in API"""
        client = Client()
        response = client.get("/api/post/100")
        self.assertEqual(response.status_code, 400)

    def test_invalid_get_all_posts(self):
        """Test for check raise exception if model return empty array"""
        client = Client()
        response = client.get("/api/posts")
        self.assertEqual(response.status_code, 400)


class TestClient(TestCase):
    def test_index_page(self):
        """Test for check main page"""
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
