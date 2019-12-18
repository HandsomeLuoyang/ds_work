import json


class Node:
    def __init__(self, name="", id=0):
        self.name = name  # 节点名字
        self.id = id
        self.isVisited = False  # 是否被访问过


class Edge:
    def __init__(self, indexA=0, indexB=0, weight=0):
        self.nodeIndexA = indexA  # 边的起始节点的序号
        self.nodeIndexB = indexB  # 边的结束节点的序号
        self.weight = weight  # 边的权重


class pMap:
    def __init__(self, capacity):
        """初始化图类"""
        self.capacity = capacity  # 容量
        self.m_pNode = list()  # 节点列表
        self.m_pMatrix = list()  # 矩阵
        for i in range(self.capacity ** 2):  # 初始化邻接矩阵
            self.m_pMatrix.append(0)
        self.m_pEdge = list()  # 边列表
        self.m_iCursize = 0  # 当前大小

    def __setValueToMatrixForDirectedGraph(self, row, col, value):
        """为有向图设置邻接矩阵的权值"""
        self.m_pMatrix[row * self.capacity + col] = value
        self.m_pMatrix[col * self.capacity + row] = value

    def setLength(self, org, des, length):
        if not isinstance(org, str):
            print("请输入正确的起始地点!")
            return
        if not isinstance(des, str):
            print("请输入正确的结束地点!")
            return

        orgid = self.__getIdFromName(org)
        desid = self.__getIdFromName(des)
        if orgid == -1:
            print("您所输入的起始地点不存在！")
            return
        if desid == -1:
            print("您所输入的结束地点不存在！")
            return
        if not isinstance(length, int) and not isinstance(length, float):
            print("距离请输入数字！")
            return
        if length <= 0:
            print("距离必须是大于0的数字！")
            return

        self.__setValueToMatrixForDirectedGraph(orgid, desid, length)

    def printMoatrix(self):
        """打印邻接矩阵"""
        t = 0
        for i in self.m_pMatrix:
            print(i, end=" ")
            t += 1
            if t == self.capacity:
                print("\t")
                t = 0

    def addNode(self, name):
        """添加一个节点"""
        if not isinstance(name, str):
            print("请输入正确的城市名字！", name)
            return
        temp = Node(name, self.m_iCursize)  # 同时给这个节点的id赋值，用户使用名字查找，我们内部使用id进行操作
        self.m_pNode.append(temp)  # 直接添加一个节点进去
        self.m_iCursize += 1

    def resetNode(self):
        """重新设置所有结点为未访问过"""
        for node in self.m_pNode:
            node.isVisited = False

    def __getValueFromMatrix(self, row, col):
        """获得邻接矩阵中的值"""
        return self.m_pMatrix[row * self.capacity + col]

    def __getIdFromName(self, name):
        """通过用户给的名字找到这个结点的id，如果查找失败返回-1"""
        for node in self.m_pNode:
            if node.name == name:
                return node.id
        return -1

    def __getNameFromId(self, id):
        """通过id查找这个节点的名字"""
        for node in self.m_pNode:
            if node.id == id:
                return node.name
        return ""

    def depthFirstTraverse(self, id=0):
        """深度优先搜索"""
        print(self.m_pNode[id].name)  # 打印，代表访问
        self.m_pNode[id].isVisited = True  # 元素设置为已访问过

        for i in range(self.m_iCursize):
            value = self.__getValueFromMatrix(id, i)
            if value > 0:
                if self.m_pNode[i].isVisited == True:
                    continue
                else:
                    self.depthFirstTraverse(i)

    def __breadthFirstTraverseImpl(self, preNodes):
        curNodes = list()
        for i in preNodes:
            for j in range(self.m_iCursize):
                value = self.__getValueFromMatrix(i, j)
                if value > 0:
                    if self.m_pNode[j].isVisited:
                        continue
                    else:
                        print(self.m_pNode[j].name)
                        self.m_pNode[j].isVisited = True
                        curNodes.append(j)
                else:
                    continue

        if len(curNodes) == 0:
            return
        else:
            self.__breadthFirstTraverseImpl(curNodes)

    def breadthFirstTraverse(self, id=0):
        """广度优先搜索"""
        print(self.m_pNode[id].name)  # 打印
        self.m_pNode[id].isVisited = True  # 设置为已经访问过
        curNodes = list()
        curNodes.append(id)
        self.__breadthFirstTraverseImpl(curNodes)

    def dijkstra(self, org):
        """迪杰斯特拉算法"""
        orgid = self.__getIdFromName(org)
        if not isinstance(org, str):
            print("请输入正确的城市名！")
            return
        if orgid == -1:
            print("请输入正确的起始地点！")
            return
        ok = list()  # 已经计算好最短路径的节点
        ok.append(orgid)  # 初始点设置为已经记录好最短路径了
        no_ok = [i for i in range(self.m_iCursize) if i != orgid]  # 没有计算好最短路径的节点
        d = dict()  # d是存放计算过程中距离的字典
        ans = dict()  # ans是存放最终得出的距离的字典

        for j in range(self.m_iCursize):
            if j == orgid:  # 自己和自己就设置为0了，直接跳过
                continue
            value = self.__getValueFromMatrix(orgid, j)
            if value > 0:  # 如果相连的话，就把权重设置为对应的大小
                d[j] = value
            else:
                d[j] = 100000000000  # 否则设置一个非常大的值

        d = dict(
            sorted(d.items(), key=lambda item: item[1], reverse=True)
        )  # 用字典的value值进行排序，倒序排序
        temp = d.popitem()  # 拿到最小的那个值
        x, y = temp
        name = self.__getNameFromId(x)
        ans[name] = y
        while d and no_ok:  # 字典为空，代表所有节点都已经计算出最终长度，或者所有点都已经找到了最短路径
            ok.append(temp[0])  # 最小的那个直接加进去
            no_ok.remove(temp[0])  # 从标识没好的列表里面把这个点去掉
            for i in range(self.m_iCursize):  # 找i的邻点来更新d列表
                if i in ok:
                    continue
                value = self.__getValueFromMatrix(temp[0], i)
                if value > 0:  # 如果相连就比较一下是否需要更新
                    d[i] = min(d[i], temp[1] + value)  # 找小的来更新
                    value = 0
                else:
                    continue
            d = dict(
                sorted(d.items(), key=lambda item: item[1], reverse=True)
            )  # 每次都要排序，这里考虑用最小堆来优化
            temp = d.popitem()  # 继续找列表中最小的点，再次循环
            x, y = temp
            name = self.__getNameFromId(x)
            ans[name] = y
        return ans  # 返回这个字典，先看看


def get_length(org, des):
    with open("temp1.txt", "r") as f:
        one_line = f.readline()
        while one_line:
            ans = json.loads(one_line, encoding="gbk")
            # print(str(ans) + "\n")
            try:
                if ans[org][des]:
                    # return ans[org][des]
                    print(ans[org][des])
                    break
            except Exception:
                pass
            one_line = f.readline()


def main():
    p = pMap(6)
    p.addNode("重庆")
    p.addNode("湖南")
    p.addNode("江苏")
    p.addNode("河南")
    p.addNode("山西")
    p.addNode("北京")

    p.setLength("重庆", "湖南", 20)
    p.setLength("湖南", "江苏", 100.23)
    p.setLength("湖南", "河南", 30)
    p.setLength("重庆", "山西", 300.6)
    p.setLength("重庆", "江苏", 150)
    p.setLength("北京", "重庆", 250)
    p.setLength("北京", "河南", 25)

    p.printMoatrix()  # 打印邻接矩阵

    p.depthFirstTraverse()  # 深度优先搜索

    p.resetNode()  # 重新设置所有结点为未访问
    print("\n")

    p.breadthFirstTraverse()  # 广搜

    with open("temp1.txt", "w") as f:
        for i in p.m_pNode:
            ans = p.dijkstra(i.name)
            ans = {i.name: ans}
            # f.write(i.name + "：" + ans.__str__()+"\n")
            json.dump(ans, f)
            f.write("\n")

    # with open("temp1.txt", "r") as f:
    #     one_line = f.readline()
    #     while one_line:
    #         ans = json.loads(one_line, encoding="gbk")
    #         print(str(ans) + "\n")
    #         one_line = f.readline()
    get_length("山西", "重庆")


if __name__ == "__main__":
    main()
