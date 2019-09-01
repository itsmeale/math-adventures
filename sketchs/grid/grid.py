class Grid:
    
    def __init__(self, width, height, x_range, y_range):
        self.width = width
        self.height = height
        self.x_range = x_range
        self.y_range = y_range
        self.x_scale = width/(x_range[1] - x_range[0])
        self.y_scale = -height/(y_range[1] - y_range[0])
        
    def draw(self):
        translate(width/2, height/2)
        background(255)
        strokeWeight(1)
        Grid.cyan_stroke()
        
        xmin, xmax = self.x_range
        ymin, ymax = self.y_range
        
        for i in range(ymin, ymax + 1):
            self.line(xmin, i, xmax, i)
        
        for i in range(xmin, xmax + 1):
            self.line(i, ymin, i, ymax)
            
        Grid.black_stroke()
        self.line(0, ymin, 0, ymax)
        self.line(xmin, 0, xmax, 0)
    
    def plot(self, x, y):
        fill(0)
        self.ellipse(x, y, 10, 10)

    def plot_fx(self, fx):
        Grid.red_stroke()
        
        x, xmax = self.x_range
        while x <= xmax:            
            self.line(x, fx(x), (x+0.1), fx(x+0.1))
            x += 0.1
            
        Grid.black_stroke()

    def line(self, x1, y1, x2, y2):
        line(
             x1 * self.x_scale, y1 * self.y_scale,
             x2 * self.x_scale, y2 * self.y_scale
        )
    
    def ellipse(self, x, y, w, h):
        ellipse(x * self.x_scale, y * self.y_scale, w, h)

    @staticmethod
    def cyan_stroke():
        stroke(0, 255, 255)
    
    @staticmethod
    def red_stroke():
        stroke(255, 0, 0)
    
    @staticmethod
    def black_stroke():
        stroke(0)
