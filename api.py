import pymysql
import random
import datetime

conn = pymysql.connect(
    host='124.71.228.59',  # 数据库地址
    port=3306,
    user='DB_USER056',  # 数据库用户名
    password='DB_USER056@123',  # 数据库密码
    db='user056db',  # 数据库名称
    charset='utf8'
)
cursor = conn.cursor()


def Fair_choose_sql():
    sql = '''SELECT * FROM 招聘会 ORDER BY 编号 '''
    cursor.execute(sql)
    res = cursor.fetchall()
    ans = []
    for item in res:
        arr = []
        arr.append(item[1])
        arr.append(item[3])
        ans.append(arr)
    return len(ans), ans


def Job_fair_sql(i = 1, j = 1):
    sql = '''SELECT * FROM 招聘信息 WHERE 招聘会编号 = '%s' GROUP BY 企业编号''' % (i)
    cursor.execute(sql)
    res = cursor.fetchall()
    sum = len(res)
    id = res[j - 1][1]
    sql1 = """SELECT * FROM 招聘信息 WHERE 招聘会编号 = '%s' AND  企业编号 = '%s'""" % (i, id)
    cursor.execute(sql1)
    res = cursor.fetchall()
    ans = ""
    for item in res:
        ans = ans + "岗位：%s，人数：%s，薪资：%s\n" % (item[2], str(item[3]), str(item[4]))
    sql2 = """SELECT * FROM 企业 WHERE 编号 = '%s'""" % id
    cursor.execute(sql2)
    res = cursor.fetchall()[0]
    companyName = res[1]
    sql3 = """SELECT * FROM 招聘会 WHERE 编号 = '%s'""" % i
    cursor.execute(sql3)
    meetingName = cursor.fetchall()[0][1]
    #print(i, sum, j)
    return sum, meetingName, companyName, ans


def Job_fair_s_sql(i = 1, j = 1):
    sql = '''SELECT * FROM 招聘信息 WHERE 招聘会编号 = '%s' GROUP BY 企业编号''' % (i)
    cursor.execute(sql)
    res = cursor.fetchall()
    sum = len(res)
    id = res[j - 1][1]
    sql1 = """SELECT * FROM 招聘信息 WHERE 招聘会编号 = '%s' AND  企业编号 = '%s'""" % (i, id)
    cursor.execute(sql1)
    res = cursor.fetchall()
    ans = ""
    for item in res:
        ans = ans + "岗位：%s，人数：%s，薪资：%s\n" % (item[2], str(item[3]), str(item[4]))
    sql2 = """SELECT * FROM 企业 WHERE 编号 = '%s'""" % id
    cursor.execute(sql2)
    res = cursor.fetchall()[0]
    companyName = res[1]
    code = res[3]
    sql3 = """SELECT * FROM 招聘会 WHERE 编号 = '%s'""" % i
    cursor.execute(sql3)
    meetingName = cursor.fetchall()[0][1]
    return sum, meetingName, companyName, ans, i, code


def IsStudent(u, p):
    if u == "" or p == "":
        return False
    sql = '''SELECT * FROM  `账户` WHERE 账号 = "%s" AND 密码 = "%s"'''%(u, p)
    cursor.execute(sql)
    res = cursor.fetchall()
    if len(res) == 0:
        return False
    # print(res[0][2])
    return res[0][2]=='学生'


def IsCompany(u, p):
    if u == "" or p == "":
        return False
    sql = '''SELECT * FROM  `账户` WHERE 账号 = "%s" AND 密码 = "%s"''' % (u, p)
    cursor.execute(sql)
    res = cursor.fetchall()
    if len(res) == 0:
        return False
    # print(res[0][2])
    return res[0][2] == '企业'


def IsSchool(u, p):
    if u == "" or p == "":
        return False
    sql = '''SELECT * FROM  `账户` WHERE 账号 = "%s" AND 密码 = "%s"''' % (u, p)
    cursor.execute(sql)
    res = cursor.fetchall()
    if len(res) == 0:
        return False
    # print(res[0][2])
    return res[0][2] == '学校'


def Student_base_info_sql(u):
    if u == "":
        return '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'
    sql = '''SELECT * FROM  `基本信息` WHERE 学号 = "%s"''' % u
    cursor.execute(sql)
    res = cursor.fetchall()
    if len(res) == 0:
        return '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'
    if len(res) > 1:
        return '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'

    return res[0][0], res[0][1], res[0][2], res[0][3], res[0][4].strftime('%Y-%m-%d'), res[0][5], res[0][6], res[0][7], boolToString(res[0][8]), res[0][9], res[0][10], res[0][11]


def boolToString(u):
    if u == 0:
        return "无"
    else:
        return "有"


def stringToNumber(u):
    if u == '有':
        return 1
    else:
        return 0


def Student_study_info_sql(u):
    if u == "":
        return '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'
    sql = '''SELECT * FROM 学业信息 WHERE 学号 = "%s"''' % u
    cursor.execute(sql)
    res = cursor.fetchall()
    if len(res) == 0:
        return '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'
    if len(res) > 1:
        return '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'
    return res[0][0], res[0][1], res[0][2], res[0][3], str(res[0][4]), res[0][5], res[0][6], res[0][7], boolToString(res[0][8]), boolToString(res[0][9]), boolToString(res[0][10])


def Company_info_sql(u):
    if u == "":
        return '1', '1', '1', '1', '1', '1', '1'
    sql = '''SELECT * FROM  `企业` WHERE 社会信用代码 = "%s"''' % u
    cursor.execute(sql)
    res = cursor.fetchall()
    if len(res) == 0:
        return '1', '1', '1', '1', '1', '1', '1'
    if len(res) > 1:
        return '1', '1', '1', '1', '1', '1', '1'
    return str(res[0][0]), res[0][1], res[0][2], res[0][3], res[0][4], res[0][5], res[0][6]


def Student_base_update_sql(u, a, b, c, d, e, f, g, h, i, k, l, m):
    if u == "":
        return False, a, b, c, d, e, f, g, h, i, k, l, m
    sql = '''UPDATE 基本信息 SET 姓名 = "%s" ,性别 = "%s" ,籍贯 = "%s" ,出生日期 = "%s" ,身份证号 = "%s" 
 ,政治面貌  = "%s" ,民族 = "%s" ,婚姻状况 = "%s" ,户口所在地 = "%s" ,联系电话 = "%s" ,电子邮箱 = "%s" WHERE 学号 = "%s"''' % (b, c, d, e, f, g, h, stringToNumber(i), k, l, m, u)
    print(sql)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        return False, a, b, c, d, e, f, g, h, i, k, l, m
    return True, a, b, c, d, e, f, g, h, i, k, l, m


def Student_study_update_sql(u, a, b, c, d, e, f, g, h, i, k, l):
    if u == "":
        return False, a, b, c, d, e, f, g, h, i, k, l

    sql = '''UPDATE 学业信息 SET 学院 = "%s" ,专业 = "%s" ,最高学历 = "%s" ,均绩 = "%s" ,英语水平 = "%s" 
    ,计算机水平  = "%s" ,普通话水平 = "%s" ,实习经历 = "%s" ,竞赛经历 = "%s" ,项目经历 = "%s" WHERE 学号 = "%s"''' % (
    b, c, d, e, f, g, h, stringToNumber(i), stringToNumber(k), stringToNumber(l), u)
    print(sql)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        return False, a, b, c, d, e, f, g, h, i, k, l
    return True, a, b, c, d, e, f, g, h, i, k, l


def Company_update_sql(u, a, b, c, d, e, f, g):
    if u == "":
        return False, a, b, c, d, e, f, g
    sql = '''UPDATE 企业 SET 编号 = "%s" ,名称 = "%s" ,类型 = "%s" ,城市 = "%s" ,邮政编码 = "%s" 
    ,联系地址  = "%s" WHERE 社会信用代码 = "%s"''' % (a, b, c, e, f, g, u)
    print(sql)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        return False, a, b, c, d, e, f, g
    return True, a, b, c, d, e, f, g


def Interview_sql(u, a, b, c):
    if u == "":
        return False
    id, _, _, _, _, _, _ = Company_info_sql(u)
    sql = '''INSERT INTO 面试 (学号, 企业编号, 岗位 , 聘用, 薪资) VALUES ("%s", "%s", "%s",  "%s", "%s")''' % (a, id, b, "1", c)
    print(sql)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        return False
    return True


def Job_fair_apply_sql(u, i):
    if u == "" or i == "":
        return False
    sql = '''INSERT INTO 参会 (学号, 招聘会编号) VALUES ("%s", "%s")''' % (u, i)
    print(sql)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        return False
    return True


def Statistic_sql(i):
    sqlCountStudent = """SELECT COUNT(DISTINCT 学号) FROM 面试 """
    cursor.execute(sqlCountStudent)
    numStudentAttend = cursor.fetchall()[0][0]
    sqlCountStudentSucceed = """SELECT COUNT(DISTINCT 学号) FROM 面试 WHERE 聘用 = 1"""
    cursor.execute(sqlCountStudentSucceed)
    numStudentSucceed = cursor.fetchall()[0][0]
    sqlCountStudentAttandMan = """WITH student AS (SELECT DISTINCT 学号 FROM 面试)
SELECT COUNT(student.学号) FROM student LEFT JOIN 基本信息 ON student.学号 = 基本信息.学号 WHERE  性别 = '男'"""
    cursor.execute(sqlCountStudentAttandMan)
    numStudentAttendMan = cursor.fetchall()[0][0]
    sqlCountStudentAttandWoman = """WITH student AS (SELECT DISTINCT 学号 FROM 面试)
    SELECT COUNT(student.学号) FROM student LEFT JOIN 基本信息 ON student.学号 = 基本信息.学号 WHERE  性别 = '女'"""
    cursor.execute(sqlCountStudentAttandWoman)
    numStudentAttendWoman = cursor.fetchall()[0][0]
    sqlCountStudentSucceedMan = """WITH student AS (SELECT DISTINCT 学号 FROM 面试 WHERE 聘用 = 1)
    SELECT COUNT(student.学号) FROM student LEFT JOIN 基本信息 ON student.学号 = 基本信息.学号 WHERE  性别 = '男'"""
    cursor.execute(sqlCountStudentSucceedMan)
    numStudentSucceedMan = cursor.fetchall()[0][0]
    sqlCountStudentSucceedWoman = """WITH student AS (SELECT DISTINCT 学号 FROM 面试 WHERE 聘用 = 1)
        SELECT COUNT(student.学号) FROM student LEFT JOIN 基本信息 ON student.学号 = 基本信息.学号 WHERE  性别 = '女'"""
    cursor.execute(sqlCountStudentSucceedWoman)
    numStudentSucceedWoman = cursor.fetchall()[0][0]
    sqlCountStudentWorkExpr = """WITH student AS (SELECT DISTINCT 学号 FROM 面试)
SELECT COUNT(student.学号) FROM student LEFT JOIN 学业信息 ON student.学号 = 学业信息.学号 WHERE  实习经历 = 1"""
    cursor.execute(sqlCountStudentWorkExpr)
    numStudentWorkExpr = cursor.fetchall()[0][0]
    sqlCountStudentNoWorkExpr = """WITH student AS (SELECT DISTINCT 学号 FROM 面试)
    SELECT COUNT(student.学号) FROM student LEFT JOIN 学业信息 ON student.学号 = 学业信息.学号 WHERE  实习经历 = 0"""
    cursor.execute(sqlCountStudentNoWorkExpr)
    numStudentNoWorkExpr = cursor.fetchall()[0][0]
    sqlCountStudentSucceedWorkExpr = """WITH student AS (SELECT DISTINCT 学号 FROM 面试 WHERE 聘用 = 1)
SELECT COUNT(student.学号) FROM student LEFT JOIN 学业信息 ON student.学号 = 学业信息.学号 WHERE  实习经历 = 1"""
    cursor.execute(sqlCountStudentSucceedWorkExpr)
    numStudentSucceedWorkExpr = cursor.fetchall()[0][0]
    sqlCountStudentSucceedNoWorkExpr = """WITH student AS (SELECT DISTINCT 学号 FROM 面试 WHERE 聘用 = 1)
SELECT COUNT(student.学号) FROM student LEFT JOIN 学业信息 ON student.学号 = 学业信息.学号 WHERE  实习经历 = 0"""
    cursor.execute(sqlCountStudentSucceedNoWorkExpr)
    numStudentSucceedNoWorkExpr = cursor.fetchall()[0][0]
    sqlCountStudentProjectExpr = """WITH student AS (SELECT DISTINCT 学号 FROM 面试)
    SELECT COUNT(student.学号) FROM student LEFT JOIN 学业信息 ON student.学号 = 学业信息.学号 WHERE  项目经历 = 1"""
    cursor.execute(sqlCountStudentProjectExpr)
    numStudentProjectExpr = cursor.fetchall()[0][0]
    sqlCountStudentNoProjectExpr = """WITH student AS (SELECT DISTINCT 学号 FROM 面试)
        SELECT COUNT(student.学号) FROM student LEFT JOIN 学业信息 ON student.学号 = 学业信息.学号 WHERE  项目经历 = 0"""
    cursor.execute(sqlCountStudentNoProjectExpr)
    numStudentNoProjectExpr = cursor.fetchall()[0][0]
    sqlCountStudentSucceedProjectExpr = """WITH student AS (SELECT DISTINCT 学号 FROM 面试 WHERE 聘用 = 1)
    SELECT COUNT(student.学号) FROM student LEFT JOIN 学业信息 ON student.学号 = 学业信息.学号 WHERE  项目经历 = 1"""
    cursor.execute(sqlCountStudentSucceedProjectExpr)
    numStudentSucceedProjectExpr = cursor.fetchall()[0][0]
    sqlCountStudentSucceedNoProjectExpr = """WITH student AS (SELECT DISTINCT 学号 FROM 面试 WHERE 聘用 = 1)
    SELECT COUNT(student.学号) FROM student LEFT JOIN 学业信息 ON student.学号 = 学业信息.学号 WHERE  项目经历 = 0"""
    cursor.execute(sqlCountStudentSucceedNoProjectExpr)
    numStudentSucceedNoProjectExpr = cursor.fetchall()[0][0]
    return '参与招聘的总人数为%s，其中男生有%s人, 女生有%s人。\n' \
           '成功获得offer的有%s人，其中男生有%s人，女生有%s人，\n' \
           '参与招聘的总人数为%s，其中有项目经历的有%s人, 无项目经历的有%s人。\n' \
           '成功获得offer的有%s人，其中有项目经历的有%s人，无项目经历的有%s人。\n' \
           '参与招聘的总人数为%s，其中有实习经历的有%s人, 无实习经历的有%s人。\n' \
           '成功获得offer的有%s人，其中有实习经历的有%s人，无实习经历的有%s人。' \
           % (numStudentAttend, numStudentAttendMan, numStudentAttendWoman,
              numStudentSucceed, numStudentSucceedMan, numStudentSucceedWoman,
              numStudentAttend, numStudentProjectExpr, numStudentNoProjectExpr,
              numStudentSucceed, numStudentSucceedProjectExpr, numStudentSucceedNoProjectExpr,
              numStudentAttend, numStudentWorkExpr, numStudentNoWorkExpr,
              numStudentSucceed, numStudentSucceedWorkExpr, numStudentSucceedNoWorkExpr,
              )


# print(IsStudent("", ""))
# print(IsCompany(951568989080269558, 951568989080269558))
# print(IsSchool(1017289122815, 1017289122815))
#print(Student_base_info_sql(1015043097720))
# print(Student_study_info_sql(1015043097720))
# print(Company_info_sql(532079464493320792))
#print(Student_base_update_sql('1015043097720', '1015043097720', '喻贶', '男', '宁夏回族自治区', '1997-08-15', '51600519970815456X', '中共预备党员', '汉族', '无', '宁夏回族自治区', '13067345030', 'duF6jSW@126.com'))
# print(Student_study_update_sql('1015043097720', '1015043097720', '通信与电子工程学院', '微电子科学与工程', '硕士', '0.0', 'TEM-4', '二级', '一乙', '无', '无', '有'))
# print(Company_update_sql('532079464493320792', '26', '上海浦东发展银行', '私营', '532079464493320792', '上海市', '928708', '普陀区'))
# print(Interview_sql(532079464493320792, 1015414997398, "算法岗", 1000))
# print(Job_fair_apply_sql(1015043097720, 1))
# print(Statistic_sql(0))
# print(Fair_choose_sql())
# print(Job_fair_sql(1, 1))
# print(Job_fair_s_sql(1, 1))
#print(Student_base_info_sql(1015043097720))
