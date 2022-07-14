# import json

# json_object = {
#     "hpc_id": '',
#     "hpc_pw": '',
#     "hpc_address": '',
#     "login_key": '',
#     "id": 1,
#     "filename": "dfsdfsdfsef.sdy",
    #   "filename_path" : ""
#     "ncpu": "8",
#     "postfix": "",
#     "run_cmd": "lsdyna ncpu=8 i=dfsdfsdfsef.sdy",
#     "include_file_n": "4",
#     "include_file": {
#         "1": "dfsdfsdfsef.k",
#         "2": "dfsdf.k",
#         "3": "dfsdss.k",
#         "4": "dfww.k"
#     },
#     "include_file_path": {
#         "1": "dfsdfsdfsef.k",
#         "2": "dfsdf.k",
#         "3": "dfsdss.k",
#         "4": "dfww.k"
#     },
#     "solve_key": '',
#     "running_key": '',
#     "error_key": '',
#     "bkill_key": '',
#     "status": 'uploading',
#     "status_progress": '22%',
#     "scratch": '1'
# }

# json_object['include_file']['1'] = ('2.k')
# json_object['id'] = ('2')
# with open('data.json', 'w') as f:
#     json_string = json.dump(json_object, f, indent=2)

ll = [2,4,7,9]
lo = [11,23,56,55]
for i, (ii, iii) in enumerate(zip(ll, lo)):
# for ii, iii in zip(ll, lo):
    globals()["table_list_{}".format(i)] = {'a': ii, 'b':iii}

d = {'a': 123123}

# d[999] = 10
d['99'] = 111
d['dd'] = [1, 2, 3]
d[(1,2)] = 'sdfwer'
d[1] = (3, 'a', 5)

print(table_list_1[999])

