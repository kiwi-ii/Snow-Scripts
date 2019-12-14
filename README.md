# Snow-Scripts

> scripts for snow

## 01 提取CSV某一列, 合并为新的CSV文件

### v1.1.20191115

> Python3

1. 通过命令行输入参数
2. 得到输出文件为`.csv`文件

### v1.2.20191213

> Python2
>
> 只修改了文件首行声明，测试可以正常输出

命令行执行格式为：`python scriptFileName csvFileFolder desFileName`

例如：

```python
python merCSV.py ./csvFiles/ snow.csv
```

### v2.0.20191214

1. 将代码重构为函数，利用`if __name__ == '__main__':`执行判断
2. 添加第一列为时间序列
3. 将起始时间统一为`2013-01-01`

命令行执行方式参考v1.2
