from cmu_graphics import *
def getData():
    xData = [ ]
    stateLabels = [ ]
    for state in app.data:
        xData.append(app.data[state])
        stateLabels.append(state)

    return xData, stateLabels

def main():
    xData, stateLabels = getData()

    manager.plotHorizontalBars(xData, color='steelBlue')
    manager.updateRanges(xMin=0)
    manager.drawTicks(yLabels=stateLabels, offsetY=True)

class PlotManager(object):
    def __init__(self, left=85, bottom=345, width=300, height=300, title='', xLabel='', yLabel=''):
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height
        self.title = title

        self.xRange = [ 0, 0 ]
        self.yRange = [ 0, 0 ]

        self.plots = [ ]

        self.tickDrawings = Group()
        self.drawing = Group(self.tickDrawings)
        self.drawAxes(xLabel, yLabel)

    def drawAxes(self, xLabel, yLabel):
        l, b, w, h = self.left, self.bottom, self.width, self.height
        self.drawing.add(
            Line(l, b - h, l, b + 5, fill='silver', lineWidth=3),
            Line(l - 5, b, l + w, b, fill='silver', lineWidth=3),
            Label(self.title, l + (w / 2), b - h - 10, size=14),
            Label(xLabel, l + w / 2, b + 30),
            Label(yLabel, l - 40, b - h / 2, rotateAngle=-90)
            )

    def getKDecimalPlaces(self, num, k):
        num = ((num * (10 ** k)) // 1) / (10 ** k)
        if (k <= 0):
            return int(num)
        else:
            return num

    def drawTicks(self, xPositions=None, xLabels=None, yPositions=None, yLabels=None, precision=[1,1], offsetX=False, offsetY=False):
        xPosDefaults, xLabDefaults, yPosDefaults, yLabDefaults = [], [], [], []
        xLen = 11 if xLabels == None else len(xLabels)
        yLen = 11 if yLabels == None else len(yLabels)
        xOffset = 0 if offsetX == False else 0.5
        yOffset = 0 if offsetY == False else 0.5

        for i in range(xLen):
            xVal = self.xRange[0] + (i + xOffset) * (self.xRange[1] - self.xRange[0]) / (xLen - 2 * (0.5 - xOffset))
            xPos, yPos = self.getPositionFromData(xVal, 0)
            xPosDefaults.append(xPos)
            xLabDefaults.append(xVal)

        for i in range(yLen-1, -1, -1):
            yVal = self.yRange[0] + (i + yOffset) * (self.yRange[1] - self.yRange[0]) / (yLen - 2 * (0.5 - yOffset))
            xPos, yPos = self.getPositionFromData(0, yVal)
            yPosDefaults.append(yPos)
            yLabDefaults.append(yVal)

        if (xPositions == None):
            xPositions = xPosDefaults
        if (xLabels == None):
            xLabels = xLabDefaults
        if (yPositions == None):
            yPositions = yPosDefaults
        if (yLabels == None):
            yLabels = yLabDefaults

        l, b = self.left, self.bottom
        self.tickDrawings.clear()

        for ind in range(len(xPositions)):
            xPos = xPositions[ind]
            xLab = xLabels[ind]
            if (isinstance(xLab, int) or isinstance(xLab, float)):
                xLab = self.getKDecimalPlaces(xLab, precision[0])
            self.tickDrawings.add(
                Line(xPos, b - 3, xPos, b + 3, fill='silver'),
                Label(xLab, xPos, b + 5, rotateAngle=-20, align='top'),
                )

        for ind in range(len(yPositions)):
            yPos = yPositions[ind]
            yLab = yLabels[ind]
            if (isinstance(yLab, int) or isinstance(yLab, float)):
                yLab = self.getKDecimalPlaces(yLab, precision[1])
            self.tickDrawings.add(
                Line(l - 3, yPos, l + 3, yPos, fill='silver'),
                Label(yLab, l - 7, yPos, align='right'),
                )

    def getPositionFromData(self, dataXVal, dataYVal):
        xMin, xMax = self.xRange[0], self.xRange[1]
        yMin, yMax = self.yRange[0], self.yRange[1]

        xPos = self.left + ((dataXVal - xMin) * self.width) / (xMax - xMin)
        yPos = self.bottom - ((dataYVal - yMin) * self.height) / (yMax - yMin)
        return xPos, yPos

    def getDataFromPosition(self, xPos, yPos):
        xMin, xMax = self.xRange[0], self.xRange[1]
        yMin, yMax = self.yRange[0], self.yRange[1]

        dataXVal = ((xPos - self.left) * (xMax - xMin)) / self.width + xMin
        dataYVal = ((self.bottom - yPos) * (yMax - yMin)) / self.height + yMin
        return dataXVal, dataYVal

    def updateRanges(self, xMin=None, xMax=None, yMin=None, yMax=None):
        if (xMin != None):
            self.xRange[0] = xMin
        if (xMax != None):
            self.xRange[1] = xMax
        if (yMin != None):
            self.yRange[0] = yMin
        if (yMax != None):
            self.yRange[1] = yMax

        for plot in self.plots:
            plot.updateDrawing()
        self.drawTicks()

    def removePlot(self, plot):
        if (plot not in self.plots):
            print('Plot does not exist')
            return
        self.plots.remove(plot)
        plot.drawing.visible = False

    def createPlot(self, xData, yData, plotType, color, resizeToNewPlot):
        if (len(xData) != len(yData)):
            print('Data lists were not the same length. Cannot plot!')
            return
        if ((isinstance(color, list) == True) and (len(color) != len(xData))):
            print('Color list and data were not the same length. Using default color!')
            color = 'black'

        newPlot = Plot(self, plotType, xData, yData)

        if (resizeToNewPlot == True):
            self.updateRanges(xMin=newPlot.xRange[0], xMax=newPlot.xRange[1],
                            yMin=newPlot.yRange[0], yMax=newPlot.yRange[1])

        newPlot.draw(color=color)
        self.plots.append(newPlot)
        self.drawing.toFront()
        return newPlot

    def plotPoints(self, xData, yData, color='black', resizeToNewPlot=True):
        return self.createPlot(xData, yData, 'scatter', color, resizeToNewPlot)

    def plotLines(self, xData, yData, color='black', resizeToNewPlot=True):
        return self.createPlot(xData, yData, 'line', color, resizeToNewPlot)

    def plotHorizontalBars(self, xData, yPositions=None, color='black', resizeToNewPlot=True):
        if (yPositions == None):
            yPositions = [ ]
            numBars = len(xData)
            top = self.bottom - self.height
            for i in range(numBars):
                yPositions.append(top + (i + 0.5) * (self.height / numBars))

        return self.createPlot(xData, yPositions, 'horiz bar', color, resizeToNewPlot)

    def plotVerticalBars(self, yData, xPositions=None, color='black', resizeToNewPlot=True):
        if (xPositions == None):
            xPositions = [ ]
            numBars = len(yData)
            for i in range(numBars):
                xPositions.append(self.left + (i + 0.5) * (self.width / numBars))

        return self.createPlot(xPositions, yData, 'vert bar', color, resizeToNewPlot)

class Plot(object):
    def __init__(self, manager, plotType, xData, yData):
        self.manager = manager
        self.plotType = plotType

        self.xData = xData
        self.yData = yData

        self.getDataRanges()
        self.drawing = Group()

    def getDataRanges(self):
        # Used in Graph.updateRanges()
        self.xRange = [ 10 ** 10, -10 ** 10 ]
        self.yRange = [ 10 ** 10, -10 ** 10 ]

        for xVal in self.xData:
            if (xVal < self.xRange[0]):
                self.xRange[0] = xVal
            if (xVal > self.xRange[1]):
                self.xRange[1] = xVal
        for yVal in self.yData:
            if (yVal < self.yRange[0]):
                self.yRange[0] = yVal
            if (yVal > self.yRange[1]):
                self.yRange[1] = yVal

        if (self.xData == [ ]):
            self.xRange = [ 0, 1 ]
        if (self.yData == [ ]):
            self.yRange = [ 0, 1 ]

    def getDatapointColor(self, index):
        if (isinstance(self.color, list) == True):
            if (index < len(self.color)):
                color = self.color[index]
            else:
                color = 'black'
        else:
            color = self.color
        return color

    def updateColor(self, newColor):
        self.color = newColor
        for ind in range(len(self.drawing.children)):
            shape = self.drawing.children[ind]
            shape.fill = self.getDatapointColor(ind)

    def updateData(self, newXData=None, newYData=None, resizeRanges=False):
        if (newXData != None):
            self.xData = newXData
        elif (self.plotType == 'vert bar'):
            newXData = [ ]
            numBars = len(newYData)
            for i in range(numBars):
                newXData.append(self.manager.left + (i + 0.5) * (self.manager.width / numBars))
            self.xData = newXData
        if (newYData != None):
            self.yData = newYData
        elif (self.plotType == 'horiz bar'):
            newYData = [ ]
            numBars = len(newXData)
            top = self.manager.bottom - self.manager.height
            for i in range(numBars):
                newYData.append(top + (i + 0.5) * (self.manager.height / numBars))
            self.yData = newYData
        if (len(newXData) != len(newYData)):
            print('Data lists were not the same length. Cannot plot!')
            return
        if (len(newXData) == 0):
            return

        self.getDataRanges()
        if (resizeRanges == True):
            self.manager.updateRanges(xMin=self.xRange[0], xMax=self.xRange[1],
                                    yMin=self.yRange[0], yMax=self.yRange[1])

        prevXVal, prevYVal = newXData[0], newYData[0]
        for ind in range(len(newXData)):
            xVal, yVal = newXData[ind], newYData[ind]
            if (ind < len(self.drawing.children)):
                shape = self.drawing.children[ind]
                if (self.plotType == 'scatter'):
                    shape.datapoint = [ xVal, yVal ]
                elif (self.plotType =='line'):
                    shape.datapoint = [ [ prevXVal, prevYVal ], [ xVal, yVal ] ]
                elif (self.plotType == 'horiz bar'):
                    shape.datapoint = [ xVal, yVal ]
                elif (self.plotType == 'vert bar'):
                    shape.datapoint = [ xVal, yVal ]
                self.updateDatapointShape(shape)
            else:
                color = self.getDatapointColor(ind)
                self.drawDatapoint(xVal, yVal, prevXVal, prevYVal, color)

            prevXVal, prevYVal = xVal, yVal

        if (len(newXData) < len(self.drawing.children)):
            for i in range(ind, len(self.drawing.children)):
                shape = self.drawing.children[i]
                self.drawing.remove(shape)

    def updateDatapointShape(self, shape):
        if (self.plotType == 'scatter'):
            xVal, yVal = shape.datapoint
            newXPos, newYPos = self.manager.getPositionFromData(xVal, yVal)
            shape.centerX, shape.centerY = newXPos, newYPos
        elif (self.plotType =='line'):
            pt1, pt2 = shape.datapoint
            shape.x1, shape.y1 = self.manager.getPositionFromData(pt1[0], pt1[1])
            shape.x2, shape.y2 = self.manager.getPositionFromData(pt2[0], pt2[1])
        elif (self.plotType == 'horiz bar'):
            xVal, yVal = shape.datapoint
            shape.x2, y = self.manager.getPositionFromData(xVal, yVal)
            shape.centerY = yVal
        elif (self.plotType == 'vert bar'):
            xVal, yVal = shape.datapoint
            x, shape.y2 = self.manager.getPositionFromData(0, yVal)
            shape.centerX = xVal

    def updateDrawing(self):
        for shape in self.drawing:
            self.updateDatapointShape(shape)

    def drawDatapoint(self, xVal, yVal, prevXVal, prevYVal, color):
        graphX, graphY = self.manager.getPositionFromData(xVal, yVal)
        if (self.plotType == 'scatter'):
            shape = Circle(graphX, graphY, 5, fill=color, opacity=40)
            shape.datapoint = [ xVal, yVal ]
        elif (self.plotType == 'line'):
            prevGraphX, prevGraphY = self.manager.getPositionFromData(prevXVal, prevYVal)
            shape = Line(prevGraphX, prevGraphY, graphX, graphY, fill=color)
            shape.datapoint = [ [ prevXVal, prevYVal ], [ xVal, yVal ] ]
            prevXVal = xVal
            prevYVal = yVal
        elif (self.plotType == 'horiz bar'):
            height = self.manager.height / (len(self.xData) * 1.5)
            shape = Line(self.manager.left, yVal, graphX, yVal, fill=color, lineWidth=height)
            shape.datapoint = [ xVal, yVal ]
        elif (self.plotType == 'vert bar'):
            width = self.manager.width / (len(self.yData) + 1)
            shape = Line(xVal, self.manager.bottom, xVal, graphY, fill=color, lineWidth=width)
            shape.datapoint = [ xVal, yVal ]
        else:
            print('Invalid plot type!')

        self.drawing.add(shape)
        return prevXVal, prevYVal

    def draw(self, color):
        self.color = color
        if (len(self.xData) == 0):
            return

        prevXVal = self.xData[0]
        prevYVal = self.yData[0]
        for index in range(len(self.xData)):
            xVal = self.xData[index]
            yVal = self.yData[index]
            color = self.getDatapointColor(index)
            prevXVal, prevYVal = self.drawDatapoint(xVal, yVal, prevXVal, prevYVal, color)

manager = PlotManager(left=35, bottom=375, width=350, height=340,
                    title='% total jobs in comp/eng/sci (by East Coast US state)')

app.data = {
    'CT': 6.7,
    'DE': 6.0,
    'DC': 11.8,
    'FL': 4.5,
    'GA': 5.5,
    'KY': 4.3,
    'ME': 5.0,
    'MD': 9.3,
    'MA': 8.8,
    'NH': 7.8,
    'NJ': 7.1,
    'NY': 5.1,
    'NC': 5.8,
    'ND': 3.3,
    'PA': 5.7,
    'RI': 5.6,
    'SC': 4.9,
    'TN': 4.6,
    'VT': 5.7,
    'VA': 8.8,
    'WV': 4.3,
}
main()

cmu_graphics.run()