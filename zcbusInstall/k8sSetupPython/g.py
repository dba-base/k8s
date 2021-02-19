import os
from pathlib import Path

## Const
DEFAULT_UID = 10000
DEFAULT_GID = 10000

PG_UID = 999
PG_GID = 999

REDIS_UID = 999
REDIS_GID = 999

## Global variable
host_root_dir = '/hostfs'

base_dir = '/harbor_make'
# test
# templates_dir = "/Users/haoxiaoyu/python-homework/zcbus/k8sSetup"
# produce
templates_dir = "/usr/src/app"

config_dir = '/config'
data_dir = '/data'

# produce
zookeeper_yaml_path = '/yaml/zookeeper.yml'
kafka_yaml_path = '/yaml/kafka.yml'
mysql_yaml_path = '/yaml/mysql.yml'
zcbus_yaml_path = '/yaml/zcbus.yml'
ansible_config_path = '/input/ansible.tmp'
# test
# zookeeper_yaml_path = './yaml/zookeeper.yml'
# kafka_yaml_path = './yaml/kafka.yml'
# mysql_yaml_path = './yaml/mysql.yml'
# zcbus_yaml_path = './yaml/zcbus.yml'
# ansible_config_path = 'ansible.tmp'
# test
# input_config_path = 'zcbus.yml'
# produce
input_config_path = '/input/zcbus.yml'
versions_file_path = Path('/usr/src/app/versions')

cert_dir = os.path.join(config_dir, "nginx", "cert")
core_cert_dir = os.path.join(config_dir, "core", "certificates")

INTERNAL_NO_PROXY_DN = {
    '127.0.0.1',
    'localhost',
    '.local',
    '.internal',
    'log',
    'db',
    'redis',
    'nginx',
    'core',
    'portal',
    'postgresql',
    'jobservice',
    'registry',
    'registryctl',
    'clair',
    'chartmuseum',
    'notary-server',
    'notary-signer',
    'clair-adapter'
    }