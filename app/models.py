class Sources:
  '''
  Source class to define Source Objects
  '''

  def __init__(self,id,name,description,url,category,country,language):
    self.id =id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
    self.country = country
    self.language = language

class Articles:
  '''
  Articles class to define articles objects
  '''
  def __init__(self,source,author,title,description,url,urlToImage,publishedAt,content):
    self.source = source
    self.author = author
    self.title = title
    self.description = description
    self.url = url
    self.urlToImage = urlToImage
    self.publishedAt = publishedAt
    self.content = content
  