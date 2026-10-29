B序列显式下降式的补充核验
主稿无编号备注及式eq:B-descent给出所有R>=3的纸面证明。
运行 python verification/b_descent/verify_b_descent.py。
只用Python标准库；从相邻rational_transform文件夹读取八个历史下降值。
结果范围R=3,...,10，正向齐次Horner、逆向三角消元、历史值、反序与望远镜恒等式均通过；不分解或搜索不可约多项式。
脚本和历史输入哈希在b_descent_audit.json。它们是有限辅助检查，不替代全参数证明，不证明剩余参数不可约或优先权。
