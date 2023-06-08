class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        
    def __enter__(self,):
        if self.filename == None:
            return None
        
    # ... Your code here ...
    def __exit__():
        pass
    # ... Your code here ...
    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        pass
    # ... Your code here ...
    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        # if self.header is False:
        #     print("we are inside header= false")
        #     return None
        file = open("./good.csv","r")
        line = file.readline().strip().replace(" ","").replace("\"","")
        # the above line is long and hardcode-> is should change it
        lst = line.split(sep = ",")
        print(line)
        print("this is lst ",lst)
    # ... Your code here ...

if __name__ == "__main__":
    obj = CsvReader()
    obj.getheader()