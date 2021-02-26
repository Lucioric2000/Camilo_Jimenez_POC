import scrapy


class CodevalidatorSpider(scrapy.Spider):
    name = 'codevalidator'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        print(response.text)
        assert 0, response
        pass

    def start_requests(self):
        login_url = "https://www.amazon.com/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgc%2Fredeem&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_gcfront_v2_us&openid.mode=checkid_setup&marketPlaceId=ATVPDKIKX0DER&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_gcfront_v2_us&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=3600&siteState=clientContext%3D136-2149562-9967828%2CsourceUrl%3Dhttps%253A%252F%252Fwww.amazon.com%252Fgc%252Fredeem%2Csignature%3DHm2IkRPdd0YabjfEWKxPFIuoFLAj3D"
        yield scrapy.http.FormRequest(login_url,
            formdata={"email": "lucioric2000@gmail.com", "password": "wl8m5tNk"}, callback=self.parse)
