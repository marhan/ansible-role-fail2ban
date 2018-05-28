import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name,version", [
    ("fail2ban", "0.9"),
])
def test_packages(host, name, version):
    subject = host.package(name)
    assert subject.is_installed
    assert subject.version.startswith(version)


def test_jail_local(host):
    subject = host.file('/etc/fail2ban/jail.local')
    assert subject.exists
    assert subject.user == 'root'
    assert subject.group == 'root'
    assert b'destemail = recipent@testdomain.com' in subject.content


@pytest.mark.parametrize("file_name", ["mail.conf", "mail-whois-lines.conf", "mail-buffered.conf", "mail-whois.conf"])
def test_action_d_conf(host, file_name):
    content = host.file('/etc/fail2ban/action.d/' + file_name).content
    assert b'dest = recipent@testdomain.com' in content
