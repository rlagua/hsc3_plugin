import wexpect
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QTextEdit, QWidget
from PyQt5.QtCore import QThread, pyqtSignal


class ReadWorker(QThread):
    msg = pyqtSignal(str)

    def __init__(self, process):
        super().__init__()
        self.process = process
        self.output_buffer = ''

    def run(self):
        while True:
            try:
                # 读取子进程输出
                output = self.process.read_nonblocking(size=1024)
                if output:
                    self.output_buffer += output  # 将新输出添加到缓冲区

                    # 检查输出是否包含换行符
                    lines = self.output_buffer.splitlines(keepends=True)
                    for line in lines:  # 处理所有完整的行
                        self.msg.emit(line)  # 发送完整行
                    self.output_buffer = ''  # 保留未完整的行

            except Exception as e:
                print(f"Error: {e}")
                break


class InteractiveShellWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interactive CMD Shell")
        self.setGeometry(200, 200, 600, 400)

        # 创建主窗口部件和布局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()

        # 命令输入框
        self.command_input = QLineEdit()
        self.command_input.setPlaceholderText("Enter command here")

        # 输出显示框
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        layout.addWidget(self.output_display)
        layout.addWidget(self.command_input)

        # 将布局应用到主窗口
        main_widget.setLayout(layout)

        # 连接输入框的回车事件
        self.command_input.returnPressed.connect(self.send_command)

        # 启动交互式 CMD shell
        self.process = wexpect.spawn('cmd.exe /k', encoding='utf-8', timeout=None)

        # 启动线程读取输出
        self.worker = ReadWorker(self.process)
        self.worker.msg.connect(self.append_output)
        self.worker.start()

        # 历史命令列表
        self.command_history = []
        self.history_index = -1  # 当前历史命令索引
        self.set_styles()

    def set_styles(self):
        """设置黑底白字的样式"""
        self.output_display.setStyleSheet("QTextEdit { background-color: gray; color: white; }")
        # self.command_input.setStyleSheet("QLineEdit { background-color: black; color: white; }")

    def send_command(self):
        # 获取输入框的命令
        command = self.command_input.text()

        if command:
            # 将命令添加到历史记录
            self.command_history.append(command)
            self.history_index = len(self.command_history)  # 重置历史索引

            # 将命令写入到子进程中
            self.process.sendline(command)
            # 清空输入框
            self.command_input.clear()

    def append_output(self, output):
        # 将输出显示到文本框中
        self.output_display.append(output)

    def keyPressEvent(self, event):
        # 上箭头
        if event.key() == 16777235:  # QKeySequence.Up
            if self.history_index > 0:
                self.history_index -= 1
                self.command_input.setText(self.command_history[self.history_index])
        
        # 下箭头
        elif event.key() == 16777237:  # QKeySequence.Down
            if self.history_index < len(self.command_history) - 1:
                self.history_index += 1
                self.command_input.setText(self.command_history[self.history_index])
            elif self.history_index == len(self.command_history) - 1:
                self.history_index += 1
                self.command_input.clear()  # 清空输入框

        # 调用父类处理其他按键事件
        super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication([])
    window = InteractiveShellWindow()
    window.show()
    app.exec_()
