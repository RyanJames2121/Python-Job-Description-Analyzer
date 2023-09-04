if __name__ == '__main__':
    import PyPDF2

    pdfFile = open('JobApplication.pdf', 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    pageObj = pdfReader.pages[0]
    for i in pageObj.extract_text().split():
        if i == 'Remote' or i == 'remote':
            print('Remote: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'Insurance' or i == 'insurance':
            print('Basic Insurance: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'Flexible' or i == 'flexible':
            print('Flexible Hours: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'Health' or i == 'health':
            print('Health Insurance: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'Dental' or i == 'dental':
            print('Dental Insurance: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'Python' or i == 'python':
            print('Uses Python: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'Word' or i == 'word':
            print('Uses Microsoft Word: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'Excel' or i == 'Excel':
            print('Uses Microsoft Excel: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'SQL' or i == 'sql':
            print('Uses SQL: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'Java' or i == 'java':
            print('Uses Java: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'hubspot' or i == 'Hubspot':
            print('Uses Hubspot: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'Senior' or i == 'Sr.':
            print('Is a senior position: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'PTO' or i == 'Paid Time Off':
            print('Has Paid Time Off: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'Degree' or i == 'degree':
            print('Degree Required: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'Overtime' or i == 'overtime':
            print('Has Overtime: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'manage' or i == 'management':
            print('Involves management: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'group' or i == 'Group':
            print('Involves group work: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'assistant' or i == 'Assistant':
            print('Is an assistant position: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'government' or i == 'governmental':
            print('Involves government based work: True')
            break
    for i in pageObj.extract_text().split():
        if i == 'confidentiality' or i == 'confidential':
            print('Has confidentiality: True')
            break
    pdfFile.close()



