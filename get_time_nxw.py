import datetime
import re

time_dict={"10":["十月", "10月"],"11":["十一月", "11月"],"12":["十二月", "12月"],"01":["一月", "1月"],"02":["二月", "2月"],"03":["三月", "3月"],"04":["四月", "4月"],"05":["五月", "5月"],"06":["六月", "6月"],"07":["七月", "7月"],"08":["八月", "8月"],"09":["九月", "9月"]}

def get_time(sentence):
    result="-".join(str(datetime.date.today()).split("-")[:2])
    for key,value_list in time_dict.items():
        for value in value_list:
            if re.search(value,sentence):
                return str(datetime.datetime.now().year)+"-"+key
            elif re.search("本月",sentence) or re.search("当前月",sentence):  
                return result
            elif re.search("上上月",sentence) or re.search("上上个月",sentence):
                if datetime.datetime.now().month==1:
                    return str(datetime.datetime.now().year-1)+"-"+str(11)
                elif datetime.datetime.now().month==2:
                    return str(datetime.datetime.now().year-1)+"-"+str(12)
                elif datetime.datetime.now().month==12:
                    return str(datetime.datetime.now().year)+"-"+str(10)
                else:
                    return str(datetime.datetime.now().year)+"-0"+str(datetime.datetime.now().month-2)
            elif re.search("上月",sentence) or re.search("上个月",sentence) or re.search("前一个月",sentence):   
                if datetime.datetime.now().month==1:
                    return str(datetime.datetime.now().year-1)+"-"+str(12)
                elif datetime.datetime.now().month==12 or datetime.datetime.now().month==11:
                    return str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month-1)
                else:
                    return str(datetime.datetime.now().year)+"-0"+str(datetime.datetime.now().month-1)
    return result      
    
print(get_time("10月金额是多少"))