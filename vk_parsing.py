import requests
from config import TOKEN_VK
from pprint import *


def getPosts(userDomain):
    TOKEN = TOKEN_VK
    VERSION_VK_API = 5.92
    USER_DOMAIN = userDomain

    resp = requests.get('https://api.vk.com/method/wall.get',
                        params={
                            'access_token': TOKEN,
                            'v': VERSION_VK_API,
                            'domain': USER_DOMAIN,
                        }
                        )
    pprint(resp.json())
    return resp.json()['response']['items']


def getUserPhotos(userDomain):
    urls = []
    try:
        data = getPosts(userDomain)
        for post in data:
            try:
                user_post = post['attachments'][0]
                if user_post['type'] == 'link':
                    urls.append(user_post['link']['photo']['sizes'][-1]['url'])
                elif user_post['type'] == 'photo':
                    urls.append(user_post['photo']['sizes'][-1]['url'])
            except:
                pass
    except:
        pass
    
    return urls

