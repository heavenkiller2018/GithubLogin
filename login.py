import requests
from lxml import etree


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        # self.logined_url = 'https://github.com/settings/profile'
        self.logined_url = 'https://github.com/settings/sessions'

        self.session = requests.Session()
        self.session.headers=self.headers
    
    def token(self):
        # response = self.session.get(self.login_url, headers=self.headers)
        response = self.session.get(self.login_url)
        print('self.login_url:{0},{1}'.format(self.login_url,response.url))
        print('------headers-----')
        print(dict(self.session.headers))
        print('------cookie from session-----')
        print(dict(self.session.cookies))
        print(response.status_code)
        print('------cookie from response-----')
        print(dict(response.cookies))
        selector = etree.HTML(response.text)
        token = selector.xpath('//div//input[2]/@value')
        return token
    
    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token()[0],
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data)
        print('post the url {0},{1}'.format(self.post_url,response.url))
        print('------headers-----')
        print(dict(self.session.headers))
        print('------cookie from session-----')
        print(dict(self.session.cookies))

        print(response.status_code)
        print('------cookie from response-----')
        print(dict(response.cookies))
        if response.status_code == 200:
            self.dynamics(response.text)
        
        response = self.session.get(self.logined_url)
        print('logined the url {0},{1}'.format(self.logined_url,response.url))
        print('------headers-----')
        print(dict(self.session.headers))
        print('------cookie from session-----')
        print(dict(self.session.cookies))
        print('post the url {0},{1}'.format(self.post_url,response.url))
        print(response.status_code)
        print('------cookie from response-----')
        print(dict(response.cookies))
        # if response.status_code == 200:
        #      print(response.text)
            # self.profile(response.text)
    
    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
        for item in dynamics:
            dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamic)
    
    def profile(self, html):
        selector = etree.HTML(html)
        # name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        # email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        # print(name, email)
        # ipxpath = r"/html/body[@class='logged-in env-production intent-mouse']/div[@class='application-main ']/div[@id='js-pjax-container']/div[@class='page-content container clearfix']/div[@class='col-9 float-left']/div[@class='Box Box-row--gray']/div[@class='Box-row p-3 js-user-session session-device']/div[@class='session-details js-details-container']/strong[@class='d-block']/span"
        ip = selector.xpath(ipxpath)[0]
        print(ip)


if __name__ == "__main__":
    login = Login()
    login.login(email='yangyong_th@qq.com', password='th12345678@')
