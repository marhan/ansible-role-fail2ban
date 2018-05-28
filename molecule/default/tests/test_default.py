import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name,version", [
    ("fail2ban", "0.9"),
])
def test_packages(host, name, version):
    package = host.package(name)
    assert package.is_installed
    assert package.version.startswith(version)


def test_jail_file(host):
    jail_file = host.file('/etc/fail2ban/jail.local')
    assert jail_file.exists
    assert jail_file.user == 'root'
    assert jail_file.group == 'root'
