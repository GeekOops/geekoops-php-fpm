#!/usr/bin/python3
# -*- coding: utf-8 -*-


import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

# Check if the service is enabled and running
def test_php_active(host):
	php_fpm = host.service("php-fpm")
	assert php_fpm.is_running
	assert php_fpm.is_enabled

# Smoketest for nginx
def test_nginx(host):
	cmd = host.run("curl -v --fail http://127.0.0.1/")
	assert 'HTTP/1.1 200 OK' in cmd.stderr
	assert "This page is a stub" in cmd.stdout

# Check if we can access the phpinfo.php
def test_phpinfo(host):
	cmd = host.run("curl -v --fail http://127.0.0.1/phpinfo.php")
	assert 'HTTP/1.1 200 OK' in cmd.stderr
	assert "PHP Version" in cmd.stdout
	assert "php-fpm" in cmd.stdout
	assert "module_core" in cmd.stdout

