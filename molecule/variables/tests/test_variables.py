import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_jail_local(host):
    subject = host.file('/etc/fail2ban/jail.local')
    assert subject.exists
    assert b'destemail = another_recipent@anotherdomain.com' in subject.content


@pytest.mark.parametrize("file_name", ["mail.conf", "mail-whois-lines.conf", "mail-buffered.conf", "mail-whois.conf"])
def test_action_d_conf(host, file_name):
    content = host.file('/etc/fail2ban/action.d/' + file_name).content
    assert b'dest = another_recipent@anotherdomain.com' in content
