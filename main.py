'''
write a  python program to calculate vowels in a given string ?
'''
print("guvi geeks private limited")

data =input("enter a string:")
count = 0
# iterate over the string
for data in data:
    if data == 'a'or data == 'u'or data =='e'or data =='i'or data =='o':
        count = count + 1

#print the total vowels in a string:
        print ("number of vowels in the string : ",count) 




'''
creat a pyramid of numbers from 1 to 20
'''           
for i in range(21):
    print(i)


    
'''
function to remove vowels
'''
str =input("enter string")
vowel_string="aeiouAEIPOU"

print("input string",str)

for char in str:
    if char in vowel_string:
        str=str.replace(char, "")

print("output string without vowels",str) 




'''
define a function to the number of unique characters in a string:
'''

string='guvi technology'
count=0
temp=[]
for i in string:
    if(i not in temp):
        count+=1
        temp.append(i)
print('Total Unique Characters count:',count) 



'''
function to check if a string is a palindrome
'''
def is_palindrome(s):
    # Convert the entire string to lowercase
    s = s.lower()
    
    # Clean the string: remove any characters that are not alphabets
    cleaned_str = ""
    for char in s:
        if char.isalpha():
            cleaned_str += char
            
    # Check for palindrome
    return cleaned_str == cleaned_str[::-1]

print(is_palindrome ("able was i ere i saw elba"))



    
'''
prompt the user to enter two strings to find the longest common substring between them
'''

def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    # Initialize a table to store lengths of longest common suffixes
    # dp[i][j] will store the length of longest common suffix of str1[0..i-1] and str2[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # To store the length of the longest common substring
    max_length = 0
    # To store the index of the last character of the longest common substring
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0

    return str1[end_index - max_length + 1: end_index + 1]

# Test the function
input_string1 = input("Enter first string: ")
input_string2 = input("Enter second string: ")
print("Longest common substring:", longest_common_substring(input_string1, input_string2))



'''
write a python program to find most frequency character in a string 
'''
#initializing string
input_str ="commitment"
#printing oringinal string
print ("the original string  is :" + input_str) 
#most frequency character in string
all_freq = {}
for char in input_str :
    if char in all_freq:
        all_freq[char] +=1
    else:
        all_freq[char] = 1
        max_char =max (all_freq, key=all_freq.get)
#printing result
        print("the maximum of all characters in commitment: "+ str (max_char))



'''
this program defines a fuction called is anagram that takes two strings as input
'''
def is_anagram(str1, str2) :
#remove spaces and convert both strings to lowercase
    str1 =str1.replace(" "," ").lower()
    str2 =str2.replace(" "," ").lower()
#check if the length of both strings are equal 
    if len(str1)!=len(str2):
        return False
#sort both strings and compare them
    return sorted (str1) == sorted (str2)
#example usage
string1 = "ate"
string2 = "eat"
print (is_anagram(string1,string2)) 



'''
fuction that counts the number of words in a given string:
'''
def count_words (input_string):
#split the string into word using whitespace as the delimiter
    count_words= input_string.split()
#return the number of word
    return len (count_words)
#example usage:
input_string = "good morning friends"
print(count_words(input_string))    
