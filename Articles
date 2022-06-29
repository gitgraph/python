import math


# *
# * Program - Artiklar

# * @author David Anderberg
class Articles :
    userInput =  "Python-inputs"
    @staticmethod
    def main( args) :
        # TODO Auto-generated method stub
        # Variabeldeklaration
        ARTICLE_NR = 1000
        articles = [[0] * (3) for _ in range(10)]
        dateSales = [None] * (10)
        sales = [[0] * (3) for _ in range(10)]
        noOfArticles = 0
        articleNumber = ARTICLE_NR
        totalNumber = 0
        run = True
        # Iteration
        while (run) :
            # Utskrift
            number = Articles.menu()
            # Selektion
            if (number==0):
                print("Skriv in ett nummer 1-6 ")
            elif(number==1):
                print("Antal artiklar: ", end ="")
                noOfArticles = Articles.input()
                # Ber?kning
                if (noOfArticles > 0) :
                    totalNumber += noOfArticles
                    articles = Articles.checkFull(articles, totalNumber)
                    articles = Articles.insertArticles(articles, articleNumber, noOfArticles)
                    articleNumber = ARTICLE_NR + totalNumber
                if (noOfArticles == 0) :
                    print("Skriv in ett nummer")
            elif(number==2):
                Articles.removeArticel(articles)
            elif(number==3):
                # Utskrift
                Articles.printArticles(articles)
            elif(number==4):
                Articles.sellArticle(sales, dateSales, articles)
            elif(number==5):
                # Utskrift
                Articles.printSales(sales, dateSales)
            elif(number==6):
                run = False
                print("Avslutar program ")
                Articles.userInput.close()
    # *
    #    * Metoden skriver ut en lista och l?ser av indata
    #    * 
    #    * @return
    @staticmethod
    def  menu() :
        print("\n1. L?gg in artiklar\n2. Ta bort artikel\n3. Visa artiklar\n4. F?rs?ljning\n5. Orderhistorik\n6. Avsluta")
        print("Ditt val: ", end ="")
        number = Articles.input()
        return number
    # *
    #    * Metoden l?ser av indata och kontrollerar v?rdet
    #    * 
    #    * @return
    @staticmethod
    def  input() :
        number = 0
        if (Articles.userInput.hasNextInt()) :
            number = input()
        elif(not Articles.userInput.hasNextInt()) :
            input()
            number = 0
        return number
    # *
    #    * Metoden skriver in v?rden in en array
    #    * 
    #    * @param articles
    #    * @param articleNumber
    #    * @param noOfArticles
    #    * @return
    @staticmethod
    def  insertArticles( articles,  articleNumber,  noOfArticles) :
        PIECE_MAX = 10
        PIECE_MIN = 1
        PRICE_MAX = 1000
        PRICE_MIN = 100
        articleCount = 0
        i = 0
        while (i < len(articles)) :
            if (articles[i][0] == 0) :
                if (articleCount < noOfArticles) :
                    articles[i][0] = articleNumber
                    articles[i][1] = int((random() * ((PIECE_MAX - PIECE_MIN) + 1))) + PIECE_MIN
                    # piece
                    articles[i][2] = int((random() * ((PRICE_MAX - PRICE_MIN) + 1))) + PRICE_MIN
                    # price
                    articleNumber += 1
                    articleCount += 1
            i += 1
        return articles
    # *
    #    * Metoden kontrollerar storleken av arrayen och kopierar v?rdena i en ny
    #    * array
    #    * 
    #    * @param articles
    #    * @param noOfArticles
    #    * @return
    @staticmethod
    def  checkFull( articles,  noOfArticles) :
        articlesArray = None
        if (noOfArticles > len(articles)) :
            articlesExtend = [[0] * (3) for _ in range(noOfArticles)]
            System.arraycopy(articles,0,articlesExtend,0,len(articles))
            articlesArray = articlesExtend
        else :
            articlesArray = articles
        return articlesArray
    # *
    #    * Metoden skriver ut och l?ser av indata, och kontrollerar v?rdet f?r att
    #    * skriva om v?rdena i arrayen
    #    * 
    #    * @param articles
    @staticmethod
    def removeArticel( articles) :
        ERROR_CODE = int(140000.0)
        print("Ta bort artikel, skriv in artikelnr: ", end ="")
        articleNumber = Articles.input()
        if (articleNumber == 0) :
            print("Skriv in artikelnr ")
        else :
            number = ERROR_CODE
            index = 0
            while (index < len(articles)) :
                if (articleNumber == articles[index][0]) :
                    number = index
                    articles[number][0] = 0
                    articles[number][1] = 0
                    articles[number][2] = 0
                index += 1
            if (number == ERROR_CODE) :
                print("Artikelnr ?r inte registrerat")
    # *
    #    * Metoden sorterar v?rdena i arrayen och skriver ut arrayen i en lista
    #    * 
    #    * @param articles
    @staticmethod
    def printArticles( articles) :
        sorted = False
        replace = [0] * (3)
        while True :
            sorted = True
            i = 0
            while (i < len(articles) - 1) :
                if (articles[i][0] > articles[i + 1][0]) :
                    replace = articles[i]
                    articles[i] = articles[i + 1]
                    articles[i + 1] = replace
                    sorted = False
                i += 1
            if((not sorted) == False) :
                    break
        print("--- Artiklar ---")
        print("Artikelnr. \t Antal \t Pris")
        i = 0
        while (i < len(articles)) :
            if (articles[i][0] != 0) :
                print("%d \t\t %d \t %d \n" % (articles[i][0],articles[i][1],articles[i][2]),end ="",sep ="")
            i += 1
    # *
    #    * Metoden skriver ut och l?ser av indata och kontrollerar om värdet ?r
    #    * registrerat, och skriver ut och l?ser av indata och skriver in värden i
    #    * sales array
    #    * 
    #    * @param sales
    #    * @param salesDate
    #    * @param articles
    @staticmethod
    def sellArticle( sales,  salesDate,  articles) :
        ERROR_CODE = int(140000.0)
        print("Sälj artikel ")
        print("Artikelnr: ", end ="")
        articleNumber = Articles.input()
        if (articleNumber != 0) :
            number = ERROR_CODE
            index = 0
            while (index < len(articles)) :
                if (articleNumber == articles[index][0]) :
                    number = index
                    print("Antal varor: ", end ="")
                    goodsNumber = Articles.input()
                    if (goodsNumber == 0) :
                        print("Skriv in ett nummer")
                    elif(goodsNumber <= articles[number][1] and goodsNumber > 0) :
                        articles[number][1] -= goodsNumber
                        count = 0
                        c = 0
                        while (c < len(sales)) :
                            if (sales[c][0] != 0) :
                                count += 1
                            c += 1
                        sales[count][0] = articles[number][0]
                        sales[count][1] = goodsNumber
                        sales[count][2] = articles[number][2] * goodsNumber
                        salesDate[count] =  java.util.Date()
                    else :
                        print("Artikelnr. %d har antal artiklar: %d \n" % (articles[number][0],articles[number][1]),end ="",sep ="")
                index += 1
            if (number == ERROR_CODE) :
                print("Artikelnr ?r inte registrerat")
        else :
            print("Skriv in ett nummer")
    # *
    #    * Metoden skriver ut en lista f?r v?rdena i sales och salesDate
    #    * 
    #    * @param sales
    #    * @param salesDate
    @staticmethod
    def printSales( sales,  salesDate) :
        print("--- Orderhistorik ---")
        print("Artikelnr. \t Antal \t Summa \t Datum")
        i = 0
        while (i < len(sales)) :
            if (sales[i][0] != 0) :
                print("%d \t\t %d \t %d \t %s \n" % (sales[i][0],sales[i][1],sales[i][2],salesDate[i].toString()),end ="",sep ="")
            i += 1
    

if __name__=="__main__":
    Articles.main([])
