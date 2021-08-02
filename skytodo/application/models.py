from django.db import models
import random

class Task(models.Model):

    class Meta:
        ordering = ['content']


    IMPORTANT_PRIORITY_LIST = [
        ['2', 'tres important'],
        ['1', 'important'],
        ['0', 'normal'],
        ['-1', 'peu important'],
        ['-2', 'très peu important'],
    ]

    TIME_PRIORITY_LIST = [
        ['2', 'très urgent'],
        ['1', 'urgent'],
        ['0', 'normal'],
        ['-1', 'peu urgent'],
        ['-2', 'très peu urgent'],
    ]

    STATUS_LIST = [
        ['to-do', 'A faire'],
        ['work-in-progress', 'En cours'],
        ['done', 'Fait'],
        ['to-reminder', 'Pour mémoire'],
    ]

    user    = models.ForeignKey("account.AppUser", related_name="task_list", null=True, blank=True, on_delete=models.CASCADE)

    tags    = models.ManyToManyField("Tag", related_name="tasks", blank=True)

    content    = models.TextField("Description de l'action")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField("status", null=False, blank=False, max_length=32, default='to-reminder', choices=STATUS_LIST)
    time_priority = models.CharField("Priorité temporelle", null=False, blank=False, max_length=32, default='normal', choices=TIME_PRIORITY_LIST)
    important_priority = models.CharField("Priorité d'importance", null=False, blank=False, max_length=32, default='normal', choices=IMPORTANT_PRIORITY_LIST)


class Tag(models.Model):

    class Meta:
        unique_together = [['name']]
        ordering = ['index']

    user    = models.ForeignKey("account.AppUser", related_name="tag_list", null=True, blank=True, on_delete=models.CASCADE)

    name = models.CharField("Nom du tag", null=False, blank=False, max_length=255)
    index = models.FloatField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Contact(models.Model):

    name = models.CharField("Votre nom", max_length=64)
    email = models.EmailField("Votre email", max_length=254)
    message = models.TextField("Votre Message")
    created_at = models.DateTimeField(auto_now_add=True)

def initialize_create_account(user):
    try:
        tags = []
        for name in ['cortex & minus', 'mission impossible']:
            tags.append(Tag.objects.create(user=user, name=name))
        for name in ['robot', 'trans-humanisme', 'start-up']:
            tag = Tag.objects.create(user=user, name=name)
            for step in range(1, 5):
                task = Task.objects.create(user=user, content="Appliquer l'action %s du plan pour %s" % (step, name), status="to-do", time_priority=str(random.randint(-2,2)), important_priority=str(random.randint(-2,2)))
                task.tags.add(tag)
                task.tags.add(random.choice(tags))
    except Exception as e:
        print(e)
