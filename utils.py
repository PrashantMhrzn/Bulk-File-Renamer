import os


class Renamer:

    @property
    def heading(self):
        print('*'*35)
        print('Welcome to the Bulk File Renamer!')
        print('*'*35)

    def rename(self, path, naming_convention):
        if path[:-1] != '/':
            path += '/'
        for self.count, self.files in enumerate(os.listdir(path), 1):
            # print(count, files)
            self.extension = self.files.split(".")
            self.filename = path + self.files
            if '.' in self.files:
                self.new_filename = naming_convention + str(self.count) + '.' + self.extension[1]
            else:
                self.new_filename = naming_convention + str(self.count)
            self.new_filename = path + self.new_filename
            os.rename(self.filename, self.new_filename)
