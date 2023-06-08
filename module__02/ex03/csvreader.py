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

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        #  error handling will be done when i'm not that tired 
        file = open("./good.csv","r")
        count = 0
        lst = []
        for line in file:
            if self.skip_top != 0 and count < self.skip_top:
                # is it = or not?
                count += 1
                continue
            if self.skip_bottom != 0 and count >= self.skip_bottom:
                break
            line = line.strip().replace(" ","").replace("\"","")
            inner_lst = line.split(",")
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
        # if self.header is False:
        #     print("we are inside header= false")
        #     return None
        file = open("./good.csv","r")
        line = file.readline().strip().replace(" ","").replace("\"","")
        file.close()
        # the above line is long and hardcode-> is should change it
        # i should try opening the file with "with"
        lst = line.split(sep = ",")
        return lst

if __name__ == "__main__":
    obj = CsvReader()
    # lst = obj.getheader()
    # print(lst)
    data = obj.getdata()
    for line in data:
        print(line)