import os

from invoke import task


@task
def runit(ctx):
    ctx.run('./manage.py collectstatic --noinput')
    ctx.run('./manage.py makemessages --all')
    ctx.run('./manage.py compilemessages')
    ctx.run('./manage.py migrate')

    uwsgi_command = ('uwsgi --module "django.core.wsgi:get_wsgi_application()"'
                     ' --master --pidfile=/tmp/project-master.pid'
                     ' --http=0.0.0.0:8000'
                     ' --processes=4'
                     ' --harakiri=20'
                     ' --max-requests=5000'
                     ' --vacuum')

    if os.getenv('PY_AUTORELOAD', 'False').lower() in ('true', '1'):
        uwsgi_command += ' --py-autoreload 1'

    ctx.run(uwsgi_command)
