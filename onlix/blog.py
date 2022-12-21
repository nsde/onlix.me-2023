import tools

import os
import flask
import markdown
import collections

from datetime import datetime

blog_bp = flask.Blueprint('blog_bp',
    __name__,
)

def get_posts(with_code=True):
    post_dates = {}

    for post in os.listdir('blog/'):
        if os.path.isdir(f'blog/{post}'):
            if (not post.endswith('.closed')) and (not post.startswith('.')): 
                post_dates[post] = os.path.getmtime(f'blog/{post}/page.md')

    posts = []

    for post in sorted(post_dates, key=post_dates.get, reverse=True):
        post_info = get_info(post)

        if not with_code:
            del post_info['md_code']

        posts.append(post_info)
    
    return posts

def get_info(post: str):
    path = f'blog/{post}'
    md_code = open(f'blog/{post}/page.md').read()

    category = md_code.split('\ncategory: ')[1].split('\n')[0]
    tags = md_code.split('\ntags: ')[1].split('\n')[0].split(', ')

    title = md_code.split('\n# ')[1].split('\n')[0]
    description = md_code.split('\nsubtitle: ')[1].split('\n')[0]

    markdown_seperator = '\n---\n'
    input_markdown = md_code.split(markdown_seperator)[1]
    markdown_code = f'{input_markdown}'.replace('$$ path $$', path)

    html_code = markdown.markdown(markdown_code, extensions=['toc']).replace('<div class="toc">', '\n<div class="toc text-box">')
    html_code = html_code.replace('</h1>', '</h1><img src="/$$ image $$" class="blog-image">')

    last_update = datetime.fromtimestamp(os.path.getmtime(f'blog/{post}/page.md')).strftime('%a %d/%m/%Y')

    wip = len(input_markdown) < 300

    return {
        'wip': wip,
        'path': path,
        'title': title,
        'category': category,
        'tags': tags,
        'md_code': html_code,
        'description': description,
        'last_update': last_update
    }

@blog_bp.route('/blog/:<int:num>')
def blog_num(num: int):
    return flask.redirect(f'/{get_posts()[num]["path"]}')

@blog_bp.route('/blog/<post>')
def blog_post(post):
    if not os.path.isdir(f'blog/{post}'):
        return tools.show('error.html', title='Blog post not found!', description='Maybe the post ID got removed or renamed. In this, use the search box below.')

    info = get_info(post)
    recommended_posts = []

    html = tools.show('blog.html', title=info['title'], description=info['description'], post=post, category=info['category'], tags=info['tags'], last_update=info['last_update'], content=info['md_code'], posts=recommended_posts)
    return html.replace('$$ image $$', f'blog/{post}/image')

@blog_bp.route('/blog/<post>/<image>')
def blog_post_image(post, image):
    return flask.send_file(f'blog/{post}/{"image.jpg" if image == "image" else image }', mimetype=f'image/{"jpg" if image == "image" else image.split(".")[-1]}')

@blog_bp.route('/blog')
def blog_posts():
    posts = get_posts()
    return tools.show('posts.html', type='All Posts', text='', tags=[], posts=posts)

@blog_bp.route('/blog/@<category>')
def blog_category(category):
    posts = [post for post in get_posts() if post['category'] == category]
    
    tags = []
    for post in posts:
        for tag in post['tags']:
            tags.append(tag)

    tags = [tag[0] for tag in collections.Counter(tags).most_common()]
    
    return tools.show('posts.html', type='Category', text='with category=' + category, tags=tags, posts=posts)

@blog_bp.route('/blog/+<tag>')
def blog_tag(tag):
    return tools.show('posts.html', type='Tag', text='with tag=' + tag, posts=[post for post in get_posts() if tag in post['tags']])
