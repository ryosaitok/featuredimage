import click


@click.command()
def cli():
    """アイキャッチ画像生成ツール"""
    featured_img()
    click.echo('featuredimg')


def featured_img():
    pass
