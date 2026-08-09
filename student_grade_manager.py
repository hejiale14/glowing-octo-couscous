
def add_student(students):
    """添加学生姓名和成绩"""
    name = input("请输入学生姓名：").strip()
    
    while True:
        try:
            score = float(input("请输入学生成绩："))
            if 0 <= score <= 100:
                break
            else:
                print("成绩应在0-100之间，请重新输入！")
        except ValueError:
            print("输入无效！请输入数字格式的成绩。")
    
    students[name] = score
    print(f"已成功添加：{name} - {score}分")


def show_all_students(students):
    """查看所有学生成绩列表"""
    if not students:
        print("暂无学生成绩信息！")
        return
    
    print("\n" + "=" * 30)
    print("学生成绩列表")
    print("=" * 30)
    for i, (name, score) in enumerate(students.items(), 1):
        print(f"{i}. {name}：{score}分")
    print("=" * 30)


def calculate_average(students):
    """计算全班成绩平均分"""
    if not students:
        print("暂无学生成绩信息，无法计算平均分！")
        return
    
    total = sum(students.values())
    count = len(students)
    average = total / count
    print(f"\n全班共有 {count} 名学生")
    print(f"总成绩：{total:.1f}分")
    print(f"平均分：{average:.1f}分")


def query_student(students):
    """查询指定学生的成绩"""
    if not students:
        print("暂无学生成绩信息！")
        return
    
    name = input("请输入要查询的学生姓名：").strip()
    
    if name in students:
        print(f"\n查询结果：{name} 的成绩是 {students[name]} 分")
    else:
        print(f"\n未找到名为 '{name}' 的学生信息！")


def show_menu():
    """显示功能菜单"""
    print("\n" + "=" * 40)
    print("学生成绩管理系统")
    print("=" * 40)
    print("1. 添加学生成绩")
    print("2. 查看所有学生成绩")
    print("3. 计算全班平均分")
    print("4. 查询学生成绩")
    print("5. 退出程序")
    print("=" * 40)


def main():
    """主函数"""
    students = {}  # 存储学生信息：{姓名: 成绩}
    
    print("欢迎使用学生成绩管理系统！")
    
    while True:
        show_menu()
        
        try:
            choice = input("\n请输入您的选择（1-5）：").strip()
            
            if choice == "1":
                add_student(students)
            elif choice == "2":
                show_all_students(students)
            elif choice == "3":
                calculate_average(students)
            elif choice == "4":
                query_student(students)
            elif choice == "5":
                print("感谢使用学生成绩管理系统，再见！")
                break
            else:
                print("无效选择！请输入1-5之间的数字。")
                
        except Exception as e:
            print(f"发生错误：{e}")
            print("请重新操作。")


if __name__ == "__main__":
    main()
