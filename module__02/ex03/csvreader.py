class CsvReader():
    def __init__(self, filename=None, sep=',',\
                header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None
        self.num_lines = 0

    def __enter__(self,):
        if self.filename is None:
            print("filename dosen't exist esssssssssssss")
            return None
        self.file = open(self.filename, "r")
        header = self.file.readline().strip().split(self.sep)
        num_lines = 1
        for line in self.file:
            line = line.strip()
            lst = line.split(self.sep)
            if len(lst) != len(header):
                print("different records ewwwwwwwwwwwww")
                return None
            if '' in lst:
                print("empty line in file ssssssss")
                return None
            num_lines += 1
        self.num_lines = num_lines
        self.file.seek(0, 0)
        if self.skip_bottom < 0 or self.skip_top < 0:
            print("negative skip lkkkkkkkkkk")
            return None
        return self

    def __exit__(self, *args, **kwargs):
        if self.file is None:
            self.file.close()
        return True

    def getdata(self,):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """

        count = 0
        lst = []
        for line in self.file:
            if count == 0 and self.header is False:
                count += 1
                continue
            elif count == 0 and self.header is True:
                line = line.strip().split(self.sep)
                lst.append(line)
                count += 1
                continue
            if self.skip_top != 0 and count <= self.skip_top:
                count += 1
                continue
            if self.skip_bottom != 0 and count >=\
                    self.num_lines - self.skip_bottom:
                break
            line = line.strip().split(self.sep)
            lst.append(line)
            count += 1
        self.file.seek(0, 0)
        return lst

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header is False:
            return None
        elif self.header is True:
            line = self.file.readline().strip()
            self.file.seek(0, 0)
            lst = line.split(self.sep)
            return lst


if __name__ == "__main__":
    with CsvReader('good.csv', header = False,\
                        skip_top = 2, skip_bottom = 2) as file:
        if file is None:
            print("baaaad file it seems ")
        data = file.getdata()
        header = file.getheader()
        print(header)
        for line in data:
            print(line)
