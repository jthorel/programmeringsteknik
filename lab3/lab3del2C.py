class FileProcessor(object):
	def __init__(self,fileName):

		try:
			self.file = open(fileName,"r") #öppnar filen med endast läsbehörighet
			self.processFile(self.file)
		except IOError:
			print(fileName + " finns ju inte.")



	def processFile(self,file): #Delegates the file read to the different functions that should process it.
		allNumbers= []

		index = 1 
		for line in file:
			line = line.rstrip('\n') #Is there a newline char? Get rid of it.

			if( self.printLineBool(line) ): #Should the line be printed?
				print("rad " + str(index) +": " + line)
				index +=1

			allNumbers.extend(self.returnNumbers(line)) #Does the row contain and numbers?

		medelVarde = self.medelvarde(allNumbers)
		medianValue = self.medianen(allNumbers)



		print("Medelvärdet är " + str(medelVarde))
		print("Medianen är " + str(medianValue))
		print("Största talet är " + str(max(allNumbers)))
		print("Minsta talet är " + str(min(allNumbers)))


	def returnNumbers(self,line): #Takes a string and returns a list with the numbers within the string.
		retList=[]
		lineArray = line.split()

		for key in lineArray:
			if(key.isdigit()):
				retList.append(int(key))
		return retList

	def printLineBool(self,line): #Returns True if the line holds character (not blankspace)
		retBool = False

		for n in line:
			try:
				kuken = float(n)
			except ValueError:
				if(n != " "):
					retBool = True

		return retBool

	def medianen(self,medianList): #Input a list and get back the median.
		medianList= sorted(medianList)
		length = len(medianList)
		half = length/2
		index = int(half)

		if length % 2 != 0:
			return medianList[index]
		else:
			leftValue = index - 1
			return (medianList[leftValue] + medianList[index]) / 2		
	def medelvarde(self,medelList): #Input a list and get back the medelvärde.
		total=0
		for n in medelList:
			total += n
		return total/len(medelList)

userInput = input("Vad heter filen?")
file = FileProcessor(userInput)