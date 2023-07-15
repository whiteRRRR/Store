from django.test import TestCase
from django.urls import reverse

from .models import *


class BaseTestCase(TestCase):
    def create_test_data(self):
        self.category = BlogCategory.objects.create(name='TestCategory', slug='test_category_slug')
        self.tags = BlogTags.objects.create(name='TestTag', slug='test_tags_slug')
        self.blog = Blog.objects.create(
            title='TestBlog',
            description='test_description_blog',
            image='blog_image/image.png',
            slug='test_blog_slug',
            category=self.category,
        )
        self.blog.tags.add(self.tags)


class BlogModelTest(BaseTestCase):
    def setUp(self):
        self.create_test_data()

    def test_blog_creation(self):
        self.assertEqual(self.blog.title, 'TestBlog')
        self.assertEqual(self.blog.description, 'test_description_blog')
        self.assertEqual(self.blog.image, 'blog_image/image.png')
        self.assertEqual(self.blog.category, self.category)
        self.assertEqual(self.blog.tags.count(), 1)
        self.assertEqual(self.blog.tags.first(), self.tags)


class CommentModelTest(BaseTestCase):
    def setUp(self):
        self.create_test_data()
        self.user = CustomUser.objects.create(
            username='User',
            first_name='user_first_name',
            last_name='user_last_name',
            email='user@gmail.com'
        )
        self.comment = CommentBlog.objects.create(
            blog=self.blog,
            content='test_comment',
            author=self.user
        )

    def test_user_creation(self):
        self.assertEqual(self.comment.blog, self.blog)
        self.assertEqual(self.comment.content, 'test_comment')
        self.assertEqual(self.comment.author, self.user)
        self.assertIsNotNone(self.comment.created_at)

    def test_comment_blog_relation(self):
        comments = self.blog.commentblog_set.all()
        self.assertEqual(comments.count(), 1)
        self.assertEqual(comments.first(), self.comment)


class BlogViewTest(BaseTestCase):
    def setUp(self):
        self.create_test_data()
        self.user = CustomUser.objects.create(
            username='User',
            first_name='user_first_name',
            last_name='user_last_name',
            email='user@gmail.com'
        )
        self.comment = CommentBlog.objects.create(
            blog=self.blog,
            content='test_comment',
            author=self.user
        )

    def test_blog_list_view(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')
        self.assertContains(response, 'TestBlog')
        self.assertEqual(len(response.context['blogs']), 1)

    def test_by_category_view(self):
        response = self.client.get(reverse('by_category', args=[self.category.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')
        self.assertContains(response, 'TestBlog')
        self.assertEqual(len(response.context['blogs']), 1)

    def test_by_tag_view(self):
        response = self.client.get(reverse('by_tag', args=[self.tags.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')
        self.assertContains(response, 'TestBlog')
        self.assertEqual(len(response.context['blogs']), 1)

    def test_blog_search_view(self):
        response = self.client.get(reverse('blog_search'), {'search': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')
        self.assertContains(response, 'TestBlog')
        self.assertEqual(len(response.context['blogs']), 1)

    def test_blog_detail_view(self):
        response = self.client.get(reverse('blog_detail', args=[self.blog.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/single-blog.html')
        self.assertContains(response, 'TestBlog')
        self.assertContains(response, 'test_comment')







