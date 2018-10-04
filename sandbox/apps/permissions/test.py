from django.contrib.auth.models import User
boss = User.objects.create(username='Big Boss')
joe = User.objects.create(username='joe')
task = Task.objects.create(summary='Some job', content='', reported_by=boss)
joe.has_perm('view_task', task)