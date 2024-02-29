import requests


def get_current_free_games():
    url = ('https://store-site-backend-static.ak.epicgames.com/'
           'freeGamesPromotions?locale=en-US&country=US&allowCountries=US')
    response = requests.get(url)
    data = response.json()

    games = data['data']['Catalog']['searchStore']['elements']
    current_offers = [game for game in games if game['price']['lineOffers'][0]['appliedRules']]

    stripped_offers = []
    for offer in current_offers:
        thumbnail_url = None
        for image in offer['keyImages']:
            if image['type'] == 'Thumbnail':
                thumbnail_url = image['url']
                break

        stripped_offers.append({
            'title': offer['title'],
            'offer_id': offer['price']['lineOffers'][0]['appliedRules'][0]['id'],
            'org_price': offer['price']['totalPrice']['fmtPrice']['originalPrice'],
            'url': f'https://www.epicgames.com/store/en-US/p/{offer["productSlug"]}',
            'description': offer['description'],
            'image': thumbnail_url
        })

    return stripped_offers


def format_game(game):
    return (f':gift: **NEW** free game on Epic Games Store: **{game["title"]}**\n\n'
            f'> {game["description"]}'
            f'\n\n~~{game["org_price"]}~~ -> **FREE**'
            f'\n[Get it for free!]({game["url"]})')
