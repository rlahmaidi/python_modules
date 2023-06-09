# Important : when iteration over a file or wrting lines to it
# the pointer is now at the end , close the file and open it again


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        # i added this attribute myself(not required by subj)
        self.file = None
        self.ret_file = None
    def __enter__(self,):
        if self.filename == None:
            return None
        self.file = open(self.filename,"r")
        header = self.file.readline().strip().split(self.sep)
        num_lines = 1
        for line in self.file:
            line = line.strip()
            lst = line.split(self.sep)
            if len(lst) != len(header):
                return None
            if '' in lst:
                print("we have an empty value")
                return None
            num_lines += 1
        # we are at EOF so we close and open again to go back to start
        self.file.close()
        self.file = open(self.filename, "r")
        if self.header is False and self.skip_bottom == self.skip_top == 0:
            self.file.readline()
            return self.file
        elif self.skip_bottom != 0 or self.skip_top != 0:
            if self.skip_bottom < 0 or self.skip_top < 0:
                return None
            self.ret_file = open("./return_file","w")
            count = 0
            lst = []
            for line in self.file:
                if count == 0 and self.header is False:
                    count += 1
                    continue
                elif count == 0 and self.header is True:
                    lst.append(line)
                    count += 1
                    continue
                if self.skip_top != 0 and count <= self.skip_top:
                    # is it = or not?
                    count += 1
                    continue
                if self.skip_bottom != 0 and count >= num_lines - self.skip_bottom:
                    break
                lst.append(line)
                count += 1
            self.ret_file.writelines(lst)
            self.ret_file.close()
            self.ret_file = open("./return_file", "r")
            self.file = self.ret_file
            return self.file
    

    def __exit__(self, *args, **kwargs):
        if self.file != None:
            self.file.close()
        if self.ret_file != None:
            self.ret_file.close()
        

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
    
        # file = open(self.filename,"r")
        count = 0
        lst = []
        for line in self.file:
            if self.skip_top != 0 and count < self.skip_top:
                # is it = or not?
                count += 1
                continue
            if self.skip_bottom != 0 and count >= self.skip_bottom:
                break
            line = line.strip()
            inner_lst = line.split(self.sep)
            lst.append(inner_lst)
            count += 1
        # file.close()
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
    obj = CsvReader("./good.csv", ',',header = True)
    lst = obj.getheader()
    print(lst)
    data = obj.getdata()
    for line in data:
        print(line)
    with CsvReader('good.csv', header = False, skip_top = 2, skip_bottom = 2) as file:
        if file == None:
            print("File is corrupted")
        else:
            print("File isn't corrupted")
            for line in file:
                print(line)
    # with CsvReader('good.csv') as file:
    #     data = file.getdata()
    #     header = file.getheader()
    