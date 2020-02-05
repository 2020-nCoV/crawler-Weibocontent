# -*- coding: UTF-8 -*-


def generator(weibo_list,username,city,time):
    totalNumber = 0
    relatedNumber = 0
    valid_list = ['新型病毒','疫情','确诊','肺炎','隔离']
    for weibo in weibo_list:
        totalNumber = totalNumber + 1
        content = weibo['content']
        for word in valid_list:
            if word in content:
                relatedNumber = relatedNumber + 1
                break
    result = []
    result.append(username)
    result.append(city)
    result.append(time)
    result.append(str(totalNumber))
    result.append(str(relatedNumber))
    result.append(str(relatedNumber/totalNumber * 100))
    return result