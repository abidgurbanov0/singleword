
# importing required modules
import PyPDF2
  
def  uncommanwords (path1,path2):
    pdfFileObj = open(path1, 'rb')
    
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    page=pdfReader.getNumPages()
    pageObj = pdfReader.getPage(page-1)

    A =(pageObj.extractText())

    pdfFileObj1 = open(path2, 'rb')
    
    # creating a pdf reader object
    pdfReader1 = PyPDF2.PdfFileReader(pdfFileObj1)
    page1=pdfReader1.getNumPages()
    pageObj1 = pdfReader1.getPage(page1-1)

    B =(pageObj1.extractText()) 
    def UncommonWords(A, B):
    
        # count will contain all the word counts
        count = {}
        
        # insert words of string A to hash
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        
        # insert words of string B to hash
        for word in B.split():
            count[word] = count.get(word, 0) + 1
    
        # return required list of words
        return [word for word in count if count[word] == 1]
    

    
    # Print required answer
    return (UncommonWords(A, B))