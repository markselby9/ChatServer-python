#byte of python exercise
__author__ = 'fengchaoyi'
import pickle, os, sys
phonebookfile = 'phonebook.data'

class Contact:
    id = 0
    name = ''
    phone = -1
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def setId(self, id):
        self.id = id
    def read(self):
        print '<id>: ',self.id, ' <name>: ',self.name , ' <phone> ',self.phone

class Phonebook:
    book = []
    def __init__(self):
        self.book=[]
        if (os.path.exists(phonebookfile)):
            f = open(phonebookfile, 'r+')
            try:
                self.book = pickle.load(f)
            except EOFError:
                print 'empty file detected, rebuild the file..'
                self.book = []
        else:
            f = open(phonebookfile, 'w')

    def read(self):
        print '=== read start ==='
        if self.book:
            for contact in self.book:
                contact.read()
        print '=== read end ==='
    #rearrange the id in the phonebook array
    def rearrange(self):
        for i in range(len(self.book)):
            contact = self.book[i]
            contact.setId(i)
    def add(self, contact):
        self.book.append(contact)
        print self.book
        self.rearrange()
    def remove(self, id):
        try:
            print id, ' to int:', int(id)
            if int(id) in range(len(self.book)):
                self.book.remove(self.book[id])
                self.rearrange()
                print 'delete complete'
            else:
                print 'id not in range'
        except:
            print 'wrong id, please check again'
    def query(self, str):
        result = []
        for contact in self.book:
            if (str in contact.name) or (str in contact.phone):
                result.append(contact)
        return  result
    def save(self):
        f = open(phonebookfile, 'r+')
        pickle.dump(self.book, f)

phonebook = Phonebook()
phonebook.read()
while True:
    instruction = raw_input('input instruction number please (0 for read, 1 for add, 2 for delete, 3 for search, 4 for end): ')
    if (instruction == '0'):
        phonebook.read()
    elif (instruction == '1'):
        name = raw_input('please input the name:')
        number = raw_input('please input the number:')
        if name and number:
            contact = Contact(name, number)
            phonebook.add(contact)
        phonebook.save()
    elif (instruction == '2'):
        phonebook.read()
        id = raw_input('give the id of the contact which you want to delete:')
        phonebook.remove(id)
        phonebook.save()
    elif (instruction == '3'):
        str = raw_input('give the name or phone number which you want to search:')
        if (str):
            result = phonebook.query(str)
            if len(result) > 0:
                for item in result:
                    item.read()
            else:
                print 'empty result'
        phonebook.save()
    elif (instruction == '4'):
        print 'thanks for using'
        phonebook.save()
        sys.exit()
    else:
        print 'wrong input, please check the instruction'
