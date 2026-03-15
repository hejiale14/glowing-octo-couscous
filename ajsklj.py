"""
简易学生成绩管理工具
适合 Python 初学者学习
"""

def show_menu():
    """显示功能菜单"""
    print("\n" + "=" * 40)
    print("       学生成绩管理系统")
    print("=" * 40)
    print("1. 添加学生成绩")
    print("2. 查看所有学生成绩")
    print("3. 计算全班平均分")
    print("4. 查询学生成绩")
    print("5. 退出系统")
    print("=" * 40)


def add_student(students):
    """添加学生成绩"""
    name = input("请输入学生姓名: ").strip()
    
    if not name:
        print("错误：姓名不能为空！")
        return
    
    try:
        score = float(input("请输入学生成绩: "))
        if score < 0 or score > 100:
            print("错误：成绩应在 0-100 之间！")
            return
        students[name] = score
        print(f"成功添加：{name} 的成绩为 {score} 分")
    except ValueError:
        print("错误：请输入有效的数字成绩！")


def show_all_students(students):
    """显示所有学生成绩"""
    if not students:
        print("暂无学生成绩记录！")
        return
    
    print("\n" + "-" * 30)
    print("   姓名\t\t成绩")
    print("-" * 30)
    for name, score in students.items():
        print(f"   {name}\t\t{score}")
    print("-" * 30)
    print(f"共 {len(students)} 名学生")


def calculate_average(students):
    """计算全班平均分"""
    if not students:
        print("暂无学生成绩记录，无法计算平均分！")
        return
    
    total = sum(students.values())
    average = total / len(students)
    print(f"\n全班平均分：{average:.2f} 分")
    print(f"最高分：{max(students.values())} 分")
    print(f"最低分：{min(students.values())} 分")


def query_student(students):
    """查询指定学生成绩"""
    name = input("请输入要查询的学生姓名: ").strip()
    
    if name in students:
        print(f"\n查询结果：{name} 的成绩为 {students[name]} 分")
    else:
        print(f"错误：未找到学生 '{name}' 的成绩记录！")


def main():
    """主程序入口"""
    students = {}
    
    print("\n欢迎使用学生成绩管理系统！")
    
    while True:
        show_menu()
        choice = input("请选择功能 (1-5): ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_all_students(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            query_student(students)
        elif choice == "5":
            print("\n感谢使用，再见！")
            break
        else:
            print("错误：请输入 1-5 之间的数字！")


if __name__ == "__main__":
    main()
