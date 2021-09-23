import requests
import pandas as pd


def crawler(start, end, interval):
    r_headers = {
        'referer': 'https://cn.investing.com/equities/apple-computer-inc-historical-data',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'curr_id': '6408',
        'smlID': '1159963',
        'header': 'AAPL历史数据',
        'st_date': start,
        'end_date': end,
        'interval_sec': interval,
        'sort_col': 'date',
        'sort_ord': 'DESC',
        'action': 'historical_data'
    }

    crawler_request = requests.post('https://cn.investing.com/instruments/HistoricalDataAjax', headers=r_headers,
                                    data=data)

    status_code = crawler_request.status_code
    assert status_code, str(status_code)

    data_table = pd.read_html(crawler_request.text)[0]

    return data_table


def main(start='2021/08/01', end='2021/09/01', interval='Daily'):
    crawler_results = crawler(start, end, interval)

    data_name = start.replace('/', '') + '_' + end.replace('/', '') + '.json'
    crawler_results.to_json(data_name, orient='records', force_ascii=False)


if __name__ == '__main__':
    # interval form : Daily / Weekly / Monthly
    # Start &End time form : YYYY/MM/DD
    start_time = '2020/08/01'
    end_time = '2021/09/01'
    interval = 'Daily'

    main(start_time, end_time, interval)