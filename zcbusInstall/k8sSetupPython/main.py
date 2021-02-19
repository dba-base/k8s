import click
from g import input_config_path
from zcbus import prepare_docker_compose,parse_yaml_config

@click.command()
@click.option('--conf', default=input_config_path, help="the path of Harbor configuration file")

def main(conf):
    prepare_docker_compose(conf)


if __name__ == '__main__':
    main()
