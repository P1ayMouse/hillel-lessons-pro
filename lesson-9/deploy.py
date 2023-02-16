import os
import sys
import logging
import pexpect
import boto3

logging.basicConfig(level=logging.INFO)

class Pexpect:
    def __init__(self, host, default_expect='ubuntu@', timeout=300):
        self.host = host
        self.default_expect = default_expect
        self.child = pexpect.spawn('ssh -o StrictHostKeyChecking=no ubuntu@{}'.format(host), timeout=timeout, encoding='utf-8')
        self.child.logfile = sys.stdout
        self.child.expect(default_expect)

    def cmd(self, cmd, expect=None, timeout=None):
        if not expect:
            expect = self.default_expect
        self.child.sendline(cmd)
        return self.child.expect(expect, timeout=timeout)

    def send_break(self, expect=None):
        if not expect:
            expect = self.default_expect
        self.child.send('\003')
        self.child.expect(expect)


def find_instances():
    ec2 = boto3.resource(service_name='ec2', region_name='us-east-1')
    running_instances = ec2.instances.filter(Filters=[
        {'Name': 'instance-state-name', 'Values': ['running']},
        {'Name': 'tag:proj', 'Values': ['hillel-lesson']},
    ])
    return running_instances


def deploy_host(instance):
    deploy_host = instance.public_ip_address
    docker_compose_file = os.getenv('DOCKER_COMPOSE_FILE', 'docker-compose.yml')
    docker_compose = 'docker compose -f {}'.format(docker_compose_file)
    expect_value = os.getenv('EXPECT_VALUE', 'ubuntu@')
    deploy_version = os.getenv('CIRCLE_SHA1')

    if not deploy_host or not deploy_version:
        raise ValueError('No env vars provided')

    expect = Pexpect(deploy_host, default_expect=expect_value)
    expect.cmd('pushd {}'.format('hillel-lessons-pro/lesson-9'))
    expect.cmd('git fetch origin')
    expect.cmd('git reset --hard')
    expect.cmd('git checkout {}'.format(deploy_version))
    expect.cmd('{} stop'.format(docker_compose))
    expect.cmd('{} up -d'.format(docker_compose))
    expect.cmd('exit', expect='logout')


def deploy():
    instances = find_instances()

    for instance in instances:
        deploy_host(instance)


if __name__ == '__main__':
    deploy_host('100.26.18.151')
