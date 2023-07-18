这个文件夹里只有MarchingCubeLandscape是有用的
在maya插件管理器里加载这个脚本就可以召唤我们的插件
加载插件后会在 工具架-自定义 出现一个M图标，那个是我们的按钮，按下去会启用 mcl_plugin包里的GUI_setup.mainGUI()，这个函数会激活我们的GUI。
但是我还没有实现按钮的删除。所以每次启动要手动删掉旧的按钮再加载。

所有功能文件请统一放在mcl_plugin里面。其它地方的文件是无效的（比如同级这几个mouse啥的）。

7.18 - 重构了整个代码框架。现在这样应该是可以的
MarchingCubeLandscape.py - 插件加载入口
mcl_plugin - 具体功能
- GUI_setup - 用来整合屠涵的那些GUI
- manager - 中控，用于控制整个插件运行
- tool_context - 画笔相关功能，用于整合徐辉男的画笔