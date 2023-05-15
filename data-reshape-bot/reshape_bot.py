class ReshapeBot:

    def __init__(self, months: dict, years: list):
        self.months = months
        self.mon_list = [
            'JAN',
            'FEB',
            'MAR',
            'APR',
            'MAY',
            'JUN',
            'JUL',
            'AUG',
            'SEP',
            'OCT',
            'NOV',
            'DEC',
        ]
        self.years = years
        self.locations = [
            'Ahmedabad',
            'Ajmer',
            'Asansole',
            'Barwala',
            'Bengaluru (CC)',
            'Brahmapur (OD)',
            'Burdwan (CC)',
            'Chennai (CC)',
            'Chittoor',
            'Delhi (CC)',
            'E.Godavari',
            'Hospet',
            'Hyderabad',
            'Jabalpur',
            'Kolkata (WB)',
            'Ludhiana',
            'Midnapur (KOL)',
            'Mumbai (CC)',
            'Mysuru',
            'Namakkal',
            'Pune',
            'Raipur',
            'Surat',
            'Vijayawada',
            'Vizag',
            'W.Godavari',
            'Warangal',
            'Prevailing Prices',
            'Allahabad (CC)',
            'Bhopal',
            'Indore (CC)',
            'Jabalpur',
            'Kanpur (CC)',
            'Luknow (CC)',
            'Muzaffurpur (CC)',
        ]

    def create_csv_files(self):
        for location in self.locations:
            cf = open('BOT_OUTPUT_DATA/' + location + '.csv', 'w+')
            cf.close()

    def work(self):
        for year in self.years:
            for month in self.months.keys():
                csv_file = open('BOT_INPUT_DATA/' + '{}_{}.csv'.format(month, year), 'r+')
                csv_lines = csv_file.readlines()

                for line in csv_lines:
                    line_arr = line.split(',')
                    for word_no in range(len(line_arr)):
                        if line_arr[word_no] in self.locations:
                            with open('BOT_OUTPUT_DATA/{}.csv'.format(line_arr[word_no]), 'a+') as op_csv:
                                for i in range(1, self.months[month] + 1):
                                    if i == 1 and month == "JAN" and year == '16':
                                        op_csv.write('ds,y\n'.format('ds', 'y'))

                                    op_csv.write('20{}-{}-{},{}\n'.format(year, self.mon_list.index(month) + 1, i, line_arr[word_no + i]))
