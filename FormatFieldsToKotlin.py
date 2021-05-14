import sys


def format_fields_to_kotlin(filePath, className):
    file = open(filePath)
    lines = file.readlines()
    toFile = open(filePath, 'w')

    expression = 'data class ' + className
    findExpressionInLines = False

    for line in lines:
        if expression in line:
            findExpressionInLines = True
            toFile.write(line)
        else:
            if findExpressionInLines:
                if line.find(')') == 0:
                    findExpressionInLines = False
                    toFile.write(line)
                else:
                    # 去掉所有的空格
                    line = line.replace(' ', '')
                    # 获取字段的注释内容
                    txt = line[line.find(":") + 1:len(line)].replace(',', '')
                    # 获取字段的数据类型
                    dataType = line[line.find('(') + 1:line.find(",")]
                    # 获取字段名
                    variableName = line[:line.find('(')]

                    dataTypeValue = 'var ' + variableName + ': ' + dataType + '? = null,'
                    if dataType == 'string':
                        dataTypeValue = 'var ' + variableName + ': String? = null,'
                    elif dataType == 'integer':
                        dataTypeValue = 'var ' + variableName + ': Int? = 0,'
                    elif dataType == 'boolean':
                        dataTypeValue = 'var ' + variableName + ': Boolean? = false,'
                    elif 'Array' in dataType:
                        dataType = dataType[dataType.find('[') +
                                            1:dataType.find(']')]
                        dataTypeValue = 'var ' + variableName + ': List<' + dataType + '>? = null,'

                    toFile.write('\t' + dataTypeValue + ' //' + txt)
            else:
                toFile.write(line)

    file.close()
    toFile.close()


if __name__ == '__main__':
    format_fields_to_kotlin(sys.argv[1], sys.argv[2])
