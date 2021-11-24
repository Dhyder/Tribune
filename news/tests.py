from .models import Editor,Article,tags
from django.test import TestCase
import datetime as dt


class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.vickie= Editor(first_name = 'Vickie', last_name ='Shiraa', email ='desastrecaliente@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.vickie,Editor))

class ArticleTestCase(TestCase):

    def setUp(self):
        #creating a new editor and saving it
        self.vickie = Editor(first_name = 'Vickie', last_name = 'Shiraa', email = 'desastrecaliente@gmail.com')
        self.vickie.save_editor()

        #creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.vickie)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
            test_date = '2021-11-23'
            date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
            news_by_date = Article.days_news(date)
            self.assertTrue(len(news_by_date) == 0)

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ('first_name',)

    def save_editor(self):
        self.save()
        
    # Testing Save Method
    def test_save_method(self):
        self.vickie.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

