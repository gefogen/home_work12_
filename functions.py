import json


def load_content_from_json():
    """ Загружаем json """
    with open("posts.json", "r", encoding="utf-8") as file:
        content_posts = json.load(file)
        return content_posts


def search_by_tag(content):
    """ Ищем соответствия по тегу """
    content_posts = load_content_from_json()
    posts = []
    for post in content_posts:
        if content.lower() in post['content'].lower():
            posts.append(post)
    return posts


def write_tag_in_json(picture, content):
    """ Записывает пост в json """
    with open("posts.json", "r", encoding="utf-8") as file:
        all_posts = json.load(file)
        new_post = {"pic": picture,
                    "content": content
                    }
        all_posts.append(new_post)
    with open("posts.json", "w+", encoding="utf-8") as file:
        json.dump(all_posts, file, ensure_ascii=False, indent=2)
    return new_post