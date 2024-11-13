import matplotlib.pyplot as plt
import platform

class ChineseFontManager:
    @staticmethod
    def setup_chinese_font():
        """设置中文字体的简单方法"""
        if platform.system().lower() == 'windows':
            plt.rcParams['font.sans-serif'] = ['SimHei']
        elif platform.system().lower() == 'darwin':  # macOS
            plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
            # plt.rcParams['font.sans-serif'] = ['Songti SC']
            # plt.rcParams['font.sans-serif'] = ['Heiti TC']
            # plt.rcParams['font.sans-serif'] = ['Source Han Sans CN']
            # plt.rcParams['font.sans-serif'] = ['Source Han Serif CN']
            # plt.rcParams['font.sans-serif'] = ['Noto Serif CJK SC']
        else:  # Linux
            plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
        
        plt.rcParams['axes.unicode_minus'] = False

# 如果直接运行此文件，测试字体设置
if __name__ == "__main__":
    ChineseFontManager.setup_chinese_font()
    
    # 简单的测试图
    plt.figure(figsize=(8, 6))
    plt.plot([1, 2, 3], [4, 5, 6], 'ro-')
    plt.title('中文测试')
    plt.xlabel('横轴')
    plt.ylabel('纵轴')
    plt.show()