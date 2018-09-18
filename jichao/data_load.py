#导入数值计算库
import numpy as np
#导入科学计算库
import pandas as pd

columns = [
           'eventid',
           'iyear',
           'imonth',
           'iday',
           'approxdate',
           'extended',
           'resolution',
           'country',
           'country_txt',
           'region',
           'region_txt',
           'provstate',
           'city',
           'latitude',
           'longitude',
           'specificity',
           'vicinity',
           'location',
           'summary', #数据字段需要处理
           'crit1',
           'crit2',
           'crit3',
           'doubtterr',
           'alternative',
           'alternative_txt',
           'multiple',
           'success',
           'suicide',
           'attacktype1',
           'attacktype1_txt',
           'attacktype2',
           'attacktype2_txt',
           'attacktype3',
           'attacktype3_txt',
           'targtype1',
           'targtype1_txt',
           'targsubtype1',
           'targsubtype1_txt',
           'corp1',
           'target1',
           'natlty1',
           'natlty1_txt',
           'targtype2',
           'targtype2_txt',
           'targsubtype2',
           'targsubtype2_txt',
           'corp2',
           'target2',
           'natlty2',
           'natlty2_txt',
           'targtype3',
           'targtype3_txt',
           'targsubtype3',
           'targsubtype3_txt',
           'corp3',
           'target3',
           'natlty3',
           'natlty3_txt',
           'gname',
           'gsubname',
           'gname2',
           'gsubname2',
           'gname3',
           'gsubname3',
           'motive',
           'guncertain1',
           'guncertain2',
           'guncertain3',
           'individual',
           'nperps',
           'nperpcap',
           'claimed',
           'claimmode',
           'claimmode_txt',
           'claim2',
           'claimmode2',
           'claimmode2_txt',
           'claim3',
           'claimmode3',
           'claimmode3_txt',
           'compclaim',

           'weaptype1',
           'weaptype1_txt',
           'weapsubtype1',
           'weapsubtype1_txt',
           'weaptype2',
           'weaptype2_txt',
           'weapsubtype2',
           'weapsubtype2_txt',
           'weaptype3',
           'weaptype3_txt',
           'weapsubtype3',
           'weapsubtype3_txt',
           'weaptype4',
           'weaptype4_txt',
           'weapsubtype4',
           'weapsubtype4_txt',
           'weapdetail',

           'nkill',
           'nkillus',
           'nkillter',
           'nwound',
           'nwoundus',
           'nwoundte',

           'property',

           'propextent',
           'propextent_txt',

           'propvalue',
           'propcomment',

           'ishostkid',
           'nhostkid',
           'nhostkidus',
           'nhours',
           'ndays',

           'divert',

           'kidhijcountry',

           'ransom',
           'ransomamt',
           'ransomamtus',
           'ransompaid',
           'ransompaidus',
           'ransomnote',

           'hostkidoutcome',
           'hostkidoutcome_txt',
           'nreleased',

           'addnotes',
           'scite1',
          'scite2',
           'scite3',
           'dbsource',
           'INT_LOG',
           'INT_IDEO',
           'INT_MISC',
           'INT_ANY',
           'related'
]

data_path = "data.xlsx"

print("Ready to Read Data")

sheet = pd.read_excel(io=data_path,
                      header=0,
                      names=columns)

print("After Reading the data")
#


sheet.pop("approxdate")
sheet.pop("country_txt")
sheet.pop("region_txt")
sheet.pop("latitude")
sheet.pop("longitude")
sheet.pop("specificity")
sheet.pop("location")
sheet.pop("summary")
sheet.pop("alternative_txt")
sheet.pop("attacktype1_txt")
sheet.pop("attacktype2_txt")
sheet.pop("attacktype3_txt")

sheet.pop("target1")
sheet.pop("targtype1_txt")
sheet.pop("targsubtype1_txt")
sheet.pop("natlty1_txt")

sheet.pop("target2")
sheet.pop("targtype2_txt")
sheet.pop("targsubtype2_txt")
sheet.pop("natlty2_txt")

sheet.pop("target3")
sheet.pop("targtype3_txt")
sheet.pop("targsubtype3_txt")
sheet.pop("natlty3_txt")

sheet.pop("gsubname")
sheet.pop("gsubname2")
sheet.pop("gsubname3")
sheet.pop("motive")

sheet.pop("claimmode_txt")
sheet.pop("claimmode2_txt")
sheet.pop("claimmode3_txt")


sheet.pop("weaptype1_txt")
sheet.pop("weapsubtype1_txt")
sheet.pop("weaptype2_txt")
sheet.pop("weapsubtype2_txt")
sheet.pop("weaptype3_txt")
sheet.pop("weapsubtype3_txt")
sheet.pop("weaptype4_txt")
sheet.pop("weapsubtype4_txt")
sheet.pop("weapdetail")

sheet.pop("propextent_txt")
sheet.pop("propcomment")
sheet.pop("ransomnote")
sheet.pop("hostkidoutcome_txt")


sheet.pop("addnotes")
sheet.pop("scite1")
sheet.pop("scite2")
sheet.pop("scite3")
sheet.pop("dbsource")
sheet.pop("related")

sheet.pop("INT_LOG")
sheet.pop("iyear")
sheet.pop("imonth")
sheet.pop("iday")
sheet.pop("extended")
sheet.pop("resolution")
sheet.pop("city")
sheet.pop("vicinity")
sheet.pop("crit1")
sheet.pop("crit2")
sheet.pop("crit3")
sheet.pop("multiple")
sheet.pop("attacktype2")
sheet.pop("attacktype3")
sheet.pop("targsubtype1")
sheet.pop("targsubtype2")
sheet.pop("corp2")
sheet.pop("natlty2")
sheet.pop("targtype3")
sheet.pop("targsubtype3")
sheet.pop("corp3")
sheet.pop("natlty3")

sheet.pop("INT_IDEO")
sheet.pop("INT_MISC")
sheet.pop("INT_ANY")
sheet.pop("ransompaidus")
sheet.pop("ransomamtus")
sheet.pop("kidhijcountry")
sheet.pop("divert")
sheet.pop("ndays")
sheet.pop("nhours")
sheet.pop("nhostkidus")
sheet.pop("propvalue")
sheet.pop("nkill")
sheet.pop("weapsubtype4")
sheet.pop("weaptype4")
sheet.pop("weapsubtype3")
sheet.pop("weaptype3")
sheet.pop("weapsubtype2")
sheet.pop("weaptype2")
sheet.pop("weapsubtype1")
sheet.pop("compclaim")
sheet.pop("claim3")
sheet.pop("claimmode3")
sheet.pop("claim2")
sheet.pop("claimmode2")
sheet.pop("individual")
sheet.pop("guncertain3")
sheet.pop("guncertain2")
sheet.pop("guncertain1")
sheet.pop("gname3")
sheet.pop("gname2")
sheet.pop("nwoundus")


# 接下来一行一行的读取数据

print(sheet.head())
print(sheet.keys())

sheet.to_csv("zhangliting.csv")
