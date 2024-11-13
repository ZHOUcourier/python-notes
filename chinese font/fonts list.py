import matplotlib.font_manager
import platform

fonts = [font.name for font in matplotlib.font_manager.fontManager.ttflist]
print("Available fonts:")
for font in sorted(set(fonts)):
    print(f"- {font}")

print(platform.system())