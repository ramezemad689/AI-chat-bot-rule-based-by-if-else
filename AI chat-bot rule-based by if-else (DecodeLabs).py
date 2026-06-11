import random
ready=input("Are you ready to chat ? ").lower().strip()
if ready=="yes":
    flag=True
    print("You can speak now ")    
elif ready=="no":
    flag=False 

cleaned_input=""


response={
   'greetings' : ["hi" , "hello" , "nice to have you" ],
    'exit'     : ["exit" , "quit" , "leave" , "bye"],
    'inquirs'  : ["internship","program","decodelabs"]
}

response2={
    'greetings' : ["I am happy to see you"
                  ,"pleasure to have you"
                  ,"nice to meet you"],

    'exit'     : ["BYE" , "see you soon" , "until we meet again"],      
    'inquirs'  : ["internship","program","training is starting from 20/5 to 20/6 and its a project-based training",
                  "further details well be cleared ASAP"]       
}

def check_exit(user_input):
    user_input = user_input.lower().strip()
    words = user_input.split()
    
    if any(word in response['exit'] for word in words):
        return True
    
    return False

def check_greetings(user_input):
    user_input = user_input.lower().strip()
    words = user_input.split()
    
    if any(word in response['greetings'] for word in words):
        return True
    
    return False

def check_inquirs(user_input):
    user_input = user_input.lower().strip()
    words = user_input.split()
    
    if any(word in response['inquirs'] for word in words):
       
        return True
    
    return False

while(flag==True):
    user_input=input("You are saying :")
    cleaned_input = user_input.lower().strip()
    
    
    
    if check_exit(user_input):
        print(random.choice(response2["exit"]))
        break   
        
    elif check_greetings(user_input):
         print(random.choice(response2["greetings"]))        

    elif  check_inquirs(user_input): 
         print(random.choice(response2["inquirs"]))
    else:
        print("AI is saying : I Do not recognize what you are saying") 

        
print(cleaned_input)