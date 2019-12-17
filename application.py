from demo import application
import click
import click_config_file
import toml


def yaml_config_provider(file_path, cmd_name):
    with open(file_path) as config_data:
        return toml.load(config_data)


@click.command()
@click.argument('host')
@click_config_file.configuration_option(provider=yaml_config_provider)
def main(host):
    application.run(host)


if __name__ == '__main__':
    main()
