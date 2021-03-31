from core import HTML
import json

class Article:
    def __init__(self,url,proxies=None,headers=None):
        self.metadata = HTML(url,proxies,headers)
        self.source = self.metadata.source
        self.parse()
        self.json = {
            'title' : self.title,
            'article_title' : self.articleTitle,
            'article_subtitle' : self.articleSubtitle,
            'seo_json' : self.seo_json,
            'meta' : self.meta,
            'content' : self.content,
            'images' : self.images
        }
        json.dump(self.json,open('test.json','w'),indent=4)

    def parse(self):
        self.title = self.getTitle()
        self.seo_json = self.getDescriptionScripts()
        self.parseMeta()
        self.parseContent()


    def getTitle(self):
        title = self.source.find('title')
        return title.text

    def getDescriptionScripts(self):
        scripts = self.source.find_all('script',{'type' : 'application/ld+json'})
        data = []
        for script in scripts:
            data.append(json.loads(script.string))
        return data
    
    def parseMeta(self):
        data = []
        meta = self.source.find_all('meta',content=True)
        for item in meta:
            data.append(item.attrs)
        self.meta = data

    def parseContent(self):
        self.articleTitle = self.source.find('h1',{'id':'article_title'}).text
        self.articleSubtitle = self.source.find('h2',{'id':'article_sapo'}).text
        self.getImages()
        self.getContent()
    
    def getImages(self):
        images = self.source.find_all('img',{'class':'news-image'})
        data = []
        for image in images:
            data.append({
                'caption' : image['alt'],
                'src' : image['src']
            })
        self.images = data
    
    def getContent(self):
        ps = self.source.find_all(lambda tag: tag.name == 'p' and not tag.attrs)
        data = []
        for p in ps:
            data.append(p.text)
        self.content = data





class Crawler:
    pass
