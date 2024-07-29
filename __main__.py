import module.properties as pp
import module.reader as rd
import module.queryParser as qp
if __name__ == '__main__':
    result = []
    attr = pp.getAttributes()
    directory = attr.get('filePath')
    #print(directory)
    fileList = rd.readAllFileDirectory(directory)
    for file in fileList:
        parseList = qp.parseFiles(file)
        filteredList = qp.queryFilter(parseList)
        result.append(filteredList)

    result = qp.clearEmptyList(result)
    for list in result:
        for var in list:
            print(var)



