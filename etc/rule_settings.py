# -*- coding: utf-8 -*-

# "sort": ["牙体牙髓", "牙周", "口腔外科", "口腔种植],
# "department : ["总院", "第一门诊部", "第二门诊部", "第三门诊部", "第四门诊部", "第五门诊部"]
# "title": ["普通号", "专家号", "主任医师", "副主任医师", "主治医师", "住院医师" , "(  )"]
# "doctor": ["xxx", "yyy"]
# "time": ["上午", "下午"]
# "week": ["星期一", "星期二", ""星期天"]

SETTINGS = {
    "sorts": ["牙体牙髓"],  # 号种
    "department": ["总院", "第一门诊部", "第二门诊部"],  # 门诊部
    "title": [],  # 医师级别
    "doctor": [],  # 医师名
    "time": [],  # 上/下午
    "week": [],  # 星期
    "title_reverse": ["住院医师", "(  )", "普通号"],  # 反选职级(不要哪些级别)
    "doctor_reverse": [],  # 反选医生(不要哪些医生)
}
