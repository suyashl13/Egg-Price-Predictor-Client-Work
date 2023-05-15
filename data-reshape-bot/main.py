from reshape_bot import ReshapeBot

months = {
    'JAN': 31,
    'FEB': 28,
    'MAR': 31,
    'APR': 30,
    'MAY': 31,
    'JUN': 30,
    'JUL': 31,
    'AUG': 31,
    'SEP': 30,
    'OCT': 31,
    'NOV': 30,
    'DEC': 31
}
years = ['16', '17', '18', '19', '20', '21', '22']

if __name__ == '__main__':
    reshape_bot = ReshapeBot(months=months, years=years)
    # reshape_bot.create_csv_files()
    reshape_bot.work()
