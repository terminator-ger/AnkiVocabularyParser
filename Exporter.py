class Exporter:
    def __init__(self):
        self.vocabularies = []
    
    def add(self, results):
        [self.vocabularies.append(x) for x in results]
    
    def save(self, filename):
        with open(filename, 'a+') as fout:
            fout.write(f"#deck:{filename}\n")
            for line in self.vocabularies:
                fout.write(f"{line[0]};{line[1]}\n")