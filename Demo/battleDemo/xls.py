from param import Param
import xlrd
class XLS(Param):
    """
    xls基本格式(如果要把xls中存储的数字按照文本读出来的话,纯数字前要加上英文单引号: 
    第一行是参数的注释,就是每一行参数是什么 
    第二行是参数名,参数名和对应模块的po页面的变量名一致 
    第3~N行是参数 最后一列是预期默认头Exp 
    """

    def __init__(self, paramConf):
        '''
        :param paramConf: xls 文件位置(绝对路径)
        '''
        self.paramConf = paramConf
        self.paramFile = self.paramConf['file']
        self.data = xlrd.open_workbook(self.paramFile)
        self.paramSheet = self.paramConf['Sheet']

    def getParamSheet(self,nsheets):
        ''' 
        设定参数所处的sheet 
        :param nsheets: 参数在第几个sheet中 :
        return: 
        '''
        self.paramSheet = self.data.sheets()[nsheets]

    def getOneLine(self,nRow):
        ''' 
        返回一行数据
        : param nRow: 行数 
        :return: 一行数据 [] 
        '''
        return self.paramSheet.row_value(nRow)

    def getOneCol(self,nCol):
        ''' 
        返回一列数据
        : param nCol: 行数 
        :return: 一列数据 [] 
        '''
        return self.paramSheet.cow_value(nCol)

    