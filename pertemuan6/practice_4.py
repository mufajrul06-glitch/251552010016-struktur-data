class TextEditor:
    def __init__(self):
        self.undo_stack = []
        self.content = ''

    def write(self, text) :
        self.undo_stack.append(self.content)
        self.content += text
        print(f'Tulis: {self.content}')

    def undo(self) :
        if self.undo_stack:
            self.content = self.undo_stack.pop()
            print(f'Undo: {self.content}')
        else:
            print('Tidak ada yang bisa di-undo.')

editor = TextEditor()
editor.write('Halo') # content: 'Halo'
editor.write(' Dunia') # content: 'Halo Dunia'
editor.write('!') # content: 'Halo Dunia!'
editor.undo() # UNDO → 'Halo Dunia'
editor.undo()