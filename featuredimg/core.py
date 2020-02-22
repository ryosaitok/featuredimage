import click
from featuredimg.drawer import save_with_message
from featuredimg.image_source import get_image


@click.command()
@click.option('--message', '-m', default='ブログの見出し文章だよ', show_default=True, help='画像に上書きする文字列')
@click.argument('keyword')
def cli(keyword, message):
    """アイキャッチ画像生成ツール"""
    crete_featured_img(keyword, message)


def crete_featured_img(keyword, message):
    with get_image(keyword) as fp:
        save_with_message(fp, message)
