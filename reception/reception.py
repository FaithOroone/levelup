def registration_checker(name):
    file1=open('names/vip_list.txt', 'r')
    content_list1=file1.readlines()
    file1.close()
    for test_name in content_list1:
        if name.lower() in test_name.lower():
            return(test_name.strip('\n')+',vip ')

    file2=open('names/ordinary_list.txt', 'r')
    content_list2=file2.readlines()
    file2.close()

    for test_name in content_list2:
        if name.lower() in test_name.lower():
            return(test_name.strip('\n')+',ordinary')
    return 'Not Registered'


name=input('Enter name:')
print(registration_checker(name))
