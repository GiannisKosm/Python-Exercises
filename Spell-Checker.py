from bitarray import bitarray
import mmh3
 
class BloomFilter:
    
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        
    def add(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            self.bit_array[result] = 1
            
    def lookup(self, string):
       for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                
                 return "--{}--".format(string)
       return string
 
bf = BloomFilter(500000, 7)
 
lines = open("/Users/GiannisKosmopoulos/Desktop/american-english.txt").read().splitlines()
for line in lines:
    bf.add(line)
#άνοιγμα αρχείου και αποθήκευση περιεχομένου σε μεταβλητή data
fin=open("/Users/GiannisKosmopoulos/Desktop/text.txt","r")
data=fin.read().replace('\n','')

#έλεγχος για το αν οι λέξεις της πρότασης ανήκουν στο λεξικό και εκτύπωση αποτελέσματος
for i in data.split():
 print bf.lookup(i),


