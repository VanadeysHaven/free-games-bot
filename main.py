import schedule
import time

from epic_games.free_epic_games import get_current_free_games, format_game as egs_format_game
from discord.webhook_sender import send_webhook

webhooks = ['webhooks_here']


def run():
    print('Running Epic Games Store check')
    free_games = get_current_free_games()
    with open('data_store/already_sent.txt', 'r') as f:
        already_sent = f.readlines()

    already_sent = [x.strip() for x in already_sent]

    for game in free_games:
        if game['offer_id'] not in already_sent:
            for webhook in webhooks:
                send_webhook(webhook, 'Epic Games', egs_format_game(game))

            with open('data_store/already_sent.txt', 'a') as f:
                f.write(f'{game["offer_id"]}\n')


if __name__ == '__main__':
    schedule.every(15).minutes.do(run)

    while True:
        schedule.run_pending()
        time.sleep(1)
