#copyright 2019 Bowen Qin

#export GOOGLE_APPLICATION_CREDENTIALS="MyFirstProject.json" 

import sys, extract_tweet, sentiment_text_analysis
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QInputDialog, 
    QTextEdit, QGridLayout, QApplication)

class cosmatter(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
        
	def initUI(self):
		self.setWindowIcon(QIcon('COSMATTER.png'))  
		self.setGeometry(300, 300, 600, 300)
		self.setWindowTitle('COSMATTER')    
		self.show()

		maxNum = self.getNum()
		hashtag = self.getHashtag()

		i = QLabel()
		i.setPixmap(QPixmap("COSMATTER.png"))

		j = QLabel("Extracted " + str(maxNum) + " tweets with hashtag #" + hashtag + "...")
		extract_tweet.getHashtagTweets(maxNum, hashtag)
		k = QLabel("Analysing sentiment...")
		score, mag = sentiment_text_analysis.analyze_sentiment_from_twitter("tweets#" + hashtag + ".txt")
		l = QLabel('---------------------------------------------------------------------------------------------------')
		x = QLabel('Score of the sentiment ranges between -1.0 (negative) and 1.0 (positive).')
		xx = QLabel('Score:'+ score)
		m = QLabel('---------------------------------------------------------------------------------------------------')
		y = QLabel('Magnitude indicates the overall strength of emotion (both positive and negative). Larger, stronger.')
		yy = QLabel('Magnitude:' + mag)

		self.setWindowIcon(QIcon('COSMATTER.png'))     
		grid = QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(i, 1, 0)
		grid.addWidget(j, 2, 0)
		grid.addWidget(k, 3, 0)
		grid.addWidget(l, 4, 0)
		grid.addWidget(x, 5, 0)
		grid.addWidget(xx, 6, 0)
		grid.addWidget(m, 7, 0)
		grid.addWidget(y, 8, 0)
		grid.addWidget(yy, 9, 0)
		self.setLayout(grid) 

	def getNum(self):
		num, okPressed = QInputDialog.getInt(self, "Get Num", "Number of tweets you want to extract:")
		if okPressed:
			return num
	def getHashtag(self):
		hashtag, okPressed = QInputDialog.getText(self, "Get Hashtag", "Hashtag you want to scrape: ")
		if okPressed:
			return hashtag
        
        

if __name__ == "__main__":

	app = QApplication(sys.argv)
	ex = cosmatter()
	sys.exit(app.exec_())

