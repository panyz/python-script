import sys


def format_fields_to_java(filePath, className):
    file = open(filePath)
    lines = file.readlines()
    toFile = open(filePath, 'w')

    expression = 'public class ' + className
    findExpressionInLines = False

    for line in lines:
        if expression in line:
            findExpressionInLines = True
            toFile.write(line)
        else:
            if findExpressionInLines:
                if line.find('}') == 0:
                    findExpressionInLines = False
                    toFile.write('\n'+line)
                else:
                    # 去掉所有的空格
                    line = line.replace(' ', '')
                    # 获取字段的注释内容
                    txt = line[line.find(":") + 1:len(line)].replace(',', '')
                    # 获取字段的数据类型
                    dataType = line[line.find('(') + 1:line.find(",")]
                    # 获取字段名
                    variableName = line[:line.find('(')]

                    dataTypeValue = 'private ' + dataType + ' ' + variableName + ';'
                    if dataType == 'string':
                        dataTypeValue = 'private String ' + variableName + ';'
                    elif dataType == 'integer':
                        dataTypeValue = 'private int ' + variableName + ';'
                    elif dataType == 'boolean':
                        dataTypeValue = 'private boolean ' + variableName + ';'
                    elif 'Array' in dataType:
                        dataType = dataType[dataType.find('[') +
                                            1:dataType.find(']')]
                        dataTypeValue = 'private List<' + dataType + '> ' + variableName + ';'

                    toFile.write('\n\t//' + txt )
                    toFile.write('\t' + dataTypeValue)
            else:
                toFile.write(line)

    file.close()
    toFile.close()


if __name__ == '__main__':
    format_fields_to_java(sys.argv[1], sys.argv[2])
