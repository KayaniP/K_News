class News:
    def __init__(self, id, title, content, image, top, state ):
        self.id = id
        self.title = title
        self.content = content
        self.image = image
        self.top = top
        self.state = state
    def get_id(self):
        return self.id
    def get_title(self):
        return self.title
    def get_content(self):
        return self.content
    def get_image(self):
        return self.image
    def get_top(self):
        return self.top
    def get_state(self):
        return self.state
   
        
