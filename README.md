# python-note-tool
python练习项目，简易记事本小程序
from fileinput import filename
from test.test_pydoc.pydocfodder import count
from turtledemo.chaos import line


def read_text(filename):
    try:#try的作用是尝试跑代码，防止一个步骤错误而导致整个程序崩溃
        with open(filename, 'r', encoding='utf-8') as f:#r是指规定只读模式，不能修改或写入  encodeing=utf-8是指用utf-8编码读取，防止乱码
            #`with`（上下文管理器，重点）
            #作用：缩进块里的代码执行完之后，**自动关闭文件**，不用手动写`f.close()`
            #好处：避免忘记关闭文件，占用电脑资源
            content = f.read()#`.read()`：文件对象的方法，**一次性读取文件里面全部文字**，返回字符串 content可以把读到的全部文本存入变量content
        return content#return带表达式或变量可以把计算结果交给外面的代码，方便后续使用
    #单写return的话会直接终止函数，返回none，代表没有结果
    except FileNotFoundError:#except可以捕获文件找不到的错误
        return f"【提示】文件{filename}不存在"#给出文件不存在提示
def save_text(filename,text):
    try:
        with open(filename, 'w', encoding='utf-8') as f:#w指写入
            f.write(text)
        print(f"文件已经保存到{filename}")
    except Exception as e:    #Exception目的为捕获绝大多数普通运行错误 FileNotFoundError更精准
        print(f"保存失败，错误：{e}")
def search_keyword(keyword):
    print(f"/n-----搜索关键词{keyword}-----")#/n表示换行
    try:
        count = 0
        with open(keyword, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, start=1):# enumerate拿到行号，从1开始计数
                if keyword.lower() in line.lower():#lower可以将字母统一转换成小写防止出现误判
                    print(f"第{line_num}行:{line.strip()}")
                    count += 1
                if count == 0:
                    print("没有找到匹配内容")
                else:
                    print(f"一共找到{count}处匹配/n")
    except FileNotFoundError:
        print("文件不存在，无法搜索")
def main():
    file_name="note.txt"
    while True:
        print("====简易记事本菜单====")
        print("1 读取文件")
        print("2 写入保存文本")
        print("3 关键词检索")
        print("0 退出程序")
        op = input("请输入功能数字：")
        if op == "1":
            res = read_text(file_name)
            print("\n文件内容：")
            print(res)
            print("-" * 30)

        elif op == "2":
            print("请输入要保存的全部内容（输入#end结束输入）：")
            lines = []
            while True:
                line = input()
                if line == "#end":
                    break
                lines.append(line)
            all_text = "\n".join(lines)
            save_text(file_name, all_text)
        elif op == "3":
            key = input("输入要搜索的关键词：")
            search_keyword(file_name, key)

        elif op == "0":
            print("程序结束")
            break
        else:
            print("输入无效，请重新选择！\n")

        if __name__ == "__main__":
            main()
