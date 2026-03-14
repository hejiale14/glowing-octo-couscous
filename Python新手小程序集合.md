# Python 新手小程序集合

以下是三个适合 Python 初学者练习的小程序，代码简洁易懂，注释清晰，可直接复制运行。

---

## 1. 简易学生成绩管理工具

### 功能描述
- 录入学生姓名和单科成绩（支持重复录入）
- 查看所有已录入的学生成绩列表
- 计算并展示全班成绩的平均分、最高分、最低分
- 支持退出程序
- 基础异常处理，避免输入非数字成绩时报错崩溃

### 完整代码
```python
# 简易学生成绩管理工具
# 使用纯 Python 基础语法实现

students = []  # 存储学生信息的列表

def show_menu():
    """显示功能菜单"""
    print("\n" + "=" * 30)
    print("学生成绩管理系统")
    print("=" * 30)
    print("1. 录入学生成绩")
    print("2. 查看所有成绩")
    print("3. 计算统计信息")
    print("4. 退出程序")
    print("=" * 30)

def input_score():
    """录入学生成绩"""
    while True:
        name = input("\n请输入学生姓名（输入 'q' 返回主菜单）：").strip()
        if name.lower() == 'q':
            break
        if not name:
            print("姓名不能为空，请重新输入！")
            continue
        
        try:
            score = float(input(f"请输入 {name} 的成绩："))
            if 0 <= score <= 100:
                students.append({"name": name, "score": score})
                print(f"已成功录入：{name} - {score} 分")
            else:
                print("成绩应在 0-100 之间，请重新输入！")
        except ValueError:
            print("输入错误！请输入有效的数字成绩。")

def show_all():
    """查看所有成绩"""
    print("\n" + "-" * 30)
    print("学生成绩列表")
    print("-" * 30)
    if not students:
        print("暂无学生成绩记录！")
        return
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']}：{student['score']} 分")
    print("-" * 30)

def calculate_stats():
    """计算统计信息"""
    if not students:
        print("\n暂无学生成绩，无法计算统计信息！")
        return
    
    scores = [s["score"] for s in students]
    avg_score = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    
    print("\n" + "=" * 30)
    print("成绩统计信息")
    print("=" * 30)
    print(f"总人数：{len(students)} 人")
    print(f"平均分：{avg_score:.2f} 分")
    print(f"最高分：{max_score} 分")
    print(f"最低分：{min_score} 分")
    print("=" * 30)

def main():
    """主函数"""
    print("欢迎使用学生成绩管理系统！")
    while True:
        show_menu()
        try:
            choice = input("请输入您的选择（1-4）：").strip()
            if choice == '1':
                input_score()
            elif choice == '2':
                show_all()
            elif choice == '3':
                calculate_stats()
            elif choice == '4':
                print("\n感谢使用，再见！")
                break
            else:
                print("输入无效，请输入 1-4 之间的数字！")
        except Exception as e:
            print(f"发生错误：{e}")

if __name__ == "__main__":
    main()
```

---

## 2. 随机趣味名言生成器

### 安装依赖
```bash
pip install colorama
```

### 功能描述
- 内置 10+ 条励志/趣味中英文名言
- 随机生成 1 条名言 / 查看所有名言 / 退出程序
- 生成名言时附带随机颜色文字输出
- 代码结构清晰，包含函数封装

### 完整代码
```python
# 随机趣味名言生成器
# 使用 colorama 库实现彩色输出

import random
from colorama import init, Fore, Back, Style

# 初始化 colorama
init(autoreset=True)

# 名言库（包含中英文）
QUOTES = [
    ("Life is like riding a bicycle. To keep your balance, you must keep moving.", "Albert Einstein"),
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("天才是百分之一的灵感加上百分之九十九的汗水。", "爱迪生"),
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    ("生活就像海洋，只有意志坚强的人，才能到达彼岸。", "马克思"),
    ("The best way to predict the future is to create it.", "Peter Drucker"),
    ("书山有路勤为径，学海无涯苦作舟。", "韩愈"),
    ("Imagination is more important than knowledge.", "Albert Einstein"),
    ("不积跬步，无以至千里；不积小流，无以成江海。", "荀子"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
    ("Where there is a will, there is a way.", "Anonymous"),
    ("坚持就是胜利！", "中国谚语"),
]

# 可用的文字颜色
COLORS = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE,
    Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

def show_menu():
    """显示菜单"""
    print("\n" + "=" * 40)
    print(Fore.CYAN + "✨ 随机趣味名言生成器 ✨")
    print("=" * 40)
    print("1. 随机生成一条名言")
    print("2. 查看所有名言")
    print("3. 退出程序")
    print("=" * 40)

def random_quote():
    """随机生成一条带颜色的名言"""
    quote, author = random.choice(QUOTES)
    color = random.choice(COLORS)
    
    print("\n" + "~" * 50)
    print(color + f"「{quote}」")
    print(color + f"    —— {author}")
    print("~" * 50)

def show_all_quotes():
    """显示所有名言"""
    print("\n" + "-" * 50)
    print(Fore.YELLOW + "📚 名言库（共 {} 条）".format(len(QUOTES)))
    print("-" * 50)
    for i, (quote, author) in enumerate(QUOTES, 1):
        print(f"{i}. {quote} —— {author}")
    print("-" * 50)

def main():
    """主函数"""
    print(Fore.GREEN + "欢迎使用随机趣味名言生成器！")
    print(Fore.GREEN + "每次为您带来不一样的心灵触动~")
    
    while True:
        show_menu()
        try:
            choice = input("请输入您的选择（1-3）：").strip()
            if choice == '1':
                random_quote()
            elif choice == '2':
                show_all_quotes()
            elif choice == '3':
                print(Fore.GREEN + "\n感谢使用，祝您生活愉快！")
                break
            else:
                print(Fore.RED + "输入无效，请输入 1-3 之间的数字！")
        except Exception as e:
            print(Fore.RED + f"发生错误：{e}")

if __name__ == "__main__":
    main()
```

---

## 3. 本地文本备忘录

### 功能描述
- 新建备忘录（写入文本内容）
- 查看已保存的备忘录内容
- 清空备忘录
- 数据永久保存在本地 txt 文件中
- 菜单式交互，异常处理完善

### 完整代码
```python
# 本地文本备忘录
# 使用纯 Python 基础语法实现

import os

# 备忘录文件路径
FILE_PATH = "memo.txt"

def show_menu():
    """显示菜单"""
    print("\n" + "=" * 30)
    print("📝 本地文本备忘录")
    print("=" * 30)
    print("1. 新建备忘录")
    print("2. 查看备忘录")
    print("3. 清空备忘录")
    print("4. 退出程序")
    print("=" * 30)

def write_memo():
    """写入备忘录内容"""
    print("\n--- 新建备忘录 ---")
    content = input("请输入备忘录内容（输入完成按回车）：\n").strip()
    
    if not content:
        print("内容不能为空！")
        return
    
    try:
        # 追加模式写入
        with open(FILE_PATH, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        print("✅ 备忘录已保存！")
    except Exception as e:
        print(f"❌ 保存失败：{e}")

def read_memo():
    """读取备忘录内容"""
    print("\n--- 备忘录内容 ---")
    
    if not os.path.exists(FILE_PATH):
        print("暂无备忘录内容！")
        return
    
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        
        if not content.strip():
            print("暂无备忘录内容！")
        else:
            print("-" * 40)
            print(content)
            print("-" * 40)
    except Exception as e:
        print(f"❌ 读取失败：{e}")

def clear_memo():
    """清空备忘录"""
    if not os.path.exists(FILE_PATH):
        print("\n暂无备忘录内容，无需清空！")
        return
    
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            pass  # 写入空内容，实现清空
        print("✅ 备忘录已清空！")
    except Exception as e:
        print(f"❌ 清空失败：{e}")

def main():
    """主函数"""
    print("欢迎使用本地文本备忘录！")
    print(f"备忘录文件保存在：{os.path.abspath(FILE_PATH)}")
    
    while True:
        show_menu()
        try:
            choice = input("请输入您的选择（1-4）：").strip()
            if choice == '1':
                write_memo()
            elif choice == '2':
                read_memo()
            elif choice == '3':
                clear_memo()
            elif choice == '4':
                print("\n感谢使用，再见！")
                break
            else:
                print("输入无效，请输入 1-4 之间的数字！")
        except KeyboardInterrupt:
            print("\n\n程序已退出！")
            break
        except Exception as e:
            print(f"发生错误：{e}")

if __name__ == "__main__":
    main()
```

---

## 使用说明

1. **学生成绩管理工具**和**本地文本备忘录**：无需安装第三方库，直接复制代码运行即可。

2. **随机名言生成器**：需要先安装 `colorama` 库：
   ```bash
   pip install colorama
   ```

3. 每个程序都有清晰的菜单提示，按照提示输入数字选择功能即可。

4. 程序都加入了基础异常处理，避免常见的输入错误导致程序崩溃。

---

## 学习要点

这三个小程序覆盖了 Python 基础学习的核心知识点：
- 变量与数据类型（列表、字典、字符串）
- 函数定义与调用
- 条件判断与循环结构
- 文件读写操作
- 异常处理（try-except）
- 第三方库的使用
- 用户交互与菜单设计

适合 Python 初学者练习和理解基础语法！
