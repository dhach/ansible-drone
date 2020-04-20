import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_sanity_check(host):
    f = host.file('/etc/passwd')
    assert f.exists
    assert f.is_file

