class Reader(object):
    def __init__(self):
        pass
    def read(self, fileName, attrType):
        file = open(fileName, mode='r', encoding='utf-8')
        lines = file.readlines()
        line = [self.parse(line, attrType=attrType) for line in lines]
        return line

    def parse(self, line, attrType):
        line = line.replace('\n', '').split('\t')
        return [attrType(x) for x in line]