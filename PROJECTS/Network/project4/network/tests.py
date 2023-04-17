from django.test import TestCase, Client

from network.services import get_api
from network.models import Post, User, Comment, Follow
from datetime import datetime


class TestServices(TestCase):
    def setUp(self) -> None:
        kem = User.objects.create(username="kem", email="k@mail.ru",
                                  password="123")
        User.objects.create(username="lel", email="k@mail.ru",
                            password="123")

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

        follow = Follow.objects.create(user=kem)
        follow.following_posts.set([1])

    def test_get_user_objets(self):
        """Test for get user kem"""
        kem = User.objects.get(username="kem")
        self.assertEqual(kem.username, "kem")

    def test_display_posts(self):
        """Test for all Post objects"""
        all_posts = Post.objects.all()
        self.assertEqual(len(all_posts), 2)

    def test_iterate_function(self):
        """Test for iterate function from services.get_api"""
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
        post_json = get_api.iterate_at_posts_array([post])
        self.assertEqual(post_json, checked_post)

    def test_get_follow_post(self):
        """Test for API get follow posts"""
        checked_post = {
            1: {
                "creator": "lel",
                "content": "Hello",
                "likes": 2,
                "datetime": "April 10, 2020, 11:30 AM",
                "comments": ["wow"],
            }
        }
        post_json = get_api.return_follow_posts_json(username="kem")
        self.assertEqual(post_json, checked_post)


class TestExceptions(TestCase):
    def setUp(self) -> None:
        kem = User.objects.create(username="kem", email="k@mail.ru",
                                  password="123")
        Follow.objects.create(user=kem)

    def test_invalid_get_id_post(self):
        """Test for invalid id post in API."""
        client = Client()
        response = client.get("/api/post/100").json()
        self.assertEqual(response["error"], "Post with id 100 does not exist.")

    def test_invalid_get_all_posts(self):
        """Test for check raise exception if model return empty array."""
        client = Client()
        response = client.get("/api/posts").json()
        self.assertEqual(response["error"], "No posts.")

    def test_invalid_get_own_posts_username(self):
        """Test for check raise exception if user does not exist."""
        client = Client()
        response = client.get("/api/posts/ab").json()
        self.assertEqual(response["error"], "User ab does not exist.")

    def test_invalid_get_own_posts_empty(self):
        """Test for check raise exception if user dont have posts."""
        client = Client()
        response = client.get("/api/posts/kem").json()
        self.assertEqual(response["error"], "No posts for user kem.")

    def test_invalid_get_follow_posts_username(self):
        """Test for check raise exception if user does not exist."""
        client = Client()
        response = client.get("/api/follow/ab").json()
        error_message = 'Object "Follow" for user ab does not exist.'
        self.assertEqual(response["error"], error_message)

    def test_invalid_get_follow_posts_empty(self):
        """Test for check raise exception if user dont have posts."""
        client = Client()
        response = client.get("/api/follow/kem").json()
        error_message = 'No following posts for user kem.'
        self.assertEqual(response["error"], error_message)


class TestClient(TestCase):
    def test_index_page(self):
        """Test for check get_api page"""
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
