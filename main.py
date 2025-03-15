from typing import Union
import csv

from fastapi import FastAPI

app = FastAPI()

evan = "cool"

scores = 'scores-test.csv'

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    global evan
    evan = evan + "!"
    return {"item_id": item_id, "q": q, "evan": evan}

@app.get("/csv")
def get_csv():
    csvout = {}
    with open(scores, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in csvreader:
            csvout[i] = row[0]
            i = i + 1
    return csvout

@app.get("/leaderboard") #preconditions: needs a csv that follows leaderboard format
def leaderboard():
    leaderboards = {}
    with open(scores, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in csvreader:
            row_vals = row[0].split(",")
            if row_vals[0] not in leaderboards:
                leaderboards[row_vals[0]] = ""
            leaderboards[row_vals[0]] = leaderboards[row_vals[0]] + row_vals[1] + ": " + row_vals[2] + "(s) | "
            i = i + 1
    return leaderboards

@app.get("/lb_org") #leaderboard organized
def lborg():
    leaderboards = {}
    with open(scores, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in csvreader:
            if not i == 0:
                row_vals = row[0].split(",")
                
                if row_vals[0] not in leaderboards: #val 0 is the leaderboard number
                    leaderboards[row_vals[0]] = {}
                
                playerinfo = row_vals[1]+","+row_vals[3] #val 1 is player name, 3 is player id
                leaderboards[row_vals[0]][playerinfo] = int(row_vals[2]) #val 2 is player time in seconds
            i = i + 1
    
    sorted_lb = {}
    for key in leaderboards:
        # print(leaderboards[key])
        sorted_board = sorted(leaderboards[key].items(), key=lambda x: x[1])
        leaderboards[key] = {}
        for p_info, p_time in sorted_board:
            leaderboards[key][p_info] = p_time

    lb_order = sorted(leaderboards)

    lb_final = {}
    for val in lb_order:
        lb_final[val] = leaderboards[val]

    return lb_final

@app.get("/lb_sort") #sorts leaderboard into lists instead of a table with keys
def lbsort():
    leaderboards = {}
    lb_sorted = [[] for i in range(5)]

    with open(scores, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in csvreader:
            if not i == 0:
                row_vals = row[0].split(",")
                
                if row_vals[0] not in leaderboards: #val 0 is the leaderboard number
                    leaderboards[row_vals[0]] = {}
                
                playerinfo = row_vals[1]+","+row_vals[3] #val 1 is player name, 3 is player id
                leaderboards[row_vals[0]][playerinfo] = int(row_vals[2]) #val 2 is player time in seconds

                lb_sorted[int(row_vals[0])-1].append((int(row_vals[2]), row_vals[1], row_vals[3]))

            i = i + 1
    
    sorted_lb = {}
    for key in leaderboards:
        # print(leaderboards[key])
        sorted_board = sorted(leaderboards[key].items(), key=lambda x: x[1])
        leaderboards[key] = {}
        for p_info, p_time in sorted_board:
            leaderboards[key][p_info] = p_time

    lb_order = sorted(leaderboards)

    lb_final = {}
    for val in lb_order:
        lb_final[val] = leaderboards[val]

    for i in range(len(lb_sorted)):
        lb_sorted[i] = sorted(lb_sorted[i])


    return {"leaderboard":lb_sorted}

@app.put("/scores/{item_id}")
def update_scores(item_id: int):
    return {"added item:":item_id}
    
