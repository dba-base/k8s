import yaml
import os
from g import DEFAULT_UID, DEFAULT_GID
from jinja2 import Environment, FileSystemLoader
from g import templates_dir,zookeeper_yaml_path,kafka_yaml_path,mysql_yaml_path,zcbus_yaml_path,ansible_config_path

zookeeper_template_path = os.path.join(templates_dir, 'templates', 'zookeeper.yaml.jinja')
kafka_template_path = os.path.join(templates_dir, 'templates', 'kafka.yaml.jinja')
mysql_template_path = os.path.join(templates_dir, 'templates', 'mysql.yaml.jinja')
zcbus_template_path = os.path.join(templates_dir, 'templates', 'zcbus.yaml.jinja')
ansible_config_template_path = os.path.join(templates_dir, 'templates', 'ansible.tmp.jinja')


jinja_env = Environment(loader=FileSystemLoader('/'), trim_blocks=True, lstrip_blocks=True)


def mark_file(path, mode=0o600, uid=DEFAULT_UID, gid=DEFAULT_GID):
    if mode > 0:
        os.chmod(path, mode)
    if uid > 0 and gid > 0:
        os.chown(path, uid, gid)

# jinjia 模版转换
def render_jinja(src, dest,mode=0o640, uid=0, gid=0, **kw):
    t = jinja_env.get_template(src)
    with open(dest, 'w') as f:
        f.write(t.render(**kw))
    mark_file(dest, mode, uid, gid)
    print("Generated configuration file: %s" % dest)

# parse yaml's configrations
def parse_yaml_config(conf):
    '''
    :param configs: config_parser object
    :returns: dict of configs
    '''

    with open(conf,encoding='utf-8') as f:
        configs = yaml.safe_load(f)
    db_config_dict = {'zcbusdb_image':configs['zcbusDB'].get('image'),
                   'master_data_path':configs['zcbusDB'].get('master_data_path'),
                   'slave_data_path':configs['zcbusDB'].get('slave_data_path'),
                   'master_worknode':configs['zcbusDB'].get('master_worknode'),
                   'slave_worknode':configs['zcbusDB'].get('slave_worknode')
                   }
    zookeeper_config_dict = {
        'zookeeper_image': configs['zcbusZookeeper'].get('image'),
        'zookeeper_worknode01': configs['zcbusZookeeper'].get('zookeeper_worknode01'),
        'zookeeper_worknode02': configs['zcbusZookeeper'].get('zookeeper_worknode02'),
        'zookeeper_worknode03': configs['zcbusZookeeper'].get('zookeeper_worknode03'),
        'zookeeper_worknode01_path': configs['zcbusZookeeper'].get('zookeeper_worknode01_path'),
        'zookeeper_worknode02_path': configs['zcbusZookeeper'].get('zookeeper_worknode02_path'),
        'zookeeper_worknode03_path': configs['zcbusZookeeper'].get('zookeeper_worknode03_path'),
        'zookeeper_storage': configs['zcbusZookeeper'].get('zookeeper_storage'),
        'zookeeper_disk_space': configs['zcbusZookeeper'].get('zookeeper_disk_space'),
        'zookeeper_mem_quota': configs['zcbusZookeeper'].get('zookeeper_mem_quota'),
        'zookeeper_cpu_quota': configs['zcbusZookeeper'].get('zookeeper_cpu_quota')
    }
    kafka_config_dict = {
        'kafka_image': configs['zcbusKafka'].get('image'),
        'kfk_ports': configs['zcbusKafka'].get('kfk_ports'),
        'kafka_volumes': configs['zcbusKafka'].get('kafka_volumes'),
        'kafka_worknode01': configs['zcbusKafka'].get('kafka_worknode01'),
        'kafka_worknode02': configs['zcbusKafka'].get('kafka_worknode02'),
        'kafka_worknode03': configs['zcbusKafka'].get('kafka_worknode03'),
        'kafka_worknode01_path': configs['zcbusKafka'].get('kafka_worknode01_path'),
        'kafka_worknode02_path': configs['zcbusKafka'].get('kafka_worknode02_path'),
        'kafka_worknode03_path': configs['zcbusKafka'].get('kafka_worknode03_path'),
        'kafka_mem_quota': configs['zcbusKafka'].get('kafka_mem_quota'),
        'kafka_cpu_quota': configs['zcbusKafka'].get('kafka_cpu_quota'),
        'kafka_containerPort': configs['zcbusKafka'].get('kafka_containerPort'),
        'kafka_disk_space': configs['zcbusKafka'].get('kafka_disk_space'),
        'kafka_storage': configs['zcbusKafka'].get('kafka_storage')

    }
    zcbus_config_dict = {
        'zcbusWebImage': configs['zcbusWeb'].get('image'),
        'zcbusWebPort': configs['zcbusWeb'].get('ports'),
        'zcbusNodePort': configs['zcbusWeb'].get('zcbusNodePort'),
        'zcbusServerImage': configs['zcbusServer'].get('image'),
        'zcbus_worknode': configs['zcbusServer'].get('worknode')

    }
    # 字典合并
    config_dict = {**db_config_dict,**zookeeper_config_dict,**kafka_config_dict,**zcbus_config_dict}


    return config_dict



def prepare_docker_compose(conf):

    rendering_variables = parse_yaml_config(conf)

    render_jinja(zookeeper_template_path, zookeeper_yaml_path, mode=0o644, **rendering_variables)
    render_jinja(kafka_template_path, kafka_yaml_path, mode=0o644, **rendering_variables)
    render_jinja(mysql_template_path, mysql_yaml_path, mode=0o644, **rendering_variables)
    render_jinja(zcbus_template_path, zcbus_yaml_path, mode=0o644, **rendering_variables)
    render_jinja(ansible_config_template_path, ansible_config_path, mode=0o644, **rendering_variables)


