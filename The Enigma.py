from random import sample
class Enigma():
    def __init__(self,a1,a2,a3):
        self.final_array_1=list(a1)
        self.final_array_2=list(a2)
        self.final_array_3=list(a3)
    
    def MonoSubsEncrypt(self,char,array):
        """This functions substitutes each char passed to the funtion
        to its corresponding char with respect to the array
        """
        main_array=sorted(list(set('qwertyuiopasdfghjklzxcvbnm')))
        index_of_char=main_array.index(char)
        return array[index_of_char]
    
    def MonoSubsDecrypt(self,char,array):
        """This functions substitutes each char passed to the funtion
        to its corresponding char with respect to the array in the exact opposite way
        to the MonosubsEncrypt function. Thereby reversing its effect
        """
        main_array=sorted(list(set('qwertyuiopasdfghjklzxcvbnm')))
        index_of_char=array.index(char)
        return main_array[index_of_char]
    
    def RotateRotor(self,array):
        """This function mimics the rotation of the rotor
        i.e cyclically rotates the array forward
        """
        last_char=array[25]
        array.remove(last_char)
        array.insert(0,last_char)
        return array
    
    def Reflector(self,char):
        """This functions mimics the reflector which monosubstitutes each character 
        with some corresponding character.
        This is constant for a particular device and does not change
        """
        array=['t', 'j', 'l', 'm', 'y', 'c', 'v', 'r', 'd', 'u', 'w', 'n', 'a', 'p', 'f', 'o', 'i', 'h', 'z', 's', 'x', 'q', 'b', 'k', 'g', 'e']
        index=array.index(char)
        char=array[25-index]
        return char
    
    def RotorWorkingEncrypt(self,array,char,rotor):
        """
        The wrapper function which does the full function of a single rotor
        in the encryption phase
        """
        char=self.MonoSubsEncrypt(char,array)
        if rotor:
            #rotor-> the boolean which determines whether the rotor must be rotated or not
            array=self.RotateRotor(array)
        return array,char

    def RotorWorkingDecrypt(self,array,char,rotor):
        """
        The wrapper function which does the full function of a single rotor
        in the Decryption phase
        """
        char=self.MonoSubsDecrypt(char,array)
        if rotor:
            #rotor-> the boolean which determines whether the rotor must be rotated or not
            array=self.RotateRotor(array)
        return array,char
    
    def PlugBoard(self,char):
        """The plug board which will swap a pair of characters both before and after
        encryption/decryption phase
        
        The n-th character from the beginning is replaced with n-th character from the end
        """
    
        array=['r', 'j', 'v', 'm', 'a', 'u', 't', 'd', 'b', 'g', 'n', 'h', 'y', 'l', 'f', 'x', 'o', 'i', 'k', 'z', 'w', 's', 'c', 'q', 'e', 'p']   
        index=array.index(char)
        char=array[25-index]
        return char
    
    def RotorMainEncrypt(self,string):
        """
        The main encryption function which controls all other aspects of encryption
        and flow of control
        """
        final_char=''
        first_rounds=0
        second_rounds=0
        char=string
        char=self.PlugBoard(char)
        self.final_array_1,char=self.RotorWorkingEncrypt(self.final_array_1,char,False)
        
        if first_rounds>25:
            #the second rotor rotates only after the first completes
            #one full rotation
            self.final_array_2,char=self.RotorWorkingEncrypt(self.final_array_2,char,False)
            first_rounds=0
            second_rounds+=1
        else:
            self.final_array_2,char=self.RotorWorkingEncrypt(self.final_array_2,char,False)

        if second_rounds>25:
            #the third rotor rotates only after the second completes
            #one full rotation
            self.final_array_3,char=self.RotorWorkingEncrypt(self.final_array_3,char,False)
            second_rounds=0
        else:
            self.final_array_3,char=self.RotorWorkingEncrypt(self.final_array_3,char,False)
        char = self.Reflector(char)
        if second_rounds>25:
            self.final_array_3,char=self.RotorWorkingEncrypt(self.final_array_3,char,True)
            second_rounds=0
        else:
            self.final_array_3,char=self.RotorWorkingEncrypt(self.final_array_3,char,False)
        if first_rounds>25:
            self.final_array_2,char=self.RotorWorkingEncrypt(self.final_array_2,char,True)
            first_rounds=0
            second_rounds+=1
        else:
            self.final_array_2,char=self.RotorWorkingEncrypt(self.final_array_2,char,False)
        
        first_rounds+=1
        #The first rotor will rotote once for every character
        self.final_array_1,char=self.RotorWorkingEncrypt(self.final_array_1,char,True)
        char=self.PlugBoard(char)
        final_char=char
        return final_char
    
    def RotorMainDecrypt(self,char):
        """
        The main decryption function which controls all other aspects of encryption
        and flow of control
        """
        final_char=''
        first_rounds=0
        second_rounds=0
        char=self.PlugBoard(char)
        self.final_array_1,char=self.RotorWorkingDecrypt(self.final_array_1,char,False)
        
        if first_rounds>25:
            #the second rotor rotates only after the first completes
            #one full rotation
            self.final_array_2,char=self.RotorWorkingDecrypt(self.final_array_2,char,False)
            first_rounds=0
            second_rounds+=1
        else:
            self.final_array_2,char=self.RotorWorkingDecrypt(self.final_array_2,char,False)

        if second_rounds>25:
            #the third rotor rotates only after the second completes
            #one full rotation
            self.final_array_3,char=self.RotorWorkingDecrypt(self.final_array_3,char,False)
            second_rounds=0
        else:
            self.final_array_3,char=self.RotorWorkingDecrypt(self.final_array_3,char,False)
        char = self.Reflector(char)
        if second_rounds>25:
            self.final_array_3,char=self.RotorWorkingDecrypt(self.final_array_3,char,True)
            second_rounds=0
        else:
            self.final_array_3,char=self.RotorWorkingDecrypt(self.final_array_3,char,False)
        if first_rounds>25:
            self.final_array_2,char=self.RotorWorkingDecrypt(self.final_array_2,char,True)
            first_rounds=0
            second_rounds+=1
        else:
            self.final_array_2,char=self.RotorWorkingDecrypt(self.final_array_2,char,False)
        
        first_rounds+=1
        #The first rotor will rotote once for every character
        self.final_array_1,char=self.RotorWorkingDecrypt(self.final_array_1,char,True)
        char=self.PlugBoard(char)
        final_char=char  
        return final_char
    
    
        
def RotorInit(no):
    """This function randomly generates a rotor and prompts the user for the currect position
    of the rotor. i.e which character it is set to in the beginning
    """
    start_char=input("Enter the current of rotor {}:".format(no))
    original_array=sorted(list(set('qwertyuiopasdfghjklzxcvbnm')))
    final_random_array=sample(original_array,26)
    index=final_random_array.index(start_char)
    left_array=final_random_array[0:index]
    right_array=final_random_array[index:26]
    right_array.extend(left_array)
    final_array=right_array
    return tuple(final_array)


def StringHandling(string,array1,array2,array3,encrypt=True):
    """This function handles the data input in the form of plain text by 
    using the appropriate methods of parsing and passing the arguements to 
    the encryption/decryption function and also passing the non-alphabets 
    as it is to the final text
    """
    if encrypt:
        #this boolean determines whether the function is encryption or decryption
        res=''
        En=Enigma(array1,array2,array3)
        #initialization
        for i in string:
            if i.isupper():
                #upper case is also handled as lower case but converted back into uppercase later
                char=En.RotorMainEncrypt(i.lower())
                res+=char.upper()
            elif i.islower():
                char=En.RotorMainEncrypt(i)
                res+=char

            else:
                #non-alphabets are ot encrypted
                res+=i
        del En
        #returns the encrypted text
        return res
    
    else:
        En1=Enigma(array1,array2,array3)
        stringOriginalRev=''
        for i in string:
            if i.isupper():
                char=En1.RotorMainDecrypt(i.lower())
                stringOriginalRev+=char.upper()
            elif i.islower():
                char=En1.RotorMainDecrypt(i)
                stringOriginalRev+=char

            else:
                stringOriginalRev+=i
        stringOriginal=stringOriginalRev
        del En1
        return stringOriginal


if __name__=='__main__':
    try:
        flag=input("Do you want to reset the rotors : ")
        if(flag.lower()=='yes' or flag.lower()== 'y' or flag.lower()== 's'):
            ar1=RotorInit(1)
            ar2=RotorInit(2)
            ar3=RotorInit(3)
        
        E=input("Press 'e' for encrpytion\n Press 'd' for decryption: ")
        string=input("\n\nEnter the string : ")
        if (E.lower()=='e'):
            print("Starting Encryption...")
            Encrypted=StringHandling(string,ar1,ar2,ar3,encrypt=True)
            print("\nEncrypted text is:",Encrypted)
        elif(E.lower()=='d'):
            print("Starting Decryption...")
            stringOriginal=StringHandling(string,ar1,ar2,ar3,encrypt=False)
            print("\nDecryped text is :",stringOriginal)
        else:
            print("Invalid function")
    except ValueError as VE:
        print("\nInvalid character as current position\n")
    except Exception as e:
        print(e)
