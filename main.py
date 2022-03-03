from time import sleep
import config, requests, tweepy, praw
from datetime import datetime


class ProjectZomboid:
    def __init__(self):
        pass

    def login_reddit(self):
        try:
            print(50*"-")
            print('Logging reddit...')
            reddit = praw.Reddit(
                client_id=config.client_id,
                client_secret=config.client_secret,
                password=config.password,
                user_agent=config.user_agent,
                username=config.username
            )
            print(f'Login succesful | Logged as {reddit.user.me()}')
            return reddit
        except Exception as error:
            print('Login failed')
            print(f'Error: {error}')
            print(50*"-")
    
    def download_image(self, url):
        try:
            print('Downloading image...')
            r = requests.get(url, stream=True)
            with open("image.jpg", 'wb') as f:
                f.write(r.content)
                print('Image downloaded!')
                f.close()
        except Exception as error:
            print(f'Error while downloading the image - Error: {error}')

    def login_twitter(self):
        try:
            print('Logging twitter...')
            auth = tweepy.OAuthHandler(config.api_key, config.api_key_secret)
            auth.set_access_token(config.access_token, config.access_token_secret)
            api = tweepy.API(auth)
            print('Login succesful')
            print(50*"-")
            return api
        except Exception as error:
            print('Login failed')
            print(f'Error: {error}')
            print(50*"-")

    def make_tweet(self, api, content):
        try:
            print('Posting tweet...')
            image_path = 'image.jpg'
            api.update_with_media(image_path, content)
            print('Tweet posted!')
        except Exception as error:
            print(f'Failed to post, error: {error}')

    def add_id(self, post_id):
        print('Adding ID to id.txt')
        with open('id.txt', 'a') as f:
            f.write(f'{post_id}, ')
            f.close()
            print('ID added to end of the file')

    def check_id(self, post_id):
        print('Checking ID')
        with open('id.txt', 'r') as f:
            all_id = f.read().split(', ')
            f.close()
        if post_id not in all_id:
            print('ID ok')
            return False
        print('Submission already post')
        print(50*"-")
        return True

    def main(self):
        reddit = self.login_reddit()
        api = self.login_twitter()
        while True:
            try:
                for submission in reddit.subreddit("projectzomboid").hot(limit=10):
                    print('Fetching submission from reddit')
                    check_id = self.check_id(submission.id)
                    if check_id == False:
                        if submission.stickied == False:
                            url = submission.url
                            title = f'{submission.title} redd.it/{str(submission)}\n#ProjectZomboid'
                            if 'jpg' in url or 'png' in url:
                                self.download_image(url)
                                self.make_tweet(api, title)
                                self.add_id(submission.id)
                                print(50*"-")
                                sleep(300)
                            else:
                                print('There\'s no image')
                                print(50*"-")
                        else:
                            print('Submission stickied, skipping...')
                            print(50*"-")
            except Exception as error:
                print(f'Error while taking informations from reddit. Error: {error}')
                sleep(60)
            now_date = datetime.now()
            print(f"{now_date.strftime('%d')}/{now_date.strftime('%m')}, {now_date.hour}:{now_date.minute} - ", end="")
            print('End of submissions, sleeping for 1 hour')
            print(50*"-")
            sleep(3600)

if __name__ == '__main__':
    pz = ProjectZomboid()
    pz.main()