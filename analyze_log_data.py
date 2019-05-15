import matplotlib.pyplot as plt
import re
import os
import numpy as np
import random


def find_all_dates(data):
    # returns array of all unique dates from the data
    date_arr = []
    for ele in data:
        row = list(ele.split())
        date = row[1][:10]
        if date not in date_arr:
            date_arr.append(date)
    return date_arr


def find_datewise_time(dates_arr, data):
    # returns array of total time date-wise
    datewise_time_arr = []
    for i in range(len(dates_arr)):
        search_date = dates_arr[i]
        time = 0
        for ele in data:
            row = list(ele.split())
            cur_date = row[1][:10]
            if cur_date == search_date:
                time += int(row[2])
        datewise_time_arr.append(time)
    return datewise_time_arr


def draw_graph(x_arr, y_arr):
    my_dpi = 96
    # print(plt.style.available)    # from the available styles choose one
    plt.style.use('fivethirtyeight')
    plt.bar(x_arr, y_arr)

    plt.xticks(x_arr, fontsize=6)
    plt.yticks(fontsize=6)

    plt.xlabel("Date", fontsize=8)
    plt.ylabel("Time (seconds)", fontsize=8)
    plt.title('Analysis of productive work')

    plt.savefig('output_graphs\{}.png'
                .format(random.randint(1, 10000)), dpi=my_dpi)
    plt.show()


if __name__ == '__main__':
    # read the log file
    fp = open('log.txt', 'r')
    # store as row-wise data
    log_data_row_wise = list(fp.read().split('\n'))
    # send data without 1st row which is blank
    dates_arr = find_all_dates(log_data_row_wise[1:])
    print(dates_arr)
    datewise_time_arr = find_datewise_time(dates_arr, log_data_row_wise[1:])
    print(datewise_time_arr)
    draw_graph(dates_arr, datewise_time_arr)