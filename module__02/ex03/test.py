if __name__ == "__main__":
    with CsvReader('good.csv',
                   header=False, skip_top=2, skip_bottom=2) as file:
        if file is None:
            print("baaaad file it seems ")
        data = file.getdata()
        header = file.getheader()
        print(header)
        for line in data:
            print(line)