`matplotlib.font_manager.fontManager.ttflist` 只会列出matplotlib能识别到的字体。`complete-font-checker.py`这个更全面的字体检测脚本，它可以：

1. 列出系统所有字体
2. 列出matplotlib可用字体
3. 检查常用中文字体是否可用

这个脚本提供了更全面的字体检查功能：

1. **系统字体检查**：
   - 检查系统字体目录中的所有字体文件
   - 支持 Windows、macOS 和 Linux 系统
   - 显示 .ttf、.ttc 和 .otf 字体文件

2. **Matplotlib 字体检查**：
   - 列出 Matplotlib 可识别的所有字体
   - 按字母顺序排序并去重

3. **中文字体检查**：
   - 检查常用中文字体是否可用
   - 根据不同操作系统检查对应的中文字体
   - 显示每个字体的可用状态

4. **中文显示测试**：
   - 使用可用的中文字体绘制测试文本
   - 直观显示不同字体的效果

使用方法：
```python
# 直接运行脚本
python fonts_list.py

# 或者在其他代码中使用
from fonts_list import FontChecker
checker = FontChecker()
checker.check_chinese_fonts()  # 检查中文字体
```

如果某些字体没有被检测到，可能的原因是：
1. 字体文件格式不受支持
2. 字体文件损坏或权限问题
3. 字体目录路径不在默认搜索路径中

解决方案：
1. 检查字体文件是否完整
2. 重新安装所需字体
3. 手动添加字体搜索路径：
```python
import matplotlib.font_manager as fm
fm.findSystemFonts(fontpaths=None, fontext='ttf')
```

这个脚本应该能更准确地检查和诊断字体问题。