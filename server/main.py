from typing import Union
import csv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["*"] for all origins during testing
    allow_credentials=True,
    allow_methods=["*"],  # or ["GET", "POST", "PUT", "OPTIONS"]
    allow_headers=["*"],
)

# evan = "cool"

scores = 'scores-test.csv'
# scores_t = 'scores-temp.csv'


lb_sorted = [[] for i in range(5)] #create lb_sorted, sorts leaderboard into lists instead of a table with keys
with open(scores, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in csvreader:
        row_vals = row[0].split(",") #val 0 is the leaderboard number, 1 is player name, 2 is player time in seconds, 3 is player id
        
        lb_sorted[int(row_vals[0])-1].append((int(row_vals[2]), row_vals[1], row_vals[3])) #lb[ leaderboard num ].append( time, name, id ) 
# for i in range(len(lb_sorted)):
#     lb_sorted[i] = sorted(lb_sorted[i])

# saved = 0

def update_csv():
        with open(scores, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

            for i in range(5):
                for j in range(len(lb_sorted[i])):
                    csvwriter.writerow([(i+1),  lb_sorted[i][j][1], lb_sorted[i][j][0], lb_sorted[i][j][2]])

@app.get("/test_connection")
def test():
    return True

@app.get("/lb_sort") #returns lb_sorted
def lbsort():
    return {"leaderboard":lb_sorted}

@app.put("/save/{lb_num}/{name}/{time}/{player_id}")
def save_lb(lb_num: int, name: str, time: int, player_id: str):
    lb_num = lb_num-1

    for i in range(len(lb_sorted[lb_num])):
        if lb_sorted[lb_num][i][0] > time:
                lb_sorted[lb_num].insert(i, (time, name, player_id))
                break


    player_found = False
    repeat_loc = -1

    for i in range(len(lb_sorted[lb_num])):
        if lb_sorted[lb_num][i][2] == player_id:
            if player_found:
                repeat_loc = i
            else:
                player_found = True
        

    if player_found and not repeat_loc == -1:
        lb_sorted[lb_num].pop(repeat_loc)

    while len(lb_sorted[lb_num]) > 10:
        lb_sorted[lb_num].pop(10)

    update_csv()
    return {"leaderboard":lb_sorted}

@app.put("/clear")
def clear_lb():
    global lb_sorted
    lb_sorted = [[] for i in range(5)]
    update_csv()
    return {"leaderboard":lb_sorted}

@app.put("/rmv/{lb_num}/{score_num}")
def rmv_score(lb_num: int, score_num: int):
    global lb_sorted
    removed = lb_sorted[lb_num].pop(score_num)
    index = {"leaderboard": lb_num, "rank": score_num}
    update_csv()
    return {"leaderboard":lb_sorted, "rmv_score":removed, "rmv_index":index}


# @app.put("/scores/{item_id}")
# def update_scores(item_id: int):
#     global saved
#     saved = item_id
#     with open(scores, 'w', newline='') as csvfile:
#         csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         csvwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#         csvwriter.writerow(['4,JAKE,420,jakejakejakejake'])
#     return {"added item:":item_id}


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     global evan
#     evan = evan + "!"
#     return {"item_id": item_id, "q": q, "evan": evan}

# @app.get("/csv")
# def get_csv():
#     csvout = {}
#     with open(scores, newline='') as csvfile:
#         csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#         i = 0
#         for row in csvreader:
#             csvout[i] = row[0]
#             i = i + 1
#     return csvout

# @app.get("/leaderboard") #preconditions: needs a csv that follows leaderboard format
# def leaderboard():
#     leaderboards = {}
#     with open(scores, newline='') as csvfile:
#         csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#         i = 0
#         for row in csvreader:
#             row_vals = row[0].split(",")
#             if row_vals[0] not in leaderboards:
#                 leaderboards[row_vals[0]] = ""
#             leaderboards[row_vals[0]] = leaderboards[row_vals[0]] + row_vals[1] + ": " + row_vals[2] + "(s) | "
#             i = i + 1
#     return leaderboards

# @app.get("/lb_org") #leaderboard organized
# def lborg():
#     leaderboards = {}
#     with open(scores, newline='') as csvfile:
#         csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#         i = 0
#         for row in csvreader:
#             if not i == 0:
#                 row_vals = row[0].split(",")
                
#                 if row_vals[0] not in leaderboards: #val 0 is the leaderboard number
#                     leaderboards[row_vals[0]] = {}
                
#                 playerinfo = row_vals[1]+","+row_vals[3] #val 1 is player name, 3 is player id
#                 leaderboards[row_vals[0]][playerinfo] = int(row_vals[2]) #val 2 is player time in seconds
#             i = i + 1
    
#     sorted_lb = {}
#     for key in leaderboards:
#         # print(leaderboards[key])
#         sorted_board = sorted(leaderboards[key].items(), key=lambda x: x[1])
#         leaderboards[key] = {}
#         for p_info, p_time in sorted_board:
#             leaderboards[key][p_info] = p_time

#     lb_order = sorted(leaderboards)

#     lb_final = {}
#     for val in lb_order:
#         lb_final[val] = leaderboards[val]

#     return lb_final

@app.get("/profanity")
def get_profanity():
    return {"profanity": ["shit", "fuck", "dick", "tit", "sex", "fuk", "fuc", "cum", "hoe", "anus"]}


@app.get("/banned")
def get_banned_list():
    return {"banned": ["rand", "dike", "homo", "sped", "fag", "nig", "nga", "cunt", "coon", "jizz", "piss", "anal", "slut"]}
