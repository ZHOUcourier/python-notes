import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import platform
import os
from pathlib import Path

class FontChecker:
    def __init__(self):
        self.system = platform.system().lower()
        
    def get_system_font_paths(self):
        """获取系统字体目录"""
        if self.system == 'windows':
            return [os.path.join(os.environ['WINDIR'], 'Fonts')]
        elif self.system == 'darwin':  # macOS
            paths = [
                '/System/Library/Fonts',
                '/Library/Fonts',
                str(Path.home() / 'Library' / 'Fonts')
            ]
            return paths
        else:  # Linux
            paths = [
                '/usr/share/fonts',
                '/usr/local/share/fonts',
                str(Path.home() / '.fonts'),
                str(Path.home() / '.local' / 'share' / 'fonts')
            ]
            return paths

    def list_system_fonts(self):
        """列出系统所有字体文件"""
        print("\n=== 系统字体文件 ===")
        font_paths = self.get_system_font_paths()
        
        for base_path in font_paths:
            if os.path.exists(base_path):
                print(f"\n在 {base_path} 中找到的字体文件:")
                for root, dirs, files in os.walk(base_path):
                    for file in files:
                        if file.lower().endswith(('.ttf', '.ttc', '.otf')):
                            print(f"- {file}")

    def list_matplotlib_fonts(self):
        """列出Matplotlib可用的字体"""
        print("\n=== Matplotlib可用字体 ===")
        fonts = sorted(set([font.name for font in fm.fontManager.ttflist]))
        for font in fonts:
            print(f"- {font}")

    def check_chinese_fonts(self):
        """检查常用中文字体是否可用"""
        print("\n=== 常用中文字体检查 ===")
        
        chinese_fonts = {
            'windows': ['SimHei', 'Microsoft YaHei', 'KaiTi', 'SimSun', 'FangSong'],
            'darwin': ['PingFang SC', 'Heiti TC', 'Songti SC', 'Arial Unicode MS', 'STHeiti'],
            'linux': ['WenQuanYi Micro Hei', 'WenQuanYi Zen Hei', 'Droid Sans Fallback']
        }
        
        system_fonts = set([font.name for font in fm.fontManager.ttflist])
        target_fonts = chinese_fonts.get(self.system, [])
        
        print(f"\n当前系统: {platform.system()}")
        print("检查结果:")
        
        for font in target_fonts:
            status = "✓ 可用" if font in system_fonts else "✗ 不可用"
            print(f"- {font}: {status}")

    def test_chinese_display(self):
        """测试中文显示效果"""
        print("\n=== 中文显示测试 ===")
        
        # 获取当前可用的中文字体
        available_fonts = [
            font.name for font in fm.fontManager.ttflist
            if any(char in font.name for char in ['Sim', 'Hei', 'Ming', 'Song', 'Yuan', 'Kai', 'Ping', 'Microsoft'])
        ]
        
        if not available_fonts:
            print("未找到可用的中文字体！")
            return
            
        print("\n测试以下字体:")
        for font in available_fonts[:5]:  # 只测试前5个字体
            print(f"- {font}")
            
            plt.figure(figsize=(10, 2))
            plt.text(0.5, 0.5, f'测试中文显示 - {font}', 
                    fontdict={'family': font, 'size': 16},
                    ha='center', va='center')
            plt.axis('off')
            plt.show()

def main():
    checker = FontChecker()
    
    # 1. 列出系统字体
    checker.list_system_fonts()
    
    # 2. 列出Matplotlib字体
    checker.list_matplotlib_fonts()
    
    # 3. 检查中文字体
    checker.check_chinese_fonts()
    
    # 4. 测试中文显示
    checker.test_chinese_display()

if __name__ == "__main__":
    main()