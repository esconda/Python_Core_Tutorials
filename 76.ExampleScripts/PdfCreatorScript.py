import os
import xml.etree.ElementTree as et
from fpdf import FPDF 

def initGlobalVars():
    global srcXmlPath
    global dstXmlPath
    global certificationReport
    global detailedTestReport
    global crtfRepAproval
    global detRepAproval
    
    srcXmlPath = "Empty"
    dstXmlPath = "Empty"
    certificationReport = "CertificationReport.pdf"
    detailedTestReport = "DetailedTestReport.pdf"
    crtfRepAproval = 0
    detRepAproval = 0

def initGlobPdfVars():
    #AutomatedRtTester
    global versionList
    global etsFirmVerList
    global projectNameList
    
    #Dut
    global vendorIdList
    global deviceIdList
    global macAdressList
    
    #Test Case
    global testCaseNameList
    global versionList
    global descriptionList
    
    #Status
    global resultList
    global errorList
    global errorCountList
    global dateList
    global timeList
    
    #LogLists    
    global logList
    global multiLogList
    
    versionList = []
    etsFirmVerList = []
    projectNameList = []
    vendorIdList = []
    deviceIdList = []
    macAdressList = []
    testCaseNameList = []
    versionList = []
    descriptionList = []
    resultList = []
    errorList = []
    errorCountList = []
    dateList = []
    timeList = []
    logList = []
    multiLogList = []
    
def printPathInfo():
    print("")
    print("############### FILE INFORMATION ################")
    print("Source Path for Xml Files : ", srcXmlPath)
    print("Destination(Final) Path for Pdf Files : ", dstXmlPath)
    print("Certification Report Name : ", certificationReport)
    print("Detailed Test Report Name : ", detailedTestReport)
    print("#################################################")
    
def printUserChoice(reportName,reportType):
    global crtfRepAproval
    global detRepAproval
    print("")
    print("Would you like to create " + reportName + " file ?" )
    print("------------------------")
    print("0 : No")
    print("1 : Yes")
    print("------------------------")
    
    if(reportType == 0):
        crtfRepAproval = input("Please enter your choice:")
        
    
    elif(reportType == 1):
        detRepAproval = input("Please enter your choice:")
        
        

def userProcess():
    global srcXmlPath
    global dstXmlPath
    
    print("")
    srcXmlPath = input("Please enter Source Path for Xml Files : ")
    dstXmlPath = input("Please enter Destination(Final) Path for Pdf Files : ")
    srcXmlPath = os.path.abspath(os.path.join(srcXmlPath,''))
    
    if os.path.isdir(srcXmlPath) and os.path.isdir(dstXmlPath):
        printUserChoice(certificationReport,0)
        printUserChoice(detailedTestReport,1)
        print("")
        print("----ALL SETTINGS ARE DONE AS BELOW INFORMATION---- ")
        printPathInfo()
        createPdfFiles()    
        
    else:
        print("ERROR : SOURCE OR DESTINATION PATH IS INCORRECT,PLEASE ENTER AGAIN")
        mainProcess()

def xmlParser(filePath):
    #AutomatedRtTester
    global versionList
    global etsFirmVerList
    global projectNameList
    
    #Dut
    global vendorIdList
    global deviceIdList
    global macAdressList
    
    #Test Case
    global testCaseNameList
    global versionList
    global descriptionList
    
    #Status
    global resultList
    global errorList
    global errorCountList
    global dateList
    global timeList
    
    #LogLists    
    global logList
    global multiLogList
    
    print("Reading & Parsing Xml Files from : " + filePath )
    tree = et.parse(filePath)
    root = tree.getroot()
    
    versionList.append(root.find('AutomatedRtTester').find('Version').text)
    etsFirmVerList.append(root.find('AutomatedRtTester').find('EtsFirmwareVersion').text)
    projectNameList.append(root.find('AutomatedRtTester').find('ProjectName').text)
    
    vendorIdList.append(root.find('Dut').find('VendorId').text)
    deviceIdList.append(root.find('Dut').find('DeviceId').text)
    macAdressList.append(root.find('Dut').find('MacAddress').text)
    
    testCaseNameList.append(root.find('Testcase').find('Name').text)
    versionList.append(root.find('Testcase').find('Version').text)
    descriptionList.append(root.find('Testcase').find('Description').find('Line').get('Text'))
    
    
    resultList.append(root.find('Status').find('Result').text)
    errorList.append(root.find('Status').find('Error').text)
    errorCountList.append(root.find('Status').find('ErrorCount').text)
    dateList.append(root.find('Status').find('Date').text)
    timeList.append(root.find('Status').find('Time').text)
    
    multiLogList.append([text.get('Text') for text in root.find('Log').findall('Line')])

def createCertTestPdf():
    
    pdf = FPDF(format='A4')
    pdf.add_page()
    
    pdf.set_font("Arial", size=12,style='b') # font and textsize
    pdf.set_y(3)
    pdf.cell(w=200, h=10,border=0, txt="Certification Report", align="L")
    
    pdf.set_font("Arial", size=12,style='b') # font and textsize
    pdf.set_y(3)
    pdf.set_x(130)
    pdf.cell(w=200, h=10,border=0, txt="Automated RT Tester" + " " + versionList[0], align="L")
    
    pdf.rect(h=0,w=180,x=11,y=12)
    
    pdf.set_font("Arial", size=16,style='b') # font and textsize
    pdf.set_y(18)
    pdf.cell(w=200, h=10,border=0, txt="Certification Report", align="L")

    pdf.set_font("Arial", size=16,style='b') # font and textsize
    pdf.set_y(33)
    pdf.cell(w=200, h=10,border=0, txt="Result:", align="L")
    
    pdf.set_font("Arial", size=20,style='b') # font and textsize
    pdf.set_text_color(r=254 ,g=194 ,b=12)
    pdf.set_y(33)
    pdf.set_x(80)
    pdf.cell(w=200, h=10,border=0, txt="PassWithHint", align="L")
    
    #General Information
    pdf.set_text_color(r=0 ,g=0 ,b=0)
    pdf.set_font("Arial", size=16,style='b') # font and textsize
    pdf.set_y(48)
    pdf.cell(w=200, h=10,border=0, txt="General Information:", align="L")
    
    pdf.set_font("Arial", size=12,style='BU') # font and textsize
    pdf.set_y(58)
    pdf.cell(w=200, h=10,border=0, txt="Date:", align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(68)
    pdf.cell(w=200, h=10,border=0, txt="Date:", align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(68)
    pdf.set_x(80)
    pdf.cell(w=200, h=10,border=0, txt=dateList[0], align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(78)
    pdf.cell(w=200, h=10,border=0, txt="Time:", align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(78)
    pdf.set_x(80)
    pdf.cell(w=200, h=10,border=0, txt=timeList[0], align="L")
    
    #Automated RT Tester    
    pdf.set_font("Arial", size=12,style='BU') # font and textsize
    pdf.set_y(90)
    pdf.cell(w=200, h=10,border=0, txt="Automated RT Tester:", align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(100)
    pdf.cell(w=200, h=10,border=0, txt="Version:", align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(100)
    pdf.set_x(80)
    pdf.cell(w=200, h=10,border=0, txt=versionList[0], align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(110)
    pdf.cell(w=200, h=10,border=0, txt="ETS Firmware-Version:", align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(110)
    pdf.set_x(80)
    pdf.cell(w=200, h=10,border=0, txt=etsFirmVerList[0], align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(120)
    pdf.cell(w=200, h=10,border=0, txt="Project Name:", align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(120)
    pdf.set_x(80)
    pdf.cell(w=200, h=10,border=0, txt=projectNameList[0], align="L")
    
    #Device
    pdf.set_font("Arial", size=12,style='BU') # font and textsize
    pdf.set_y(132)
    pdf.cell(w=200, h=10,border=0, txt="Device:", align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(142)
    pdf.cell(w=200, h=10,border=0, txt="Vendor ID:", align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(142)
    pdf.set_x(80)
    pdf.cell(w=200, h=10,border=0, txt=vendorIdList[0], align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(152)
    pdf.cell(w=200, h=10,border=0, txt="Device ID:", align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(152)
    pdf.set_x(80)
    pdf.cell(w=200, h=10,border=0, txt=deviceIdList[0], align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(162)
    pdf.cell(w=200, h=10,border=0, txt="Mac Adress:", align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(162)
    pdf.set_x(80)
    pdf.cell(w=200, h=10,border=0, txt=macAdressList[0], align="L")
    
    #Test Execution
    pdf.set_font("Arial", size=16,style='B') # font and textsize
    pdf.set_y(182)
    pdf.cell(w=200, h=10,border=0, txt="Test Execution:", align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(192)
    pdf.cell(w=200, h=10,border=0, txt="Number of Errors:" , align="L")
    
    pdf.set_font("Arial", size=12,style='B') # font and textsize
    pdf.set_y(192)
    pdf.set_x(50)
    pdf.cell(w=200, h=10,border=0, txt="0", align="L")
    
    #Next Pages with table
    pdf.add_page()
    
    pdf.set_font("Arial", size=12,style='b') # font and textsize
    pdf.set_y(3)
    pdf.cell(w=200, h=10,border=0, txt="Certification Report", align="L")
    
    pdf.set_font("Arial", size=12,style='b') # font and textsize
    pdf.set_y(3)
    pdf.set_x(130)
    pdf.cell(w=200, h=10,border=0, txt="Automated RT Tester" + " " + versionList[0], align="L")
    
    pdf.set_font("Arial", size=12,style='b') # font and textsize
    pdf.set_y(23)
    pdf.set_x(27)
    pdf.cell(w=200, h=10,border=0, txt="Test case overview" + " " + versionList[0], align="L")
    
    pdf.rect(h=0,w=180,x=11,y=12)
    
    pdf.set_font("Arial", size=8, style='B') # font and textsize
    pdf.set_y(35)
    pdf.set_line_width(0.1)
    with pdf.table(width=150, col_widths=(15, 130, 35, 60, 45), line_height=8) as table:
        for i in range(len(testCaseNameList)):
            dataRow = table.row()
            
            if(i == 0):
                dataRow.cell("#")
                dataRow.cell("Test Case")
                dataRow.cell("Version")
                dataRow.cell("Execution Date")
                dataRow.cell("Result")
            else:
                num = i+1
                testCaseName = testCaseNameList[i]
                version = versionList[i]
                execDate = dateList[i] + ";" + " " + timeList[i]
                result = resultList[i]
            
                dataRow.cell(str(num))
                dataRow.cell(testCaseName)
                dataRow.cell(version)
                dataRow.cell(execDate)
            
                if(result == "Pass"):
                    pdf.set_text_color(r=50 ,g=205 ,b=50)
            
                elif(result == "None"):
                    pdf.set_text_color(r=255 ,g=0 ,b=0)
                
                elif(result == "PassWithHint"):
                    pdf.set_text_color(r=254 ,g=194 ,b=12)
            
                else:
                    pdf.set_text_color(r=0 ,g=0 ,b=0)
                
                dataRow.cell(result)
                pdf.set_text_color(r=0 ,g=0 ,b=0)
            
    #pdf.output(os.path.join("C://Users//PM_br//Desktop//PDF-Script//Destination//Certification.pdf"))
    pdf.output(os.path.join(dstXmlPath,certificationReport))

def createDetailTestPdf():
    allreports = " " 
    reportIndex = 0
    if(not os.path.isdir(os.path.join(dstXmlPath,"All_Reports"))):
        os.mkdir(os.path.abspath(os.path.join(dstXmlPath,"All_Reports")))
    
    allreports = os.path.abspath(os.path.join(dstXmlPath,"All_Reports"))
    
        
    for filename in os.listdir(srcXmlPath):
        
        pFileName = filename.replace(".xml",".pdf")
        
        pdf = FPDF(format='A4')
        pdf.add_page()
        
        pdf.set_font("Arial", size=12,style='b') # font and textsize
        pdf.set_y(3)
        pdf.cell(w=200, h=10,border=0, txt="Detailed Test Report", align="L")
    
        pdf.set_font("Arial", size=12,style='b') # font and textsize
        pdf.set_y(3)
        pdf.set_x(130)
        pdf.cell(w=200, h=10,border=0, txt="Automated RT Tester" + " " + versionList[0], align="L")
    
        pdf.rect(h=0,w=180,x=11,y=12)
    
        pdf.set_font("Arial", size=16,style='b') # font and textsize
        pdf.set_y(18)
        pdf.cell(w=200, h=10,border=0, txt="Test Case Report", align="L")

        pdf.set_font("Arial", size=16,style='b') # font and textsize
        pdf.set_y(33)
        pdf.cell(w=200, h=10,border=0, txt="Test case:", align="L")
    
        pdf.set_font("Arial", size=16,style='b') # font and textsize
        pdf.set_y(33)
        pdf.set_x(80)
        pdf.cell(w=200, h=10,border=0, txt=testCaseNameList[reportIndex], align="L")
        
        pdf.set_font("Arial", size=16,style='b') # font and textsize
        pdf.set_y(48)
        pdf.cell(w=200, h=10,border=0, txt="Result:", align="L")
    
        pdf.set_font("Arial", size=16,style='b') # font and textsize
        pdf.set_text_color(r=254 ,g=194 ,b=12)
        pdf.set_y(48)
        pdf.set_x(80)
        pdf.cell(w=200, h=10,border=0, txt=resultList[reportIndex], align="L")
        
        pdf.set_text_color(r=0 ,g=0 ,b=0)
        
        #Test case description
        pdf.set_font("Arial", size=15,style='b') # font and textsize
        pdf.set_y(65)
        pdf.cell(w=200, h=10,border=0, txt="Test case description:", align="L")
        
        pdf.set_font('Arial', size=12,style='b') # font and textsize
        pdf.set_y(80)
        pdf.multi_cell(200, 5, txt=descriptionList[reportIndex].encode('utf-8').decode('latin-1'), align = 'L')
        
        reportIndex = reportIndex + 1
        pdf.output(os.path.join(allreports,pFileName)) 
    
def createPdfFiles():
    print(" ")
    print("################ AVAILABLE XML FILES ################")
          
    for filename in os.listdir(srcXmlPath):
        if filename.endswith(".xml"):
            filePath = os.path.join(srcXmlPath,filename)
            xmlParser(filePath)
    print("#####################################################")
    
    print(" ")
    print("Creating Pdf Files....")
    
    if crtfRepAproval == '1' and detRepAproval == '1' :
        createCertTestPdf()
        createDetailTestPdf()
        
    elif crtfRepAproval == '1' and detRepAproval == '0':
        createCertTestPdf()
        
    elif crtfRepAproval == '0' and detRepAproval == '1':
        createDetailTestPdf()
    else :
        print(" ")
        print("No Pdf document was created according to your selection....")
    
    
        
def mainProcess():
    initGlobalVars()
    initGlobPdfVars()
    printPathInfo()
    userProcess()
    
    
def main():
    mainProcess()
    #createCertTestPdf()
    

if __name__ == '__main__':
    main()