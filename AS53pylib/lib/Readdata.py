from xlrd import open_workbook

class as53data:
    def testingdata(self):
        dataget = open_workbook('C:/usr/local/bin/as5300data_auto.xlsx')

        values = []
        for s in dataget.sheets():
            for row in range(1,s.nrows):
                col_names=s.row(0)
                col_value=[]
                for name, col in zip (col_names,range(s.ncols)):
                    values = (s.cell(row,col).value)
                    try:
                        values = str(int(values))
                    except:
                        pass
                    col_value.append(values)
                values.append(col_value)
        return values
