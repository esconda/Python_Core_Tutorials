from inspect import getfile
import scrapy
import os
class StackOvFlowSpider(scrapy.Spider):
    name = 'stackoverflow' # each spider has a unique name
    start_urls = ['http://stackoverflow.com/questions?sort=votes'] # the parsing starts from a specific set of urls
    
    def parse(self, response): # for each request this generator yields, its response is sent to parse_question
        print(response.css('.question-summary a::attr(href)'))
        for href in response.css('.question-summary h3 a::attr(href)'): # do some scraping stuffusing css selectors to find question urls
            
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)
    
    def getFile(pFileName):
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #it gets the folder location
        fileName= os.path.join(location,pFileName)#add file name to folder location
        return fileName
        
    def parse_question(self, response):
        print("HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        dataInfo = {'title': response.css('h1 a::text').extract_first(),
            'votes': response.css('.question .vote-count-post::text').extract_first(),
            'body': response.css('.question .post-text').extract_first(),
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url}
        print(getfile("data.csv"))
        with open(getfile("data.csv"), 'wb') as f:
            f.write(dataInfo)
        yield {
            'title': response.css('h1 a::text').extract_first(),
            'votes': response.css('.question .vote-count-post::text').extract_first(),
            'body': response.css('.question .post-text').extract_first(),
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
        }
        