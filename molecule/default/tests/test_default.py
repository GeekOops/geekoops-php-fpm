#!/usr/bin/python3
# -*- coding: utf-8 -*-


import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
 
def test_phpinfo(host):
	cmd = host.run("curl -v http://127.0.0.1/phpinfo.php")
	assert 'HTTP/1.1 200 OK' in cmd.stderr
	assert "PHP Version" in cmd.stdout
	assert "php-fpm" in cmd.stdout
	assert "module_core" in cmd.stdout

