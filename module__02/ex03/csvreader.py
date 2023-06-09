class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        # i added this attribute myself(not required by subj)
        self.file = None
    def __enter__(self,):
        if self.filename == None:
            return None
        print("the filname is ", self.filename)
        file = open(self.filename,"r")
        self.file = file
        header = line = file.readline().strip().split(self.sep)
        for line in file:
            line = line.strip()
            lst = line.split(self.sep)
            if len(lst) != len(header):
                return None
            if '' in lst:
                print("we have an empty value")
                return None
        # return self.getdata()
        return file
# i should remember that all of the good.csv should be replaced 
# with self.filename
    def __exit__(self, *args, **kwargs):
        if self.file != None:
            self.file.close()
        

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        #  error handling will be done when i'm not that tired 
        file = open(self.filename,"r")
        count = 0
        lst = []
        for line in file:
            if self.skip_top != 0 and count < self.skip_top:
                # is it = or not?
                count += 1
                continue
            if self.skip_bottom != 0 and count >= self.skip_bottom:
                break
            # line = line.strip().replace(" ","").replace("\"","")
            line = line.strip()
            inner_lst = line.split(self.sep)
            lst.append(inner_lst)
            count += 1
        file.close()
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
            file = open(self.filename,"r")
            line = file.readline().strip()
            file.close()
            # the above line is long and hardcode-> is should change it
            # i should try opening the file with "with"
            lst = line.split(self.sep)
            return lst

if __name__ == "__main__":
    # obj = CsvReader("./good.csv", ',',header = True)
    # lst = obj.getheader()
    # print(lst)
    # data = obj.getdata()
    # for line in data:
    #     print(line)
    with CsvReader('good.csv') as file:
        if file == None:
            print("File is corrupted")
        else:
            print("File isn't corrupted")