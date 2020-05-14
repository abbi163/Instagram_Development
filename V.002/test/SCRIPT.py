
from instagram_private_api import Client, ClientCompatPatch
from instagram_private_api.errors import ClientError  
import time
class Instagram(object):
    def __init__(self, username = None, password = None):
        self.username = username
        self.password = password
        self.api = self.login()
        
    def login(self):
        return Client(self.username, self.password)
    
    def get_userId(self, user):
        # Getting userId to send follo or unfollow request according to this python package !
        ''' return userId for crossponding user which can be used to send follow | unfollow request '''
        return self.api.user_detail_info(user)['reel_feed']['id']
    
    def get_mediaId(self, user):
        ''' Returns mediaId for public account, 
            Note: Only top 12 media id is returned if total number of media is more than 12 else return media id
            of all the posts
        '''
        return [item['id'] for item in self.api.user_detail_info(user)['feed']['items']]
    
    def follow(self, user):
        userId = self.api.user_detail_info(user)['reel_feed']['id']
        self.api.friendships_create(userId)
        
    def unfollow(self, user):
        userId = self.api.user_detail_info(user)['reel_feed']['id']
        self.api.friendships_destroy(userId) 
        
    def likeUserPhotos(self, user, amount = None, sleepTime = 2):
        '''
        Like photos of user if username is given.
        
        # Note : change sleepTime if required
        
        Example: 
            >>> likeUserPhotos(user, amount = None, sleepTime = 2)
        '''
        media_id = [item['id'] for item in self.api.user_detail_info(user)['feed']['items']]
        if amount == None : 
            count = len(media_id)
        elif amount > len(media_id):
            count = len(media_id)
        else:
            count = amount
        for i in range(0 , count):
            self.api.post_like(media_id[i])
            time.sleep(sleepTime)
    def privateAccount(self, user):
        ''' True if the account is private else False '''
        return self.api.user_detail_info(user)['user_detail']['user']['is_private']
            