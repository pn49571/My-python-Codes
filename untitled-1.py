def find_emails(s):
    return re.findall(r'\w*.?\w*@\w+.\w+.?\w*',s)


find_emails([kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk",'kenneth@teamtreehouse.com', 'ryan@teamtreehouse.com', 'test@example.co.uk'])