
""" Pre - analyzing """

from Bio import SeqIO
import glob
import os
import os
import re
from tkinter import filedialog
from tkinter import *
from Bio import SeqIO
import glob
from tkinter import messagebox
from Bio.Blast import NCBIWWW
import os
#from shutil import copyfile
import shutil


top = Tk()
top.geometry("300x300")

class mypath:
       p="temp"#fasta folder
       folder_selected="temp"
       
def chose_folder_fastq():
    
   folder_selected = filedialog.askdirectory()
   mypath.folder_selected=folder_selected
   convert_all_fastq_to_fasta(folder_selected)
   change_der(folder_selected)
   convert_fasta_to_txt()
   small_seq()
   smaller_seq()
   deletesimilar()
   text_to_fasta()
   blast_result()
   messagebox._show("Done","done convert")
   # messagebox.showinfo("done convert")

def change_der(path):
   print("the path is"+ path)
   os.chdir(path)
   for file in glob.glob("*.fasta"):
      newDir = path + '/fasta'
      if not os.path.exists(newDir):
         oldmask = os.umask(000)
         os.makedirs(newDir, 0o777)
         os.umask(oldmask)
      os.chdir(newDir)
      # newDir= '{}/{}'.format(newDir, file)
      dir = '{}/{}'.format(path, file)
   
       
      shutil.copy(dir,newDir)
      


def convert_all_fastq_to_fasta(path):
   os.chdir(path)
   for file in glob.glob("*.fastq"):
      nameFile = file.split(".fastq")
      s = path.split(".fastq")
      newDir = path + '/fasta'
      
   
      if not os.path.exists(newDir):
         os.makedirs(newDir)
      # newDir = os.mkdir(path+'/fasta')
      #print(newDir)
      mypath.p= newDir
      dir = '{}/{}'.format( newDir,nameFile[0])
     
      SeqIO.convert(file, "fastq", (dir + "_output") + ".fasta", "fasta")
   convert_fasta_to_txt()
   return
       
def chose_file_fastq():
  
   root = top
   root.filename = filedialog.asksaveasfilename(initialdir="/", title="Select folder",
                                                filetypes=((("fastq files", "*.fastq"), ("all files", "*.*"))))
   convert_file_fastq_to_fasta(root.filename)
   convert_fasta_to_txt()
   messagebox._show("Done", "done convert")



def convert_file_fastq_to_fasta(path):

  
   # os.chdir(path)
   nameFile = path.split(".fastq")
   s = nameFile[0].split("/")

   newPath =''
   for i in range(len(s)-1):
      newPath += '{}/'.format(s[i])
   newPath += 'fasta'
   mypath.p=newPath
   if not os.path.exists(newPath):
      os.makedirs(newPath)
   newPath+='/{}'.format(s[-1])
   SeqIO.convert(path, "fastq", (newPath + "_output") + ".fasta", "fasta")
   # print(newPath)

   return
           
def convert_fasta_to_txt():

   os.chdir(mypath.p)
 
   for file in glob.glob("*.fasta"):
          
      nameFile = file.split(".fasta")
      newDir = mypath.folder_selected + '/txt'
      
   
      if not os.path.exists(newDir):
         os.makedirs(newDir)
     
      newfile = '{}/{}.{}'.format( newDir,nameFile[0],"txt")
    
      #newfile= mypath.folder_selected+ "/txt/"+file+".txt" 
      oldfile=mypath.p+ "/"+file 
      seq_file = open(newfile, "w")
      for seq_record in SeqIO.parse(oldfile, "fasta"):
          my_seq = seq_record.seq
          seq_file.write(str(my_seq)+"\n")
      seq_file.close()
      
      
def small_seq():
      newDir = mypath.folder_selected + '/small_seq'
         
      if not os.path.exists(newDir):
         os.makedirs(newDir)    
      oldfolder= mypath.folder_selected + '/txt'
      os.chdir(oldfolder)
      for file in glob.glob("*.txt"):
         newfile=newDir+"/"+ file
         print(newfile) 
         file_seq = open(file, 'r')
         out_small_seq = open(newfile, 'w')
         for line in file_seq:
            small_seq = line[28:52]
            out_small_seq.write(small_seq+'\n')
         file_seq.close()
         out_small_seq.close() 
         
def smaller_seq():
      newDir = mypath.folder_selected + '/smaller_seq'
         
      if not os.path.exists(newDir):
         os.makedirs(newDir)    
      oldfolder= mypath.folder_selected + '/small_seq'
      os.chdir(oldfolder)
      for file in glob.glob("*.txt"):
         newfile= newDir+"/"+ file
         smaller_seq = open(file, "r")
         out_14 = open(newfile, "w")
         for seq in smaller_seq:
            if "TA" in seq:
               seq_14 = seq[seq.index("TA"):(seq.index("TA")+14)]
               out_14.write(seq_14+"\n")
         smaller_seq.close()
         out_14.close()
         
def deletesimilar():
      newDir = mypath.folder_selected + '/deletesimilar'
         
      if not os.path.exists(newDir):
         os.makedirs(newDir)    
      oldfolder= mypath.folder_selected + '/smaller_seq'
      os.chdir(oldfolder)
      for file in glob.glob("*.txt"):
         newfile= newDir+"/"+ file
         seen = set()
         with open(file) as infile:
            with open(newfile, 'w') as outfile:
               for line in infile:
                  if line not in seen:
                        outfile.write(line)
                        seen.add(line)         
def text_to_fasta():
         newDir = mypath.folder_selected + '/text_to_fasta'
         
         if not os.path.exists(newDir):
            os.makedirs(newDir)    
         oldfolder= mypath.folder_selected + '/deletesimilar'
         os.chdir(oldfolder)
         for file in glob.glob("*.txt"):
            newfile= newDir+"/"+ file
                  #File input
            fileInput = open(file)

            #File output
            fileOutput = open(newfile, "w")

            #Seq count
            count = 1 ;

            #Loop through each line in the input file
           
            for strLine in fileInput:

               #Strip the endline character from each input line
               strLine = strLine.rstrip("\n")

               #Output the header
               fileOutput.write(">" + str(count) + "\n")
               fileOutput.write(strLine + "\n")

               count = count + 1
         

            #Close the input and output file
            fileInput.close()
            fileOutput.close()




def blast_result(): 
      newDir = mypath.folder_selected + '/blast_result'
        
      if not os.path.exists(newDir):
         os.makedirs(newDir)    
      oldfolder= mypath.folder_selected + '/text_to_fasta'
      os.chdir(oldfolder)
      for file in glob.glob("*.txt"):
         newfile= newDir+"/"+ file+"1.xml"
         save_file= open (newfile, "w")
         fasta_string = open(file).read()
         print("test1")
         result_handle = NCBIWWW.qblast("blastn", "nt",  fasta_string, entrez_query="txid262316[Organism]")
         print("test3")
         #result_handle=NCBIWWW.qblast("blastp", "nr", "4504191", entrez_query="mammalia[Orgn]")
         print("test4")
         save_file.write(result_handle.read())
         save_file.close()
         result_handle.close()
            
   
   
             
B = Button(top, text = "chose a folder", command = chose_folder_fastq)
B.place(x =160,y =90)

c= Button(top, text = "chose a file", command = chose_file_fastq)
c.place(x = 30,y =90)
top.mainloop()
