class Piece:
    def __init__(self, x: int, y: str, side, is_king=False):
        self.x = x
        self.y = y
        self.spot = f'{x}, {y}'
        self.is_king = is_king
        self.side = side
        self.color = \
            '%s ⚫ %s' if side == 'player' else '%s ⭕ %s'

    def make_king(self):
        self.is_king = True
        self.color = '%s[K]%s' if self.side == 'player' else '%s(K)%s'
        return self

    def move(self, up_down, left_right, spaces=1):
        if self.is_king:
            if self.side == 'player':
                self.x -= spaces
                if left_right == 'left':
                    self.y = chr(ord(self.y) - spaces)
                elif left_right == 'right':
                    self.y = chr(ord(self.y) + spaces)
            elif self.side == 'cpu':
                self.x += spaces
                if left_right == 'left':
                    self.y = chr(ord(self.y) + spaces)
                elif left_right == 'right':
                    self.y = chr(ord(self.y) - spaces)
        else:
            if up_down == 'up':
                self.x -= spaces
            elif up_down == 'down':
                self.x += spaces

            if left_right == 'left':
                self.y = chr(ord(self.y) - spaces)
            elif left_right == 'right':
                self.y = chr(ord(self.y) + spaces)

        return self
