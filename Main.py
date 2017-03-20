var  = raw_input("Which file do you want to open")
if var == "StudentBecomesTeacher.py":
    import StudentBecomesTeacher
elif var == "BattleShip.py":
    import BattleShip
elif var == "ExamStatistics.py":
    import ExamStatistics
else :
    print "Wrong input!! No such file exists!!"
