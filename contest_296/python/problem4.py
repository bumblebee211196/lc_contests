class TextEditor:

    def __init__(self):
        self.lstack = []
        self.rstack = []

    def addText(self, text: str) -> None:
        for c in text:
            self.lstack.append(c)

    def deleteText(self, k: int) -> int:
        dels = 0
        while self.lstack and k > 0:
            self.lstack.pop()
            k -= 1
            dels += 1
        
        return dels

    def cursorLeft(self, k: int) -> str:
        while self.lstack and k > 0:
            self.rstack.append(self.lstack.pop())
            k -= 1
        
        l = len(self.lstack)
        return "".join(self.lstack[max(0, l - 10) : ])

    def cursorRight(self, k: int) -> str:
        while self.rstack and k > 0:
            self.lstack.append(self.rstack.pop())
            k -= 1
        
        l = len(self.lstack)
        return "".join(self.lstack[max(0, l - 10) : ])
