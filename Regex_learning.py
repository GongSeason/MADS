import re

m_list = []
pattern1 = """
(?P<host>.*)  #find the host
(\ -\ )  #an indicator of the -
(?P<user_name>.*)  #find the username
(\ \[)  #separator for the time
(?P<time>.*)  #find the time
(\]\ ")  #separator for the request
(?P<request>.*)
("\ )
(?P<others>.*)  #others
"""
pattern2 = """
(?P<host>.*)  #find the host
(\ -\ -\ )  #an indicator of the -
(?P<user_name>.*)  #find the username
(\ \[)  #separator for the time
(?P<time>.*)  #find the time
(\]\ ")  #separator for the request
(?P<request>.*)
("\ )
(?P<others>.*)  #others
"""


def logs():
    with open("logdata.txt", "r", encoding="utf-8") as file:
        logdata = file.read()

    for item in re.finditer(pattern1, logdata, re.VERBOSE):
        result = item.groupdict()
        if result['user_name'] is None:
            result['user_name'] = '-'
        #if "POST" in result['request']:
        one_item = {'host': result['host'],
                        'user_name': result['user_name'],
                        'time': result['time'],
                        'request': result['request']}
        m_list.append(one_item)
    # for item in re.finditer(pattern2, logdata, re.VERBOSE):
    #     result = item.groupdict()
    #     if result['user_name'] is None:
    #         result['user_name'] = '-'
    #     #if "POST" in result['request']:
    #     one_item = {'host': result['host'],
    #                     'user_name': result['user_name'],
    #                     'time': result['time'],
    #                     'request': result['request']}
    #     m_list.append(one_item)
    return m_list

    # YOUR CODE HERE
    # raise NotImplementedError()


print(len(logs()))